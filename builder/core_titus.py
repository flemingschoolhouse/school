# Titus (K) + Nayeli (Pre-K) core pages — week of Nov 10–14, 2026.
# Theme for both: ANIMAL HOMES (bird/nest, bee/hive, bear/den, rabbit/burrow, frog/pond).
from core_young import ic, I, icon, objs, shape_path, dots_on, SHAPES
from core_common import *
import random, math as M

# ---------------- extra line icons (stroke only, kids color them) ----------------
I.update({
 "bird": ic('<path d="M22,44 C22,26 40,20 52,28 C58,20 72,20 74,32 L84,34 L74,38 C72,58 52,66 36,62 L14,70 L22,54 Z"/>'
            '<circle cx="64" cy="30" r="2"/><path d="M34,40 C42,50 54,50 60,42"/><path d="M40,62 L38,74 M50,62 L50,74"/>'),
 "nest": ic('<path d="M8,40 C12,72 78,72 82,40"/><path d="M8,40 C30,48 60,48 82,40"/>'
            '<path d="M14,52 L76,46 M18,60 L72,54 M12,46 L40,58 M50,58 L78,44"/>'
            '<ellipse cx="34" cy="34" rx="8" ry="10"/><ellipse cx="52" cy="33" rx="8" ry="10"/>'),
 "bee": ic('<ellipse cx="48" cy="50" rx="26" ry="17"/><path d="M40,34 L40,66 M52,34 L52,66 M63,37 L63,63"/>'
           '<circle cx="24" cy="46" r="10"/><circle cx="21" cy="44" r="1.5"/><path d="M20,37 L12,24 M26,36 L28,22"/>'
           '<ellipse cx="44" cy="22" rx="10" ry="14"/><ellipse cx="62" cy="24" rx="9" ry="12"/><path d="M74,50 L84,50"/>'),
 "hive": ic('<path d="M45,4 L45,10"/><path d="M30,10 L60,10"/>'
            '<path d="M28,12 C18,14 18,24 28,26 L62,26 C72,24 72,14 62,12 Z"/>'
            '<path d="M22,26 C10,28 10,40 22,42 L68,42 C80,40 80,28 68,26"/>'
            '<path d="M18,42 C6,44 6,58 18,60 L72,60 C84,58 84,44 72,42"/>'
            '<path d="M16,60 C6,62 6,74 16,76 L74,76 C84,74 84,62 74,60"/><path d="M38,76 C38,64 52,64 52,76"/>'),
 "bear": ic('<circle cx="45" cy="40" r="22"/><circle cx="27" cy="22" r="8"/><circle cx="63" cy="22" r="8"/>'
            '<ellipse cx="45" cy="48" rx="10" ry="8"/><circle cx="45" cy="45" r="3"/><circle cx="37" cy="34" r="2"/><circle cx="53" cy="34" r="2"/>'
            '<path d="M41,52 C43,55 47,55 49,52"/>'),
 "den": ic('<path d="M4,74 C6,30 24,8 46,8 C70,8 86,32 86,74 Z"/><path d="M26,74 C26,48 34,36 45,36 C56,36 64,48 64,74"/>'
           '<path d="M14,40 L22,46 M70,30 L76,38 M60,16 L66,20"/><path d="M32,74 C32,64 40,58 45,62 C50,58 58,64 58,74"/>'),
 "rabbit": ic('<ellipse cx="34" cy="16" rx="5" ry="15"/><ellipse cx="48" cy="16" rx="5" ry="15"/><circle cx="41" cy="38" r="12"/>'
              '<ellipse cx="50" cy="62" rx="22" ry="14"/><circle cx="74" cy="58" r="5"/><circle cx="37" cy="36" r="1.6"/>'
              '<path d="M38,43 L41,45 L44,43"/><path d="M36,76 L46,76 M58,76 L68,76"/>'),
 "burrow": ic('<path d="M2,26 L28,26 M62,26 L88,26"/><path d="M28,26 C28,14 62,14 62,26"/>'
              '<path d="M30,26 C34,40 30,50 44,58 C56,64 70,60 74,70"/><path d="M44,26 C46,36 46,44 56,48 C66,52 80,52 84,62"/>'
              '<ellipse cx="74" cy="66" rx="12" ry="8"/><path d="M8,40 L12,40 M18,62 L22,62 M80,36 L84,36"/>'),
 "frog": ic('<circle cx="30" cy="24" r="9"/><circle cx="60" cy="24" r="9"/><circle cx="30" cy="24" r="3"/><circle cx="60" cy="24" r="3"/>'
            '<path d="M20,30 C8,40 10,62 30,64 L60,64 C80,62 82,40 70,30"/><path d="M32,44 C40,50 50,50 58,44"/>'
            '<path d="M24,62 L10,72 L24,72 M66,62 L80,72 L66,72"/>'),
 "pond": ic('<ellipse cx="45" cy="52" rx="40" ry="20"/><path d="M22,52 C28,48 34,56 40,52 M50,58 C56,54 62,62 68,58"/>'
            '<path d="M58,44 A9,6 0 1 1 66,46 L62,44 Z"/><path d="M14,40 L12,14 M20,40 L22,18 M12,14 C8,8 14,6 12,14 M22,18 C20,10 26,10 22,18"/>'),
 "apple": ic('<path d="M45,22 C30,10 8,18 10,42 C12,64 30,78 45,70 C60,78 78,64 80,42 C82,18 60,10 45,22 Z"/><path d="M45,22 L47,6"/><path d="M48,12 C56,4 66,6 68,10 C60,16 52,16 48,12 Z"/>'),
 "ant": ic('<circle cx="18" cy="44" r="9"/><ellipse cx="40" cy="46" rx="10" ry="8"/><ellipse cx="66" cy="48" rx="16" ry="12"/>'
           '<path d="M14,36 L6,22 M22,36 L26,22 M36,52 L28,68 M40,54 L40,70 M44,52 L54,68"/>'),
 "pig": ic('<circle cx="45" cy="42" r="28"/><ellipse cx="45" cy="50" rx="13" ry="9"/><circle cx="40" cy="50" r="2.5"/><circle cx="50" cy="50" r="2.5"/>'
           '<circle cx="35" cy="34" r="2"/><circle cx="55" cy="34" r="2"/><path d="M22,26 L18,8 L36,16 M68,26 L72,8 L54,16"/>'),
 "pan": ic('<ellipse cx="36" cy="42" rx="30" ry="22"/><ellipse cx="36" cy="42" rx="22" ry="15"/><path d="M64,36 L88,30 L88,38 L65,46"/>'),
})
ANIMALS = ["bird", "bee", "bear", "rabbit", "frog"]
HOMES = {"bird": "nest", "bee": "hive", "bear": "den", "rabbit": "burrow", "frog": "pond"}

