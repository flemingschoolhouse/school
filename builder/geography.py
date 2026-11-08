from lib import *
from core_common import mc, qs, mark_list, MC_HINT
from worldmap import world_map, proj

WK = 3
JAX = (-81.66, 30.33)
VID = {
 0: yt("GEO landforms for kids"), 1: yt("GEO bodies of water for kids"),
 2: yt("GEO island peninsula isthmus"), 3: yt("GEO world rivers for kids"),
 4: yt("GEO land and water song"),
}
TITLES = ["Landforms", "Bodies of Water", "Islands, Peninsulas & Isthmuses", "Great Rivers & Mountains", "Florida's Land & Water + Review"]
TIER = {"Titus": "A", "Nariah": "A", "Naomi": "B", "Nevaeh": "C", "Nylah": "C"}

WATER = "#cfe0ff"   # light blue (blue is the largest channel)
LAND = "#ffffff"
ST = 'stroke="#1f2a5c" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"'

def _svg(inner, w):
    return f'<svg width="{w}" height="{w*0.66:.0f}" viewBox="0 0 120 80">{inner}</svg>'

def landform(name, w=120):
    pics = {
     "mountain": f'<polygon points="10,74 60,8 110,74" fill="{LAND}" {ST}/><polyline points="44,30 52,34 60,28 68,34 76,30" fill="none" {ST}/>',
     "hill": f'<path d="M4,74 C30,36 90,36 116,74 Z" fill="{LAND}" {ST}/>',
     "plain": f'<line x1="4" y1="60" x2="116" y2="60" {ST}/>' + "".join(f'<path d="M{10+k*14},60 l3,-8 M{14+k*14},60 l-2,-7" fill="none" {ST} stroke-width="1.6"/>' for k in range(8)),
     "valley": f'<polygon points="2,74 30,10 60,62 90,10 118,74" fill="{LAND}" {ST}/><path d="M48,74 C56,66 64,66 72,74" fill="{WATER}" {ST} stroke-width="1.6"/>',
     "plateau": f'<polygon points="8,74 26,24 94,24 112,74" fill="{LAND}" {ST}/>',
     "river": f'<path d="M0,20 C30,10 40,50 70,40 C95,32 100,62 120,58 L120,74 C96,78 92,48 70,56 C40,66 30,26 0,36 Z" fill="{WATER}" {ST}/>',
     "lake": f'<ellipse cx="60" cy="42" rx="44" ry="24" fill="{WATER}" {ST}/>',
     "ocean": f'<rect x="4" y="18" width="112" height="56" fill="{WATER}" {ST}/>' + "".join(f'<path d="M{12+k*26},{40+(k%2)*14} q6,-6 12,0 q6,6 12,0" fill="none" {ST} stroke-width="1.6"/>' for k in range(4)),
     "bay": f'<rect x="4" y="4" width="112" height="72" fill="{WATER}" {ST}/><path d="M4,4 L116,4 L116,60 C96,60 92,28 60,28 C28,28 24,60 4,60 Z" fill="{LAND}" {ST}/>',
     "island": f'<rect x="4" y="4" width="112" height="72" fill="{WATER}" {ST}/><path d="M40,40 C40,22 82,20 84,38 C86,56 46,60 40,40 Z" fill="{LAND}" {ST}/>',
     "peninsula": f'<rect x="4" y="4" width="112" height="72" fill="{WATER}" {ST}/><path d="M4,4 L116,4 L116,22 L70,22 C76,40 72,70 56,70 C42,70 44,40 50,22 L4,22 Z" fill="{LAND}" {ST}/>',
     "isthmus": f'<rect x="4" y="4" width="112" height="72" fill="{WATER}" {ST}/><path d="M8,14 L46,14 C50,34 70,34 74,14 L112,14 L112,66 L74,66 C70,46 50,46 46,66 L8,66 Z" fill="{LAND}" {ST}/>',
    }
    return _svg(pics[name], w)

def card(name, label=True, w=120, num=None):
    lab = f'<div class="big" style="font-weight:600">{name}</div>' if label else (f'<div class="big"><b>{num}.</b> <span class="blank-ln" style="min-width:100px"></span></div>' if num else "")
    return f'<div class="box center" style="padding:4px">{landform(name, w)}{lab}</div>'

def wordbank(words):
    return '<div>' + "".join(f'<span class="pill">{esc(w)}</span>' for w in words) + '</div>'

def head(text, v):
    return f'<div class="flexrow"><div class="learn grow">{text}</div>{v}</div>'

