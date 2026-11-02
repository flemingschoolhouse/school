# Shared building blocks for Grace's combined weekly packets.
# NO YELLOW: every color below has blue as its largest channel (=> 0% yellow in CMYK).
import html, urllib.parse
from reportlab.graphics.barcode.qr import QrCodeWidget

C = dict(
    navy="#1f2a5c", blue="#2f5bd3", indigo="#4338ca", purple="#6d28d9",
    violet="#7b3fc4", plum="#8a3ab9", magenta="#a21caf", orchid="#b02fc9",
    ink="#111111", gray="#555566", lite="#d6d6e0", wash="#eef1fb", lav="#f1ebfd",
)
SUBJ = {  # subject -> accent color
    "Morning Work": C["navy"], "Math": C["blue"], "Math Crash Course": C["blue"],
    "English": C["violet"], "Letters & Writing": C["violet"], "Science": C["indigo"],
    "History": C["plum"], "Social Studies": C["plum"], "Civics": C["plum"], "Florida History": C["plum"],
    "Multiplication Mastery": C["purple"], "Skip Count Stars": C["purple"],
    "Speech Stars": C["magenta"], "Geography": C["blue"], "Fun Electives": C["orchid"],
    "Pre-K": C["magenta"], "Mom": C["navy"],
}
DAYS = [("Day 1", "Tuesday", "Nov 3"), ("Day 2", "Wednesday", "Nov 4"), ("Day 3", "Thursday", "Nov 5"),
        ("Day 4", "Friday", "Nov 6"), ("Day 5", "Saturday", "Nov 7")]

esc = html.escape

MISSING = set()
def yt(q):
    from videos import V
    if q in V:
        return "https://www.youtube.com/watch?v=" + V[q]
    MISSING.add(q)
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q)

def qr_svg(url, size=78):
    w = QrCodeWidget(url); w.barLevel = "M"; w.draw(); q = w.qr
    n = q.getModuleCount(); b = 2; tot = n + 2 * b
    rects = [f'<rect x="{c+b}" y="{r+b}" width="1.02" height="1.02"/>'
             for r in range(n) for c in range(n) if q.isDark(r, c)]
    return (f'<svg class="qr" width="{size}" height="{size}" viewBox="0 0 {tot} {tot}" '
            f'shape-rendering="crispEdges"><rect width="{tot}" height="{tot}" fill="#fff"/>'
            f'<g fill="#000">{"".join(rects)}</g></svg>')

WEB = {"on": False}

def qr_box(url, label, size=74):
    if WEB["on"]:
        vid = url.split("watch?v=")[1] if "watch?v=" in url else ""
        return f'<a class="vidbtn" data-vid="{vid}" href="{esc(url)}" target="_blank" rel="noopener">▶ {esc(label)}</a>'
    return f'<div class="qrbox">{qr_svg(url,size)}<div class="qrl">{esc(label)}</div></div>'

