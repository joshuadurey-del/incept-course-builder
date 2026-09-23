// node test_asap_ui.cjs; add --browser with the existing Playwright runtime available.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
require('./timeline.js'); // Includes the existing source-binding self-test.
const { asapPosition, bindCourseState, populationRows, readASAPStages, validateNeedsHuman } = globalThis.AP4_BOARD;
const generated = JSON.parse(fs.readFileSync(path.join(__dirname, 'process.json')));
const stages = readASAPStages(generated);
assert.deepEqual(stages.map(stage => [stage.id, stage.native_phases]), [
  ['align', ['p12']], ['synthesize', ['content', 'p3']], ['assemble', ['p5']], ['prove', ['p6', 'p7', 'p8']],
]);
assert.equal(readASAPStages({ ...generated, asap_stages: stages.slice(1) }).length, 0);
assert.equal(readASAPStages({ ...generated, asap_stages: stages.map(stage => ({ ...stage, native_phases: ['p3'] })) }).length, 0);
const now = Date.now();
const stamp = new Date(now - 3600000).toISOString();
const ids = ['humgeo', 'apwh', 'psych', 'apush'];
const phases = ['p12', 'p3', 'p5', 'fleet-held'];
const data = { snapshot: stamp, claims: ids.map((id, index) => ({
  claim_id: `${id}.blueprint.audit`, status: 'OBSERVED', value: 'Subset bank PASS; other populations unmeasured.',
  observed_at: stamp, freshness_limit_hours: 24, process_position: { current_stage: phases[index], state: 'Scope needs verification' },
})) };
const evidenceRow = {value:'0 / 10 accepted',detail:'Fixture inventory only.',next_step:'10 pending.',level:'Acceptance ledger',observed_at:stamp,evidence:[{url:`https://github.com/example/course/blob/${'a'.repeat(40)}/ledger.json`,sha256:'b'.repeat(64)}]};
data.population_coverage = {schema:'population-evidence/v1',courses:{apwh:{Practice:evidenceRow}}};
assert.equal(populationRows(data,'apwh',['Practice'],now)[0].value,'0 / 10 accepted');
assert.equal(populationRows(data,'humgeo',['Practice'],now)[0].measured,false,'No cross-course evidence');
for (const id of ids) for (const label of ['Train Your Eye','Embedded checks','Unit assessments']) {
  assert.deepEqual(populationRows(data,id,[label],now)[0],{label,measured:false,reporting_status:'NOT_REPORTED',course_status:'NOT_ASSESSED'});
}
assert.equal(populationRows({population_coverage:{schema:'population-evidence/v1',courses:{humgeo:{Practice:{reporting_status:'NOT_REPORTED',course_status:'NOT_ASSESSED'}}}}},'humgeo',['Practice'],now)[0].reporting_status,'NOT_REPORTED');
assert.equal(populationRows(data,'apwh',['Practice'],now+48*3600000)[0].stale,true);
for (const delta of [{evidence:[]},{evidence:[null]},{evidence:[{url:'javascript:alert(1)',sha256:'b'.repeat(64)}]},{observed_at:'bad'},{observed_at:new Date(now+3600000).toISOString()}]) {
  assert.equal(populationRows({population_coverage:{schema:'population-evidence/v1',courses:{apwh:{Practice:{...evidenceRow,...delta}}}}},'apwh',['Practice'],now)[0].measured,false);
  assert.equal(populationRows({population_coverage:{schema:'population-evidence/v1',courses:{apwh:{Practice:{...evidenceRow,...delta}}}}},'apwh',['Practice'],now)[0].reporting_status,'INVALID_EVIDENCE');
}
const processValue = { ...generated, courses: Object.fromEntries(data.claims.map((claim, index) => [ids[index], {
  ...claim.process_position, detail: claim.value, as_of: stamp,
  coverage: { gate_mcqs: { accepted: 10, required: 10, verdict: 'PASS' } },
}])) };
const courses = bindCourseState(data, processValue, now);
assert.deepEqual(courses.map(course => asapPosition(course, stages).stage), ['align', 'synthesize', null, 'assemble']);
for (const phase of ['p0', 'p4', 'unknown', 'fleet-held']) {
  assert.equal(asapPosition({ ...courses[0], phaseStates: [{ code: phase }] }, stages).stage, null);
}
assert.equal(asapPosition({ ...courses[0], stale: true }, stages).stage, null);
assert.equal(asapPosition({ ...courses[0], claimStatus: 'PLANNED' }, stages).stage, null);
assert.equal(asapPosition({ ...courses[0], phaseStates: [{ code: 'p3' }, { code: 'p5' }] }, stages).stage, null);
assert.equal(asapPosition({ ...courses[0], available: false }, stages).stage, null);
assert.match(asapPosition(courses[1], stages).reason, /Stage placement only/);
const item = { id: 'a'.repeat(16), ts: stamp, course: 'humgeo', kind: 'decision', title: 'A title', deadline: '' };
for (const code of [0, 9, 10, 31]) {
  assert.equal(validateNeedsHuman({ schema: 'needs-human-public/v1', generated_ts: stamp, open: [{ ...item, title: `A${String.fromCharCode(code)}title` }] }, now).status, 'hold');
}
assert(!fs.readFileSync(path.join(__dirname, 'timeline.js')).includes(0), 'JavaScript source contains a literal NUL');
console.log('ASAP mapping, unknown/stale/mixed scope, subset acceptance and title validation passed.');