def icn(name, scale):
    return icon(name, scale)

# ---------------- math helpers ----------------
def bear_row(n, sz=34, color="#4338ca"):
    """little counting-bear outlines (head, ears, body) in a row"""
    s = ""
    for k in range(n):
        x = 4 + k * (sz + 6); c = x + sz / 2; h = sz * 0.22
        s += (f'<g fill="#fff" stroke="{color}" stroke-width="2.2"><circle cx="{c-h:.1f}" cy="{sz*0.16+4:.1f}" r="{sz*0.1:.1f}"/><circle cx="{c+h:.1f}" cy="{sz*0.16+4:.1f}" r="{sz*0.1:.1f}"/>'
              f'<ellipse cx="{c:.1f}" cy="{sz*1.0+4:.1f}" rx="{sz*0.36:.1f}" ry="{sz*0.42:.1f}"/><circle cx="{c:.1f}" cy="{sz*0.38+4:.1f}" r="{sz*0.26:.1f}"/></g>')
    return f'<svg style="flex-shrink:0" width="{n*(sz+6)+6}" height="{sz*1.5+6:.0f}">{s}</svg>'

def shp(name, cx, cy, s):
    if name == "hexagon":
        pts = " ".join(f"{cx + s*M.cos(M.pi/3*k):.1f},{cy + s*M.sin(M.pi/3*k):.1f}" for k in range(6))
        return f'<polygon points="{pts}"/>'
    return shape_path(name, cx, cy, s)

def shape_svg(name, s=40, stroke="#2f5bd3", w=None, h=None, sw=3):
    w = w or (s * 3 if name == "rectangle" else s * 2 + 8); h = h or s * 2 + 8
    return f'<svg style="flex-shrink:0" width="{w:.0f}" height="{h:.0f}"><g fill="#fff" stroke="{stroke}" stroke-width="{sw}">{shp(name, w/2, h/2 + (3 if name == "triangle" else 0), s)}</g></svg>'

CORNERS = {"circle": 0, "triangle": 3, "square": 4, "rectangle": 4, "hexagon": 6}
TSH = ["circle", "square", "triangle", "rectangle", "hexagon"]

def write_box(w=60):
    return f'<span class="blank-ln" style="min-width:{w}px;height:30px"></span>'

