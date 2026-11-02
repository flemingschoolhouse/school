from lib import *
import random, math

VID = [yt("count by 5s song for kids"), yt("count by 10s song for kids"), yt("multiplication 5s and 10s trick kids"),
       yt("multiplication word problems 5s 10s kids"), yt("skip counting by 5 and 10 song")]
TITLES = ["The 5s", "The 10s", "5s & 10s Mix-Up", "Word Problems + Speed Drill", "Saturday Checkpoint"]
KEYS = {}  # (day) -> answer html

def facts(day, n, pool, seed):
    r = random.Random(seed); out = []
    while len(out) < n:
        a, b = r.choice(pool)
        if r.random() < 0.5: a, b = b, a
        if out and out[-1] == (a, b): continue
        out.append((a, b))
    return out

def fact_grid(fs, cols=5, size="15pt"):
    cells = "".join(f'<div style="font-size:{size};padding:8px 0">{a} × {b} = <span class="blank-ln" style="min-width:44px"></span></div>' for a, b in fs)
    return f'<div class="grid{cols}">{cells}</div>'

def skip_row(step, n, given):
    cells = "".join(f'<div style="border:1.6px solid #c9cde3;border-radius:6px;height:38px;display:flex;align-items:center;justify-content:center;font-size:15pt;font-weight:600">'
                    f'{step*(k+1) if (k in given) else ""}</div>' for k in range(n))
    return f'<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:5px">{cells}</div>'

def array_svg(rows, cols, r=7, gap=22):
    w = cols * gap + 10; h = rows * gap + 10
    dots = "".join(f'<circle cx="{12+c*gap}" cy="{12+rr*gap}" r="{r}" fill="#6d28d9"/>' for rr in range(rows) for c in range(cols))
    return f'<svg width="{w}" height="{h}">{dots}</svg>'

FIVES = [(5, k) for k in range(1, 11)]; TENS = [(10, k) for k in range(1, 11)]
OLD = [(a, k) for a in (0, 1, 2) for k in range(1, 11)]

WORD = [
 ("Mom bought 6 packs of gum. Each pack has 5 pieces. How many pieces in all?", 30),
 ("Nevaeh saved 7 dimes. Each dime is worth 10 cents. How many cents does she have?", 70),
 ("There are 9 kids. Each kid holds up one hand with 5 fingers. How many fingers?", 45),
 ("A box holds 10 crayons. How many crayons are in 8 boxes?", 80),
 ("Titus has 4 nickels. A nickel is 5 cents. How many cents is that?", 20),
 ("Dad set up 5 rows of chairs at church with 10 chairs in each row. How many chairs?", 50),
]

