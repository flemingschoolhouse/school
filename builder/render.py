import asyncio, sys
from playwright.async_api import async_playwright

CHECK = """() => { const out=[]; document.querySelectorAll('.page').forEach((p,i)=>{
  const b=p.querySelector('.body'); if(!b) return;
  if (b.scrollHeight > b.clientHeight+2) out.push([i+1, b.scrollHeight-b.clientHeight, (p.querySelector('.subj .t')||{}).textContent]);
}); return out; }"""

async def render_many(jobs):
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page()
        for html_path, pdf_path in jobs:
            await pg.goto("file://" + html_path)
            await pg.wait_for_load_state("networkidle")
            over = await pg.evaluate(CHECK)
            if over:
                print("OVERFLOW", pdf_path, over)
            await pg.pdf(path=pdf_path, width="8.5in", height="11in", print_background=True,
                         margin=dict(top="0", bottom="0", left="0", right="0"))
            print("ok", pdf_path)
        await br.close()

def render(jobs):
    asyncio.run(render_many(jobs))