# ======================= TITUS (K) =======================
def titus_math():
    S = Subject("Titus", "Math", "Level 1 · More, Less & Shapes")
    # ---- D1 more / fewer / same ----
    pairs = [(5, 3, "MORE"), (4, 7, "FEWER"), (6, 6, "MORE"), (8, 5, "FEWER"), (3, 9, "MORE")]
    def cmp_row(n, a, b, q):
        return (f'<div class="box" style="padding:4px 10px"><div class="flexrow" style="align-items:flex-end;gap:8px">'
                f'<b class="big" style="color:#2f5bd3">{n}.</b>{bear_row(a, 26)}{write_box(44)}'
                f'<div style="margin-left:auto;display:flex;align-items:flex-end;gap:8px">{bear_row(b, 26, "#a21caf")}{write_box(44)}</div></div>'
                f'<div style="font-size:13pt">Which group has <b>{q}</b>? {pick("◀ this one", "this one ▶", "same")}</div></div>')
    def ans(a, b, q):
        if a == b: return "same"
        return "◀ left group" if (a > b) == (q == "MORE") else "right group ▶"
    k1 = "; ".join(f"{n+1}) {a} and {b} → {ans(a, b, q)}" for n, (a, b, q) in enumerate(pairs))
    onemore = [7, 12, 19, 29]
    S.set(0, "More, Fewer, or Same?",
        learnbox("<p class='big'><b>More</b> means a bigger group. <b>Fewer</b> means a smaller group. <b>Same</b> means equal! "
                 "Line up your counting bears to check — the row that sticks out has more.</p>", yt("TT more fewer same kindergarten"))
        + '<div class="lab">Count each group and write the number on the line. Then circle the answer.</div>'
        + "".join(cmp_row(n + 1, a, b, q) for n, (a, b, q) in enumerate(pairs))
        + '<div class="lab">1 more! Write the number that comes next.</div><div class="grid4">'
        + "".join(f'<div class="huge center">{x} → {write_box(54)}</div>' for x in onemore) + '</div>'
        + '<div class="big">Counting bears: Make a row of 7 bears and a row of 4 bears. Which row has more? '
        + pick("7 bears", "4 bears") + '</div>',
        k1 + ". 1 more: " + ", ".join(f"{x}→{x+1}" for x in onemore) + ". Bears: 7 bears has more.")
    # ---- D2 flat shapes ----
    r = random.Random(310)
    hunt = TSH * 3; r.shuffle(hunt)
    cells = "".join(f'<g fill="#fff" stroke="#1f2a5c" stroke-width="3">{shp(nm, 60 + (k % 5) * 130, 44 + (k // 5) * 104, 38)}</g>' for k, nm in enumerate(hunt))
    cnt = {s: hunt.count(s) for s in TSH}
    S.set(1, "Flat Shapes",
        learnbox("<p class='big'>A <b>circle</b> is round — no corners. A <b>triangle</b> has 3 sides. A <b>square</b> has 4 sides, all the same. "
                 "A <b>rectangle</b> has 4 sides — 2 long, 2 short. A <b>hexagon</b> has 6 sides, like a honeycomb!</p>", yt("TT flat shapes kindergarten"))
        + '<div class="lab">Put a dot-marker dot on every CORNER. Count the dots and write how many.</div>'
        + '<div class="flexrow" style="justify-content:space-between;align-items:flex-end">'
        + "".join(f'<div class="center">{shape_svg(nm, 44, "#4338ca")}<div class="big">{nm}</div><div>{write_box(46)}</div></div>' for nm in TSH) + '</div>'
        + '<div class="lab">Shape hunt! Dot every HEXAGON with your dot marker. Color the circles.</div>'
        + f'<svg width="660" height="296" style="align-self:center;flex-shrink:0">{cells}</svg>'
        + qs([("How many hexagons did you dot?", [str(cnt["hexagon"]), str(cnt["hexagon"] + 1), str(cnt["hexagon"] - 1)]),
              ("Which shape has 3 sides?", ["triangle", "square", "circle"]),
              ("Which shape has NO corners?", ["circle", "rectangle", "hexagon"])]),
        "Corners: circle 0, square 4, triangle 3, rectangle 4, hexagon 6. "
        f"Shape hunt has {cnt['hexagon']} hexagons and {cnt['circle']} circles. 1) {cnt['hexagon']} 2) triangle 3) circle.")
    # ---- D3 patterns ----
    pats = [(["circle", "square"], "AB", 6), (["triangle", "circle", "circle"], "ABB", 6),
            (["square", "triangle", "hexagon"], "ABC", 6), (["hexagon", "square"], "AB", 5)]
    def pat_row(n, unit, typ, shown):
        seq = [unit[k % len(unit)] for k in range(shown)]; nxt = unit[shown % len(unit)]
        sv = "".join(f'<g fill="#fff" stroke="#6d28d9" stroke-width="3">{shp(nm, 34 + k * 66, 34, 24)}</g>' for k, nm in enumerate(seq))
        sv += f'<rect x="{34 + shown*66 - 28}" y="6" width="56" height="56" rx="8" fill="none" stroke="#9aa0bb" stroke-width="2.5" stroke-dasharray="6,5"/>'
        opts = list(dict.fromkeys([nxt] + unit + ["circle", "square", "triangle"]))[:3]
        return (f'<div class="box" style="padding:6px 10px"><div class="flexrow" style="align-items:center"><b class="big" style="color:#2f5bd3">{n}.</b>'
                f'<svg style="flex-shrink:0" width="{(shown+1)*66+8}" height="68">{sv}</svg></div>'
                f'<div class="flexrow" style="gap:20px"><span>What comes next?{mc_opts(opts, f"pat{n}")}</span>'
                f'<span>Pattern type?{mc_opts([typ] + [t for t in ["AB", "ABB", "ABC"] if t != typ], f"pt{n}")}</span></div></div>'), nxt
    rows, keys3 = "", []
    for n, (u, t, sh) in enumerate(pats):
        h, nx = pat_row(n + 1, u, t, sh); rows += h; keys3.append(f"{n+1}) {nx}, {t}")
    S.set(2, "Patterns: AB, ABB, ABC",
        learnbox("<p class='big'>A <b>pattern</b> repeats again and again! <b>AB:</b> clap, stomp, clap, stomp. <b>ABB:</b> clap, stomp, stomp. "
                 "<b>ABC:</b> clap, stomp, jump. Put a sticker in each empty box!</p>", yt("TT patterns AB ABB ABC"))
        + rows
        + '<div class="lab">Make your own! Use 2 kinds of stickers to make an AB pattern.</div>'
        + '<div class="flexrow" style="gap:10px;justify-content:center">' + "".join('<div style="width:62px;height:62px;border:2.5px dashed #9aa0bb;border-radius:8px"></div>' for _ in range(8)) + '</div>'
        + '<div class="big">Counting bears: make an <b>ABC</b> pattern with 3 colors of bears. Show Mom! <span class="star">☆</span></div>',
        "; ".join(keys3) + ". Own patterns vary.")
    # ---- D4 adding with story pictures ----
    stories = [("bird", 3, 2, "birds sit in a nest. {b} more fly in. How many birds?"),
               ("bee", 4, 3, "bees are on the hive. {b} more buzz in. How many bees?"),
               ("frog", 5, 1, "frogs sit by the pond. {b} more hop over. How many frogs?"),
               ("rabbit", 2, 4, "rabbits are in the grass. {b} more hop out. How many rabbits?"),
               ("bear", 6, 3, "bears are in the woods. {b} more come. How many bears?")]
    def story_row(n, an, a, b, txt):
        pics = "".join(icon(an, 0.52) for _ in range(a)) + '<span class="huge" style="padding:0 6px">+</span>' + "".join(icon(an, 0.52) for _ in range(b))
        return (f'<div class="box" style="padding:4px 10px"><div class="big"><b style="color:#2f5bd3">{n}.</b> {a} {txt.format(b=b)}</div>'
                f'<div class="flexrow" style="align-items:center;gap:2px">{pics}<div class="huge" style="margin-left:auto">{a} + {b} = {write_box(54)}</div></div></div>')
    S.set(3, "Adding Stories",
        learnbox("<p class='big'>A story can be a math problem! Some animals are there, then <b>more</b> come. "
                 "<b>Count them all</b> to add. Use your counting bears to act out each story.</p>", yt("TT addition stories kindergarten"))
        + "".join(story_row(n + 1, *s) for n, s in enumerate(stories))
        + qs([("2 birds + 2 birds = ?", ["4", "3", "5"]), ("5 bees + 5 bees = ?", ["10", "9", "8"])], 6)
        + '<div class="lab">Trace your answers! Numbers 5 to 10:</div>'
        + '<div class="trow" style="gap:14px">' + "".join(school_print(str(n), 56, "trace") for n in range(5, 11)) + '</div>',
        "; ".join(f"{n+1}) {a}+{b}={a+b}" for n, (_, a, b, _t) in enumerate(stories)) + "; 6) 4; 7) 10.")
    # ---- D5 checkpoint ----
    S.set(4, "Checkpoint",
        learnbox("<p class='big'><b>Checkpoint!</b> 10 questions. Goal: <b>8 right</b>. Mom can read each one to you.</p>")
        + f'<div class="flexrow" style="align-items:center;gap:16px"><div>{bear_row(4, 30)}</div><div>{bear_row(6, 30, "#a21caf")}</div></div>'
        + qs([("Which group has MORE bears?", ["the 6 bears", "the 4 bears", "same"]),
              ("Which group has FEWER bears?", ["the 4 bears", "the 6 bears", "same"])])
        + '<div class="flexrow" style="justify-content:space-around">' + "".join(f'<div class="center"><b>{n}.</b> {shape_svg(nm, 38, "#4338ca")}</div>' for n, nm in [(3, "hexagon"), (4, "triangle"), (5, "rectangle")]) + '</div>'
        + qs([("What is shape 3?", ["hexagon", "square", "circle"]), ("What is shape 4?", ["triangle", "rectangle", "hexagon"]),
              ("What is shape 5?", ["rectangle", "square", "triangle"])], 3)
        + '<div class="flexrow" style="align-items:center"><b>6.</b>' + "".join(f'<svg style="flex-shrink:0" width="54" height="54"><g fill="#fff" stroke="#6d28d9" stroke-width="3">{shp(nm, 27, 27, 22)}</g></svg>' for nm in ["circle", "square", "square"] * 2) + ' What comes next? ' + mc_opts(["circle", "square", "triangle"], "cp6") + '</div>'
        + '<div class="flexrow" style="justify-content:space-around">' + "".join(f'<div class="huge"><b class="big">{n}.</b> {a} + {b} = {write_box(54)}</div>' for n, a, b in [(7, 4, 2), (8, 3, 5), (9, 6, 4)]) + '</div>'
        + '<div class="huge"><b class="big">10.</b> 1 more than 15 is ' + write_box(60) + '</div>'
        + '<div class="big">Score: ______ / 10 &nbsp; <span class="star">☆☆☆</span></div>',
        "1) the 6 bears 2) the 4 bears 3) hexagon 4) triangle 5) rectangle 6) circle (ABB) 7) 6 8) 8 9) 10 10) 16.")
    return S