# ---------------- ball-and-stick school print (stroke font) ----------------
# units: top=0, midline=5, baseline=10, descender=14.  (width, path)
G = {
 'a': (5, "M5,7.5 A2.5,2.5 0 1 1 5,7.49 M5,5 L5,10"),
 'b': (5, "M0,0 L0,10 M0,7.5 A2.5,2.5 0 1 1 0,7.51"),
 'c': (4.6, "M4.6,5.9 A2.5,2.5 0 1 0 4.6,9.1"),
 'd': (5, "M5,7.5 A2.5,2.5 0 1 1 5,7.49 M5,0 L5,10"),
 'e': (5, "M0.1,7.5 L5,7.5 A2.5,2.5 0 1 0 4.4,9.2"),
 'f': (4, "M4,1 A2,2 0 0 0 1.5,2.6 L1.5,10 M0,5 L3.6,5"),
 'g': (5, "M5,7.5 A2.5,2.5 0 1 1 5,7.49 M5,5 L5,12 A2.2,2.2 0 0 1 0.6,12.8"),
 'h': (5, "M0,0 L0,10 M0,7.5 A2.5,2.5 0 0 1 5,7.5 L5,10"),
 'i': (0.6, "M0.3,5 L0.3,10 M0.3,2.6 L0.3,2.7"),
 'j': (3, "M3,5 L3,12 A2.2,2.2 0 0 1 -1.2,12.8 M3,2.6 L3,2.7"),
 'k': (4.4, "M0,0 L0,10 M4.2,5 L0,8 M1.6,6.9 L4.4,10"),
 'l': (0.6, "M0.3,0 L0.3,10"),
 'm': (8, "M0,5 L0,10 M0,7 A2,2 0 0 1 4,7 L4,10 M4,7 A2,2 0 0 1 8,7 L8,10"),
 'n': (5, "M0,5 L0,10 M0,7.5 A2.5,2.5 0 0 1 5,7.5 L5,10"),
 'o': (5, "M0,7.5 A2.5,2.5 0 1 1 0,7.51"),
 'p': (5, "M0,5 L0,14 M0,7.5 A2.5,2.5 0 1 1 0,7.51"),
 'q': (5, "M5,7.5 A2.5,2.5 0 1 1 5,7.49 M5,5 L5,14"),
 'r': (3.6, "M0,5 L0,10 M0,7.6 A2.6,2.6 0 0 1 3.6,5.4"),
 's': (4.2, "M4,5.7 C3.2,4.8 0.4,4.8 0.4,6.4 C0.4,8 4.1,7.3 4.1,8.9 C4.1,10.6 1,10.6 0,9.5"),
 't': (3.6, "M1.8,1.5 L1.8,10 M0,5 L3.6,5"),
 'u': (5, "M0,5 L0,7.5 A2.5,2.5 0 0 0 5,7.5 M5,5 L5,10"),
 'v': (5, "M0,5 L2.5,10 L5,5"),
 'w': (7, "M0,5 L1.75,10 L3.5,5 L5.25,10 L7,5"),
 'x': (4.6, "M0,5 L4.6,10 M4.6,5 L0,10"),
 'y': (5, "M0,5 L2.5,10 M5,5 L1.6,14"),
 'z': (4.6, "M0,5 L4.6,5 L0,10 L4.6,10"),
 'A': (7, "M0,10 L3.5,0 L7,10 M1.3,6.4 L5.7,6.4"),
 'B': (5.8, "M0,0 L0,10 M0,0 L3,0 A2.5,2.5 0 0 1 3,5 L0,5 M0,5 L3.3,5 A2.5,2.5 0 0 1 3.3,10 L0,10"),
 'C': (8.6, "M8.6,1.6 A5,5 0 1 0 8.6,8.4"),
 'D': (7, "M0,0 L0,10 L2,10 A5,5 0 0 0 2,0 L0,0"),
 'E': (5.6, "M5.6,0 L0,0 L0,10 L5.6,10 M0,5 L4.6,5"),
 'F': (5.6, "M5.6,0 L0,0 L0,10 M0,5 L4.6,5"),
 'G': (10, "M8.6,1.6 A5,5 0 1 0 10,5 L6,5"),
 'H': (6, "M0,0 L0,10 M6,0 L6,10 M0,5 L6,5"),
 'I': (4, "M0,0 L4,0 M2,0 L2,10 M0,10 L4,10"),
 'J': (5, "M5,0 L5,7.5 A2.5,2.5 0 0 1 0,7.5"),
 'K': (6, "M0,0 L0,10 M6,0 L0,6 M2.1,4.3 L6,10"),
 'L': (5.4, "M0,0 L0,10 L5.4,10"),
 'M': (8, "M0,10 L0,0 L4,10 L8,0 L8,10"),
 'N': (6.4, "M0,10 L0,0 L6.4,10 L6.4,0"),
 'O': (10, "M0,5 A5,5 0 1 1 0,5.01"),
 'P': (5.8, "M0,10 L0,0 L3,0 A2.6,2.6 0 0 1 3,5.2 L0,5.2"),
 'Q': (10, "M0,5 A5,5 0 1 1 0,5.01 M6.4,7 L10,10.6"),
 'R': (6, "M0,10 L0,0 L3,0 A2.6,2.6 0 0 1 3,5.2 L0,5.2 M2.6,5.2 L6,10"),
 'S': (6, "M5.6,1.4 C4.6,-0.4 0.4,-0.3 0.4,2.6 C0.4,5.4 5.8,4.6 5.8,7.4 C5.8,10.6 1,10.6 0,8.6"),
 'T': (7, "M0,0 L7,0 M3.5,0 L3.5,10"),
 'U': (6.4, "M0,0 L0,6.8 A3.2,3.2 0 0 0 6.4,6.8 L6.4,0"),
 'V': (7, "M0,0 L3.5,10 L7,0"),
 'W': (10, "M0,0 L2.5,10 L5,0 L7.5,10 L10,0"),
 'X': (6.4, "M0,0 L6.4,10 M6.4,0 L0,10"),
 'Y': (6.4, "M0,0 L3.2,5 L6.4,0 M3.2,5 L3.2,10"),
 'Z': (6.4, "M0,0 L6.4,0 L0,10 L6.4,10"),
 '0': (5.6, "M2.8,0 C-0.9,0 -0.9,10 2.8,10 C6.5,10 6.5,0 2.8,0"),
 '1': (2.6, "M0,2 L2.2,0 L2.2,10"),
 '2': (5.6, "M0.3,2.6 A2.7,2.6 0 1 1 5,4.4 L0,10 L5.6,10"),
 '3': (5.4, "M0.2,1.2 A2.6,2.4 0 1 1 2.6,4.9 M2.6,4.9 A2.7,2.6 0 1 1 0,8.8"),
 '4': (6, "M4.6,10 L4.6,0 L0,6.6 L6,6.6"),
 '5': (5.6, "M5.4,0 L1,0 L0.5,4.4 C2.8,3.2 5.8,4.2 5.6,7.1 C5.4,10.6 1.2,10.6 0,8.8"),
 '6': (5.6, "M4.6,0.4 C1.4,1.2 0,4.4 0,7.1 A2.8,2.8 0 1 0 0.5,5.6"),
 '7': (5.6, "M0,0 L5.6,0 L1.8,10"),
 '8': (5.4, "M2.7,4.8 A2.3,2.4 0 1 1 2.71,4.8 M2.7,4.8 A2.7,2.6 0 1 1 2.69,4.8"),
 '9': (5.6, "M5.6,2.9 A2.8,2.8 0 1 0 5.6,3 M5.6,2.9 L5.6,10"),
 '.': (0.6, "M0.3,9.9 L0.3,10"),
 ',': (1, "M0.6,9.6 L0,11.4"),
 '!': (0.6, "M0.3,0 L0.3,7 M0.3,9.9 L0.3,10"),
 '?': (5, "M0.2,2.4 A2.5,2.4 0 1 1 2.5,5 L2.5,7 M2.5,9.9 L2.5,10"),
 "'": (0.6, "M0.3,0 L0.3,2.6"),
 '-': (3, "M0,6.5 L3,6.5"),
 ' ': (3.2, ""),
}
GAP = 2.1

