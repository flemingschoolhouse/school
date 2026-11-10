import sys, os
sys.path.insert(0, "/home/claude")
from lib import *
from render import render
import morning, geography, mult, speech, electives, plans
import core_nevaeh, core_nylah, core_naomi
from core_nariah import nariah_math, nariah_english, nariah_science, nariah_ss
from core_titus import titus_math, titus_letters, titus_science, nayeli_pages

OUT = "/home/claude/out"; os.makedirs(OUT, exist_ok=True)

KIDS = {
 "Nevaeh": dict(grade="8th Grade", morning="teen", core=core_nevaeh.build(), mult="mm", speech=False, geo=True, el=True),
 "Nylah":  dict(grade="7th Grade", morning="teen", core=core_nylah.build(), mult="mm", speech=False, geo=True, el=True),
 "Naomi":  dict(grade="4th Grade", morning="mid", core=core_naomi.build(), mult="mm", speech=False, geo=True, el=True),
 "Nariah": dict(grade="2nd Grade", morning="early", core=[nariah_math(), nariah_english(), nariah_science(), nariah_ss()], mult="mm", speech=True, geo=True, el=True),
 "Titus":  dict(grade="Kindergarten", morning="k", core=[titus_math(), titus_letters(), titus_science()], mult="sc", speech=True, geo=True, el=True),
 "Nayeli": dict(grade="Pre-K", morning="pk", core=None, mult="sc", speech=True, geo=False, el=False),
}

def day_pages(kid, cfg, i):
    pg = []
    pg.append(("Morning Work", morning.page_for(cfg["morning"], kid, i)))
    if cfg["core"]:
        for S in cfg["core"]:
            pg.append((S.subject, S.days[i]))
    else:
        for n, p in enumerate(nayeli_pages(i)):
            pg.append(("Pre-K" if n == 0 else "", p))
    if cfg["mult"] == "mm": pg.append(("Multiplication Mastery", mult.mult_page(kid, i)))
    else: pg.append(("Skip Count Stars", mult.skipstars_page(kid, i)))
    if cfg["speech"]: pg.append(("Speech Stars", speech.speech_page(kid, i)))
    if cfg["geo"]: pg.append(("Geography", geography.geo_page(kid, i)))
    if cfg["el"]: pg.append(("Fun Electives", electives.el_page(kid, i)))
    return pg

WK_COVER = "" if UNDATED else " · Week of " + WEEK_LONG
WK_HEAD = "" if UNDATED else "Week of " + WEEK_RANGE

def cover(kid, cfg, subjects):
    head = "".join("<th class='center'>" + d + ("" if UNDATED else "<div class='small'>" + w[:3] + "</div>") + "</th>" for d, w, _ in DAYS)
    rows = "".join(f"<tr><td style='height:40px'><b>{s}</b></td>" + "".join("<td class='center'><span class='chk' style='width:22px;height:22px'></span></td>" for _ in DAYS) + "</tr>" for s in subjects)
    return (f'<div class="page" style="--ac:#1f2a5c"><div style="text-align:center;margin-top:40px">'
            f'<div style="font-size:44pt;font-weight:700;color:#1f2a5c">{kid}</div>'
            f'<div style="font-size:16pt;color:#6d28d9;font-weight:600">{cfg["grade"]}{WK_COVER}</div>'
            f'<div style="margin:14px auto 22px;width:70%;border-top:3px solid #6d28d9"></div></div>'
            f'<div class="lab" style="font-size:14pt;margin-bottom:6px">My week — check it off when it\'s done!</div>'
            f'<table class="t" style="font-size:13pt"><tr><th></th>{head}</tr>{rows}</table>'
            f'<div class="verse" style="margin-top:22px">“{esc(morning.VERSE if cfg["morning"] in ("teen","mid") else morning.VERSE_SHORT)}”<div class="small">{morning.REF} · this week\'s memory verse</div></div>'
            f'<div style="flex:1"></div><div class="center small">All For His Glory</div></div>')

def build_kid(kid, cfg):
    P = Packet(kid, kid)
    subjects = [n for n, _ in day_pages(kid, cfg, 0) if n]
    P.add(cover(kid, cfg, subjects)); P.pad_even()
    for i in range(5):
        for _, p in day_pages(kid, cfg, i):
            P.add(p)
        P.pad_even()
    return P