def titus_letters():
    S = Subject("Titus", "Letters & Writing", "Week 3 · Aa and Pp")
    aw = [("apple", 1), ("ant", 1), ("bed", 0), ("alligator", 1), ("sun", 0), ("ax", 1), ("map", 0), ("astronaut", 1)]
    pw = [("pig", 1), ("pan", 1), ("cat", 0), ("pumpkin", 1), ("fish", 0), ("popcorn", 1), ("sock", 0), ("puppy", 1)]
    def listen(words, letter):
        return ('<div class="lab">Mom reads each word. Does it START with /' + letter + '/? Circle the ' + letter.upper() + ' for yes, the ✗ for no.</div>'
                '<div class="grid4">' + "".join(f'<div class="box center"><div class="small">{n+1}. (Mom: “{w}”)</div><span class="huge">{pick(letter.upper(), "✗")}</span></div>' for n, (w, _) in enumerate(words)) + '</div>')
    def lkey(words):
        return "Yes: " + ", ".join(w for w, y in words if y) + ". No: " + ", ".join(w for w, y in words if not y) + "."
    def hunt(letters, seed, target):
        r = random.Random(seed); pool = [r.choice(letters) for _ in range(24)]
        n = sum(1 for c in pool if c.lower() == target)
        cells = "".join(f'<div class="center" style="font-size:30pt;font-weight:700;color:#1f2a5c;border:1.6px solid #c9cde3;border-radius:50%;width:64px;height:64px;line-height:64px;justify-self:center">{c}</div>' for c in pool)
        return f'<div class="grid6" style="gap:8px">{cells}</div>', n
    ha, na = hunt("AaAamsMtTSo", 31, "a")
    hp, np_ = hunt("PpPpbdqmMsS", 32, "p")
    S.set(0, "Big A, Little a",
        learnbox("<p class='big'><b>A</b> says /ă/ — like when the doctor says “open wide: aaa!” <b>a</b>pple, <b>a</b>nt, <b>a</b>lligator!</p>", yt("letter A song for kids"))
        + '<div class="lab">Trace big A.</div>' + trace_line("A", 66, 6) + '<div class="lab">Trace little a.</div>' + trace_line("a", 66, 7)
        + '<div class="lab">Trace the word:</div>' + trace_line("ant", 66, 2)
        + '<div class="lab">Letter hunt! Dot every A and a with your dot marker.</div>' + ha
        + f'<div class="big">How many did you dot? {write_box(60)}</div>',
        f"Letter hunt: {na} A/a.")
    S.set(1, "A Words",
        learnbox("<p class='big'>Listen for the <b>/ă/</b> sound at the start of words. Open your mouth wide: ă, ă, apple!</p>", yt("letter A sound words for kids"))
        + listen(aw, "a")
        + '<div class="lab">Trace:</div>' + trace_line("at", 60, 3) + trace_line("am", 60, 3)
        + '<div class="lab">Draw something that starts with A (an apple? an ant?).</div><div class="answer-space" style="min-height:200px"></div>',
        lkey(aw))
    S.set(2, "Big P, Little p",
        learnbox("<p class='big'><b>P</b> says /p/ — a little puff of air! Hold your hand by your mouth: <b>p</b>, <b>p</b>, <b>p</b>ig! <b>p</b>op!</p>", yt("letter P song for kids"))
        + '<div class="lab">Trace big P.</div>' + trace_line("P", 66, 7) + '<div class="lab">Trace little p.</div>' + trace_line("p", 66, 7)
        + '<div class="lab">Trace the word:</div>' + trace_line("pan", 66, 2)
        + '<div class="lab">Letter hunt! Dot every P and p with your dot marker. (Watch out for b, d and q!)</div>' + hp
        + f'<div class="big">How many did you dot? {write_box(60)}</div>',
        f"Letter hunt: {np_} P/p.")
    psort = [("apple", "A"), ("pig", "P"), ("pie", "P"), ("ant", "A"), ("pan", "P"), ("pond", "P")]
    S.set(3, "P Words",
        learnbox("<p class='big'>Listen for <b>/p/</b> at the start. Feel the puff of air on your hand: p, p, pumpkin!</p>", yt("letter P sound words for kids"))
        + listen(pw, "p")
        + '<div class="lab">Picture sort! Say the name. Does it start with A or P? Circle one.</div>'
        + '<div class="grid6">' + "".join(f'<div class="center">{icon(p, 0.85)}<div class="small">{p}</div><div class="big">{pick("A", "P")}</div></div>' for p, _ in psort) + '</div>'
        + '<div class="lab">Read and trace: A + P + other letters you know make words!</div>' + trace_line("pat", 56, 2) + trace_line("tap", 56, 2)
        + qs([("Which word starts with P?", ["pot", "top", "mop"]), ("Which word starts with A?", ["ant", "sat", "map"])]),
        lkey(pw) + " Picture sort: " + ", ".join(f"{p} {l}" for p, l in psort) + ". 1) pot 2) ant.")
    S.set(4, "Review: A, P, M, S, T & My Name",
        learnbox("<p class='big'>Show what you know! Trace your letters and your name.</p>")
        + '<div class="lab">Trace:</div>' + trace_line("Aa", 56, 3) + trace_line("Pp", 56, 3)
        + '<div class="trow" style="gap:24px">' + school_print("Mm", 56, "trace") + school_print("Ss", 56, "trace") + school_print("Tt", 56, "trace") + '</div>'
        + '<div class="lab">My name:</div>' + trace_line("Titus", 66, 2)
        + '<div class="lab">Now write your name by yourself:</div>' + school_print("", 66, "blank", extra_w=600)
        + qs([("What letter does “pig” start with?", ["P", "A", "S"]), ("What letter does “apple” start with?", ["A", "P", "M"]),
              ("What letter does “top” start with?", ["T", "P", "M"])])
        + '<div class="big">Mom asks the sound: A <span class="star">☆</span> P <span class="star">☆</span> M <span class="star">☆</span> S <span class="star">☆</span> T <span class="star">☆</span></div>',
        "1) P 2) A 3) T. Sounds: A /ă/, P /p/, M /m/, S /s/, T /t/.")
    return S

