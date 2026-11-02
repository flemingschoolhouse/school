from lib import *
from worldmap import world_map, CONT_LABEL, OCEAN_LABEL

CONTS = list(CONT_LABEL)   # 7
OCEANS = list(OCEAN_LABEL) # 5
JAX = (-81.66, 30.33)
NUM = {k: str(i + 1) for i, k in enumerate(CONTS)}
LET = {k: chr(65 + i) for i, k in enumerate(OCEANS)}
VID = {
 0: yt("seven continents song for kids"), 1: yt("five oceans song for kids"),
 2: yt("hemispheres equator prime meridian for kids"), 3: yt("latitude and longitude for kids"),
 4: yt("Florida geography for kids"),
}
TITLES = ["The 7 Continents", "The 5 Oceans", "Hemispheres", "Latitude & Longitude", "Where in the World Is Jacksonville?"]
TIER = {"Titus": "A", "Nariah": "A", "Naomi": "B", "Nevaeh": "C", "Nylah": "C"}

def wordbank(words):
    return '<div>' + "".join(f'<span class="pill">{esc(w)}</span>' for w in words) + '</div>'

def label_lines(keys, cols=2):
    cells = "".join(f'<div><b>{k}.</b> <span class="blank-ln" style="min-width:210px"></span></div>' for k in keys)
    return f'<div class="grid{cols}">{cells}</div>'