function playwrightRuntime() {
  try { return require('playwright'); }
  catch (error) {
    if (error.code !== 'MODULE_NOT_FOUND') throw error;
    return require('playwright-core');
  }
}

async function browserCheck() {
  const { chromium } = playwrightRuntime();
  const browser = await chromium.launch({ channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome', headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    const errors = []; page.on('pageerror', error => errors.push(error.message));
    let processFails = false;
    const fixtures = { 'data.json': data, 'process.json': processValue, 'updates.json': [{ts:stamp,course:'dashboard',writer:'test fixture',text:'Receipt '+ 'a'.repeat(160)}],
      'needs-human.json': { schema: 'needs-human-public/v1', generated_ts: stamp, open: [] } };
    await page.route('https://asap.test/**', route => {
      const filename = new URL(route.request().url()).pathname.slice(1) || 'index.html';
      if (filename === 'process.json' && processFails) return route.fulfill({ status: 503, body: 'Unavailable' });
      if (fixtures[filename]) return route.fulfill({ contentType: 'application/json', body: JSON.stringify(fixtures[filename]) });
      if (!(['docs/assets/workspace-preview.png','docs/assets/incept-book.svg'].includes(filename) || /^[a-z][a-z0-9.-]*\.(html|js|css|json|svg)$/.test(filename)) || !fs.existsSync(path.join(__dirname, filename))) return route.fulfill({ status: 404, body: '' });
      return route.fulfill({ contentType: filename.endsWith('.png') ? 'image/png' : filename.endsWith('.js') ? 'text/javascript' : filename.endsWith('.css') ? 'text/css' : filename.endsWith('.svg') ? 'image/svg+xml' : filename.endsWith('.json') ? 'application/json' : 'text/html',
        body: fs.readFileSync(path.join(__dirname, filename)) });
    });
    const ready = async () => {
      await page.waitForFunction(() => globalThis.AP4_DASHBOARD?.ready);
      await page.evaluate(async () => { await AP4_DASHBOARD.ready; });
      if (await page.locator('#needs-human-strip').count()) await page.waitForSelector('#needs-human-strip:not(.is-loading)');
    };
    const visible = () => page.locator('[data-course-card]:visible').evaluateAll(cards => cards.map(card => card.dataset.courseCard));
    await page.goto('https://asap.test/index.html');
    assert.equal(await page.locator('#course-release-timeline, .population-coverage, .source-sync-bar, #needs-human-strip').count(), 0, 'Home must remain a product entry');
    assert.equal(await page.locator('#install-command').count(), 1);
    assert.equal(await page.locator('.hero-banner').evaluate(img => img.complete && img.naturalWidth > 0), true);
    assert(await page.evaluate(() => document.querySelector('.hero-banner').getBoundingClientRect().left > document.querySelector('.hero-copy').getBoundingClientRect().right), 'Banner sits beside desktop copy');
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(() => document.querySelector('.hero-banner').getBoundingClientRect().top >= document.querySelector('.hero-copy').getBoundingClientRect().bottom), 'Banner stacks below mobile copy');
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    await page.setViewportSize({width:1280,height:900});
    await page.locator('#copy-install').click();
    await page.waitForFunction(() => document.querySelector('#copy-install-status').textContent.length > 0);
    assert.equal(await page.locator('a[href="courses.html"]').count(), 0, 'Home must not promote monitoring unrelated courses');
    assert.match(await page.locator('.home-preview').textContent(), /Start a new course build.*pauses at design.*Create a new test course.*Resume a course built here/s);
    if (process.env.UI_SCREENSHOT_DIR) await page.screenshot({path:path.join(process.env.UI_SCREENSHOT_DIR,'home-desktop.png'),fullPage:true});
    await page.getByRole('link', {name: 'Open setup guide'}).click();
    assert.equal(new URL(page.url()).pathname, '/about.html');
    assert.equal(new URL(page.url()).hash, '#install');
    assert.match(await page.locator('#install').textContent(), /Review the costs/);
    await page.goto('https://asap.test/courses.html'); await ready();
    assert.equal(await page.locator('.population-coverage').count(), 0, 'Full population table belongs on each course');
    assert(await page.locator('#course-release-timeline').evaluate(el => el.offsetTop < document.querySelector('#needs-human-strip').offsetTop));
    await page.getByText('Source sync and verification', {exact:true}).click();
    assert.match(await page.locator('.source-sync-link').getAttribute('href'), /InceptTrilogy.*dashboard-repo-poll.yml$/);
    await page.locator('.source-refresh').click(); await ready();
    assert.match(await page.locator('.source-sync-status').textContent(), /No live-source sync recorded/);
    assert.equal(await page.locator('.site-header .site-identity img').evaluate(image => image.complete && image.naturalWidth > 0), true);
    assert.equal(await page.evaluate(() => getComputedStyle(document.body).backgroundColor), 'rgb(20, 22, 21)');
    await page.getByText('Filter by build stage', {exact:true}).click();
    const contrast = await page.evaluate(() => {
      const canvas = document.createElement('canvas'); canvas.width = canvas.height = 1;
      const ctx = canvas.getContext('2d');
      const rgb = color => { ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = color; ctx.fillRect(0, 0, 1, 1); return [...ctx.getImageData(0, 0, 1, 1).data]; };
      const lum = color => color.slice(0, 3).map(value => value / 255).map(value => value <= .04045 ? value / 12.92 : ((value + .055) / 1.055) ** 2.4).reduce((sum, value, i) => sum + value * [.2126, .7152, .0722][i], 0);
      return ['.sub', '.asap-summary', '.asap-coverage', '.course-card-status', '.header-install', 'nav a.active'].map(selector => {
        const node = document.querySelector(selector); let parent = node; let bg;
        while (parent) { bg = rgb(getComputedStyle(parent).backgroundColor); if (bg[3] === 255) break; parent = parent.parentElement; }
        const fg = lum(rgb(getComputedStyle(node).color)), back = lum(bg);
        return [selector, (Math.max(fg, back) + .05) / (Math.min(fg, back) + .05)];
      });
    });
    for (const [selector, ratio] of contrast) assert(ratio >= 4.5, `${selector} text contrast ${ratio.toFixed(2)} is too low`);
    if (process.env.UI_SCREENSHOT_DIR) { fs.mkdirSync(process.env.UI_SCREENSHOT_DIR, { recursive: true }); await page.screenshot({ path: path.join(process.env.UI_SCREENSHOT_DIR, 'overview-desktop.png'), fullPage: true }); }
    assert.equal(await page.locator('.asap-card[aria-expanded="false"]').count(), 4);
    assert.equal((await visible()).length, 4);
    await page.locator('#asap-synthesize').click();
    assert.deepEqual(await visible(), ['apwh', 'apush']);
    assert.equal(await page.locator('#asap-panel-synthesize').isVisible(), true);
    assert.match(await page.locator('.asap-unassigned').textContent(), /APUSH/);
    await page.locator('#asap-align').focus(); await page.keyboard.press('Enter');
    assert.deepEqual(await visible(), ['humgeo', 'apush']);
    await page.keyboard.press('Space'); assert.equal((await visible()).length, 4);
    await page.keyboard.press('Enter'); await page.keyboard.press('Escape');
    assert.equal(await page.locator('#asap-align').getAttribute('aria-expanded'), 'false');
    assert.equal(await page.locator('#asap-align').evaluate(node => node === document.activeElement), true);
    await page.locator('#asap-prove').click(); assert.deepEqual(await visible(), ['apush']);
    await page.locator('#asap-show-all').click(); assert.equal((await visible()).length, 4);
    await page.setViewportSize({ width: 375, height: 812 });
    await page.locator('#asap-assemble').click();
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'Mobile document overflows');
    const old = new Date(now - 48 * 3600000).toISOString();
    data.claims[0].observed_at = old; processValue.courses.humgeo.as_of = old;
    await page.evaluate(async () => { await AP4_DASHBOARD.refresh(); });
    assert.deepEqual(await visible(), ['humgeo', 'apush', 'psych']);
    assert.match(await page.locator('[data-course-card="humgeo"] .course-asap-position').textContent(), /stale/);
    processFails = true; await page.reload(); await ready();
    assert.match(await page.locator('#asap-stage-view').textContent(), /unavailable/);
    assert.equal((await visible()).length, 4);
    assert.equal(await page.locator('.asap-card').count(), 0);
    processFails = false;
    await page.goto('https://asap.test/humgeo.html'); await ready();
    assert.equal(await page.locator('.population-coverage tbody tr').count(), generated.population_scope.length);
    assert.equal(await page.locator('.population-recorded').count(), 0);
    assert.equal(await page.locator('#population-course').count(), 0, 'A course page must not switch to another course silently');
    await page.getByRole('link', {name:'APWH',exact:true}).click(); await ready();
    assert.equal(await page.locator('.population-recorded').count(), 1);
    assert.match(await page.locator('.population-recorded').textContent(), /0 \/ 10 accepted/);
    assert.equal(await page.locator('.population-pending').count(), generated.population_scope.length-1);
    assert.match(await page.locator('.population-pending').first().textContent(), /no finding about course completion/);
    processFails = true; await page.reload(); await ready();
    assert.match(await page.locator('[data-population-coverage]').textContent(), /unavailable/);
    assert.equal(await page.locator('.population-recorded').count(), 0);
    processFails = false;
    await page.goto('https://asap.test/updates.html');
    await page.waitForSelector('.update-item');
    for (const width of [320, 390]) {
      await page.setViewportSize({width, height:844});
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'Long update receipt overflows on mobile');
    }
    for (const filename of fs.readdirSync(__dirname).filter(name => name.endsWith('.html') && name !== 'builder.html')) {
      await page.goto(`https://asap.test/${filename}`);
      const expectedNav = ['index.html', 'about.html'].includes(filename) ? ['Get started','Docs','Spec'] : ['Courses','Docs','Impact'];
      assert.deepEqual(await page.locator('nav[aria-label="Main navigation"] > a').allTextContents(), expectedNav, filename);
      assert.equal(await page.locator('footer a[href="about.html"]').count(), 1, filename);
      const links = await page.locator('a[href]').evaluateAll(links => links.map(a => a.getAttribute('href')).filter(h => !/^(https?:|mailto:|#)/.test(h)));
      for (const href of links) { const target=href.split(/[?#]/)[0]; if(target) assert(fs.existsSync(path.join(__dirname,target)), `${filename} has broken local link: ${href}`); }
      assert.equal(await page.locator('.site-header a[href="https://github.com/joshuadurey-del/incept-course-builder"]').count(), 1, filename);
      assert.equal(await page.locator('.skip-link').count(), 1, filename);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, `${filename} overflows on mobile`);
    }
    await page.goto('https://asap.test/about.html');
    assert.equal(await page.locator('footer a[href="about.html"]').count(), 1);
    assert.equal(await page.locator('#install').count(), 1);
    await page.locator('.skip-link').focus(); await page.keyboard.press('Enter');
    assert.equal(await page.evaluate(() => location.hash), '#main-content');
    assert.equal(await page.evaluate(() => document.activeElement.id), 'main-content');
    await page.evaluate(() => { document.activeElement.blur(); scrollTo(0, 0); });
    if (process.env.UI_SCREENSHOT_DIR) await page.screenshot({ path: path.join(process.env.UI_SCREENSHOT_DIR, 'about-mobile.png'), fullPage: true });
    await page.goto('https://asap.test/economics.html');
    assert.match(await page.locator('#roi-result').textContent(), /Enter all five/);
    for (const [field, value] of Object.entries({ courses: 4, hours: 10, rate: 100, investment: 1000, operating: 100 })) await page.locator(`#roi-${field}`).fill(String(value));
    assert.match(await page.locator('#roi-result').textContent(), /\$2,600/);
    assert.match(await page.locator('#roi-result').textContent(), /260\.0%/);
    await page.locator('#roi-operating').fill('');
    assert.match(await page.locator('#roi-result').textContent(), /Enter all five/);
    await page.locator('#roi-operating').fill('0');
    assert.match(await page.locator('#roi-result').textContent(), /\$3,000/);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'ROI mobile overflow');
    if (process.env.UI_SCREENSHOT_DIR) await page.screenshot({ path: path.join(process.env.UI_SCREENSHOT_DIR, 'economics-mobile.png'), fullPage: true });
    assert.deepEqual(errors, []);
    console.log('Site browser PASS: Home/install, workspace routing, stage filters, course coverage, stale/failed loads, all-page links, mobile, keyboard/focus, About and Impact.');
  } finally { await browser.close(); }
}
if (process.argv.includes('--browser')) browserCheck().catch(error => { console.error(error); process.exitCode = 1; });

async function localBuilderCheck() {
  const { chromium } = playwrightRuntime();
  const browser = await chromium.launch({ channel: process.env.PLAYWRIGHT_CHANNEL || 'chrome', headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 1000 } });
    const errors = []; page.on('pageerror', error => errors.push(error.message));
    // Match app.local_state and screen.summary, rather than the retired checkpoint dashboard.
    let state = {course: 'Fixture course built here', command: "/tmp/Builder's bin/incept-course-builder",
      local: true, revision: 'fixture-revision', version: '0.fixture',
      build: {live: false, next: 'lessons/001/article.md', open: [{target: 'lessons/001/article.md'}],
        counts: {fetched: 1, derived: 1, answered: 1, authored: 0, person: 0}, targets: [
          {step: 'onboard', target: 'Owner account', state: 'done', provenance: 'own-run identity receipt'},
          {step: 's1-blueprint', target: 'blueprint.json', state: 'done', provenance: 'fetched'},
          {step: 's2-map', target: 'course-map.json', state: 'done', provenance: 'derived'},
          {step: 's3-content', target: 'lessons/001/article.md', state: 'open', provenance: 'factory verdict pending'},
          {step: 'p7-walk', target: 'Owner learner acceptance', state: 'todo', provenance: 'UNMEASURED'},
          {step: 'p8-release', target: 'Launch', state: 'todo', provenance: 'UNMEASURED'},
        ]},
      screen: {next_step: 's3-content', rows: [{step: 's3-content', label: 'Lessons with checks', detail: '0 of 1 articles accepted'}],
        missing: [{text: 'One lesson has no accepted article.', lessons: [{n: 1, unit: 1, topic: '1.1', code: 'fixture-lesson', title: 'Map skills'}]}],
        options: [{label: 'Continue this build', note: 'Review the next action in Terminal'}]},
      receipts: {'s3-content': {step: 's3-content', accepted: 0, result: '<script>bad()</script> pending verdict'}},
      course_map: {units: [{unit: 1, title: 'Map skills', lesson_count: 1, kind_counts: {Article: 1},
        topics: [{code: '1.1', title: 'Reading maps', kind_counts: {Article: 1}, lessons: [{title: 'Map skills', xp: 0, items: [{kind: 'Article', title: 'Map article', xp: 0}]}]}]}],
        kind_counts: {Article: 1}, total_xp: null, course_milestones: [], unassigned: 0}};
    let failState = false, reads = 0;
    const requests = [];
    await page.route('**/*', route => {
      const request = route.request(), url = new URL(request.url());
      requests.push([request.method(), url.origin, url.pathname]);
      assert.equal(url.origin, 'https://builder.test', 'Local page must not contact external or paid services');
      assert.equal(request.method(), 'GET', 'The local dashboard is read-only');
      const filename = url.pathname.slice(1) || 'builder.html';
      if (filename === 'local-state.json') {
        reads++;
        return route.fulfill(failState ? {status: 503, body: 'temporarily unavailable'} : {contentType: 'application/json', body: JSON.stringify(state)});
      }
      if (!['builder.html', 'builder.css', 'builder.js', 'builder-mark.svg'].includes(filename)) return route.fulfill({status: 404, body: ''});
      return route.fulfill({contentType: filename.endsWith('.js') ? 'text/javascript' : filename.endsWith('.css') ? 'text/css' : filename.endsWith('.svg') ? 'image/svg+xml' : 'text/html', body: fs.readFileSync(path.join(__dirname, filename))});
    });
    const waitFor = condition => page.waitForFunction(condition, null, {timeout: 12000});
    const tableRows = () => page.locator('#target-rows tr');
    await page.goto('https://builder.test');
    await waitFor(() => document.querySelector('#course').textContent === 'Fixture course built here');
    assert.equal(await page.locator('#revision').textContent(), 'LOCAL · 0.fixture');
    assert.match(await page.locator('#bar').textContent(), /3 \/ 6$/);
    assert.equal(await page.locator('#status').textContent(), 'WORK ORDERS OPEN');
    assert.match(await page.locator('#glance-now').textContent(), /Lessons with checks/);
    assert.equal(await page.locator('#glance-next').textContent(), '0 of 1 articles accepted');
    assert.match(await page.locator('#provenance').textContent(), /fetched 1 · derived 1 · answered 1 · authored 0 · person 0/);
    assert.equal(await page.locator('#step-strip li').count(), 5);
    assert.equal(await page.locator('#step-strip li.done').count(), 3);
    assert.equal(await page.locator('#step-strip li.current').count(), 1);
    assert.match(await page.locator('#needs-list').textContent(), /no accepted article.*Lesson 1.*Map skills.*Continue this build/s);
    assert.equal(await page.locator('input, textarea, form').count(), 0, 'Credentials and work remain in Terminal');
    assert.equal(await page.locator('a[href="courses.html"], [data-course-card], #population-course').count(), 0, 'No foreign-course monitoring or course switcher');

    await page.locator('details.details > summary').click();
    assert.equal(await tableRows().count(), state.build.targets.length);
    assert.deepEqual(await page.locator('.targets th').allTextContents(), ['Step', 'Target', 'State', 'Provenance']);
    assert.match(await tableRows().nth(3).textContent(), /Lessons with checks.*article.md.*open.*factory verdict pending/);
    assert.match(await tableRows().nth(4).textContent(), /Owner learner acceptance.*todo.*UNMEASURED/);
    await page.locator('#step-strip li').nth(3).focus(); await page.keyboard.press('Enter');
    assert.equal(await page.locator('#step-panel').isVisible(), true);
    assert.match(await page.locator('#panel-title').textContent(), /Lessons with checks/);
    assert.match(await page.locator('#panel-body').textContent(), /factory verdict pending.*accepted0.*<script>bad\(\)<\/script>/s);
    assert.equal(await page.locator('#panel-body script').count(), 0, 'Receipt text must not execute markup');
    await page.locator('#panel-close').click();
    assert.equal(await page.locator('#step-panel').isVisible(), false);
    await page.locator('#step-strip li').nth(2).focus(); await page.keyboard.press('Space');
    assert.match(await page.locator('#panel-body').textContent(), /1 units · 1 lessons · total XP UNMEASURED/);
    await page.locator('.map-topic > summary').click(); await page.locator('.map-lesson > summary').click();
    assert.match(await page.locator('.map-lesson ul').textContent(), /Map article · 0 XP/);
    await page.locator('#panel-close').click();

    state.connections = {observed_at: '2026-09-22T00:00:00Z', live_checks: true, checks: [
      {id: 'factory', label: 'Content Factory', state: 'CURRENT', detail: '<script>bad()</script> descriptor only'},
      {id: 'publication', label: 'TimeBack and AP One', state: 'SELECT_PUBLISH_CONFIG', detail: 'Native course configuration required'},
    ]};
    state.build.targets[3] = {...state.build.targets[3], state: 'done', provenance: 'own-run accepted receipt'};
    state.build.next = 'Owner learner acceptance'; state.build.open = [];
    state.screen = {next_step: 'p7-walk', rows: [{step: 'p7-walk', label: 'Walk and accept', detail: 'Owner walkthrough remains unmeasured'}],
      missing: [{text: 'Confirm this new course in the learner view.'}], options: [{label: 'Continue this build'}]};
    await waitFor(() => document.querySelector('#glance-next').textContent === 'Owner walkthrough remains unmeasured');
    assert.ok(reads >= 2, 'Progress must refresh without a reload');
    assert.match(await page.locator('#bar').textContent(), /4 \/ 6$/);
    assert.equal(await tableRows().count(), 6, 'Polling must replace target rows, not duplicate them');
    assert.equal(await page.locator('#step-strip li').count(), 5, 'Polling must replace step controls');
    assert.equal(await page.locator('#status').textContent(), 'BUILDING', 'Partial receipts must not claim the course is live');
    assert.equal(await page.locator('#connection-list li').count(), 2);
    assert.match(await page.locator('#connection-list').textContent(), /Content Factory.*current.*<script>bad/s);
    assert.equal(await page.locator('#connection-list script').count(), 0);
    assert.match(await page.locator('#connections-note').textContent(), /Native checks observed 2026-09-22/);
    await page.goto('about:blank'); await page.goBack();
    await waitFor(() => document.querySelector('#course')?.textContent === 'Fixture course built here');
    assert.equal(await tableRows().count(), 6);
    assert.equal(await page.locator('#connection-list li').count(), 2);
    assert.deepEqual(await page.locator('section.outcomes h2').allTextContents(), ['Targets']);
    assert.equal(await page.locator('#start-command').textContent(), "'/tmp/Builder'\\''s bin/incept-course-builder'");
    await page.locator('#copy-command').focus(); await page.keyboard.press('Enter');
    await waitFor(() => document.querySelector('#copy-status').textContent.length > 0);
    assert.equal(await page.locator('#copy-command').isEnabled(), true);
    for (const width of [320, 375]) {
      await page.setViewportSize({width, height: 812});
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'Local mobile document overflows');
    }
    if (process.env.BUILDER_SCREENSHOT) await page.screenshot({path: process.env.BUILDER_SCREENSHOT, fullPage: true});

    failState = true;
    await waitFor(() => document.querySelector('#live-status').textContent.includes('Reconnecting'));
    assert.equal(await page.locator('#glance-next').textContent(), 'Owner walkthrough remains unmeasured');
    assert.equal(await tableRows().count(), 6, 'Transient failure must preserve the last measured state');
    failState = false; state.command = null;
    const beforeInvalid = reads;
    await page.waitForResponse(response => response.url().endsWith('local-state.json') && response.status() === 200, {timeout: 12000});
    await waitFor(() => document.querySelector('#live-status').textContent.includes('Reconnecting'));
    assert.ok(reads > beforeInvalid, 'The malformed response must actually be read');
    assert.equal(await page.locator('#glance-next').textContent(), 'Owner walkthrough remains unmeasured');
    assert.equal(await tableRows().count(), 6);

    // app.local_state deliberately returns an empty build for a workspace not built here.
    state = {course: null, command: '/tmp/incept-course-builder', local: true, version: '0.fixture',
      build: {targets: [], live: false}, workorders: [], receipts: {}};
    await waitFor(() => document.querySelector('#course').textContent === 'not chosen yet');
    assert.equal(await page.locator('#status').textContent(), 'NOT STARTED');
    assert.match(await page.locator('#bar').textContent(), /0 \/ 0$/);
    assert.equal(await tableRows().count(), 0);
    assert.equal(await page.locator('#connection-list li').count(), 0, 'A new empty workspace must not show old connection rows');
    assert.equal(await page.locator('#needs-you').isVisible(), false);
    assert.equal(await page.locator('#provenance').textContent(), '');
    assert.match(await page.locator('#live-status').textContent(), /^Live/);
    assert.doesNotMatch(await page.locator('main').textContent(), /Fixture course built here|Owner learner acceptance|own-run accepted receipt/);
    assert(requests.every(([method, origin]) => method === 'GET' && origin === 'https://builder.test'));
    assert.deepEqual(errors, []);
    console.log('Local browser PASS: own-run Targets/progress, unmeasured acceptance and XP, safe receipt text, native connections, polling/no duplicates, failed/malformed-state recovery, empty workspace isolation, keyboard panels/copy, literal command, read-only requests and mobile.');
  } finally { await browser.close(); }
}
if(process.argv.includes('--local'))localBuilderCheck().catch(error=>{console.error(error);process.exitCode=1;});