def titus_science():
    S = Subject("Titus", "Science", "Week 3 · Animal Homes")
    VS = [yt("AH birds nests"), yt("AH bees hive"), yt("AH bears den"), yt("AH frogs pond")]
    def pair(a, h, sc=2.0):
        return f'<div class="flexrow" style="justify-content:center;align-items:center;gap:30px">{icon(a, sc)}<div class="huge">→</div>{icon(h, sc)}</div>'
    S.set(0, "Birds & Nests",
        learnbox("<p class='big'>Every animal needs a <b>home</b> — a safe place to sleep and raise babies. Many birds build a <b>nest</b> with "
                 "twigs, grass, and leaves. Robins even use <b>mud</b>! The mother bird lays her <b>eggs</b> in the nest and sits on them to keep them warm.</p>", VS[0])
        + pair("bird", "nest")
        + qs([("What is a bird's home called?", ["a nest", "a hive", "a den"]), ("What do birds use to build nests?", ["twigs and grass", "bricks", "ice"]),
              ("What does the mother bird lay in the nest?", ["eggs", "rocks", "honey"])])
        + '<div class="lab">Nest walk! Look up in the trees with Mom. Did you see a nest?</div><div class="big">' + pick("yes", "no") + '</div>'
        + '<div class="lab">Draw a nest with eggs in it. How many eggs? ' + write_box(50) + '</div><div class="answer-space" style="min-height:150px"></div>'
        + '<div class="lab">Trace:</div>' + trace_line("nest", 56, 3),
        "1) a nest 2) twigs and grass 3) eggs. Nest walk / drawing vary.")
    hexes = "".join(f'<g fill="#fff" stroke="#4338ca" stroke-width="3">{shp("hexagon", 50 + c*60, 42 + r*69.3 + (34.6 if c % 2 else 0), 40)}</g>' for r in range(3) for c in range(9))
    S.set(1, "Bees & Hives",
        learnbox("<p class='big'>Honeybees live together in a <b>hive</b>. They make <b>wax</b> from their bodies and build a <b>honeycomb</b>. "
                 "Each little room is a <b>hexagon</b> — 6 sides! Bees store honey and raise baby bees in the rooms. Each hive has one <b>queen</b> bee.</p>", VS[1])
        + pair("bee", "hive", 1.7)
        + '<div class="lab">Honeycomb! Put a dot-marker dot in every hexagon. Count them: ' + write_box(60) + '</div>'
        + f'<svg width="590" height="256" style="align-self:center;flex-shrink:0">{hexes}</svg>'
        + qs([("What is a bee's home called?", ["a hive", "a nest", "a pond"]), ("What shape is each honeycomb room?", ["hexagon", "circle", "square"]),
              ("What do bees make?", ["honey", "milk", "mud"])])
        + '<div class="lab">Trace:</div>' + trace_line("hive", 50, 3),
        "Honeycomb: 27 hexagons (9 columns of 3). 1) a hive 2) hexagon 3) honey.")
    S.set(2, "Bears & Dens",
        learnbox("<p class='big'>When winter comes, many bears find a <b>den</b> — a cave, a hollow tree, or a hole they dig. "
                 "They sleep there most of the winter and live off the fat they stored up in the fall. Mother bears have their tiny <b>cubs</b> in the den! "
                 "Florida has black bears too.</p>", VS[2])
        + pair("bear", "den")
        + qs([("What is a bear's home called?", ["a den", "a hive", "a nest"]), ("When do bears sleep in their dens?", ["winter", "summer", "every lunch time"]),
              ("What are baby bears called?", ["cubs", "chicks", "tadpoles"])])
        + '<div class="lab">Act it out! Make a “den” under a table with a blanket. Curl up like a sleepy bear, then wake up in spring and stretch! <span class="star">☆</span></div>'
        + '<div class="lab">Color the bear and its den.</div>' + f'<div class="center">{icon("bear", 1.5)}{icon("den", 1.5)}</div>'
        + '<div class="lab">Trace:</div>' + trace_line("den", 56, 4),
        "1) a den 2) winter 3) cubs.")
    S.set(3, "Rabbits & Frogs",
        learnbox("<p class='big'>Many wild rabbits dig a <b>burrow</b> — a tunnel home under the ground where they hide and keep their babies safe. "
                 "<b>Frogs</b> live in and near a <b>pond</b>. A mother frog lays eggs in the water. <b>Tadpoles</b> hatch and swim with tails, then grow legs and become frogs!</p>", VS[3])
        + '<div class="flexrow" style="justify-content:space-around">' + pair("rabbit", "burrow", 1.3) + pair("frog", "pond", 1.3) + '</div>'
        + '<div class="lab">Where does it live? Circle the home.</div>'
        + '<div class="grid2">' + "".join(f'<div class="box center">{icon(a, 1.0)}{mc_opts(c, "wh" + a)}</div>' for a, c in
             [("rabbit", ["burrow", "pond", "hive"]), ("frog", ["pond", "nest", "den"]), ("bee", ["hive", "burrow", "pond"]), ("bird", ["nest", "den", "hive"])]) + '</div>'
        + qs([("What does a tadpole grow into?", ["a frog", "a rabbit", "a fish"]), ("Is a burrow above or under the ground?", ["under the ground", "up in a tree", "in the water"])], 5)
        + '<div class="lab">Trace:</div>' + trace_line("pond", 56, 3),
        "1) burrow 2) pond 3) hive 4) nest 5) a frog 6) under the ground.")
    left = ANIMALS; right = ["hive", "pond", "nest", "burrow", "den"]
    svg = '<svg width="660" height="416" style="align-self:center;flex-shrink:0">'
    for k, a in enumerate(left):
        svg += f'<g transform="translate(20,{k*84})">{icon(a, 0.95)}</g><circle cx="140" cy="{38+k*84}" r="7" fill="#4338ca"/>'
    for k, h in enumerate(right):
        svg += f'<circle cx="440" cy="{38+k*84}" r="7" fill="#4338ca"/><g transform="translate(470,{k*84})">{icon(h, 0.95)}</g>'
    svg += '</svg>'
    S.set(4, "Animal Homes Review",
        learnbox("<p class='big'><b>Review!</b> 10 points. Goal: <b>8 right</b>. Draw a line from each animal to its home.</p>")
        + svg
        + qs([("A nest is made of…", ["twigs and grass", "ice", "honey"]), ("Which home is a hole under the ground?", ["burrow", "hive", "nest"]),
              ("Which animal has its babies in a den in winter?", ["bear", "bee", "frog"]), ("Which home has hexagon rooms?", ["hive", "pond", "den"]),
              ("Where do tadpoles swim?", ["in a pond", "in a nest", "in a hive"])], 6)
        + '<div class="big">Score: ______ / 10 &nbsp; Thank You, God, for safe homes! <span class="star">☆</span></div>',
        "Lines: bird–nest, bee–hive, bear–den, rabbit–burrow, frog–pond (5 pts). 6) twigs and grass 7) burrow 8) bear 9) hive 10) in a pond.")
    return S