def word_width(t):
    return sum(G.get(ch, G[' '])[0] + GAP for ch in t) - GAP

def school_print(text, h=36, mode="trace", lines=True, extra_w=0, color=None):
    """Render text in ball-and-stick print on handwriting lines. mode: trace | solid | blank"""
    u = h / 14.0  # px per unit (14 units: 0..14 incl descender)
    w_units = word_width(text) if text else 0
    pad = 1.5
    W = (w_units + 2 * pad) * u + extra_w
    sw = max(2.2, u * 0.95)
    out = [f'<svg width="{W:.1f}" height="{h+4:.1f}" viewBox="{-pad*u:.1f} -2 {W:.1f} {h+4:.1f}">']
    if lines:
        x0, x1 = -pad * u, W - pad * u
        out.append(f'<line x1="{x0}" x2="{x1}" y1="0" y2="0" stroke="#7d8bb8" stroke-width="1"/>')
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{5*u}" y2="{5*u}" stroke="#9aa6cc" stroke-width="1" stroke-dasharray="5,4"/>')
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{10*u}" y2="{10*u}" stroke="#1f2a5c" stroke-width="1.4"/>')
    if mode != "blank" and text:
        if mode == "trace":
            st = f'stroke="#9a9aa8" stroke-width="{sw:.2f}" stroke-dasharray="{sw*0.2:.2f},{sw*1.3:.2f}"'
        else:
            st = f'stroke="{color or "#1f2a5c"}" stroke-width="{sw:.2f}"'
        out.append(f'<g fill="none" {st} stroke-linecap="round" stroke-linejoin="round" transform="scale({u})">')
        x = 0
        for ch in text:
            gw, p = G.get(ch, G[' '])
            if p:
                out.append(f'<path transform="translate({x},0)" d="{p}" vector-effect="non-scaling-stroke"/>')
            x += gw + GAP
        out.append('</g>')
    out.append('</svg>')
    return "".join(out)