# rough Florida outline (lon, lat)
FL = [(-87.6, 31.0), (-85.0, 31.0), (-84.9, 30.7), (-82.2, 30.57), (-82.0, 30.8), (-81.45, 30.71), (-81.3, 29.9), (-80.6, 28.6),
      (-80.5, 28.2), (-80.05, 26.7), (-80.1, 25.8), (-80.4, 25.2), (-81.1, 25.1), (-81.8, 26.1), (-82.2, 26.7), (-82.8, 27.9),
      (-82.7, 28.7), (-83.7, 29.9), (-84.3, 30.0), (-85.4, 29.7), (-86.5, 30.4), (-87.4, 30.3)]
def florida_map(W=300, H=300, labels=False, star=True):
    x0, x1, y0, y1 = -88.0, -79.5, 31.4, 24.6
    P = lambda lo, la: ((lo - x0) / (x1 - x0) * W, (la - y0) / (y1 - y0) * H)
    pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in (P(*p) for p in FL))
    # St. Johns River (rough): rises in the marshes of east-central Florida and flows NORTH, then east to the Atlantic at Jacksonville
    sj = [(-80.75, 27.75), (-80.85, 28.3), (-81.05, 28.8), (-81.35, 29.1), (-81.6, 29.6), (-81.65, 30.0), (-81.65, 30.3), (-81.5, 30.4), (-81.4, 30.4)]
    sjp = " ".join(f"{a:.1f},{b:.1f}" for a, b in (P(*p) for p in sj))
    ox, oy = P(-80.83, 26.95)
    o = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="background:{WATER};border:1.5px solid #9aa6cc;border-radius:6px">',
         f'<polygon points="{pts}" fill="#fff" {ST}/>',
         f'<polyline points="{sjp}" fill="none" stroke="#2f5bd3" stroke-width="3"/>',
         f'<ellipse cx="{ox:.0f}" cy="{oy:.0f}" rx="{W*0.03:.0f}" ry="{W*0.035:.0f}" fill="{WATER}" stroke="#2f5bd3" stroke-width="2"/>']
    if star:
        sx, sy = P(*JAX); o.append(f'<text x="{sx:.0f}" y="{sy+6:.0f}" text-anchor="middle" font-size="20" fill="#a21caf">★</text>')
    if labels:
        for t, x, y in [("A", W - 22, P(0, 29.0)[1]), ("B", P(-85.2, 0)[0], P(0, 27.0)[1]), ("C", ox + 22, oy + 4), ("D", P(-82.15, 0)[0], P(0, 29.35)[1])]:
            o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" fill="#fff" stroke="#6d28d9" stroke-width="1.6"/>'
                     f'<text x="{x:.0f}" y="{y+4.5:.0f}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#6d28d9">{t}</text>')
    o.append('</svg>')
    return "".join(o)

WORLD_MARKS = [("4", "Nile River", 31, 22), ("2", "Amazon River", -60, -3), ("6", "Mississippi River", -90, 35),
               ("1", "Himalayas (Mount Everest)", 86.9, 28), ("5", "Andes Mountains", -70, -22), ("3", "Rocky Mountains", -110, 45)]
def world_marks(W, H):
    s = ""
    for t, n, lo, la in WORLD_MARKS:
        x, y = proj(lo, la, W, H)
        if "River" in n:
            s += f'<path d="M{x-10},{y} q5,-6 10,0 q5,6 10,0" fill="none" stroke="#2f5bd3" stroke-width="2.5"/>'
        else:
            s += f'<polygon points="{x-9},{y+7} {x},{y-9} {x+9},{y+7}" fill="#fff" stroke="#1f2a5c" stroke-width="2"/>'
        s += (f'<circle cx="{x+16}" cy="{y-10}" r="10" fill="#fff" stroke="#6d28d9" stroke-width="1.6"/>'
              f'<text x="{x+16}" y="{y-5.5}" text-anchor="middle" font-size="12" font-weight="700" fill="#6d28d9">{t}</text>')
    return s

