import sys, os, shutil
sys.path.insert(0, "/home/claude")
import lib; lib.WEB["on"] = True
import build, web
from web import API, WEEK as WK
from lib import CSS, esc

WEEK, LABEL = "2026-11-03", "November 3–7, 2026"
REPO = "/home/claude/school"
KIDS = ["Nevaeh", "Nylah", "Naomi", "Nariah", "Titus", "Nayeli"]
pdfdir = f"{REPO}/weeks/{WEEK}/pdf"; os.makedirs(pdfdir, exist_ok=True)
names = {}
for k in KIDS + ["Mom's Guide"]:
    src = f"/home/claude/out/{k} - Week of Nov 3.pdf"; dst = k.lower().replace("'", "").replace(" ", "-") + ".pdf"
    shutil.copy(src, f"{pdfdir}/{dst}"); names[k] = dst

import mult, quest
for i in range(5): mult.mult_page("x", i)

DASH = """<div class="mhead" id="progress"><h2>📊 Progress this week</h2><div id="pg">Loading…</div>
<p class="small">Updates a few seconds after the kids type. ✅ done · 🟡 started · ⬜ not started. Drawings save on the tablet only.</p></div>
<style>#pg table{width:100%;border-collapse:collapse;font:14px Poppins,sans-serif}#pg td,#pg th{border:1px solid #d6d6e0;padding:6px;text-align:center}
#pg th{background:#eef1fb}#pg .kid{font-weight:700;text-align:left}#pg details{text-align:left;margin:6px 0;font:13px Poppins}#pg summary{cursor:pointer;font-weight:600;color:#4338ca}
#pg li{margin:2px 0}.c2{background:#e4f6e7}.c1{background:#fff4cc}</style>
<script>
(function(){var API='__API__',WEEK='__WK__',KIDS=['Nevaeh','Nylah','Naomi','Nariah','Titus','Nayeli'];
fetch(API+'?action=all&week='+WEEK).then(function(r){return r.json()}).then(function(j){
 var rows={};(j.rows||[]).forEach(function(r){rows[r.kid]=r});
 var h='<table><tr><th>Kid</th><th>Day 1</th><th>Day 2</th><th>Day 3</th><th>Day 4</th><th>Day 5</th></tr>',det='';
 KIDS.forEach(function(k){var r=rows[k];h+='<tr><td class="kid">'+k+'</td>';
  for(var d=1;d<=5;d++){if(!r){h+='<td>—</td>';continue}var tot=0,dn=0,st=0;
   for(var key in r.progress){if(key.indexOf('D'+d+'|')===0){tot++;if(r.progress[key]==2)dn++;else if(r.progress[key]==1)st++}}
   var cls=tot&&dn==tot?'c2':(dn||st?'c1':'');h+='<td class="'+cls+'">'+(tot?dn+'/'+tot:'—')+'</td>'}
  h+='</tr>';
  if(r){var li='';Object.keys(r.progress).sort().forEach(function(key){var v=r.progress[key],p=key.split('|');
    li+='<li>'+(v==2?'✅':v==1?'🟡':'⬜')+' Day '+p[0].slice(1)+' · '+p[1]+' — '+p[2]+'</li>'});
   det+='<details><summary>'+k+' — last saved '+new Date(r.saved).toLocaleString()+' · <a href="'+k.toLowerCase()+'.html?view=1">see answers</a></summary><ul>'+li+'</ul></details>'}});
 document.getElementById('pg').innerHTML=h+'</table>'+det;
}).catch(function(){document.getElementById('pg').textContent='Could not load progress right now — try refreshing.'});})();
</script>""".replace("__API__", API).replace("__WK__", WK)

M = build.build_mom()
pages = "".join(p for p in M.pages if 'class="page blank"' not in p)
btn = lambda href, txt, col: f'<a class="mb" href="{href}" style="background:{col}">{txt}</a>'
top = (f'<div class="mhead"><h1>Mom\'s Corner</h1><p>Week of {LABEL}</p>'
       '<h2>Kids\' pages</h2><div class="row">' + "".join(btn(f"{k.lower()}.html", k, "#4338ca") for k in KIDS) + '</div>'
       '<h2>Print the packets (PDF)</h2><div class="row">' + "".join(btn(f"weeks/{WEEK}/pdf/{names[k]}", f"🖨 {k}", "#6d28d9") for k in KIDS + ["Mom's Guide"]) + '</div>'
       + DASH + quest.MOM_BOARD + '<div class="mhead"><h2>Lesson plans & answer keys</h2><p class="small">Scroll down — this is your Mom\'s Guide. This page isn\'t linked from the kids\' home page.</p></div></div>')
MCSS = """.mhead{max-width:816px;margin:0 auto;padding:16px;font-family:Poppins,sans-serif;color:#1f2a5c;text-align:center}
.mhead h1{margin:6px 0 0;font-size:32px}.mhead h2{font-size:18px;margin:18px 0 8px}.row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.mb{color:#fff;text-decoration:none;font-weight:600;padding:10px 16px;border-radius:20px;font-size:15px}"""
html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<meta name='robots' content='noindex'><title>Mom's Corner · Week of Nov 3</title>"
        f"<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@400;500;600;700&display=swap'>"
        f"<style>{CSS}{web.WEBCSS}{MCSS}</style></head><body>{top}{pages}{web.MODAL}"
        "<script>function fit(){var w=Math.min(window.innerWidth-12,816);document.querySelectorAll('.page').forEach(function(p){p.style.zoom=(w/816)})}window.addEventListener('resize',fit);fit();</script></body></html>")
open(f"{REPO}/mom-96b4fb.html", "w").write(html)
shutil.copy(f"{REPO}/mom-96b4fb.html", f"{REPO}/weeks/{WEEK}/mom-96b4fb.html")
print("ok")
