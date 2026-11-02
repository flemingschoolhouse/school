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

## Less writing: mix in multiple choice (Grace's request, Nov 2 2026)
- About HALF of each kid's independent questions should be multiple choice instead of written/typed answers. Not exactly half — just mix it up.
- **Nariah (2nd grade, still learning to write): mostly multiple choice/tap** — keep her tracing and drawing, but almost no free-writing answers.
- Titus (K): tracing and number writing are the skill practice, so keep those.
- Helpers in core_common.py (work on paper AND tablet — kids circle on paper, tap on the tablet; answers save and count toward progress):
  - `qs([("question", ["correct", "wrong", "wrong"]), ("written question", 2)])` — a list of choices makes it multiple choice; correct answer FIRST (order is shuffled automatically and stays the same every build).
  - `mc(question, choices, num)` for a one-off question; `pick("I", "me")` for an inline "(I / me)" choice inside a sentence.
  - `mark_list(items, choices)` for sort/label lists (each item gets tappable choice bubbles) — use instead of fill-in tables for sorting.
- Keep journals, "explain/defend" questions, and paragraph writing as written work (roughly the other half).

## Chore Quest (daily game checklists — added Nov 2 2026)
- builder/quest.py builds quest-<kid>.html (+ .webmanifest and icons/quest-<kid>.png) at the site ROOT. These are NOT weekly — don't copy them into weeks/.
  Edit routines, Grace's family chore chart (TEAM), team-chore goals, XP, levels, rewards and badges in its CONFIG section, then run `python3 quest.py`.
- index.html has a "🎮 Daily Quest" row linking each kid's quest page — keep it when updating the week lines.
- mompage.py imports quest.MOM_BOARD (Chore Quest scoreboard + "Inspection passed" buttons) into Mom's Corner — keep that import.
- Saves through the same Apps Script API (kid/week rows "quest-stats" and "questmom"); no script changes needed.