def geo_page(name, i):
    T = TIER[name]; v = qr_box(VID[i], "Watch first", 64)
    if i == 0:
        if T == "A":
            body = (f'<div class="flexrow"><div class="learn grow"><p class="big">A <b>continent</b> is a HUGE piece of land. The world has <b>7</b> of them! '
                    'We live on <b>North America</b>.</p></div>' + v + '</div>' + world_map(660, 315, cont_marks=NUM)
                    + '<div class="lab">Mom points and says each name. Put a dot-marker dot (or sticker) on each continent as you count!</div>'
                    + '<div class="big">How many continents? Trace it:</div>' + trace_line("7", 60, 3)
                    + '<div class="lab">Color the continent where WE live (#1).</div>')
        else:
            body = (f'<div class="flexrow"><div class="learn grow"><p>A <b>continent</b> is one of Earth\'s 7 great land masses: North America, South America, Europe, Asia, '
                    'Africa, Australia, and Antarctica. Europe and Asia actually share one big land mass — the dashed line shows the usual border.</p></div>' + v + '</div>'
                    + world_map(700, 330, cont_marks=NUM) + '<div class="lab">Label each numbered continent.</div>' + wordbank(sorted(CONTS))
                    + label_lines(range(1, 8)))
            if T == "B":
                body += ('<div class="grid2"><div>Which continent do we live on?<div class="ln"></div></div>'
                         '<div>Which continent is covered in ice?<div class="ln"></div></div></div>')
            else:
                body += ('<table class="t"><tr><th>Fast fact</th><th>Continent</th></tr>'
                         '<tr><td>Largest continent and most people</td><td></td></tr><tr><td>Smallest continent (also a country)</td><td></td></tr>'
                         '<tr><td>Coldest, with no permanent towns</td><td></td></tr><tr><td>Has the Sahara Desert and the Nile River</td><td></td></tr>'
                         '<tr><td>Has the Amazon rainforest</td><td></td></tr></table>')
    elif i == 1:
        if T == "A":
            body = (f'<div class="flexrow"><div class="learn grow"><p class="big">An <b>ocean</b> is a giant body of salty water. The world has <b>5</b> oceans. '
                    'The ocean by our house is the <b>Atlantic</b>!</p></div>' + v + '</div>' + world_map(660, 315, ocean_marks=LET)
                    + '<div class="lab">Color all the water BLUE. Mom says each ocean name as you point to the letters.</div>'
                    + '<div class="big">Trace:</div>' + trace_line("ocean", 52, 2))
        else:
            body = (f'<div class="flexrow"><div class="learn grow"><p>Oceans cover about <b>71%</b> of Earth. The 5 oceans are the Pacific, Atlantic, Indian, Arctic, '
                    'and Southern. They are all connected — one world ocean with 5 names.</p></div>' + v + '</div>'
                    + world_map(700, 330, ocean_marks=LET, cont_marks=NUM) + '<div class="lab">Label each lettered ocean.</div>'
                    + wordbank(sorted(OCEANS)) + label_lines("ABCDE"))
            if T == "B":
                body += '<div>Which ocean touches Jacksonville, Florida?<div class="ln"></div></div><div>Color the oceans blue when you finish.</div>'
            else:
                body += ('<table class="t"><tr><th>Fast fact</th><th>Ocean</th></tr><tr><td>Largest and deepest (Mariana Trench)</td><td></td></tr>'
                         '<tr><td>Smallest and shallowest; frozen much of the year</td><td></td></tr><tr><td>Between Africa and Australia</td><td></td></tr>'
                         '<tr><td>Circles Antarctica</td><td></td></tr><tr><td>Between the Americas and Europe/Africa</td><td></td></tr></table>')
    elif i == 2:
        if T == "A":
            body = (f'<div class="flexrow"><div class="learn grow"><p class="big">The <b>equator</b> is a pretend line around the middle of the Earth, like a belt. '
                    'The top half is the <b>North</b>. The bottom half is the <b>South</b>.</p></div>' + v + '</div>'
                    + '<svg width="300" height="300" viewBox="0 0 300 300" style="align-self:center"><circle cx="150" cy="150" r="130" fill="#fff" stroke="#1f2a5c" stroke-width="3"/>'
                    '<text x="150" y="95" text-anchor="middle" font-size="26" font-weight="700" fill="#1f2a5c">NORTH</text>'
                    '<text x="150" y="225" text-anchor="middle" font-size="26" font-weight="700" fill="#1f2a5c">SOUTH</text>'
                    '<line x1="20" x2="280" y1="150" y2="150" stroke="#9a9aa8" stroke-width="5" stroke-dasharray="2,10" stroke-linecap="round"/></svg>'
                    + '<div class="lab">Trace the equator belt with a marker. Color the NORTH half blue and the SOUTH half purple.</div>'
                    + '<div class="big">We live in the: &nbsp; <span class="chk"></span>North &nbsp;&nbsp; <span class="chk"></span>South</div>')
        else:
            body = (f'<div class="flexrow"><div class="learn grow"><p>The <b>equator</b> (0° latitude) splits Earth into the <b>Northern</b> and <b>Southern Hemispheres</b>. '
                    'The <b>prime meridian</b> (0° longitude) runs through Greenwich, England, and splits Earth into the <b>Eastern</b> and <b>Western Hemispheres</b>. '
                    'Every place is in two hemispheres at once — one north/south and one east/west.</p></div>' + v + '</div>'
                    + world_map(700, 330, cont_marks=NUM, eq="label", pm="label", star=JAX)
                    + '<div class="lab">Write N or S and E or W for each place.</div>'
                    '<table class="t"><tr><th>Place</th><th>N or S?</th><th>E or W?</th></tr>'
                    + "".join(f"<tr><td>{p}</td><td></td><td></td></tr>" for p in ["Jacksonville, Florida (★)", "Australia", "Europe", "South America (mostly)"]
                              + (["Japan", "Most of Africa is in which N/S hemisphere? (trick: it's in both!)"] if T == "C" else [])) + '</table>')
            if T == "C":
                body += '<div>Explain why some continents are in more than one hemisphere.' + lines(2) + '</div>'
    elif i == 3:
        if T == "A":
            cells = ""
            marks = {(1, 2): "★", (3, 4): "♥", (4, 1): "●", (2, 3): "▲"}
            for r in range(5):
                for c in range(5):
                    cells += f'<rect x="{40+c*60}" y="{10+r*60}" width="60" height="60" fill="#fff" stroke="#1f2a5c" stroke-width="2"/>'
                    if (r, c) in marks:
                        cells += f'<text x="{70+c*60}" y="{52+r*60}" text-anchor="middle" font-size="30" fill="#2f5bd3">{marks[(r,c)]}</text>'
            for r in range(5):
                cells += f'<text x="22" y="{48+r*60}" text-anchor="middle" font-size="20" font-weight="700" fill="#6d28d9">{"ABCDE"[r]}</text>'
            for c in range(5):
                cells += f'<text x="{70+c*60}" y="335" text-anchor="middle" font-size="20" font-weight="700" fill="#6d28d9">{c+1}</text>'
            body = (f'<div class="flexrow"><div class="learn grow"><p class="big">Maps have <b>lines</b> that help us find places — like a treasure map! '
                    'Find the row letter, then the column number.</p></div>' + v + '</div>'
                    f'<svg width="360" height="345" style="align-self:center">{cells}</svg>'
                    '<div class="big">Mom asks: “What is in box B3?” Point to it! Then find: D5, E2, C4.</div>'
                    '<div class="big">Draw a ☺ in box E5 and a circle in box A1.</div>')
        else:
            body = (f'<div class="flexrow"><div class="learn grow"><p><b>Latitude</b> lines run east–west (like rungs on a ladder) and measure how far north or south of the '
                    'equator a place is (0° to 90°). <b>Longitude</b> lines run north–south, pole to pole, and measure how far east or west of the prime meridian '
                    'a place is (0° to 180°). Write latitude first: Jacksonville is about <b>30°N, 82°W</b>.</p></div>' + v + '</div>'
                    + world_map(700, 330, grid=True, lat_labels=True, eq=True, pm=True,
                                extra="".join(f'<text x="{(lon+180)/360*600}" y="{(84-lat)/168*290+5}" text-anchor="middle" font-size="13" font-weight="700" fill="#a21caf">{t}</text>'
                                              for t, lon, lat in [("A", -90, 30), ("B", 30, 0), ("C", 150, -30), ("D", 90, 60), ("E", -60, -30)]))
                    + '<div class="lab">Write the latitude and longitude of each letter (they sit right on grid lines).</div>'
                    + "".join(f'<div><b>{k}.</b> <span class="blank-ln" style="min-width:110px"></span> , <span class="blank-ln" style="min-width:110px"></span></div>' for k in "ABCDE"))
            if T == "C":
                body += '<div>Which letter is in the Southern and Eastern Hemispheres? <span class="blank-ln"></span>&nbsp; Which continent is it on? <span class="blank-ln" style="min-width:150px"></span></div>'
    else:
        if T == "A":
            body = (f'<div class="flexrow"><div class="learn grow"><p class="big">We live in <b>Jacksonville</b>, in the state of <b>Florida</b>, in the country of the '
                    '<b>United States</b>, on the continent of <b>North America</b>!</p></div>' + v + '</div>'
                    + world_map(660, 315, star=JAX) + '<div class="lab">Color North America. Find the ★ — that\'s us!</div>'
                    + '<div class="big">Trace:</div>' + trace_line("Florida", 50, 1)
                    + '<div class="big">Show Mom on the globe: a continent · an ocean · the equator · Florida <span class="star">☆☆☆☆</span></div>')
        else:
            body = (f'<div class="flexrow"><div class="learn grow"><p>Put it all together! Use what you learned this week (and your atlas or globe) to describe exactly where we live.</p></div>{v}</div>'
                    + world_map(660, 315, star=JAX, eq=True, pm=True)
                    + '<table class="t">' + "".join(f"<tr><td style='width:55%'>{q}</td><td></td></tr>" for q in
                        ["City and state", "Country", "Continent", "Nearest ocean", "Hemispheres (N/S and E/W)", "Approximate latitude, longitude"]
                        + (["A continent in the Southern AND Eastern Hemispheres", "The ocean you would cross to fly from Florida to Japan", "Is Jacksonville closer to the equator or the North Pole? How do you know?"] if T == "C" else ["The river that runs through Jacksonville (ask Mom or check the atlas!)"])) + '</table>')
    return page(name, i, "Geography", f"Week 2 · {TITLES[i]}", body)

