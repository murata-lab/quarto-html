"""Update this gh-pages worktree from a separate main checkout.

uv run --with beautifulsoup4 python build.py /path/to/quarto-html
Only generated site copies are written; the original deck is never modified.
"""
from pathlib import Path
import shutil
import subprocess
import sys
from bs4 import BeautifulSoup

source = Path(sys.argv[1]).resolve()
site = Path(__file__).resolve().parent
original = source / 'output/nco-intro.html'
doc = BeautifulSoup(original.read_text(), 'html.parser')
slide = doc.select_one('section.slide#background')
if slide is None:
    raise SystemExit('Missing slide: background')
slide['class'] = list(slide.get('class', [])) + ['active']
slide['aria-hidden'] = 'false'
sample = BeautifulSoup('<!doctype html><html lang="ja"><head></head><body><div class="reveal"><main id="stage" class="slides"></main></div></body></html>', 'html.parser')
for tag in list(doc.head.contents):
    sample.head.append(tag.extract())
sample.title.string = '研究背景 — アニメーション例'
sample.select_one('#stage').append(slide.extract())
style = sample.new_tag('style')
style.string = 'html,body{margin:0;overflow:hidden;background:#fff} .page-number{display:none!important}'
sample.head.append(style)
script = sample.new_tag('script', src='demo.js')
sample.body.append(script)
(site / 'background.html').write_text(str(sample))
for suffix in ['html', 'pdf']:
    shutil.copy2(source / f'output/nco-intro.{suffix}', site / f'nco-intro.{suffix}')
revision = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
(site / 'source-revision.txt').write_text(revision + '\n')
(site / '.nojekyll').touch()
print(f'Extracted background slide; source revision: {revision}')