# ======================= NAYELI (Pre-K) =======================
# Each big animal = a few ellipses (cx, cy, rx, ry). Only the OUTER outline of their union is drawn,
# and dot-marker circles are spaced evenly along it (no overlapping dots).
BIG = {
 "bird":   dict(parts=[(290, 330, 175, 120), (490, 200, 68, 68)],
                extra='<polygon points="585,188 645,203 585,218"/><path d="M86,330 L22,278 L32,388 Z"/><circle cx="510" cy="185" r="9"/>'
                      '<path d="M250,478 L250,526 M340,478 L340,526"/><path d="M220,320 C260,390 360,390 400,320"/>'),
 "bee":    dict(parts=[(370, 360, 175, 110), (160, 350, 62, 62), (310, 185, 62, 82), (440, 185, 62, 82)],
                extra='<path d="M300,289 L300,431 M380,280 L380,440 M460,295 L460,425"/><path d="M140,256 L112,200 M182,256 L208,200"/>'
                      '<circle cx="140" cy="340" r="9"/><path d="M576,360 L630,360"/>'),
 "bear":   dict(parts=[(340, 335, 175, 165), (192, 165, 55, 55), (488, 165, 55, 55)],
                extra='<ellipse cx="340" cy="390" rx="70" ry="55"/><circle cx="340" cy="370" r="14"/><circle cx="275" cy="290" r="10"/><circle cx="405" cy="290" r="10"/><path d="M315,410 C330,425 350,425 365,410"/>'),
 "rabbit": dict(parts=[(285, 140, 40, 108), (395, 140, 40, 108), (340, 375, 155, 135)],
                extra='<circle cx="290" cy="345" r="10"/><circle cx="390" cy="345" r="10"/><path d="M325,395 L340,410 L355,395"/><path d="M340,410 L340,430 M260,400 L190,385 M260,415 L190,425 M420,400 L490,385 M420,415 L490,425"/>'),
 "frog":   dict(parts=[(340, 375, 225, 135), (235, 215, 60, 60), (445, 215, 60, 60)],
                extra='<circle cx="235" cy="215" r="18"/><circle cx="445" cy="215" r="18"/><path d="M220,410 C280,460 400,460 460,410"/>'),
}
def _inside(x, y, p, pad=1.0):
    cx, cy, rx, ry = p
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 < pad

