from lib import *
import random, math

WK = 3
VID = [yt("MM 3 times table song"), yt("MM 4 times table song"), yt("MM skip counting by 3 song"),
       yt("MM one step multiplication word problems"), yt("MM four times table song 2")]
VIDSC = [yt("SC count by 2s Jack Hartmann"), yt("SC count by 2s and move"), yt("SC dancing twos"),
         yt("SC get ready count by 2s"), yt("SC count by 2s song")]
TITLES = ["The 3s", "The 4s", "3s & 4s Mix-Up", "Word Problems + Speed Drill", "Saturday Checkpoint"]
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

THREES = [(3, k) for k in range(1, 11)]; FOURS = [(4, k) for k in range(1, 11)]
OLD = [(a, k) for a in (0, 1, 2, 5, 10) for k in range(1, 11)]

WORD = [
 ("A tricycle has 3 wheels. How many wheels are on 7 tricycles?", 21),
 ("Each chair has 4 legs. How many legs do 6 chairs have?", 24),
 ("Mom packed 3 crackers for every kid. There are 8 kids. How many crackers?", 24),
 ("A pack holds 4 juice boxes. How many juice boxes are in 9 packs?", 36),
 ("Nylah read 3 chapters every day for 5 days. How many chapters did she read?", 15),
 ("There are 4 quarters in a dollar. How many quarters are in 7 dollars?", 28),
]

def mult_page(name, i):
    v = qr_box(VID[i], "Watch the song", 64)
    def table(n):
        return ('<div class="lab">Write the ' + str(n) + 's table. Say each fact out loud as you write it.</div><div class="grid2" style="width:70%">'
                + "".join(f'<div style="font-size:16pt;padding:5px 0">{n} × {k} = <span class="blank-ln" style="min-width:50px"></span></div>' for k in range(1, 11)) + '</div>')
    if i == 0:
        fs = facts(0, 20, THREES, 31)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>This week: the 3s and 4s.</b> Read the 3s table out loud 3 times, then cover it and say it from memory. '
                'Chant it like a song: “3, 6, 9… 12, 15, 18… 21, 24, 27… 30!”</p><p style="font-size:14pt;font-weight:600">3 · 6 · 9 · 12 · 15 · 18 · 21 · 24 · 27 · 30</p></div>' + v + '</div>'
                + table(3) + '<div class="lab">Mixed 3s facts</div>' + fact_grid(fs))
        KEYS[0] = "3s table: 3,6,9,…,30. Facts: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 1:
        fs = facts(1, 20, FOURS, 32)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>The 4s:</b> every answer is an even number. Read the table out loud 3 times, '
                'then cover it and say it from memory. Watch the tricky ones: 4 × 6 = 24, 4 × 7 = 28, 4 × 8 = 32.</p><p style="font-size:14pt;font-weight:600">4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 36 · 40</p></div>' + v + '</div>'
                + table(4) + '<div class="lab">Mixed 4s facts</div>' + fact_grid(fs))
        KEYS[1] = "4s table: 4,8,12,…,40. Facts: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 2:
        fs = facts(2, 30, THREES + FOURS + THREES + FOURS + OLD, 33)
        body = (f'<div class="flexrow"><div class="learn grow"><p><b>Mix-up day!</b> Say the 3s and 4s tables out loud once each. Then do all 30 facts — '
                'they include the 0s, 1s, 2s, 5s, and 10s you already know. Circle any you had to stop and think about, and practice those 3 extra times.</p></div>' + v + '</div>'
                + '<div class="lab">Mixed facts</div>' + fact_grid(fs, 5, "16pt")
                + '<div class="lab">Facts I circled (write each one 3 times):</div>' + lines(3))
        KEYS[2] = "Mixed: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    elif i == 3:
        fs = facts(3, 20, THREES + FOURS, 34)
        body = (f'<div class="flexrow"><div class="learn grow"><p>“Each” and “every” are clue words to multiply. Write the multiplication fact, then the answer.</p></div>' + v + '</div>'
                + "".join(f'<div class="box"><b>{n+1}.</b> {esc(q)}<div style="margin-top:4px">Fact: <span class="blank-ln" style="min-width:120px"></span> &nbsp; Answer: <span class="blank-ln"></span></div></div>' for n, (q, a) in enumerate(WORD))
                + '<div class="lab">Speed drill — Mom times 2 minutes. Time: ______</div>' + fact_grid(fs))
        KEYS[3] = "Word problems: " + ", ".join(f"{n+1}) {a}" for n, (q, a) in enumerate(WORD)) + ". Drill: " + ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    else:
        fs = facts(4, 40, THREES + FOURS + THREES + FOURS + OLD, 35)
        body = ('<div class="learn"><p><b>Checkpoint!</b> 40 facts. Mom times you — aim to finish in 4 minutes. Goal: <b>32 or more right (80%)</b>. '
                'Circle any you miss, and practice those on Monday.</p></div>'
                + fact_grid(fs, 4, "14pt") + '<div class="big" style="margin-top:6px">Score: ______ / 40 &nbsp;&nbsp; Time: ______</div>'
                '<div class="lab">Facts I need to practice:</div>' + lines(1))
        KEYS[4] = ", ".join(f"{a}×{b}={a*b}" for a, b in fs)
    return page(name, i, "Multiplication Mastery", f"Week {WK} · {TITLES[i]}", body)