# ---------------- MOM PACKET ----------------
def mom_page(title, body, sub="Mom's Guide"):
    return (f'<div class="page" style="--ac:#1f2a5c;font-size:10pt"><div class="hdr"><div class="dayblk"><div class="d" style="font-size:22pt">{esc(sub)}</div>'
            f'<div class="w">{WK_HEAD}</div></div><div class="subj"><span class="s">Mom</span><div class="t">{esc(title)}</div></div></div>'
            f'<div class="body" style="gap:7px">{body}</div><div class="foot"><span>Mom\'s Guide</span><span>All For His Glory</span></div></div>')

def build_mom():
    P = Packet("Mom", "Mom")
    glance = ("<p>Every kid has <b>one packet</b> with the whole week in order: <b>Day 1 (Tue) → Day 5 (Sat)</b>. Inside each day the order is always the same: "
              "Morning Work → core subjects → Multiplication / Skip Count → Speech → Geography → Elective. Each day starts on a fresh sheet so you can pull one day "
              "at a time if you want. Shared pages (geography, electives, multiplication, speech) are already copied into each kid's packet — no extra copies needed.</p>"
              "<p><b>Printing:</b> print double-sided, “flip on long edge.” Nothing uses yellow ink. To save ALL color ink, choose “Grayscale” in your printer settings — "
              "every page still works in black and white.</p>")
    t = ("<table class='t'><tr><th>Kid</th><th>What's in the packet</th></tr>"
         "<tr><td><b>Nevaeh</b> (8th)</td><td>Morning (Joseph) · <b>Math Crash Course Week 2 of 12</b> (fractions: all four operations) · English: punctuation power · "
         "Science: matter & its changes · History: the road to Revolution · Multiplication W3 (3s & 4s) · Geography W3 (Tier C) · Electives (Tier C)</td></tr>"
         "<tr><td><b>Nylah</b> (7th)</td><td>Morning · <b>Math Crash Course Level 3</b> (multiplication & division) · English: sentence building · Science: human body systems · "
         "Civics: the Bill of Rights · Multiplication W3 · Geography (Tier C) · Electives (Tier C)</td></tr>"
         "<tr><td><b>Naomi</b> (4th)</td><td>Morning · Math: multiplying by one digit · English: verbs · Science: habitats & adaptations · Florida History: Spanish & French Florida "
         "(Fort Caroline!) · Multiplication W3 · Geography (Tier B) · Electives (Tier B)</td></tr>"
         "<tr><td><b>Nariah</b> (2nd)</td><td>Morning · Math Level 2 (money & time to 5 minutes, with a regrouping warm-up daily) · English: long vowels & describing words · "
         "Science: how plants grow · Social Studies: American symbols (Veterans Day, Day 2) · Multiplication W3 · Speech Stars W3 (TH) · Geography (Tier A) · Electives (Tier A)</td></tr>"
         "<tr><td><b>Titus</b> (K)</td><td>Morning · Math: more, less & shapes · Letters: Aa & Pp · Science: animal homes · Skip Count Stars W3 (2s) · Speech Stars W3 (TH) · "
         "Geography (Tier A) · Electives (Tier A)</td></tr>"
         "<tr><td><b>Nayeli</b> (Pre-K)</td><td>Mini morning sheet · Pre-K animal of the day (dot marker, trace, sticker — matches Titus's animal homes) · her own Skip Count Stars & Speech Stars pages</td></tr></table>")
    P.add(mom_page("This Week at a Glance", glance + t +
        "<h3>Supplies</h3><p><b>All week:</b> dot markers, stickers, crayons/colored pencils, counting bears (3 colors), a small mirror (speech — TH “tongue peek”), globe/atlas. "
        "<b>Geography:</b> play-dough (Day 1–3), a cup of salt water (Day 2), a shallow pan of water (Day 3), yarn (Day 4). "
        + electives.MATERIALS + " <b>Science:</b> Nariah's bean sprout bag starts Day 2 (2–3 dry beans, a paper towel, a zip bag, tape for a sunny window). "
        "Titus: a short walk to look for nests (Day 1) and a blanket over a table for a “bear den” (Day 3). Nevaeh (optional): baking soda + vinegar demo for Days 3–4. "
        "<b>Social Studies:</b> Nariah makes a thank-you card for a veteran on Day 2 (Veterans Day lesson) — you write the words. "
        "<b>Optional field trip:</b> Fort Caroline National Memorial is right here in Jacksonville (Naomi's Day 2).</p>"))
    for i in range(5):
        P.add(mom_page("Teaching Together — Lesson Plans", plans.day_plan(i), sub=DAYS[i][0].upper() if UNDATED else f"{DAYS[i][0].upper()} · {DAYS[i][1]}"))
    P.add(mom_page("Morning Work",
        f"<h3>Morning Work — {morning.THEME}</h3>" + morning.mom_notes()
        + "<h3>Speech Stars</h3>" + speech.MOM))
    P.add(mom_page("Math Crash Course Plans",
        "<h3>Nevaeh's Math Crash Course — 12-week roadmap</h3><p>This is <b>Week 2: fractions</b>. Saturday's checkpoint is 15 problems — 12 right (80%) passes. "
          "If she scores under 12, re-teach the missed skills at the start of next week before Week 3 (decimals & money).</p>"
        + ol([f"<b>Week {n+1}:</b> {t}" for n, t in enumerate(core_nevaeh.ROADMAP)])
        + "<h3>Nylah's Math Crash Course</h3><p>Her 7-level ladder (K → 7th) moves up to <b>Level 3: multiplication & division</b> (standard methods only — carrying and long division). "
          "Every lesson starts with a worked example. Saturday's Level 3 Checkpoint is 12 problems — 10 right passes, and Level 4 (fractions) is next. If not, we re-teach Level 3. "
          "(If she didn't pass last week's Level 2 checkpoint, tell me and I'll swap in a Level 2 review week.)</p>"
        + "<h3>Naomi & Nariah</h3><p><b>Naomi:</b> multiplying by one digit with the standard algorithm (carrying). <b>Nariah:</b> Level 2 — coins and time to 5 minutes, "
          "with a short regrouping warm-up every day so Level 1 stays fresh. Her Saturday checkpoint is 8 of 10.</p>"))
    # answer keys
    entries = []
    for kid, cfg in KIDS.items():
        if not cfg["core"]: continue
        for S in cfg["core"]:
            body = "".join(f"<div style='margin:2px 0'><b>Day {i+1} · {esc(S.titles[i])}:</b> {S.keys[i]}</div>" for i in range(5) if S.keys[i] and S.keys[i] != "—")
            if body: entries.append(f"<div class='box' style='padding:5px 9px'><div class='lab'>{kid} · {S.subject}</div>{body}</div>")
    entries.append("<div class='box' style='padding:5px 9px'><div class='lab'>Multiplication Mastery (Nevaeh, Nylah, Naomi, Nariah)</div>"
                   + "".join(f"<div><b>Day {i+1}:</b> {mult.KEYS[i]}</div>" for i in range(5)) + "</div>")
    entries.append(f"<div class='box' style='padding:5px 9px'><div class='lab'>Skip Count Stars (Titus, Nayeli)</div>{mult.SC_KEY}</div>")
    entries.append(f"<div class='box' style='padding:5px 9px'><div class='lab'>Geography Week {geography.WK}</div>{geography.KEY}</div>")
    entries.append(f"<div class='box' style='padding:5px 9px'><div class='lab'>Fun Electives</div>{electives.KEY}</div>")
    # paginate by size
    pages, cur, size = [], [], 0
    for e in entries:
        L = len(e)
        if cur and size + L > 3400:
            pages.append(cur); cur, size = [], 0
        cur.append(e); size += L
    if cur: pages.append(cur)
    for n, pgs in enumerate(pages):
        P.add(mom_page(f"Answer Keys ({n+1}/{len(pages)})", "".join(pgs)))
    return P

if __name__ == "__main__":
    jobs = []
    order = ["Nevaeh", "Nylah", "Naomi", "Nariah", "Titus", "Nayeli"]
    for kid in order:
        P = build_kid(kid, KIDS[kid])
        h = f"{OUT}/{kid}.html"; open(h, "w").write(P.html())
        jobs.append((h, f"{OUT}/{kid} - Week of {WEEK_SHORT}.pdf"))
    M = build_mom(); h = f"{OUT}/Mom.html"; open(h, "w").write(M.html())
    jobs.append((h, f"{OUT}/Mom's Guide - Week of {WEEK_SHORT}.pdf"))
    render(jobs)