def big_dots(an, gap=56):
    d = BIG[an]; parts = d["parts"]; segs, dots = [], []
    for j, p in enumerate(parts):
        cx, cy, rx, ry = p; cur = []
        for k in range(361):
            t = M.radians(k); x, y = cx + rx * M.cos(t), cy + ry * M.sin(t)
            if any(_inside(x, y, q, 0.98) for m, q in enumerate(parts) if m != j):
                if len(cur) > 1: segs.append(cur)
                cur = []; continue
            cur.append((x, y))
            if all((x - a) ** 2 + (y - b) ** 2 >= gap * gap for a, b in dots):
                dots.append((x, y))
        if len(cur) > 1: segs.append(cur)
    outl = "".join('<path d="M' + " L".join(f"{x:.0f},{y:.0f}" for x, y in s) + '"/>' for s in segs)
    dc = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="24" fill="#fff" stroke="#a21caf" stroke-width="3"/>' for x, y in dots)
    return (f'<svg width="680" height="546" viewBox="0 0 680 546" style="align-self:center;flex-shrink:0">'
            f'<g fill="none" stroke="#c9cde3" stroke-width="4">{outl}</g>{dc}'
            f'<g fill="none" stroke="#1f2a5c" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{d["extra"]}</g></svg>'), len(dots)