KEY = ("<b>Continents:</b> 1 North America, 2 South America, 3 Europe, 4 Asia, 5 Africa, 6 Australia, 7 Antarctica. "
       "Fast facts: Asia · Australia · Antarctica · Africa · South America.<br>"
       "<b>Oceans:</b> A Pacific, B Atlantic, C Indian, D Arctic, E Southern. Fast facts: Pacific · Arctic · Indian · Southern · Atlantic. Jacksonville → Atlantic.<br>"
       "<b>Hemispheres:</b> Jacksonville N/W · Australia S/E · Europe N/E (a sliver W) · South America S/W (mostly) · Japan N/E · Africa: both N and S.<br>"
       "<b>Lat/Long:</b> A 30°N, 90°W · B 0°, 30°E · C 30°S, 150°E · D 60°N, 90°E · E 30°S, 60°W. S+E = C, on Australia.<br>"
       "<b>Tier A grid:</b> B3 ★ · D5 ♥ · E2 ● · C4 ▲.<br>"
       "<b>Jacksonville:</b> United States · North America · Atlantic · Northern & Western · ~30°N, 82°W · St. Johns River. "
       "Southern+Eastern: Australia (or Antarctica, part of Africa). Florida → Japan: Pacific. Closer to the equator (30° vs 60° to the pole).")