def geo_page(name, i):
    T = TIER[name]; v = qr_box(VID[i], "Watch first", 64)
    if i == 0:
        five = ["mountain", "hill", "plain", "valley", "plateau"]
        if T == "A":
            body = (head('<p class="big">A <b>landform</b> is a shape of the land. God made mountains tall, hills small, and plains flat!</p>', v)
                    + '<div class="grid5">' + "".join(card(n, True, 108) for n in five) + '</div>'
                    + '<div class="lab">Mom reads. Circle (or tap) the answer.</div>'
                    + mc("Which landform is the tallest?", ["mountain", "hill", "plain"], 1)
                    + mc("Which landform is flat?", ["plain", "mountain", "valley"], 2)
                    + mc("Which is low land between two mountains?", ["valley", "plateau"], 3)
                    + '<div class="lab">Put a dot-marker dot on the top of every mountain and hill. Then trace:</div>' + trace_line("hill", 52, 4))
        else:
            body = (head('<p>A <b>landform</b> is a natural shape on Earth\'s surface. <b>Mountains</b> rise high with steep sides and a peak. <b>Hills</b> are lower and rounded. '
                         '<b>Plains</b> are wide, flat land — great for farming. A <b>valley</b> is low land between hills or mountains, often with a river. '
                         'A <b>plateau</b> is high land with a flat top and steep sides.</p>', v)
                    + '<div class="grid5">' + "".join(card(n, False, 112, k + 1) for k, n in enumerate(["valley", "plateau", "mountain", "plain", "hill"])) + '</div>'
                    + '<div class="lab">Label each picture.</div>' + wordbank(sorted(five))
                    + qs([("Which landform has a flat top and steep sides?", ["plateau", "valley", "hill"]),
                          ("Where would a river most likely run?", ["through a valley", "on a mountain peak", "on top of a plateau"]),
                          ("Why do many farms sit on plains?", ["The land is flat with good soil.", "Plains are the coldest places.", "Plains are always near volcanoes."])], 6))
            if T == "B":
                body += qs([("Is Florida mostly plains or mountains? How can you tell when we drive around?", 2)], 9)
            else:
                body += ('<table class="t"><tr><th>U.S. example</th><th>Which landform?</th></tr>'
                         + "".join(f"<tr><td>{x}</td><td></td></tr>" for x in ["The Rocky Mountains", "The Great Plains", "The Colorado Plateau", "Death Valley"]) + '</table>'
                         + qs([("How can a river make a valley over a long time? Explain.", 2)], 9))
    elif i == 1:
        if T == "A":
            body = (head('<p class="big">Water comes in different shapes too! A <b>river</b> flows like a long road of water. A <b>lake</b> has land all around it. '
                         'The <b>ocean</b> is huge and salty.</p>', v)
                    + '<div class="grid3">' + "".join(card(n, True, 170) for n in ["river", "lake", "ocean"]) + '</div>'
                    + '<div class="lab">Color all the water BLUE.</div>'
                    + mc("Which water is salty?", ["the ocean", "a river", "a lake"], 1)
                    + mc("Which water has land all around it?", ["a lake", "the ocean"], 2)
                    + mc("We live by the St. Johns. Is it a river or a mountain?", ["a river", "a mountain"], 3)
                    + '<div class="lab">Trace:</div>' + trace_line("lake", 52, 4))
        else:
            body = (head('<p>A <b>body of water</b> is any large area of water. <b>Oceans</b> are the largest and are salt water. A <b>river</b> is fresh water flowing in a channel '
                         'from a <b>source</b> to its <b>mouth</b>, where it empties into a bigger body of water. A <b>lake</b> is water surrounded by land (most are fresh). '
                         'A <b>bay</b> is part of an ocean or lake that curves into the land; a <b>gulf</b> is like a bay, but usually larger.</p>', v)
                    + '<div class="grid4">' + "".join(card(n, False, 120, k + 1) for k, n in enumerate(["lake", "bay", "river", "ocean"])) + '</div>'
                    + '<div class="lab">Label each picture.</div>' + wordbank(["bay", "lake", "ocean", "river"])
                    + '<div class="lab">Fresh water (F) or salt water (S)?</div>'
                    + mark_list(["Atlantic Ocean", "Lake Okeechobee", "Pacific Ocean", "Mississippi River", "Tampa Bay", "Lake Michigan"], ["F", "S"], 5, cols=2)
                    + qs([("Where a river empties into the ocean is called its…", ["mouth", "source", "peak"])], 11))
            if T == "C":
                body += qs([("The Great Salt Lake in Utah is salty even though it's a lake. Rivers flow in, but no river flows out. Explain why that could make it salty.", 2)], 12)
            else:
                body += qs([("Which body of water would you most like to visit? Why?", 2)], 12)
    elif i == 2:
        if T == "A":
            body = (head('<p class="big">An <b>island</b> has water all the way around. A <b>peninsula</b> has water on 3 sides. '
                         '<b>Florida is a peninsula!</b> Look — water on 3 sides!</p>', v)
                    + '<div class="grid2">' + card("island", True, 190) + card("peninsula", True, 190) + '</div>'
                    + f'<div class="flexrow" style="align-items:center;justify-content:center;gap:20px">{florida_map(250, 250)}'
                    '<div class="big" style="max-width:300px">Color Florida. Color the water around it blue. Find the ★ — that\'s Jacksonville!</div></div>'
                    + mc("Florida has water on 3 sides. It is a…", ["peninsula", "island", "mountain"], 1)
                    + mc("Water all the way around is an…", ["island", "plain"], 2))
        else:
            body = (head('<p>An <b>island</b> is land surrounded by water on all sides; a group of islands is an <b>archipelago</b> (like Hawaii). '
                         'A <b>peninsula</b> is land surrounded by water on three sides — Florida is one of the most famous peninsulas in the world! '
                         'An <b>isthmus</b> is a narrow strip of land that connects two larger land areas, with water on both sides (the Isthmus of Panama joins North and South America).</p>', v)
                    + '<div class="grid4">' + "".join(card(n, False, 118, k + 1) for k, n in enumerate(["peninsula", "isthmus", "island", "bay"])) + '</div>'
                    + '<div class="lab">Label each picture.</div>' + wordbank(["bay", "island", "isthmus", "peninsula"])
                    + qs([("Hawaii is a chain of islands. What is that called?", ["an archipelago", "an isthmus", "a plateau"]),
                          ("Which country is a boot-shaped peninsula in Europe?", ["Italy", "Japan", "Egypt"]),
                          ("Which connects North and South America?", ["the Isthmus of Panama", "the Nile River", "the Andes"]),
                          ("Florida touches water on three sides. Name two of those bodies of water.", 1)], 5))
            if T == "C":
                body += qs([("Being a peninsula affects life in Florida. Give two ways (think beaches, weather, ships, fishing).", 3)], 9)
            else:
                body += '<div class="lab">Bonus: draw your own island and give it a name.</div><div class="answer-space" style="min-height:80px"></div>'
    elif i == 3:
        if T == "A":
            body = (head('<p class="big">The tallest mountain in the world is <b>Mount Everest</b>. The longest river is the <b>Nile</b> in Africa. '
                         'Rivers are wavy lines ∿ and mountains are triangles ▲ on this map.</p>', v)
                    + world_map(660, 315, extra=world_marks(660, 315))
                    + '<div class="lab">Put a dot-marker dot on every ▲ mountain. Trace every ∿ river with a blue crayon.</div>'
                    + mc("What is the tallest mountain in the world?", ["Mount Everest", "a little hill", "our backyard"], 1)
                    + '<div class="big">Draw a tall mountain with a river running down it:</div><div class="answer-space"></div>')
        else:
            body = (head('<p><b>Mount Everest</b> in the Himalayas (Asia) is the highest mountain above sea level — about 29,032 feet (8,849 m). '
                         'The <b>Nile</b> (Africa, about 4,130 miles) is usually called the longest river, and the <b>Amazon</b> (South America) carries the most water. '
                         'The <b>Andes</b> are the longest mountain range on land. In North America, the <b>Mississippi River</b> flows south to the Gulf, and the '
                         '<b>Rocky Mountains</b> run through the West.</p>', v)
                    + world_map(700, 330, extra=world_marks(700, 330))
                    + '<div class="lab">Match each place to its number on the map. (▲ = mountains, ∿ = river)</div>'
                    + mark_list(["Nile River", "Amazon River", "Mississippi River", "Himalayas", "Andes Mountains", "Rocky Mountains"], ["1", "2", "3", "4", "5", "6"], 1, cols=1))
            if T == "C":
                body += qs([("Which continent are the Himalayas on?", ["Asia", "Africa", "Europe"]),
                            ("Why do you think so many big cities are built on rivers? Give two reasons.", 2)], 7)
            else:
                body += qs([("Which river carries the most water?", ["the Amazon", "the Nile", "the St. Johns"])], 7)
    else:
        if T == "A":
            body = (head('<p class="big">Florida has lots of water: the <b>Atlantic Ocean</b>, the <b>St. Johns River</b> (it runs right through Jacksonville!), and a big lake — '
                         '<b>Lake Okeechobee</b>. Florida is very flat — no mountains!</p>', v)
                    + f'<div class="flexrow" style="align-items:center;justify-content:center;gap:16px">{florida_map(240, 240)}'
                    '<div class="big" style="max-width:320px">Trace the blue St. Johns River with your finger — it ends near the ★! Dot the big lake.</div></div>'
                    + '<div class="lab">Review! Mom reads. Circle (or tap) the answer.</div>'
                    + '<div class="grid4">' + "".join(card(n, True, 110) for n in ["mountain", "island", "river", "plain"]) + '</div>'
                    + mc("Which one has water all around the land?", ["island", "mountain", "plain"], 1)
                    + mc("Which is the tallest?", ["mountain", "plain", "river"], 2)
                    + '<div class="big">Show Mom on the globe: a mountain · a river · an island · Florida <span class="star">☆☆☆☆</span></div>')
        else:
            body = (head('<p><b>Florida\'s land & water:</b> Florida is a low, flat peninsula — its highest point, Britton Hill, is only 345 feet high, the lowest high point '
                         'of any state. The <b>St. Johns River</b> (about 310 miles) is Florida\'s longest river and flows <b>north</b>, '
                         'emptying into the Atlantic near Jacksonville. <b>Lake Okeechobee</b> is Florida\'s largest lake.</p>', v)
                    + f'<div class="flexrow" style="gap:14px">{florida_map(220, 220, labels=True)}<div class="grow"><div class="lab">Match each letter on the map.</div>'
                    + mark_list(["St. Johns River", "Lake Okeechobee", "Atlantic Ocean", "the Gulf"], ["A", "B", "C", "D"], 1)
                    + '</div></div>'
                    + '<div class="lab">Week review — 8 of 10 to pass (the 4 map letters count too).</div>'
                    + qs([("High land with a flat top and steep sides:", ["plateau", "valley", "plain"]),
                          ("Land with water on three sides:", ["peninsula", "island", "isthmus"]),
                          ("Where a river begins:", ["its source", "its mouth", "its bay"]),
                          ("Which way does the St. Johns River flow?", ["north", "south", "west"])], 5))
            if T == "C":
                body += qs([("Name the tallest mountain on Earth and the continent it's on.", 1),
                            ("Explain the difference between a bay and a peninsula.", 2)], 9)
            else:
                body += qs([("Name the largest lake in Florida.", 1), ("What is a valley?", 1)], 9)
    return page(name, i, "Geography", f"Week {WK} · {TITLES[i]}", body)

