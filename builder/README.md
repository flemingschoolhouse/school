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
- Each new week: update DAYS dates in lib.py, write the new week's content in the content modules,
  bump week/level numbers, rebuild, copy web pages to root + weeks/<date>/, add the week to index.html.
