"""Build i18n data into index.html.

Source of truth: locales/ru.json + locales/en.json
Usage:  python build.py
It validates key parity + data-lang coverage, then (re)generates the
`const translations = {...}` block between /*__I18N_BEGIN__*/ and /*__I18N_END__*/.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(ROOT, 'index.html')
RU = os.path.join(ROOT, 'locales', 'ru.json')
EN = os.path.join(ROOT, 'locales', 'en.json')

with io.open(RU, 'r', encoding='utf-8') as f:
    ru = json.load(f)
with io.open(EN, 'r', encoding='utf-8') as f:
    en = json.load(f)

if set(ru) != set(en):
    print('FAIL: key mismatch')
    print('  only ru:', sorted(set(ru) - set(en)))
    print('  only en:', sorted(set(en) - set(ru)))
    sys.exit(1)

with io.open(HTML, 'r', encoding='utf-8') as f:
    html = f.read()

used = set(re.findall(r'data-lang="([A-Za-z0-9_]+)"', html))
missing = used - set(ru)
if missing:
    print('FAIL: data-lang keys missing in locales:', sorted(missing))
    sys.exit(1)
unused = set(ru) - used
if unused:
    print('WARN unused keys (kept):', sorted(unused))

dump = json.dumps({'ru': ru, 'en': en}, ensure_ascii=False, indent=4)
block = '/*__I18N_BEGIN__*/\n        const translations = ' + dump + ';\n        /*__I18N_END__*/'

pat = re.compile(r'/\*__I18N_BEGIN__\*/.*?/\*__I18N_END__\*/', re.S)
if not pat.search(html):
    print('FAIL: i18n markers not found in index.html')
    sys.exit(1)

html = pat.sub(lambda _: block, html, count=1)

with io.open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print('OK: %d keys per language, %d data-lang usages covered' % (len(ru), len(used)))
