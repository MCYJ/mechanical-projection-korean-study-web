from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,re,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];D=R/'dist';BASE='/mechanical-projection-korean-study-web/';ORIGIN='https://mcyj.github.io';files=list(D.rglob('*.html'));assert len(files)==42
class Page(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.h1=0;self.attrs=[];self.form=False;self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.attrs.append((tag,a))
  if tag=='h1':self.h1+=1
  if tag=='form':self.form=True
  if tag=='html':self.lang=a.get('lang')
checks=[];links=0
for p in files:
 raw=p.read_text();page=Page();page.feed(raw);assert page.h1==1,p;assert not page.form,p
 for tag,a in page.attrs:
  if tag=='img':assert 'alt' in a,p
  for name in ['href','src']:
   u=a.get(name)
   if not u or u.startswith(('mailto:','#')):continue
   parsed=urlsplit(u)
   if parsed.scheme or parsed.netloc:
    assert parsed.scheme=='https',(p,u)
    assert parsed.netloc not in ['apps.apple.com','play.google.com','itunes.apple.com'],('Unverified store CTA',p,u)
    if parsed.netloc!='mcyj.github.io' or not parsed.path.startswith(BASE):continue
   if not parsed.path.startswith(BASE):continue
   part=unquote(parsed.path[len(BASE):]);target=D/part
   if not target.suffix:target=target/'index.html'
   assert target.is_file(),(p,u);assert target.resolve().is_relative_to(D.resolve());links+=1
 if p.name=='404.html':continue
 canonical=[a['href'] for t,a in page.attrs if t=='link' and a.get('rel')=='canonical'];route=str(p.relative_to(D)).removesuffix('index.html');assert canonical==[ORIGIN+BASE+route],(p,canonical)
 desc=[a.get('content','') for t,a in page.attrs if t=='meta' and a.get('name')=='description'];assert len(desc)==1 and len(desc[0])>15,p
 alt=[a.get('hreflang') for t,a in page.attrs if t=='link' and a.get('rel')=='alternate'];assert sorted(alt)==['en','ko','x-default'],p
 if route:
  schema=re.findall(r'<script type="application/ld\+json">(.*?)</script>',raw,re.S);assert len(schema)==1;pdata=json.loads(schema[0]);assert pdata['url']==canonical[0] and pdata['inLanguage']==page.lang
 checks.append({'path':str(p.relative_to(D)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
urls=[x.text for x in ET.parse(D/'sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')];assert len(urls)==41 and len(set(urls))==41
G=json.loads((R/'content/guides.json').read_text());assert len(G)==10
for g in G:assert len(g['sections'])>=3 and len({s[1][0] for s in g['sections']})==3 and all(len(s[0][1])>50 and len(s[1][1])>100 for s in g['sections'])
js=(D/'assets/site.js').read_text();assert not re.search(r'fetch\s*\(|XMLHttpRequest|WebSocket|localStorage|sessionStorage|document\.cookie|sendBeacon',js)
for p in D.rglob('*'):
 if p.is_file():
  assert p.suffix.lower() not in ['.p8','.ipa','.aab','.apk','.mobileprovision','.keystore','.jks','.dart','.swift','.zip']
  if p.suffix in ['.js','.html','.css','.xml','.txt']:assert 'PRIVATE KEY-----' not in p.read_text()
(R/'qa').mkdir(exist_ok=True);proof={'status':'passed_static_site_structure_and_release_claim_checks','htmlFiles':42,'indexableRoutes':41,'guideLocales':['ko','en'],'guidesPerLocale':10,'resolvedLocalLinks':links,'allImagesHaveAlt':True,'allLanguagePageCanonicalAndHreflangVerified':True,'unverifiedDownloadLinks':0,'messageSubmissionForms':0,'siteJavaScriptNetworkOrPersistenceCalls':0,'privateAppOrSigningFiles':0,'files':checks};(R/'qa/static-checks-v1.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps({k:v for k,v in proof.items() if k!='files'}))
