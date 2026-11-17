from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.title=False;self.desc=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='description':self.desc=True
  for k in ('href','src'):
   if k in a:self.links.append(a[k])
pages={}
for f in root.rglob('*.html'):
 q=Page();q.feed(f.read_text());pages[f]=q
errors=[]
for f,q in pages.items():
 if len(q.ids)!=len(set(q.ids)):errors.append(f'{f}: duplicate IDs')
 if not q.title:errors.append(f'{f}: missing title')
 if f.parent==root and f.name!='404.html' and not q.desc:errors.append(f'{f}: missing description')
 for link in q.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{f}: missing {link}')
  elif u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{f}: missing fragment {link}')
for f in (root/'assets').glob('*.svg'):ET.parse(f)
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML files; local links, assets, fragments, titles, descriptions, unique IDs and SVG XML.')
