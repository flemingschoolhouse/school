# Nariah (2nd grade) core studies — week of Nov 10–14, 2026.
# Mostly tap/circle answers + tracing + drawing (tablet reads aloud). Keys are computed from the same numbers.
from core_common import *
from mathgen import *
from core_young import ic, I, icon, time_choices, clock_pick
import random, math as M

KID = "Nariah"

# ---------------- new line icons (no fills -> she colors them) ----------------
def _star(cx, cy, R, r=None):
    r = r or R * 0.42
    return " ".join(f"{cx + (R if j % 2 == 0 else r) * M.sin(j * M.pi / 5):.1f},{cy - (R if j % 2 == 0 else r) * M.cos(j * M.pi / 5):.1f}" for j in range(10))

def _flag():
    s = '<path d="M8,4 L8,98"/><rect x="12" y="8" width="160" height="78"/>'
    h = 78 / 13
    s += "".join(f'<path d="M{78 if k < 7 else 12},{8 + k*h:.1f} L172,{8 + k*h:.1f}" stroke-width="1.4"/>' for k in range(1, 13))
    s += '<rect x="12" y="8" width="66" height="42"/>'
    s += "".join(f'<polygon points="{_star(20 + c*12.5 + (6 if rw % 2 else 0), 15 + rw*7.2, 2.6)}" stroke-width="1"/>'
                 for rw in range(5) for c in range(5 if rw % 2 == 0 else 4))
    return ic(s, 180, 100, "0 0 180 100")

I.update({
 "kite": ic('<path d="M45,4 L68,28 L45,60 L22,28Z"/><path d="M45,4 L45,60 M22,28 L68,28"/><path d="M45,60 C38,66 52,70 45,78"/><path d="M40,68 L50,66"/>'),
 "cake": ic('<rect x="14" y="40" width="62" height="32" rx="3"/><path d="M14,52 C24,60 34,44 45,52 C56,60 66,44 76,52"/><path d="M45,40 L45,26"/><path d="M45,14 C38,22 52,22 45,14Z"/>'),
 "bike": ic('<circle cx="20" cy="56" r="14"/><circle cx="70" cy="56" r="14"/><path d="M20,56 L38,30 L62,30 L70,56 M38,30 L46,56 L62,30 M46,56 L20,56"/><path d="M36,24 L44,24 M62,30 L58,18 L66,18"/>'),
 "bone": ic('<path d="M24,32 C10,30 10,14 22,16 C26,6 38,14 32,26 L58,26 C52,14 64,6 68,16 C80,14 80,30 66,32 C80,34 80,50 68,48 C64,58 52,50 58,38 L32,38 C38,50 26,58 22,48 C10,50 10,34 24,32Z"/>'),
 "cube": ic('<path d="M22,26 L48,14 L74,26 L74,60 L48,72 L22,60Z"/><path d="M22,26 L48,38 L74,26 M48,38 L48,72"/>'),
 "rose": ic('<path d="M45,40 L45,78"/><path d="M45,62 C34,54 26,58 24,64 C34,68 40,66 45,62"/><path d="M45,40 C30,38 26,22 32,10 C38,16 42,14 45,8 C48,14 52,16 58,10 C64,22 60,38 45,40Z"/><path d="M38,20 C42,28 48,28 52,20"/>'),
 "sun": ic('<circle cx="45" cy="40" r="15"/>' + "".join(f'<path d="M{45+21*M.sin(k*M.pi/4):.1f},{40-21*M.cos(k*M.pi/4):.1f} L{45+32*M.sin(k*M.pi/4):.1f},{40-32*M.cos(k*M.pi/4):.1f}"/>' for k in range(8))),
 "drop": ic('<path d="M45,6 C36,26 24,38 24,52 C24,66 34,74 45,74 C56,74 66,66 66,52 C66,38 54,26 45,6Z"/><path d="M34,52 C34,60 38,64 44,65"/>'),
 "air": ic('<path d="M8,30 L56,30 C68,30 68,14 58,14 C50,14 50,24 56,24"/><path d="M8,44 L72,44 C84,44 84,60 72,60 C64,60 64,52 70,52"/><path d="M8,58 L44,58"/>'),
 "soil": ic('<path d="M6,40 L84,40 L80,74 L10,74Z"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(20, 52), (36, 62), (52, 50), (66, 64), (28, 68), (60, 56), (74, 48)]) + '<path d="M45,40 L45,22 M45,30 C36,22 32,26 30,22 M45,26 C54,18 58,22 60,18"/>'),
 "seed": ic('<path d="M6,60 L84,60"/><ellipse cx="45" cy="44" rx="16" ry="10"/><path d="M34,44 C40,40 50,40 56,44"/>'),
 "sprout": ic('<path d="M6,60 L84,60"/><path d="M45,60 L45,34"/><path d="M45,40 C34,28 24,32 22,26 C30,22 42,26 45,40"/><path d="M45,36 C56,24 66,28 68,22 C60,18 48,22 45,36"/><path d="M45,60 L38,72 M45,60 L52,72 M45,60 L45,74"/>'),
 "youngplant": ic('<path d="M6,64 L84,64"/><path d="M45,64 L45,12"/>' + "".join(f'<path d="M45,{y} C{45+d*14},{y-12} {45+d*30},{y-6} {45+d*32},{y-2} C{45+d*24},{y+4} {45+d*10},{y+4} 45,{y}"/>' for y, d in [(50, -1), (40, 1), (28, -1), (18, 1)]) + '<path d="M45,64 L36,76 M45,64 L54,76 M45,64 L45,78"/>'),
 "flower": ic('<path d="M6,66 L84,66"/><path d="M45,66 L45,32"/><circle cx="45" cy="20" r="6"/>' + "".join(f'<circle cx="{45+12*M.sin(k*M.pi/3):.1f}" cy="{20-12*M.cos(k*M.pi/3):.1f}" r="6.5"/>' for k in range(6)) + '<path d="M45,54 C32,42 22,48 20,42 C28,38 40,42 45,54"/><path d="M45,48 C58,36 68,42 70,36 C62,32 50,36 45,48"/><path d="M45,66 L36,78 M45,66 L54,78"/>'),
 "carrot": ic('<path d="M30,22 C40,18 54,20 58,28 C50,46 40,62 22,76 C24,56 24,38 30,22Z"/><path d="M44,20 C44,10 50,4 56,4 M48,22 C54,12 64,10 70,12 M52,24 C62,20 72,22 76,26"/><path d="M32,38 L40,40 M28,52 L34,54"/>'),
 "apple": ic('<path d="M45,24 C30,14 14,22 16,42 C18,62 32,76 45,70 C58,76 72,62 74,42 C76,22 60,14 45,24Z"/><path d="M45,24 C45,16 48,10 52,6"/><path d="M48,14 C56,6 66,10 66,12 C58,18 52,16 48,14"/>'),
 "flag": _flag(),
 "medal": ic('<path d="M30,4 L42,34 M60,4 L48,34 M30,4 L40,4 L48,22 M60,4 L50,4 L45,14"/><circle cx="45" cy="54" r="20"/>' f'<polygon points="{_star(45, 55, 12)}"/>'),
 "eagle": ic('<path d="M14,78 C12,52 20,30 40,20 C52,14 66,16 74,24 C80,28 84,34 86,42 C80,40 76,40 72,42 C70,48 64,50 60,46 C56,54 54,66 56,78"/>'
             '<circle cx="62" cy="28" r="2.6"/><path d="M70,30 C76,32 80,36 82,40"/><path d="M28,62 C34,56 40,56 46,60 M22,70 C30,64 38,64 44,68"/>'),
 "bell": ic('<path d="M30,20 C30,10 60,10 60,20 C62,40 66,54 76,62 L14,62 C24,54 28,40 30,20Z"/><path d="M14,62 L76,62 L76,67 L14,67Z"/><path d="M38,12 L38,4 L52,4 L52,12"/><path d="M47,28 L42,38 L48,46 L43,58"/><circle cx="45" cy="73" r="4"/>'),
 "torch": ic('<path d="M38,40 L52,40 L48,76 L42,76Z"/><path d="M33,34 L57,34 L52,40 L38,40Z"/><path d="M45,32 C30,24 38,14 38,4 C46,10 46,16 50,14 C56,20 56,28 45,32Z"/>'),
 "card": ic('<rect x="10" y="10" width="70" height="60" rx="4"/><path d="M45,10 L45,70"/><path d="M62,34 C58,26 50,30 54,38 L62,46 L70,38 C74,30 66,26 62,34Z"/>'),
})

def icap(name, scale, cap):
    return f'<div class="center">{icon(name, scale)}<div class="big"><b>{cap}</b></div></div>'

# ---------------- coins (simple circles sized like the real coins) ----------------
CENTS = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}
MM = {"penny": 19.05, "nickel": 21.21, "dime": 17.91, "quarter": 24.26}
def coin(name, k=2.7, value=True):
    r = MM[name] * k / 2; W = 2 * r + 4; c = W / 2
    fs = r * 0.42 if name != "quarter" else r * 0.37
    val = (f'<text x="{c}" y="{c + r*0.5:.1f}" text-anchor="middle" font-size="{r*0.42:.1f}" font-weight="700" fill="#1f2a5c">{CENTS[name]}¢</text>' if value else "")
    ty = c - r * 0.02 if value else c + fs * 0.35
    return (f'<svg width="{W:.0f}" height="{W:.0f}" style="vertical-align:middle;margin:0 2px"><circle cx="{c}" cy="{c}" r="{r:.1f}" fill="#fff" stroke="#1f2a5c" stroke-width="2.4"/>'
            f'<circle cx="{c}" cy="{c}" r="{r-4:.1f}" fill="none" stroke="#9aa0bb" stroke-width="1" stroke-dasharray="2,2"/>'
            f'<text x="{c}" y="{ty:.1f}" text-anchor="middle" font-size="{fs:.1f}" font-weight="600" fill="#1f2a5c">{name}</text>{val}</svg>')