def mult_page(name, i):
    v = qr_box(VID[i], "Watch the song", 64)
    def table(n):
        return ('<div class="lab">Write the ' + str(n) + 's table. Say each fact out loud as you write it.</div><div class="grid2" style="width:70%">'
                + "".join(f'<div style="font-size:16pt;padding:5px 0">{n} × {k} = <span class="blank-ln" style="min-width:50px"></span></div>' for k in range(1, 11)) + '</div>')
    if i == 0:
        fs = facts(0, 20, FIVES, 11)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>This week: the 5s and 10s.</b> Read the 5s table out loud 3 times, then cover it and say it from memory. '
                'Every 5s answer ends in 5 or 0.</p><p style="font-size:14pt;font-weight:600">5 · 10 · 15 · 20 · 25 · 30 · 35 · 40 · 45 · 50</p></div>' + v + '</div>'
                + table(5) + '<div class="lab">Mixed 5s facts</div>' + fact_grid(fs))
        KEYS[0] = "5s table: 5,10,15,…,50. Facts: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 1:
        fs = facts(1, 20, TENS, 12)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>The 10s:</b> any number times 10 — write the number and put a 0 on the end. 6 × 10 = 60. '
                'Read the table out loud 3 times, then say it from memory.</p><p style="font-size:14pt;font-weight:600">10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100</p></div>' + v + '</div>'
                + table(10) + '<div class="lab">Mixed 10s facts</div>' + fact_grid(fs))
        KEYS[1] = "10s table: 10,20,…,100. Facts: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 2:
        fs = facts(2, 30, FIVES + TENS + OLD, 13)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>Mix-up day!</b> Say the 5s and 10s tables out loud once each. Then do all 30 facts — '
                'they include last week\'s 0s, 1s, and 2s. Circle any you had to stop and think about, and practice those 3 extra times.</p></div>' + v + '</div>'
                + '<div class="lab">Mixed facts</div>' + fact_grid(fs, 5, "16pt")
                + '<div class="lab">Facts I circled (write each one 3 times):</div>' + lines(3))
        KEYS[2] = "Mixed: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 3:
        fs = facts(3, 20, FIVES + TENS, 14)
        body = (f'<div class="flexrow"><div class="learn grow"><p>“Each” and “every” are clue words to multiply. Write the multiplication fact, then the answer.</p></div>' + v + '</div>'
                + "".join(f'<div class="box"><b>{n+1}.</b> {esc(q)}<div style="margin-top:4px">Fact: <span class="blank-ln" style="min-width:120px"></span> &nbsp; Answer: <span class="blank-ln"></span></div></div>' for n, (q, a) in enumerate(WORD))
                + '<div class="lab">Speed drill — Mom times 2 minutes. Time: ______</div>' + fact_grid(fs))
        KEYS[3] = "Word problems: " + ", ".join(f"{n+1}) {a}" for n, (q, a) in enumerate(WORD)) + ". Drill: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    else:
        fs = facts(4, 40, FIVES + TENS + OLD, 15)
        body = ('<div class="learn"><p><b>Checkpoint!</b> 40 facts. Mom times you — aim to finish in 4 minutes. Goal: <b>32 or more right (80%)</b>. '
                'Circle any you miss, and practice those on Monday.</p></div>'
                + fact_grid(fs, 4, "14pt") + '<div class="big" style="margin-top:6px">Score: ______ / 40 &nbsp;&nbsp; Time: ______</div>'
                '<div class="lab">Facts I need to practice:</div>' + lines(1))
        KEYS[4] = ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    return page(name, i, "Multiplication Mastery", f"Week 2 · {TITLES[i]}", body)

# ---------------- Skip Count Stars (Titus + Nayeli) ----------------
SC_TITLES = ["Counting by 10s", "Counting by 5s", "High Five! Hands Make 5", "Ten-Frame Towers", "Dot-to-Dot by 10s"]

def ten_frame(filled=0, sz=34):
    cells = "".join(f'<rect x="{2+c*sz}" y="{2+r*sz}" width="{sz}" height="{sz}" fill="#fff" stroke="#1f2a5c" stroke-width="2"/>'
                    + (f'<circle cx="{2+c*sz+sz/2}" cy="{2+r*sz+sz/2}" r="{sz*0.36}" fill="#6d28d9"/>' if r*5+c < filled else "")
                    for r in range(2) for c in range(5))
    return f'<svg width="{5*sz+4}" height="{2*sz+4}">{cells}</svg>'

def hand_svg(w=70):
    # simple open hand outline
    return (f'<svg width="{w}" height="{w*1.1}" viewBox="0 0 70 77"><path d="M18,75 C8,60 4,46 6,38 C8,32 14,34 16,42 L18,48 L16,14 C16,8 24,8 24,14 L25,36 '
            'L26,6 C26,0 34,0 34,6 L35,36 L37,9 C37,3 45,3 45,9 L44,38 L47,17 C48,11 56,12 55,18 L52,52 C51,64 46,72 42,75 Z" '
            'fill="#fff" stroke="#1f2a5c" stroke-width="2"/></svg>')

