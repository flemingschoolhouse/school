# Fleming Schoolhouse weekly packet builder

Python code that builds Grace's weekly homeschool packets (one PDF per kid + Mom's Guide)
and the tablet web pages published on this site.

- Content for a week lives in: morning.py, geography.py, mult.py, speech.py, electives.py,
  plans.py (Mom's lesson plans), core_nevaeh.py, core_nylah.py, core_naomi.py, core_young.py.
- Shared layout/helpers: lib.py (no-yellow palette, school-print stroke font, page frame),
  mathgen.py, worldmap.py, core_common.py. Rendering: render.py (Playwright).
- build.py -> PDFs in /home/claude/out ; web.py -> tablet HTML in /home/claude/web
  (both expect the .py files to sit in /home/claude).
- Site layout: root <kid>.html = CURRENT week (tablet home-screen shortcuts point here);
  weeks/<YYYY-MM-DD>/<kid>.html = archive; index.html lists current + past weeks.
- Mom page: mompage.py builds mom-96b4fb.html (unlisted; lesson plans, answer keys, kid links, PDF print links in weeks/<date>/pdf/).
- Each new week: update DAYS dates in lib.py, write the new week's content in the content modules,
  bump week/level numbers, rebuild, copy web pages to root + weeks/<date>/, add the week to index.html.
- Progress saving: pages sync answers + per-page progress to Grace's Google Apps Script web app (API in web.py;
  script source in builder/progress-sheet-script.gs). Each new week set WEEK in web.py AND WEEK/LABEL in mompage.py
  to the new Tuesday date so progress is tracked per week. Never change API. Mom's Corner shows the progress board;
  <kid>.html?view=1 shows a kid's synced answers (drawings stay on the tablet).
