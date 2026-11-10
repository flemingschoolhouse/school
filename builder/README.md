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
  to the new Tuesday date so progress is tracked per week. Never change API.
  IMPORTANT: the week key sent to the sheet is 'wk-'+WEEK (web.py SCHOOL config, mompage.py DASH). A bare date like
  '2026-11-03' gets auto-converted to a Date by Google Sheets and then never matches again (Mom's board showed nothing). Keep the 'wk-' prefix.
  Kid pages also sync once on open; Mom's board auto-refreshes every 60s, has a Refresh button and per-kid "answers" buttons. Mom's Corner shows the progress board;
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

## Week of Nov 10, 2026 notes
- Week dates/labels now live in ONE place: DAYS + WEEK_ISO/WEEK_SHORT/WEEK_RANGE/WEEK_LONG in lib.py (build.py uses them for covers, headers, PDF names).
  Still also set WEEK in web.py and WEEK/LABEL (+ PDF names) in mompage.py.
- Nariah's subjects are in core_nariah.py, Titus's + Nayeli's Pre-K pages in core_titus.py (both import small helpers from core_young.py, which holds the Nov 3 week).
- test_core.py renders one module to PNGs and reports OVERFLOW / missing videos / answer keys:
  `python3 test_core.py core_nevaeh` or `python3 test_core.py core_titus titus_math --nayeli`.
- While building, new video ids can go in /home/claude/vids_<name>.py (V = {...}); fold them into videos.py before committing.

## Fall break + UNDATED packets (Grace, Nov 9 2026)
- Fall break was Fri Nov 6 – Mon Nov 16; back to school Tue Nov 17. The kids had finished Days 1–3 of the Nov 3 packet.
  Plan: Nov 17–18 = Days 4–5 of the Nov 3 packet · Nov 19–21 = Days 1–3 of the Nov 10 packet · Nov 24–25 = its Days 4–5 ·
  Thanksgiving Nov 26–28 off · next NEW packet starts Tue Dec 1 (Sunday build Nov 29). No new packets on Nov 15 or Nov 22.
- Grace wants packets UNDATED: pages show DAY N only, no weekday or date, so a packet can start on any day and slide when life happens.
  lib.UNDATED = True does this (page headers/footers, covers, Mom's Guide). Keep WEEK_ISO / WEEK in web.py / mompage.py as the Tuesday the
  packet was built for — it is only the folder name + progress key now. Don't write "today is <holiday/date>" into lessons.
- The Nov 3 and Nov 10 tablet pages and the Nov 10 PDFs were un-dated in place (the PDFs by covering the date text; they were not rebuilt).
  The root kid pages carry a "Welcome back — finish Day 4 & 5 first" banner linking to weeks/2026-11-03/; it disappears with the next build.
- mompage.py: the "'s answers" button text must not use \' inside the non-raw DASH string (Python drops the backslash and the
  progress-board script dies with a syntax error — that happened in the Nov 10 build). It now uses a curly apostrophe.