def coins(lst, k=2.4, value=False):
    return "".join(coin(n, k, value) for n in lst)
def cents(n): return f"{n}¢"

def coin_set(r, lo=20, hi=99, nmin=3, nmax=6):
    while True:
        lst = [r.choice(["quarter", "quarter", "dime", "dime", "nickel", "penny", "penny"]) for _ in range(r.randint(nmin, nmax))]
        t = sum(CENTS[c] for c in lst)
        if lo <= t <= hi and len(set(lst)) >= 2:
            return lst, t
def money_choices(t):
    out = [t]
    for d in (5, 10, -5, -10, 1, 15):
        if t + d > 0 and t + d not in out: out.append(t + d)
        if len(out) == 3: break
    return [cents(x) for x in out]

# ---------------- math helpers ----------------
def vg(probs, start=1, cols=4):
    return f'<div class="grid{cols}" style="justify-items:center">' + "".join(
        f'<div style="display:flex;gap:4px"><span class="q" style="font-size:10pt;color:#2f5bd3;font-weight:700">{start+n}.</span>{vert(a,b,op).replace("class=\"vert\"", "class=\"vert\" style=\"padding-bottom:42px\"")}</div>'
        for n, (a, b, op) in enumerate(probs)) + '</div>'
def add_rg(r):
    while True:
        a, b = r.randint(14, 68), r.randint(13, 39)
        if a % 10 + b % 10 >= 10 and a + b < 100: return (a, b, "+")
def sub_rg(r):
    while True:
        a, b = r.randint(31, 96), r.randint(12, 58)
        if a % 10 < b % 10 and a > b + 5: return (a, b, "−")
def solve(p):
    a, b, op = p
    return a + b if op == "+" else a - b
def warmup(r, n, start=1, cols=4):
    ps = [(add_rg if k % 2 == 0 else sub_rg)(r) for k in range(n)]
    html_ = ('<div class="lab">Warm-up: regrouping! (Carry or borrow when you need to.)</div>' + vg(ps, start, cols))
    return html_, ps
def keylist(ps, start=1):
    return ", ".join(f"{start+n}) {solve(p)}" for n, p in enumerate(ps))

