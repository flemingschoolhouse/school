import sys, os
sys.path.insert(0, "/home/claude")
from lib import *
from render import render
import morning, geography, mult, speech, electives, plans
import core_nevaeh, core_nylah, core_naomi
from core_young import *

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

def cover(kid, cfg, subjects):
    head = "".join(f"<th class='center'>{d}<div class='small'>{w[:3]}</div></th>" for d, w, _ in DAYS)
    rows = "".join(f"<tr><td style='height:40px'><b>{s}</b></td>" + "".join("<td class='center'><span class='chk' style='width:22px;height:22px'></span></td>" for _ in DAYS) + "</tr>" for s in subjects)
    return (f'<div class="page" style="--ac:#1f2a5c"><div style="text-align:center;margin-top:40px">'
            f'<div style="font-size:44pt;font-weight:700;color:#1f2a5c">{kid}</div>'
            f'<div style="font-size:16pt;color:#6d28d9;font-weight:600">{cfg["grade"]} · Week of November 3–7, 2026</div>'
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
            f'<div class="w">Week of Nov 3–7, 2026</div></div><div class="subj"><span class="s">Mom</span><div class="t">{esc(title)}</div></div></div>'
            f'<div class="body" style="gap:7px">{body}</div><div class="foot"><span>Mom\'s Guide</span><span>All For His Glory</span></div></div>')

def build_mom():
    P = Packet("Mom", "Mom")
    glance = ("<p>Every kid has <b>one packet</b> with the whole week in order: <b>Day 1 (Tue) → Day 5 (Sat)</b>. Inside each day the order is always the same: "
              "Morning Work → core subjects → Multiplication / Skip Count → Speech → Geography → Elective. Each day starts on a fresh sheet so you can pull one day "
              "at a time if you want. Shared pages (geography, electives, multiplication, speech) are already copied into each kid's packet — no extra copies needed.</p>"
              "<p><b>Printing:</b> print double-sided, “flip on long edge.” Nothing uses yellow ink. To save ALL color ink, choose “Grayscale” in your printer settings — "
              "every page still works in black and white.</p>")
    t = ("<table class='t'><tr><th>Kid</th><th>What's in the packet</th></tr>"
         "<tr><td><b>Nevaeh</b> (8th)</td><td>Morning (Gideon) · <b>Math Crash Course Week 1 of 12</b> (whole numbers & order of operations) · English: building better sentences · "
         "Science: atoms & periodic table · History: Thirteen Colonies · Multiplication W2 · Geography W2 (Tier C) · Electives W3 (Tier C)</td></tr>"
         "<tr><td><b>Nylah</b> (7th)</td><td>Morning · <b>Math Crash Course Level 2</b> (place value, regrouping, rounding) · English: parts of speech · Science: cells · "
         "Civics: three branches · Multiplication W2 · Geography (Tier C) · Electives (Tier C)</td></tr>"
         "<tr><td><b>Naomi</b> (4th)</td><td>Morning · Math: big numbers · English: nouns · Science: food chains & webs · Florida History: first peoples · Multiplication W2 · "
         "Geography (Tier B) · Electives (Tier B)</td></tr>"
         "<tr><td><b>Nariah</b> (2nd)</td><td>Morning · Math Level 1 continued (regrouping + time) · English: short vowels, nouns, verbs · Science: butterfly life cycle · "
         "Social Studies: first Thanksgiving · Multiplication W2 · Speech Stars W2 (cont.) · Geography (Tier A) · Electives (Tier A)</td></tr>"
         "<tr><td><b>Titus</b> (K)</td><td>Morning · Math: numbers to 20, add & take away · Letters: Mm & Ss · Science: 5 senses · Skip Count Stars W2 · Speech Stars W2 (cont.) · "
         "Geography (Tier A) · Electives (Tier A)</td></tr>"
         "<tr><td><b>Nayeli</b> (Pre-K)</td><td>Mini morning sheet · Pre-K shape of the day (dot marker, trace, sticker) · her own Skip Count Stars & Speech Stars pages</td></tr></table>")
    P.add(mom_page("This Week at a Glance", glance + t +
        "<h3>Supplies</h3><p><b>All week:</b> dot markers, stickers, crayons/colored pencils, counting bears, a small mirror (speech), globe/atlas (geography). "
        + electives.MATERIALS + " <b>Science:</b> Naomi's backyard hunt (Day 4), Titus's taste test foods (Day 3: banana/apple, lemon, pretzel, pickle) and a "
        "mystery bag (Day 4). <b>Nevaeh & Nylah:</b> a periodic table (online is fine) for Nevaeh on Day 3.</p>"))
    for i in range(5):
        P.add(mom_page("Teaching Together — Lesson Plans", plans.day_plan(i), sub=f"{DAYS[i][0].upper()} · {DAYS[i][1]}"))
    P.add(mom_page("Morning Work",
        "<h3>Morning Work — Gideon</h3>" + morning.mom_notes()
        + "<h3>Speech Stars</h3>" + speech.MOM))
    P.add(mom_page("Math Crash Course Plans",
        "<h3>Nevaeh's Math Crash Course — 12-week roadmap</h3><p>No pre-test — she starts at Week 1 and each Saturday checkpoint (80% to pass) decides whether we "
          "move on or re-teach. Her Core Studies math is now this crash course.</p>"
        + ol([f"<b>Week {n+1}:</b> {t}" for n, t in enumerate(core_nevaeh.ROADMAP)])
        + "<h3>Nylah's Math Crash Course</h3><p>Picking up her 7-level ladder (K → 7th) at <b>Level 2</b> (2nd–3rd grade skills: place value, regrouping, rounding). "
          "No placement test — if she passes Saturday's checkpoint (10 of 12), Level 3 is multiplication & division. Her Core Studies math is now this crash course.</p>"))
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
    entries.append(f"<div class='box' style='padding:5px 9px'><div class='lab'>Geography Week 2</div>{geography.KEY}</div>")
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
        jobs.append((h, f"{OUT}/{kid} - Week of Nov 3.pdf"))
    M = build_mom(); h = f"{OUT}/Mom.html"; open(h, "w").write(M.html())
    jobs.append((h, f"{OUT}/Mom's Guide - Week of Nov 3.pdf"))
    render(jobs)