def trace_line(text, h=40, repeats=1, sep=8, blank_after=0):
    """A full-width practice row: model (solid) then traces then blank space."""
    parts = [school_print(text, h, "solid")]
    parts += [school_print(text, h, "trace") for _ in range(repeats)]
    if blank_after:
        parts.append(school_print("", h, "blank", extra_w=blank_after))
    return f'<div class="trow" style="gap:{sep}px">{"".join(parts)}</div>'

# ---------------- page scaffolding ----------------
CSS = """
@page { size: 8.5in 11in; margin: 0; }
* { box-sizing: border-box; }
body { margin:0; font-family: 'Poppins', 'Inter', sans-serif; color:#111; font-size: 11.5pt; }
.page { width:8.5in; height:11in; padding:0.45in 0.5in 0.4in; position:relative; overflow:hidden;
        page-break-after: always; display:flex; flex-direction:column; }
.page.blank { page-break-after: always; }
.hdr { display:flex; align-items:flex-end; justify-content:space-between; border-bottom:3px solid var(--ac);
       padding-bottom:6px; margin-bottom:10px; }
.dayblk .d { font-size:34pt; font-weight:700; line-height:0.95; color:var(--ac); letter-spacing:0.5px; }
.dayblk .w { font-size:10.5pt; color:#555566; font-weight:500; margin-top:2px; }
.subj { text-align:right; }
.subj .s { display:inline-block; background:var(--ac); color:#fff; font-weight:600; font-size:11pt;
           padding:3px 12px; border-radius:20px; }
.subj .t { font-size:13.5pt; font-weight:600; margin-top:4px; color:#1f2a5c; }
.subj .n { font-size:9.5pt; color:#555566; margin-top:1px; }
.body { flex:1; display:flex; flex-direction:column; gap:9px; min-height:0; }
.foot { font-size:8pt; color:#777788; display:flex; justify-content:space-between; margin-top:6px; }
h3 { margin:2px 0 2px; font-size:12.5pt; color:var(--ac); }
p { margin:0 0 5px; line-height:1.38; }
.learn { background:#eef1fb; border-left:5px solid var(--ac); padding:8px 12px; border-radius:6px; }
.learn p:last-child { margin-bottom:0; }
.box { border:1.6px solid #c9cde3; border-radius:8px; padding:8px 12px; }
.lab { font-weight:700; color:var(--ac); }
ol, ul { margin:2px 0 4px 20px; padding:0; } li { margin:2px 0 4px; line-height:1.35; }
.ln { border-bottom:1.3px solid #9aa0bb; height:26px; }
.lns > .ln { margin-bottom:2px; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:6px 18px; }
.grid3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px 14px; }
.grid4 { display:grid; grid-template-columns:repeat(4,1fr); gap:8px 12px; }
.grid6 { display:grid; grid-template-columns:repeat(6,1fr); gap:8px 8px; }
.grid5 { display:grid; grid-template-columns:repeat(5,1fr); gap:8px 10px; }
.prob { font-size:13pt; padding:4px 2px; }
.prob .q { font-weight:600; color:#1f2a5c; margin-right:4px; }
.vert { font-family:'Inter', monospace; font-size:17pt; text-align:right; display:inline-block; line-height:1.15;
        min-width:70px; padding-bottom:58px; font-variant-numeric: tabular-nums; }
.vert .bar { border-top:2px solid #111; }
.blank-ln { display:inline-block; border-bottom:1.4px solid #333; min-width:70px; height:18px; }
.qrrow { display:flex; gap:14px; align-items:center; }
.qrbox { display:flex; flex-direction:column; align-items:center; width:92px; }
.qrl { font-size:7.5pt; text-align:center; color:#444455; line-height:1.15; margin-top:2px; }
.trow { display:flex; flex-wrap:wrap; align-items:flex-end; margin:3px 0; }
.chk { display:inline-block; width:15px; height:15px; border:1.6px solid #1f2a5c; border-radius:3px; vertical-align:-2px; margin-right:6px; }
table.t { border-collapse:collapse; width:100%; font-size:10.5pt; }
table.t td, table.t th { border:1.2px solid #b9bed6; padding:5px 7px; vertical-align:top; }
table.t th { background:#eef1fb; color:#1f2a5c; text-align:left; }
.big { font-size:15pt; } .huge { font-size:22pt; font-weight:700; }
.center { text-align:center; } .small { font-size:9.5pt; color:#444455; }
.verse { font-size:13pt; font-weight:600; color:#1f2a5c; background:#f1ebfd; border-radius:8px; padding:8px 12px; }
.mcq { break-inside:avoid; }
.mcopts { display:flex; flex-wrap:wrap; gap:3px 8px; margin:2px 0 1px 20px; }
.mcopts .opt, .pick .opt { display:inline-block; border:1.4px solid #9aa0bb; border-radius:14px; padding:0 10px; font-size:11pt; line-height:1.45; background:#fff; }
.pick .opt { padding:0 7px; margin:0 2px; font-size:inherit; }
.mchint { font-size:9.5pt; color:#6b7280; font-style:italic; }
.pill { display:inline-block; border:1.5px solid var(--ac); color:var(--ac); border-radius:14px; padding:1px 10px; font-weight:600; font-size:10pt; margin:2px 4px 2px 0; }
.star { font-size:20pt; color:#b9bed6; letter-spacing:4px; }
.word { font-size:20pt; font-weight:700; color:#1f2a5c; }
.flexrow { display:flex; gap:14px; align-items:flex-start; }
.grow { flex:1; }
.answer-space { flex:1; border:1.6px dashed #c9cde3; border-radius:8px; min-height:60px; }
"""