def _t(h, m): return f"{h}:{m:02d}"
def five_choices(h, m):
    """correct first; then 'read the number as minutes' mistake and 'wrong hour' mistake."""
    out = [_t(h, m)]
    for c in (_t(h, m // 5) if m % 5 == 0 and m // 5 != m else _t(h, 30), _t(h % 12 + 1, m), _t(h, (m + 30) % 60)):
        if c not in out: out.append(c)
    return out[:3]
def clock5_pick(h, m, size):
    return f'<div class="center">{clock(h, m, size)}{mc_opts(five_choices(h, m), f"c5{h}{m}{size}")}</div>'
def clock_ring(size=200, h=None, m=None):
    """clock with the 5-minute counts written outside each number (blue)."""
    p = 26; W = size + 2 * p; c = W / 2; R = size / 2 + 11
    lab = "".join(f'<text x="{c + R*M.sin(M.radians(k*30)):.1f}" y="{c - R*M.cos(M.radians(k*30)) + 5:.1f}" text-anchor="middle" '
                  f'font-size="13" font-weight="700" fill="#2f5bd3">{k*5:02d}</text>' for k in range(12))
    inner = clock(h or 0, m or 0, size, hands=h is not None)
    return f'<svg width="{W}" height="{W}">{lab}<g transform="translate({p},{p})">{inner}</g></svg>'

# ======================= MATH =======================
def nariah_math():
    S = Subject(KID, "Math", "Level 2 · Money & Time"); r = random.Random(1110)
    # ---- D1 coins
    wu, ps = warmup(r, 4)
    ident = ["dime", "quarter", "penny", "nickel", "quarter", "dime"]
    S.set(0, "Coins & Their Values",
        learnbox("<p class='big'>Meet the coins! A <b>penny</b> is <b>1¢</b>. A <b>nickel</b> is <b>5¢</b>. A <b>dime</b> is <b>10¢</b>. "
                 "A <b>quarter</b> is <b>25¢</b>. The ¢ sign means <b>cents</b>. Tricky: the <b>dime</b> is the smallest coin, but it is worth more than a penny or a nickel!</p>",
                 yt("N2 coin values song"), "Coin song")
        + f'<div class="flexrow" style="justify-content:space-around;align-items:center">{coins(["penny", "nickel", "dime", "quarter"], 3.0, True)}</div>'
        + wu
        + '<div class="lab">How much is each coin worth? Circle it.</div>'
        + mark_list([coin(n, 1.9, False) for n in ident], ["1¢", "5¢", "10¢", "25¢"], 5, cols=2)
        + '<div class="grid2">' + qs([("Which coin is worth the <b>most</b>?", ["quarter", "dime", "nickel", "penny"]),
              ("How many pennies make <b>1 nickel</b>?", ["5", "10", "1"]),
              ("How many pennies make <b>1 dime</b>?", ["10", "5", "25"]),
              ("Which coin is the <b>smallest</b>?", ["dime", "penny", "quarter"])], 11) + '</div>'
        + '<div class="lab">Trace:</div>' + trace_line("dime", 40, 2),
        f"Warm-up: {keylist(ps)}. Coins: " + ", ".join(f"{n+5}) {cents(CENTS[c])}" for n, c in enumerate(ident)) + ". 11) quarter 12) 5 13) 10 14) dime.")
    # ---- D2 counting coins
    wu, ps = warmup(r, 3, cols=3)
    sets = [coin_set(r) for _ in range(8)]
    S.set(1, "Counting Coins",
        learnbox("<p class='big'>To count coins, <b>start with the biggest</b> value and count on. "
                 "Quarter, then dimes, then nickels, then pennies. "
                 "<b>25</b> … <b>35</b> (+10) … <b>40</b> (+5) … <b>41</b> (+1). That's <b>41¢</b>!</p>"
                 '<p class="small">penny 1¢ · nickel 5¢ · dime 10¢ · quarter 25¢</p>', yt("N2 counting coins 2nd grade"), "Counting coins")
        + f'<div class="center">{coins(["quarter", "dime", "nickel", "penny"], 2.4, True)} <span class="big">= <b>41¢</b></span></div>'
        + wu
        + '<div class="lab">How much money? Start with the biggest coin. Circle the total.</div>'
        + '<div class="grid2" style="gap:10px 20px">' + "".join(
            f'<div class="mcq box"><b>{n+4}.</b> {coins(lst, 1.9)}{mc_opts(money_choices(t), f"cs{n}{t}")}</div>' for n, (lst, t) in enumerate(sets)) + '</div>',
        f"Warm-up: {keylist(ps)}. " + ", ".join(f"{n+4}) {cents(t)}" for n, (l, t) in enumerate(sets)) + ".")
    # ---- D3 time to 5 minutes
    wu, ps = warmup(r, 3, cols=3)
    times = [(3, 20), (7, 45), (10, 10), (1, 35), (5, 50), (8, 15)]
    S.set(2, "Time to 5 Minutes",
        '<div class="flexrow" style="align-items:center">'
        + learnbox("<p class='big'>The long <b>minute hand</b> moves <b>5 minutes</b> from one number to the next. "
                   "<b>Count by 5s</b> around the clock: 5, 10, 15, 20 … 55. "
                   "Short hand = hour. Count by 5s to the long hand. This clock says <b>2:25</b>.</p>",
                   yt("N2 telling time to 5 minutes song"), "Time song")
        + f'<div>{clock_ring(130, 2, 25)}</div></div>'
        + wu
        + '<div class="lab">What time is it? Count by 5s. Circle the time.</div><div class="grid3" style="justify-items:center">'
        + "".join(clock5_pick(h, m, 104) for h, m in times) + '</div>'
        + '<div class="lab">Draw the hands.</div><div class="grid3" style="justify-items:center">'
        + "".join(f'<div class="center">{clock(0, 0, 100, False)}<div class="big"><b>{t}</b></div></div>' for t in ["4:05", "9:40", "12:25"]) + '</div>',
        f"Warm-up: {keylist(ps)}. Clocks: " + ", ".join(_t(h, m) for h, m in times)
        + ". Drawn: 4:05 (short just past 4, long on 1), 9:40 (short between 9 &amp; 10, long on 8), 12:25 (short just past 12, long on 5).")
    # ---- D4 mixed + word problems
    wu, ps = warmup(r, 4)
    sets = [coin_set(r, 30, 95, 4, 6) for _ in range(2)]
    tm = [(6, 55), (11, 30), (2, 5)]
    wp = [("Nariah has 1 quarter and 1 dime. How much money is that?", [cents(35), cents(26), cents(15)]),
          ("A pencil costs 10¢. Nariah has 4 dimes. How many pencils can she buy?", ["4", "10", "40"]),
          ("Titus had 50¢. He spent 25¢ on a sticker. How much is left?", [cents(25), cents(75), cents(50)]),
          ("Bible study starts at 7:00. It is 6:55. How many minutes until it starts?", ["5 minutes", "55 minutes", "1 minute"])]
    assert 25 + 10 == 35 and 40 // 10 == 4 and 50 - 25 == 25
    S.set(3, "Mix It Up!",
        learnbox("<p class='big'>Money, time, and math all together! Read each word problem slowly (or let your tablet read it). "
                 "Look for clue words: <b>in all</b> means add, <b>left</b> means subtract.</p>", yt("N2 money word problems 2nd grade"), "Money problems")
        + wu
        + '<div class="lab">How much money? Circle it.</div><div class="grid2" style="gap:8px 20px">'
        + "".join(f'<div class="mcq box"><b>{n+5}.</b> {coins(l, 2.0)}{mc_opts(money_choices(t), f"d4{n}{t}")}</div>' for n, (l, t) in enumerate(sets)) + '</div>'
        + '<div class="lab">Circle the time.</div><div class="grid3" style="justify-items:center">' + "".join(clock5_pick(h, m, 110) for h, m in tm) + '</div>'
        + '<div class="lab">Word problems</div>' + qs(wp, 10),
        f"Warm-up: {keylist(ps)}. 5) {cents(sets[0][1])} 6) {cents(sets[1][1])}. Clocks 6:55, 11:30, 2:05. 10) 35¢ 11) 4 12) 25¢ 13) 5 minutes.")
    # ---- D5 checkpoint (10 scored)
    cp = [add_rg(r), sub_rg(r)]
    sets = [coin_set(r, 25, 90, 3, 5) for _ in range(3)]
    tm = [(4, 40), (9, 15), (12, 50)]
    wp = [("Which coin is worth 5¢?", ["nickel", "dime", "penny"]),
          ("Mom has 3 dimes. How much money is that?", [cents(30), cents(3), cents(13)])]
    S.set(4, "Level 2 Checkpoint",
        learnbox("<p class='big'><b>Level 2 Checkpoint!</b> 10 questions. Get <b>8 of 10</b> right to pass Level 2. "
                 "Take your time, count by 5s, and start with the biggest coin. You can do it!</p>")
        + '<div class="lab">Regrouping</div>' + vg(cp, 1, 2)
        + '<div class="lab">How much money? Circle it.</div><div class="grid3" style="gap:8px 12px">'
        + "".join(f'<div class="mcq box"><b>{n+3}.</b><br>{coins(l, 1.9)}{mc_opts(money_choices(t), f"d5{n}{t}")}</div>' for n, (l, t) in enumerate(sets)) + '</div>'
        + '<div class="lab">What time is it? (6–8)</div><div class="grid3" style="justify-items:center">' + "".join(clock5_pick(h, m, 110) for h, m in tm) + '</div>'
        + qs(wp, 9)
        + '<div class="huge center" style="margin-top:6px">Score: ______ / 10 &nbsp; <span class="big">(8 = pass!)</span></div>',
        f"1) {solve(cp[0])} 2) {solve(cp[1])} " + " ".join(f"{n+3}) {cents(t)}" for n, (l, t) in enumerate(sets))
        + " 6) 4:40 7) 9:15 8) 12:50 9) nickel 10) 30¢. Pass = 8 of 10.")
    return S

# ======================= ENGLISH =======================
def pic_pick(name, scale, choices, num):
    return f'<div class="mcq center"><b>{num}.</b> {icon(name, scale)}{mc_opts(choices, "pp" + name)}</div>'

def nariah_english():
    S = Subject(KID, "English", "Week 3 · Long Vowels & Describing Words")
    S.set(0, "Silent e: a_e & i_e",
        learnbox("<p class='big'><b>Silent e</b> is sneaky! It makes <b>no sound</b>, but it makes the vowel say its <b>name</b>. "
                 "<b>cap</b> + e = <b>cape</b>. &nbsp;<b>kit</b> + e = <b>kite</b>. &nbsp;<b>hid</b> + e = <b>hide</b>.</p>", yt("N2 magic e song a_e i_e"), "Magic e song")
        + '<div class="lab">Look at the picture. Circle the word.</div><div class="grid4" style="justify-items:center">'
        + pic_pick("kite", 1.05, ["kite", "kit", "cat"], 1) + pic_pick("cake", 1.05, ["cake", "cak", "cap"], 2)
        + pic_pick("bike", 1.05, ["bike", "bik", "bake"], 3) + pic_pick("hand", 1.05, ["five", "fiv", "fin"], 4) + '</div>'
        + '<div class="lab">Long a, long i, or short vowel? Circle it.</div>'
        + mark_list(["cape", "hid", "lake", "pin", "time", "cap", "made", "ride"], ["long a", "long i", "short"], 5, cols=2)
        + '<div class="lab">Trace.</div>' + trace_line("cake", 42, 2) + trace_line("kite", 42, 2)
        + '<div class="lab">Circle the word that makes sense.</div><div class="big" style="line-height:2.05">'
        + f'13. I can fly my {pick("kit", "kite")}.<br>14. Dad gave me a {pick("bit", "bite")} of his apple.<br>15. We swim in the {pick("lake", "lack")}.</div>'
        + '<div class="box big"><b>Read it:</b> Kate ate a big cake. Then she rode her bike to the lake to fly a kite.</div>',
        "1) kite 2) cake 3) bike 4) five. 5) long a 6) short 7) long a 8) short 9) long i 10) short 11) long a 12) long i. 13) kite 14) bite 15) lake.")
    S.set(1, "Silent e: o_e & u_e",
        learnbox("<p class='big'>Silent e works with <b>o</b> and <b>u</b> too! &nbsp;<b>hop</b> + e = <b>hope</b>. &nbsp;<b>not</b> + e = <b>note</b>. "
                 "&nbsp;<b>cub</b> + e = <b>cube</b>. &nbsp;<b>tub</b> + e = <b>tube</b>.</p>", yt("N2 magic e long o o_e"), "Long o song")
        + '<div class="lab">Look at the picture. Circle the word.</div><div class="grid4" style="justify-items:center">'
        + pic_pick("bone", 1.05, ["bone", "bon", "bun"], 1) + pic_pick("nose", 1.05, ["nose", "nos", "nut"], 2)
        + pic_pick("cube", 1.05, ["cube", "cub", "cob"], 3) + pic_pick("rose", 1.05, ["rose", "rod", "rug"], 4) + '</div>'
        + '<div class="lab">Circle the word that makes sense.</div>'
        + '<div class="big" style="line-height:2.05">'
        + f'5. I {pick("hop", "hope")} it is sunny today.<br>6. The dog dug up a {pick("bon", "bone")}.<br>'
        + f'7. Mom wrote me a {pick("not", "note")}.<br>8. The baby bear is a {pick("cub", "cube")}.<br>9. We went {pick("hom", "home")} after church.</div>'
        + '<div class="lab">Long o, long u, or short vowel?</div>'
        + mark_list(["rope", "mule", "dog", "tune", "cut", "home"], ["long o", "long u", "short"], 10, cols=2)
        + '<div class="lab">Trace.</div>' + trace_line("home", 42, 2),
        "1) bone 2) nose 3) cube 4) rose. 5) hope 6) bone 7) note 8) cub 9) home. 10) long o 11) long u 12) short 13) long u 14) short 15) long o.")
    S.set(2, "Describing Words",
        learnbox("<p class='big'>An <b>adjective</b> is a <b>describing word</b>. It tells about a noun: what color, what size, how it feels, how many. "
                 "<i>a <b>red</b> ball · a <b>big</b> dog · a <b>soft</b> kitten · <b>three</b> bugs</i></p>", yt("N2 adjectives song for kids"), "Adjective song")
        + '<div class="lab">Is it a describing word? Circle yes or no.</div>'
        + mark_list(["tall", "jump", "fuzzy", "cup", "green", "happy", "run", "cold"], ["yes", "no"], 1, cols=2)
        + '<div class="lab">Which word describes the noun? Circle it.</div>'
        + qs([("The <b>fluffy</b> dog ran home. Which word describes the dog?", ["fluffy", "dog", "ran"]),
              ("I have a <b>blue</b> kite. Which word tells the color?", ["blue", "kite", "have"]),
              ("The ice is very ______.", ["cold", "jump", "hand"]),
              ("An elephant is ______.", ["big", "tiny", "sing"])], 9)
        + '<div class="lab">Draw a <b>big</b>, <b>round</b>, <b>red</b> apple with a <b>small green</b> leaf.</div><div class="answer-space" style="min-height:150px"></div>',
        "Yes: tall, fuzzy, green, happy, cold. No: jump, cup, run. (1 yes 2 no 3 yes 4 no 5 yes 6 yes 7 no 8 yes) 9) fluffy 10) blue 11) cold 12) big. Drawing: big round red apple, small green leaf.")
    sents = [["The cat is on the mat.", "the cat is on the mat.", "The cat is on the mat"],
             ["We like to sing.", "we like to sing", "We like to sing"],
             ["My dog is big.", "my dog is big.", "My dog is big"],
             ["I can ride a bike.", "i can ride a bike.", "I can ride a bike"],
             ["Mom made a cake.", "mom made a cake", "Mom made a cake"],
             ["God loves me.", "god loves me.", "God loves me"]]
    S.set(3, "Telling Sentences",
        learnbox("<p class='big'>A sentence <b>starts with a capital letter</b> and <b>ends with a period</b>. "
                 "<span style='font-size:18pt'><b style='color:#7b3fc4'>T</b>he sun is hot<b style='color:#7b3fc4'>.</b></span> "
                 "The word <b>I</b> and names like <b>God</b> and <b>Mom</b> always get a capital too!</p>", yt("N2 sentence song uppercase period"), "Sentence song")
        + '<div class="lab">Circle the sentence that is written the right way.</div>'
        + "".join(f'<div class="mcq big" style="display:flex;align-items:center"><b>{n+1}.</b>{mc_opts(c, "sn" + c[0])}</div>' for n, c in enumerate(sents))
        + '<div class="lab">Does it start with a capital and end with a period? Circle yes or no.</div>'
        + mark_list(["The bird can fly.", "my sister is kind.", "We go to church", "I see a kite."], ["yes", "no"], 7, cols=2)
        + '<div class="lab">Trace the sentence. Then draw a picture of it!</div>' + trace_line("I like my home.", 40, 1)
        + '<div class="answer-space" style="min-height:150px"></div>',
        " ".join(f"{n+1}) {c[0]}" for n, c in enumerate(sents)) + " 7) yes 8) no (needs capital M) 9) no (needs a period) 10) yes.")
    S.set(4, "Review & Read",
        learnbox("<p class='big'>Read the story (or let your tablet read it to you). Then circle the answers. Goal: <b>7 of 8</b>!</p>")
        + '<div class="box" style="font-size:15pt;line-height:1.6">Jake has a small white mule named Rose. One fine day, Jake and Rose went to the lake. '
          'Jake had a long rope and a red kite. The wind came, and the kite rode up high! Rose ate green grass. '
          'At five, they went home. Jake gave Rose a big hug.</div>'
        + qs([("What is the mule's name?", ["Rose", "Jake", "Kate"]), ("Where did Jake and Rose go?", ["to the lake", "to the store", "to church"]),
              ("What color was the kite?", ["red", "white", "green"]), ("When did they go home?", ["at five", "at nine", "at night"]),
              ("Which word has a silent e?", ["kite", "red", "big"]), ("Which word is a describing word?", ["small", "mule", "went"]),
              ("Which sentence is written the right way?", ["Jake has a mule.", "jake has a mule.", "Jake has a mule"]),
              ("Which word has a long u?", ["mule", "hug", "rope"])])
        + '<div class="lab">Trace.</div>' + trace_line("Rose ate grass.", 40, 1),
        "1) Rose 2) to the lake 3) red 4) at five 5) kite 6) small 7) Jake has a mule. 8) mule. Pass = 7 of 8.")
    return S

# ======================= SCIENCE =======================
PLANT = ic('<path d="M4,70 L86,70"/><path d="M45,70 L45,26"/><circle cx="45" cy="16" r="5"/>'
           + "".join(f'<circle cx="{45+10*M.sin(k*M.pi/3):.1f}" cy="{16-10*M.cos(k*M.pi/3):.1f}" r="5.5"/>' for k in range(6))
           + '<path d="M45,52 C32,40 20,46 16,40 C26,34 40,38 45,52"/><path d="M45,44 C58,32 70,38 74,32 C64,26 50,30 45,44"/>'
           + '<path d="M45,70 L34,84 L28,88 M34,84 L36,92 M45,70 L45,96 M45,82 L40,90 M45,70 L58,84 L64,90 M58,84 L56,94"/>',
           230, 260, "0 0 90 100")

def nariah_science():
    S = Subject(KID, "Science", "Week 3 · How Plants Grow")
    def labeled_plant():
        T = lambda x, y, w: f'<text x="{x}" y="{y}" font-size="16" font-weight="700" fill="#4338ca">{w}</text>'
        L = lambda a, b, c, d: f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#9aa0bb" stroke-width="1.5" stroke-dasharray="4,3"/>'
        # plant drawn 230x260 at x offset 50: flower ~ (165,40), leaves ~ (225,100), stem ~ (165,150), roots ~ (165,230)
        return (f'<svg width="340" height="262"><g transform="translate(50,0)">{PLANT}</g>'
                + T(0, 46, "flower") + L(56, 41, 130, 41) + T(272, 96, "leaves") + L(268, 91, 236, 96)
                + T(0, 156, "stem") + L(40, 151, 160, 151) + T(0, 236, "roots") + L(46, 231, 140, 228) + '</svg>')
    S.set(0, "Parts of a Plant",
        learnbox("<p class='big'>A plant has 4 main parts. <b>Roots</b> grow under the soil — they hold the plant in place and drink up water. "
                 "The <b>stem</b> holds the plant up and carries water to the leaves. <b>Leaves</b> use sunlight to make food for the plant. "
                 "The <b>flower</b> makes <b>seeds</b> for new plants!</p>", yt("N2 parts of a plant song"), "Plant parts song")
        + f'<div class="flexrow" style="align-items:center"><div>{labeled_plant()}</div><div class="grow big"><b>Color the plant!</b><br>Roots brown, stem and leaves green, flower any color you like.</div></div>'
        + '<div class="lab">Which part does this job? Circle it.</div>'
        + mark_list(["Holds the plant in the soil", "Makes food from sunlight", "Holds the plant up tall", "Makes seeds"], ["roots", "stem", "leaves", "flower"], 1)
        + qs([("Which part is under the ground?", ["roots", "flower", "leaves"]), ("What do roots drink?", ["water", "milk", "juice"])], 5)
        + '<div class="lab">Trace.</div><div class="flexrow" style="gap:30px">' + trace_line("roots", 40, 1) + trace_line("stem", 40, 1) + '</div>',
        "1) roots 2) leaves 3) stem 4) flower 5) roots 6) water.")
    S.set(1, "What Plants Need",
        learnbox("<p class='big'>Plants are alive, so they need things to grow! A plant needs <b>sunlight</b>, <b>water</b>, <b>air</b>, "
                 "<b>soil</b> (dirt with food in it), and <b>space</b> to grow. No sun or no water? The plant will wilt and die.</p>", yt("N2 what plants need to grow"), "Plant needs")
        + '<div class="grid4" style="justify-items:center">' + icap("sun", 0.85, "sunlight") + icap("drop", 0.85, "water") + icap("air", 0.85, "air") + icap("soil", 0.85, "soil") + '</div>'
        + '<div class="lab">Does a plant need it? Circle yes or no.</div>'
        + mark_list(["sunlight", "candy", "water", "a blanket", "air", "soil", "a toy", "space"], ["yes", "no"], 1, cols=2)
        + qs([("A plant sat in a dark closet for 2 weeks. What will happen?", ["It will wilt and die.", "It will grow taller.", "It will grow flowers."]),
              ("Which part of the plant drinks water from the soil?", ["roots", "flower", "leaves"])], 9)
        + '<div class="box"><b>Try it with Mom! Bean in a bag.</b> Wet a paper towel, fold it around 2–3 dry beans, and put it in a zip bag. '
          'Tape the bag to a sunny window. Look every day! Draw your bean today:</div><div class="answer-space" style="min-height:110px"></div>',
        "Yes: sunlight, water, air, soil, space. No: candy, a blanket, a toy. (1 yes 2 no 3 yes 4 no 5 yes 6 yes 7 no 8 yes) 9) It will wilt and die. 10) roots.")
    order = ["flower", "seed", "youngplant", "sprout"]   # shown in this mixed-up order
    num = {"seed": 1, "sprout": 2, "youngplant": 3, "flower": 4}
    cap = {"seed": "seed", "sprout": "sprout", "youngplant": "plant", "flower": "flower"}
    S.set(2, "Seed to Flower",
        learnbox("<p class='big'>Plants have a <b>life cycle</b>, like the butterfly! A <b>seed</b> gets water and warmth. It cracks open and a tiny root and shoot "
                 "come out — a <b>sprout</b>! The sprout grows into a <b>plant</b> with a stem and leaves. Then it grows a <b>flower</b>, and the flower "
                 "makes new <b>seeds</b>. Then it starts all over!</p>", yt("N2 plant life cycle for kids"), "Plant life cycle")
        + '<div class="lab">Circle the right number (1–4) under each stage.</div>'
        + '<div class="grid4" style="justify-items:center">' + "".join(f'<div class="center">{icon(n, 1.25)}<div class="big"><b>{cap[n]}</b><br><span style="white-space:nowrap;font-size:12.5pt">{pick("1", "2", "3", "4")}</span></div></div>' for n in order) + '</div>'
        + qs([("What comes out of a seed first?", ["a sprout", "a flower", "an apple"]), ("What does the flower make?", ["new seeds", "soil", "rain"]),
              ("What does a seed need to start growing?", ["water and warmth", "a toy", "the dark only"]), ("How is a plant like a butterfly?", ["Both have a life cycle.", "Both can fly.", "Both eat milkweed."])], 5)
        + '<div class="lab">Bean check! Draw your bean today. Do you see a root yet?</div><div class="answer-space" style="min-height:140px"></div>',
        "flower 4, seed 1, plant 3, sprout 2. 5) a sprout 6) new seeds 7) water and warmth 8) Both have a life cycle.")
    foods = [("carrot", "root"), ("celery", "stem"), ("lettuce", "leaf"), ("broccoli", "flower"), ("apple", "fruit"), ("peas", "seed"), ("spinach", "leaf"), ("radish", "root")]
    S.set(3, "Plants We Eat",
        learnbox("<p class='big'>We eat lots of plant parts! A <b>carrot</b> is a <b>root</b>. <b>Celery</b> is a <b>stem</b>. <b>Lettuce</b> is a <b>leaf</b>. "
                 "<b>Broccoli</b> is a bunch of tiny <b>flowers</b>! An <b>apple</b> is a <b>fruit</b> — it holds the seeds. <b>Peas</b> are <b>seeds</b>.</p>", yt("N2 plant parts we eat"), "Plants we eat")
        + '<div class="flexrow" style="justify-content:center;gap:40px">' + icap("carrot", 1.0, "root") + icap("apple", 1.0, "fruit") + '</div>'
        + '<div class="lab">Which part of the plant do we eat? Circle it.</div>'
        + mark_list([f for f, _ in foods], ["root", "stem", "leaf", "flower", "fruit", "seed"], 1)
        + qs([("Which one grows under the ground?", ["carrot", "apple", "lettuce"])], 9)
        + '<div class="lab">Draw your favorite plant food. Circle what part it is: root · stem · leaf · flower · fruit · seed</div><div class="answer-space" style="min-height:130px"></div>',
        " ".join(f"{n+1}) {f}—{p}" for n, (f, p) in enumerate(foods)) + " 9) carrot.")
    S.set(4, "Plant Review",
        learnbox("<p class='big'>Show what you know about plants! Circle the answers. Goal: <b>7 of 8</b>.</p>", yt("N2 how plants grow review"), "How plants grow")
        + qs([("Which part holds the plant in the soil?", ["roots", "flower", "stem"]), ("Which part makes food from sunlight?", ["leaves", "roots", "seeds"]),
              ("Which part makes seeds?", ["flower", "stem", "roots"]), ("Which does a plant NOT need?", ["candy", "water", "sunlight"]),
              ("What comes after the seed?", ["sprout", "flower", "fruit"]), ("Celery is which part?", ["stem", "root", "seed"]),
              ("A carrot is which part?", ["root", "leaf", "flower"]), ("What does the stem do?", ["holds the plant up and carries water", "makes seeds", "eats bugs"])])
        + '<div class="lab">Bean check! Draw your bean now. How has it changed since Wednesday?</div><div class="answer-space" style="min-height:150px"></div>',
        "1) roots 2) leaves 3) flower 4) candy 5) sprout 6) stem 7) root 8) holds the plant up and carries water. Pass = 7 of 8.")
    return S

# ======================= SOCIAL STUDIES =======================
def nariah_ss():
    S = Subject(KID, "Social Studies", "Week 3 · American Symbols")
    S.set(0, "The American Flag",
        learnbox("<p class='big'>A <b>symbol</b> is a picture or thing that stands for something. The <b>American flag</b> stands for our country! "
                 "It has <b>50 stars</b> — one for each of the <b>50 states</b> (Florida is one!). It has <b>13 stripes</b>, 7 red and 6 white, "
                 "for the <b>13 colonies</b> that became the first 13 states. People call it the <b>Stars and Stripes</b>.</p>", yt("N2 American flag for kids"), "The flag")
        + '<div class="center">' + I["flag"].replace('width="180" height="100"', 'width="320" height="178"') + '</div>'
        + '<div class="lab">Color the flag! Top stripe red, then white, red, white … The box behind the stars is blue.</div>'
        + qs([("How many stars are on the flag?", ["50", "13", "100"]), ("Why are there 50 stars?", ["one for each state", "one for each president", "one for each city"]),
              ("How many stripes are there?", ["13", "50", "7"]), ("The stripes stand for the first 13 ______.", ["colonies", "flags", "cars"]),
              ("What do people call the flag?", ["the Stars and Stripes", "the Big Dipper", "the Red Rose"])])
        + '<div class="box big"><b>Fun fact:</b> Hawaii was the 50th state. Its star was added to the flag in 1960, so our flag has looked like this for over 60 years!</div>'
        + '<div class="lab">Trace.</div>' + trace_line("USA", 40, 3),
        "1) 50 2) one for each state 3) 13 4) colonies 5) the Stars and Stripes. Coloring: 7 red stripes (top and bottom are red), 6 white, blue box with white stars.")
    S.set(1, "Veterans Day",
        learnbox("<p class='big'><b>Today is Veterans Day!</b> A <b>veteran</b> is someone who served our country in the military — the Army, Navy, Air Force, "
                 "Marines, Coast Guard, or Space Force. Long ago, a big war called <b>World War I</b> stopped on the <b>11th hour</b> of the <b>11th day</b> of the "
                 "<b>11th month</b> in <b>1918</b>. That is why Veterans Day is on <b>November 11</b>. Today we say <b>thank you</b> to veterans!</p>", yt("N2 Veterans Day for kids"), "Veterans Day")
        + f'<div class="center">{icon("medal", 1.3)}</div>'
        + qs([("What is a veteran?", ["someone who served in the military", "a doctor for pets", "a teacher"]), ("What date is Veterans Day?", ["November 11", "July 4", "December 25"]),
              ("Why November 11?", ["World War I stopped that day in 1918.", "It is the flag's birthday.", "It is the first day of winter."]),
              ("What can we say to a veteran?", ["Thank you for serving!", "Go away!", "Happy birthday!"])])
        + '<div class="lab">Trace.</div>' + trace_line("Thank you", 42, 1)
        + '<div class="lab">Make a thank-you card for a veteran! Draw a picture. Mom can help you write the words.</div><div class="answer-space" style="min-height:140px"></div>',
        "1) someone who served in the military 2) November 11 3) World War I stopped that day in 1918 (11th hour, 11th day, 11th month) 4) Thank you for serving! Card varies.")
    S.set(2, "The Bald Eagle",
        learnbox("<p class='big'>The <b>bald eagle</b> is our <b>national bird</b>. It was picked as a symbol of America way back in <b>1782</b> because it is "
                 "<b>strong</b> and <b>free</b>. It is not really bald! It has <b>white feathers</b> on its head and a brown body. Eagles catch <b>fish</b> with their "
                 "sharp claws and build <b>giant nests</b> in tall trees. Lots of bald eagles live in <b>Florida</b>!</p>", yt("N2 bald eagle national bird kids"), "Bald eagle")
        + f'<div class="flexrow" style="justify-content:center;align-items:center;gap:20px">{icon("eagle", 1.8)}<div class="big">Color the head <b>white</b><br>(leave it!), the beak<br>orange, and the body brown.</div></div>'
        + qs([("What is our national bird?", ["the bald eagle", "the robin", "the turkey"]), ("Is the bald eagle really bald?", ["No — it has white head feathers.", "Yes, it has no feathers.", "Yes, it lost its feathers."]),
              ("What does a bald eagle like to eat?", ["fish", "pizza", "grass"]), ("Why was it chosen as a symbol?", ["It is strong and free.", "It is small and quiet.", "It can talk."])])
        + '<div class="box big">Isaiah 40:31 — “they who wait for the LORD shall renew their strength; they shall mount up with wings like eagles.”</div>'
        + '<div class="lab">Trace.</div>' + trace_line("eagle", 44, 3),
        "1) the bald eagle 2) No — it has white head feathers 3) fish 4) It is strong and free.")
    S.set(3, "Statue of Liberty & Liberty Bell",
        learnbox("<p class='big'><b>Liberty</b> means <b>freedom</b>. The <b>Statue of Liberty</b> is a giant lady holding a <b>torch</b> in New York. She was a gift from "
                 "<b>France</b> in <b>1886</b>. She is green because she is made of copper. The <b>Liberty Bell</b> is in <b>Philadelphia</b>. It has a big "
                 "<b>crack</b> and a Bible verse on it (Leviticus 25:10) about proclaiming liberty throughout the land.</p>", yt("N2 Statue of Liberty FreeSchool"), "Lady Liberty")
        + '<div class="flexrow" style="justify-content:center;gap:60px">' + icap("torch", 1.2, "Statue of Liberty's torch") + icap("bell", 1.2, "Liberty Bell") + '</div>'
        + '<div class="lab">Statue of Liberty or Liberty Bell? Circle it.</div>'
        + mark_list(["holds a torch", "has a big crack", "a gift from France", "is in Philadelphia", "is in New York", "has a Bible verse on it"], ["Statue", "Bell"], 1)
        + qs([("What does liberty mean?", ["freedom", "money", "a bell"]), ("Why is the Statue of Liberty green?", ["She is made of copper.", "She was painted green.", "She is covered in leaves."])], 7)
        + '<div class="lab">Trace.</div>' + trace_line("liberty", 44, 2),
        "1) Statue 2) Bell 3) Statue 4) Bell 5) Statue 6) Bell. 7) freedom 8) She is made of copper.")
    L = ["flag", "50 stars", "bald eagle", "Liberty Bell", "Statue of Liberty"]
    R = ["has a big crack", "our national bird", "Stars and Stripes", "holds a torch", "one for each state"]
    S.set(4, "American Symbols Review",
        learnbox("<p class='big'>Show what you know about American symbols! 11 questions. Goal: <b>9 of 11</b>.</p>", yt("N2 American symbols review"), "US symbols")
        + '<div class="lab">Draw a line from each symbol to what it means.</div>'
        + '<svg width="620" height="250" style="align-self:center;flex-shrink:0">'
          + "".join(f'<text x="10" y="{40+k*50}" font-size="19" font-weight="700" fill="#1f2a5c">{k+1}. {w}</text><circle cx="215" cy="{34+k*50}" r="6" fill="#8a3ab9"/>' for k, w in enumerate(L))
          + "".join(f'<circle cx="300" cy="{34+k*50}" r="6" fill="#8a3ab9"/><text x="320" y="{40+k*50}" font-size="18" fill="#1f2a5c">{w}</text>' for k, w in enumerate(R))
          + '</svg>'
        + qs([("How many stripes are on the flag?", ["13", "50", "11"]), ("When is Veterans Day?", ["November 11", "July 4", "November 26"]),
              ("Which bird is our national bird?", ["bald eagle", "pelican", "owl"]), ("Where is the Liberty Bell?", ["Philadelphia", "Florida", "France"]),
              ("Who gave us the Statue of Liberty?", ["France", "England", "Mexico"]), ("What does liberty mean?", ["freedom", "a torch", "a song"])], 6)
        + '<div class="lab">Draw your favorite American symbol!</div><div class="answer-space" style="min-height:80px"></div>',
        "1) flag–Stars and Stripes; 2) 50 stars–one for each state; 3) bald eagle–our national bird; 4) Liberty Bell–has a big crack; 5) Statue of Liberty–holds a torch. "
        "6) 13 7) November 11 8) bald eagle 9) Philadelphia 10) France 11) freedom. Pass 9 of 11.")
    return S