KEY = ("<b>Day 1 Landforms:</b> Tier A: mountain · plain · valley. Tier B/C pictures: 1 valley, 2 plateau, 3 mountain, 4 plain, 5 hill; 6 plateau; 7 through a valley; 8 flat land with good soil; "
       "9 (B) mostly plains — it's flat everywhere we drive; (C) table: Rockies = mountains, Great Plains = plain, Colorado Plateau = plateau, Death Valley = valley; 9 (C) flowing water wears away (erodes) rock and soil and carries it off, cutting the land lower.<br>"
       "<b>Day 2 Water:</b> Tier A: the ocean · a lake · a river. B/C pictures: 1 lake, 2 bay, 3 river, 4 ocean. Fresh/salt: 5 Atlantic S, 6 Okeechobee F, 7 Pacific S, "
       "8 Mississippi F, 9 Tampa Bay S, 10 Lake Michigan F. 11 mouth. 12 (C) water evaporates and leaves the salt behind; with no outlet the salt builds up.<br>"
       "<b>Day 3 Islands etc.:</b> Tier A: peninsula · island. B/C: 1 peninsula, 2 isthmus, 3 island, 4 bay; 5 an archipelago, 6 Italy, 7 the Isthmus of Panama, 8 the Atlantic Ocean and the Gulf (also the Straits of Florida). "
       "9 (C) e.g. long coastline & beaches, hurricanes can come from both sides, ports & shipping, fishing, ocean-warmed weather.<br>"
       "<b>Day 4 Rivers & Mountains:</b> Tier A: Mount Everest. B/C: 1 Nile = 4, 2 Amazon = 2, 3 Mississippi = 6, 4 Himalayas = 1, 5 Andes = 5, 6 Rockies = 3. B 7: the Amazon. C 7: Asia; 8: water for drinking & farming, boats for travel and trade, food.<br>"
       "<b>Day 5 Florida & review:</b> Tier A: island · mountain. B/C map: 1 St. Johns River = D, 2 Lake Okeechobee = C, 3 Atlantic = A, 4 the Gulf = B. 5 plateau, 6 peninsula, 7 its source, 8 north; "
       "C 9 Mount Everest, Asia; 10 a bay is water curving into the land; a peninsula is land reaching out into the water. B 9 Lake Okeechobee; 10 low land between hills or mountains.")