class Packet:
    def __init__(self, owner, title):
        self.owner, self.title, self.pages = owner, title, []
    def add(self, html_page):
        self.pages.append(html_page)
    def pad_even(self):
        if len(self.pages) % 2:
            self.pages.append('<div class="page blank"></div>')
    def html(self):
        return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(self.pages)}</body></html>"

def page(owner, day_i, subject, title, body, sub=None):
    ac = SUBJ.get(subject, C["navy"])
    if day_i is None:
        dayblk = f'<div class="dayblk"><div class="d" style="font-size:24pt">{esc(sub or "")}</div></div>'
    else:
        d, wd, dt = DAYS[day_i]
        dayblk = f'<div class="dayblk"><div class="d">{d.upper()}</div><div class="w">{wd} · {dt}</div></div>'
    return (f'<div class="page" style="--ac:{ac}"><div class="hdr">{dayblk}'
            f'<div class="subj"><span class="s">{esc(subject)}</span><div class="t">{esc(title)}</div>'
            f'<div class="n">{esc(owner)}</div></div></div><div class="body">{body}</div>'
            f'<div class="foot"><span>{esc(owner)}</span><span>Week of Nov 3, 2026</span></div></div>')

def lines(n, h=26):
    return '<div class="lns">' + "".join(f'<div class="ln" style="height:{h}px"></div>' for _ in range(n)) + '</div>'

def ol(items, start=1):
    return f'<ol start="{start}">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def stars(n=5):
    return '<span class="star">' + "☆" * n + "</span>"