def skipstars_page(name, i):
    v = qr_box(VID[[1, 0, 4, 1, 1][i]], "Sing along", 62)
    if i == 0:
        nums = "".join(f'<div style="display:flex;flex-direction:column;align-items:center">{school_print(str(n), 62, "trace", False)}</div>' for n in range(10, 101, 10))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Let\'s count by <b>10s</b>! 10, 20, 30… all the way to 100! Sing it with the song.</p></div>' + v + '</div>'
                '<div class="lab">Trace each number as you count by 10s.</div>'
                f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;justify-items:center">{nums}</div>'
                '<div class="lab">Dot each ten-frame full with your dot marker. Count by 10s: “10, 20, 30!”</div>'
                f'<div style="display:flex;gap:16px;justify-content:center">{ten_frame(0,44)}{ten_frame(0,44)}{ten_frame(0,44)}</div>'
                '<div class="big center">How many dots? &nbsp; <span class="blank-ln"></span></div>')
    elif i == 1:
        nums = "".join(f'<div>{school_print(str(n), 62, "trace", False)}</div>' for n in range(5, 51, 5))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Now count by <b>5s</b>: 5, 10, 15, 20… Numbers that end in 5 or 0!</p></div>{v}</div>'
                '<div class="lab">Trace the 5s.</div>'
                f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;justify-items:center">{nums}</div>'
                '<div class="lab">Put a sticker (or dot) on every number that ends in 5 or 0.</div>'
                '<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:4px">'
                + "".join(f'<div style="border:1.5px solid #c9cde3;border-radius:5px;text-align:center;font-size:16pt;padding:10px 0">{n}</div>' for n in range(1, 51)) + '</div>')
    elif i == 2:
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">One hand has <b>5</b> fingers. Count the hands by 5s!</p></div>{v}</div>'
                + "".join(f'<div class="flexrow" style="align-items:center">{"".join(hand_svg(74) for _ in range(k))}'
                          f'<div class="big" style="margin-left:auto">= <span class="blank-ln" style="min-width:60px"></span></div></div>' for k in (1, 2, 3, 4))
                + '<div class="lab">Trace your own hand in the box and color it!</div><div class="answer-space"></div>')
    elif i == 3:
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">A ten-frame holds <b>10</b>. Count the full frames by 10s, then write how many.</p></div>{v}</div>'
                + "".join(f'<div class="flexrow" style="align-items:center;gap:10px">{"".join(ten_frame(10, 30) for _ in range(k))}'
                          f'<div class="big" style="margin-left:auto">= <span class="blank-ln" style="min-width:60px"></span></div></div>' for k in (2, 4, 5))
                + '<div class="lab">Dot-marker time! Fill these frames, then count by 10s.</div>'
                f'<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">{ten_frame(0,40)}{ten_frame(0,40)}{ten_frame(0,40)}{ten_frame(0,40)}</div>'
                '<div class="big center">I counted: <span class="blank-ln"></span></div>')
    else:
        pts = []
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5
            rad = 150 if k % 2 == 0 else 62
            pts.append((210 + rad * math.cos(ang), 190 + rad * math.sin(ang)))
        dots = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#1f2a5c"/><text x="{x+(10 if x>=210 else -10):.0f}" y="{y-8:.0f}" '
                       f'text-anchor="{"start" if x>=210 else "end"}" font-size="18" font-weight="700" fill="#6d28d9">{(k+1)*10}</text>' for k, (x, y) in enumerate(pts))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Connect the dots by 10s: start at 10, then 20, 30… up to 100, then back to 10. What did you make?</p></div>{v}</div>'
                f'<svg width="420" height="370" style="align-self:center">{dots}</svg>'
                '<div class="big center">I made a <span class="blank-ln" style="min-width:140px"></span>! Color it in!</div>'
                '<div class="big center">Say it to Mom: count by 10s to 100 <span class="star">☆</span> &nbsp; count by 5s to 50 <span class="star">☆</span></div>')
    return page(name, i, "Skip Count Stars", f"Week 2 · {SC_TITLES[i]}", body)

SC_KEY = "Day 1: 30 dots. Day 3: 5, 10, 15, 20. Day 4: 20, 40, 50. Day 5: a star."
