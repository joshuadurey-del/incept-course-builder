#!/usr/bin/env python3
"""Render spec.html from SPEC.md so the human page and the agent-read Markdown never drift.

Run from the repository root: python3 bin/build-spec-page.py. Stdlib only. The page reuses
retro.html's head, header and navigation so the site shell stays identical.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

def render(markdown):
    lines = markdown.splitlines(); out = []; i = 0; code = None
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            if code is None: code = []
            else: out.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>'); code = None
            i += 1; continue
        if code is not None: code.append(line); i += 1; continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            rows = [r for r in rows if not all(re.fullmatch(r':?-+:?', c) for c in r)]
            head, body = rows[0], rows[1:]
            table = '<table class="spec">'
            if any(head): table += '<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead>'
            table += '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in body) + '</tbody></table>'
            out.append(table); continue
        heading = re.match(r'^(#{1,3}) (.*)', line)
        if heading:
            level, text = len(heading.group(1)), heading.group(2)
            slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
            out.append(f'<h1>{inline(text)}</h1>' if level == 1 else f'<h{level} id="{slug}">{inline(text)}</h{level}>')
            i += 1; continue
        if re.match(r'^(- |\d+\. )', line):
            tag = 'ul' if line.startswith('- ') else 'ol'; items = []
            while i < len(lines) and re.match(r'^(- |\d+\. )', lines[i]):
                items.append(re.sub(r'^(- |\d+\. )', '', lines[i])); i += 1
            out.append(f'<{tag} class="work-list">' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>'); continue
        if not line.strip(): i += 1; continue
        para = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||- |\d+\. |```)', lines[i]): para.append(lines[i]); i += 1
        out.append('<p>' + inline(' '.join(para)) + '</p>')
    return '\n  '.join(out)

def main():
    retro = (ROOT / 'retro.html').read_text()
    head = retro.split('<main id="main-content" tabindex="-1">')[0]
    head = re.sub(r'href="style\.css(?:\?[^"]*)?"', 'href="style.css?v=20260922-spec-containment"', head)
    head = head.replace('<title>Publication runbook retro</title>', '<title>Course Builder spec sheet</title>')
    head = head.replace('<a href="spec.html">Spec sheet</a><a href="retro.html" aria-current="page" class="active">Runbook</a>',
                        '<a href="spec.html" aria-current="page" class="active">Spec sheet</a><a href="retro.html">Runbook</a>')
    footer = retro.split('</main>')[1].split('<script')[0]
    body = render((ROOT / 'SPEC.md').read_text())
    page = (head + '<main id="main-content" tabindex="-1">\n  <section id="spec-sheet">\n  ' + body +
            '\n  <p class="sub">Source of this page: <a href="SPEC.md">SPEC.md</a> in the repository, rendered by <code>bin/build-spec-page.py</code>. Agents read the Markdown; the machine summary at the end is the contract.</p>\n  </section>\n</main>' + footer + '</body></html>\n')
    (ROOT / 'spec.html').write_text(page)
    print('spec.html', len(page), 'bytes')

if __name__ == '__main__': main()
