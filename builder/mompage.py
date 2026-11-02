import sys, os, shutil
sys.path.insert(0, "/home/claude")
import lib; lib.WEB["on"] = True
import build, web
from lib import CSS, esc

WEEK, LABEL = "2026-11-03", "November 3–7, 2026"
REPO = "/home/claude/school"
KIDS = ["Nevaeh", "Nylah", "Naomi", "Nariah", "Titus", "Nayeli"]
pdfdir = f"{REPO}/weeks/{WEEK}/pdf"; os.makedirs(pdfdir, exist_ok=True)
names = {}
for k in KIDS + ["Mom's Guide"]:
    src = f"/home/claude/out/{k} - Week of Nov 3.pdf"; dst = k.lower().replace("'", "").replace(" ", "-") + ".pdf"
    shutil.copy(src, f"{pdfdir}/{dst}"); names[k] = dst

import mult
for i in range(5): mult.mult_page("x", i)
M = build.build_mom()
pages = "".join(p for p in M.pages if 'class="page blank"' not in p)
btn = lambda href, txt, col: f'<a class="mb" href="{href}" style="background:{col}">{txt}</a>'
top = (f'<div class="mhead"><h1>Mom\'s Corner</h1><p>Week of {LABEL}</p>'
       '<h2>Kids\' pages</h2><div class="row">' + "".join(btn(f"{k.lower()}.html", k, "#4338ca") for k in KIDS) + '</div>'
       '<h2>Print the packets (PDF)</h2><div class="row">' + "".join(btn(f"weeks/{WEEK}/pdf/{names[k]}", f"🖨 {k}", "#6d28d9") for k in KIDS + ["Mom's Guide"]) + '</div>'
       '<h2>Lesson plans & answer keys</h2><p class="small">Scroll down — this is your Mom\'s Guide. This page isn\'t linked from the kids\' home page.</p></div>')
MCSS = """.mhead{max-width:816px;margin:0 auto;padding:16px;font-family:Poppins,sans-serif;color:#1f2a5c;text-align:center}
.mhead h1{margin:6px 0 0;font-size:32px}.mhead h2{font-size:18px;margin:18px 0 8px}.row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.mb{color:#fff;text-decoration:none;font-weight:600;padding:10px 16px;border-radius:20px;font-size:15px}"""
html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<meta name='robots' content='noindex'><title>Mom's Corner · Week of Nov 3</title>"
        f"<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@400;500;600;700&display=swap'>"
        f"<style>{CSS}{web.WEBCSS}{MCSS}</style></head><body>{top}{pages}"
        "<script>function fit(){var w=Math.min(window.innerWidth-12,816);document.querySelectorAll('.page').forEach(function(p){p.style.zoom=(w/816)})}window.addEventListener('resize',fit);fit();</script></body></html>")
open(f"{REPO}/mom-96b4fb.html", "w").write(html)
shutil.copy(f"{REPO}/mom-96b4fb.html", f"{REPO}/weeks/{WEEK}/mom-96b4fb.html")
print("ok")
