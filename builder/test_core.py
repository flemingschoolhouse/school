# Quick test harness: render one core module's Subjects to a PDF + PNG previews and report overflow / missing videos.
# usage: python3 test_core.py core_nevaeh            (module with build())
#        python3 test_core.py core_young nariah_math nariah_english ...   (named Subject functions)
#        python3 test_core.py core_young --nayeli   (Nayeli pre-K pages)
import sys, os, asyncio
sys.path.insert(0, "/home/claude")
import importlib, lib
from lib import Packet, CSS
from playwright.async_api import async_playwright
from render import CHECK

mod = importlib.import_module(sys.argv[1])
names = sys.argv[2:]
pages, keys = [], []
if names == ["--nayeli"]:
    for i in range(5): pages += mod.nayeli_pages(i)
else:
    subs = [getattr(mod, n)() for n in names] if names else mod.build()
    for S in subs:
        for i in range(5):
            pages.append(S.days[i]); keys.append(f"{S.kid} {S.subject} D{i+1} {S.titles[i]}: {S.keys[i]}")
P = Packet("t", "t"); P.pages = pages
out = f"/home/claude/test_{sys.argv[1]}{'_' + '_'.join(names) if names else ''}".replace("--", "")
open(out + ".html", "w").write(P.html())

async def go():
    async with async_playwright() as p:
        br = await p.chromium.launch(); pg = await br.new_page(viewport={"width": 816, "height": 1056})
        await pg.goto("file://" + out + ".html"); await pg.wait_for_load_state("networkidle")
        over = await pg.evaluate(CHECK)
        print("OVERFLOW:", over if over else "none")
        os.makedirs(out + "_png", exist_ok=True)
        n = await pg.evaluate("document.querySelectorAll('.page').length")
        for k in range(n):
            el = (await pg.query_selector_all(".page"))[k]
            await el.screenshot(path=f"{out}_png/p{k+1:02d}.png")
        await br.close()
asyncio.run(go())
print("MISSING VIDEOS:", sorted(lib.MISSING) if lib.MISSING else "none")
print("PNG previews:", out + "_png/")
print("\n".join(keys))
