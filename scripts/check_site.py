"""Dependency-free static checks for Kunal's Data Lab site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.hrefs = []
        self.assets = []
        self.cards = 0
        self.filter_options = set()
        self.categories = []
        self.has_main = False
        self.has_description = False
        self.has_h1 = False

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if 'id' in props:
            self.ids.append(props['id'])
        if tag == 'main':
            self.has_main = True
        if tag == 'h1':
            self.has_h1 = True
        if tag == 'meta' and props.get('name') == 'description':
            self.has_description = bool(props.get('content'))
        if tag == 'a':
            self.hrefs.append(props.get('href',''))
        if tag in ('script', 'link'):
            file = props.get('src') or props.get('href','')
            if file and not urlparse(file).scheme and not file.startswith('#'):
                self.assets.append(file)
        if tag == 'article' and 'project-card' in props.get('class','').split():
            self.cards += 1
            self.categories.append(props.get('data-category'))
        if tag == 'button' and 'data-filter' in props:
            self.filter_options.add(props['data-filter'])

p = SiteParser()
p.feed((ROOT/'index.html').read_text(encoding='utf-8'))
assert p.has_main and p.has_h1 and p.has_description, 'Missing page structure or metadata'
assert len(p.ids)==len(set(p.ids)), 'Duplicate HTML ids'
assert all(h[1:] in p.ids for h in p.hrefs if h.startswith('#')), 'Broken internal anchor'
assert all((ROOT/a.removeprefix('./')).is_file() for a in p.assets), 'Missing local asset'
assert p.cards == 6, f'Expected six featured projects, got {p.cards}'
assert {'all', *p.categories} == p.filter_options, 'Project filters mismatch categories'
assert (ROOT/'.nojekyll').is_file(), 'Missing GitHub Pages .nojekyll file'
print('PASS: metadata, headings, anchors, unique IDs, asset files, six project cards, filters, .nojekyll')