# ---------------- Skip Count Stars (Titus + Nayeli) ----------------
SC_TITLES = ["Counting by 2s", "Pairs of Socks", "Froggy Hops by 2s", "Review: 2s, 5s & 10s", "Dot-to-Dot by 2s"]

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

def sock_pair(w=58):
    sock = ('<path d="M10,4 L26,4 L26,40 C26,48 34,50 40,52 C48,55 46,66 36,66 L14,66 C8,66 6,60 8,54 L10,46 Z" fill="#fff" stroke="#1f2a5c" stroke-width="2.4"/>'
            '<path d="M10,12 L26,12" stroke="#1f2a5c" stroke-width="2"/>')
    return (f'<svg width="{w*1.6:.0f}" height="{w*1.2:.0f}" viewBox="0 0 96 70">{sock}<g transform="translate(44,0)">{sock}</g></svg>')

def skipstars_page(name, i):
    v = qr_box(VIDSC[i], "Sing along", 62)
    if i == 0:
        nums = "".join(f'<div>{school_print(str(n), 62, "trace", False)}</div>' for n in range(2, 21, 2))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">This week we count by <b>2s</b>! 2, 4, 6, 8, 10… skip one number every time! Sing it with the song.</p></div>' + v + '</div>'
                '<div class="lab">Trace each number as you count by 2s.</div>'
                f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;justify-items:center">{nums}</div>'
                '<div class="lab">Count 1 to 20 with Mom. Put a dot-marker dot on every number you SAY when you count by 2s: 2, 4, 6…</div>'
                '<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:5px">'
                + "".join(f'<div style="border:1.5px solid #c9cde3;border-radius:50%;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:18pt;font-weight:600">{n}</div>' for n in range(1, 21)) + '</div>'
                '<div class="big center">Say it to Mom: 2, 4, 6, 8, 10! <span class="star">☆</span></div>')
    elif i == 1:
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">A <b>pair</b> means 2! Socks come in pairs. Count the socks by 2s, then write how many.</p></div>{v}</div>'
                + "".join(f'<div class="flexrow" style="align-items:center">{"".join(sock_pair(54) for _ in range(k))}'
                          f'<div class="big" style="margin-left:auto">= <span class="blank-ln" style="min-width:60px"></span></div></div>' for k in (1, 2, 3, 4, 5))
                + '<div class="lab">Color each pair of socks to match — the same colors on both socks!</div>'
                '<div class="big center">Find pairs at home: shoes, eyes, ears, hands! <span class="star">☆☆☆</span></div>')
    elif i == 2:
        W, n = 680, 10
        ticks = "".join(f'<line x1="{20+k*64}" x2="{20+k*64}" y1="120" y2="140" stroke="#1f2a5c" stroke-width="2.5"/>'
                        f'<text x="{20+k*64}" y="166" text-anchor="middle" font-size="20" font-weight="700" fill="#1f2a5c">{2*k if k in (0,1,2,5,8,10) else ""}</text>' for k in range(n + 1))
        hops = "".join(f'<path d="M{20+k*64},118 Q{52+k*64},50 {84+k*64},118" fill="none" stroke="#6d28d9" stroke-width="2.5" stroke-dasharray="6,5"/>' for k in range(n))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Froggy hops by <b>2s</b>! Trace each hop with your finger and say the number where he lands. '
                'Write the missing numbers under the lines.</p></div>{v}</div>'
                f'<svg width="{W}" height="180" style="align-self:center"><line x1="10" x2="{W-10}" y1="130" y2="130" stroke="#1f2a5c" stroke-width="3"/>{ticks}{hops}</svg>'
                '<div class="lab">Fill in the missing 2s. Dot each box when you say it!</div>' + skip_row(2, 10, {0, 1, 3, 5, 6, 8})
                + '<div class="lab">Draw 3 frogs. Give each frog 2 eyes. How many eyes? <span class="blank-ln"></span></div><div class="answer-space"></div>')
    elif i == 3:
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Review day! Count by <b>2s</b>, <b>5s</b>, and <b>10s</b>. Write the missing numbers (Mom helps you count out loud).</p></div>{v}</div>'
                '<div class="lab">By 2s</div>' + skip_row(2, 10, {0, 2, 4, 6, 8})
                + '<div class="lab">By 5s</div>' + skip_row(5, 10, {0, 1, 3, 5, 7, 9})
                + '<div class="lab">By 10s</div>' + skip_row(10, 10, {0, 2, 4, 6, 8})
                + '<div class="lab">Counting-bear time! Make groups of 2 bears. Count them by 2s. How many bears? <span class="blank-ln"></span></div>'
                f'<div style="display:flex;gap:16px;justify-content:center">{ten_frame(0,44)}{ten_frame(0,44)}</div>'
                '<div class="big center">Dot 2 circles at a time and count by 2s to 20!</div>')
    else:
        pts = []
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5
            rad = 150 if k % 2 == 0 else 62
            pts.append((210 + rad * math.cos(ang), 190 + rad * math.sin(ang)))
        dots = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#1f2a5c"/><text x="{x+(10 if x>=210 else -10):.0f}" y="{y-8:.0f}" '
                       f'text-anchor="{"start" if x>=210 else "end"}" font-size="18" font-weight="700" fill="#6d28d9">{(k+1)*2}</text>' for k, (x, y) in enumerate(pts))
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Connect the dots by 2s: start at 2, then 4, 6… up to 20, then back to 2. What did you make?</p></div>{v}</div>'
                f'<svg width="420" height="370" style="align-self:center">{dots}</svg>'
                '<div class="big center">I made a <span class="blank-ln" style="min-width:140px"></span>! Color it in!</div>'
                '<div class="big center">Say it to Mom: count by 2s to 20 <span class="star">☆</span> &nbsp; 5s to 50 <span class="star">☆</span> &nbsp; 10s to 100 <span class="star">☆</span></div>')
    return page(name, i, "Skip Count Stars", f"Week {WK} · {SC_TITLES[i]}", body)

SC_KEY = "Day 1: dots on 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Day 2: 2, 4, 6, 8, 10. Day 3: number line missing 6, 8, 12, 14, 18; boxes missing 6, 10, 16, 20; 3 frogs = 6 eyes. Day 4: 2s 4,8,12,16,20 · 5s 15,25,35,45 · 10s 20,40,60,80,100. Day 5: a star."