def trace_path(kind, y, x0=130, x1=560, h=40):
    if kind == "straight": d = f"M{x0},{y} L{x1},{y}"
    elif kind == "wavy": d = f"M{x0},{y} " + " ".join(f"Q{x0 + (k+0.5)*(x1-x0)/6:.0f},{y + (-h if k % 2 == 0 else h)} {x0 + (k+1)*(x1-x0)/6:.0f},{y}" for k in range(6))
    elif kind == "zigzag": d = f"M{x0},{y} " + " ".join(f"L{x0 + (k+1)*(x1-x0)/8:.0f},{y + (-h if k % 2 == 0 else h)*0.8 if k < 7 else y}" for k in range(8))
    else: d = f"M{x0},{y} " + " ".join(f"Q{x0 + (k+0.5)*(x1-x0)/4:.0f},{y - 2*h} {x0 + (k+1)*(x1-x0)/4:.0f},{y}" for k in range(4))  # hills
    return f'<path d="{d}"/><circle cx="{x0}" cy="{y}" r="9" fill="#a21caf" stroke="none"/>'

def nayeli_pages(i):
    an = ANIMALS[i]; home = HOMES[an]; Nm = "Nayeli"
    # ---- p1 dot marker ----
    big, nd = big_dots(an)
    p1 = page(Nm, i, "Pre-K", f"Animal of the Day · {an.title()}",
        f'<div class="center huge">This is a {an}!</div>'
        f'<div class="big center">Mom reads: “Dot every circle. Then color the {an}!”</div>'
        + big
        + f'<div class="flexrow" style="justify-content:center;align-items:center;gap:24px">{icon(an, 1.4)}<div class="huge">lives in a {home}</div>{icon(home, 1.4)}</div>'
        + f'<div class="big center">Say it with Mom: “{an}… {home}!” <span class="star">☆</span></div>')
    # ---- p2 tracing ----
    kinds = [["straight", "wavy", "zigzag", "hills"], ["wavy", "straight", "hills", "zigzag"], ["zigzag", "hills", "straight", "wavy"],
             ["hills", "zigzag", "wavy", "straight"], ["straight", "hills", "zigzag", "wavy"]][i]
    rows = ""
    for k, kd in enumerate(kinds):
        y = 70 + k * 130
        rows += (f'<g transform="translate(0,{y-38})">{icon(an, 0.95)}</g><g transform="translate(570,{y-38})">{icon(home, 0.95)}</g>'
                 f'<g fill="none" stroke="#9a9aa8" stroke-width="7" stroke-dasharray="2,13" stroke-linecap="round">{trace_path(kd, y, 115, 565)}</g>')
    strokes = {0: "|", 1: "—", 2: "|", 3: "—", 4: "o"}[i]
    if strokes == "|": st = "".join(f'<path d="M{40+k*62},14 L{40+k*62},96"/><circle cx="{40+k*62}" cy="14" r="7" fill="#a21caf" stroke="none"/>' for k, _ in enumerate(range(10)))
    elif strokes == "—": st = "".join(f'<path d="M{30+k*215},55 L{200+k*215},55"/><circle cx="{30+k*215}" cy="55" r="7" fill="#a21caf" stroke="none"/>' for k in range(3))
    else: st = "".join(f'<circle cx="{70+k*130}" cy="55" r="42"/>' for k in range(5))
    p2 = page(Nm, i, "Pre-K", f"Help the {an.title()} Get Home",
        f'<div class="big center">Mom reads: “Start at the pink dot. Trace each path to take the {an} home to its {home}!”</div>'
        f'<svg width="680" height="560" style="align-self:center;flex-shrink:0">{rows}</svg>'
        f'<div class="big center">Now trace these lines with a crayon:</div>'
        f'<svg width="660" height="112" style="align-self:center;flex-shrink:0" fill="none" stroke="#9a9aa8" stroke-width="7" stroke-dasharray="2,13" stroke-linecap="round">{st}</svg>')
    # ---- p3 stickers ----
    r = random.Random(500 + i); n = [4, 5, 3, 5, 4][i]
    picks = [an] * n + r.sample([x for x in ANIMALS if x != an] * 3, 12 - n); r.shuffle(picks)
    grid = "".join(f'<div class="center" style="border:2px solid #c9cde3;border-radius:14px;padding:6px">{icon(p, 1.65)}</div>' for p in picks)
    nums = list(range(1, 7))
    p3 = page(Nm, i, "Pre-K", f"Find the {an.title()}s",
        f'<div class="big center">Mom reads: “Put a sticker on every {an} like this one. Then color them!”</div>'
        f'<div class="center">{icon(an, 1.3)}</div>'
        f'<div class="grid4" style="gap:12px">{grid}</div>'
        f'<div class="big center">How many {an}s? Count with your finger, then dot the number!</div>'
        f'<div class="flexrow" style="justify-content:center;gap:18px">' + "".join(f'<div class="huge center" style="width:66px;height:66px;line-height:66px;border:2.5px solid #a21caf;border-radius:50%">{k}</div>' for k in nums) + '</div>')
    return [p1, p2, p3]

NAYELI_KEY = {i: f"{ANIMALS[i]}: sticker page has {[4,5,3,5,4][i]} {ANIMALS[i]}s" for i in range(5)}
