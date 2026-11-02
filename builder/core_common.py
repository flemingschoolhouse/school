from lib import *

def learnbox(html_, vid=None, label="Watch"):
    q = qr_box(vid, label, 62) if vid else ""
    return f'<div class="flexrow"><div class="learn grow">{html_}</div>{q}</div>'

import zlib, random as _rnd

def mc_opts(choices, seed=""):
    """Tap/circle answer pills. choices[0] is the correct answer; order is shuffled the same way every build."""
    ch = list(choices)
    _rnd.Random(zlib.crc32(seed.encode()) ^ len(ch)).shuffle(ch)
    return '<div class="mcopts">' + "".join(f'<span class="opt">{c}</span>' for c in ch) + '</div>'

def mc(q, choices, num=None):
    """Multiple-choice question: circle it on paper, tap it on the tablet."""
    lead = f"<b>{num}.</b> " if num is not None else ""
    return f'<div class="mcq">{lead}{q}{mc_opts(choices, q)}</div>'

def pick(*opts):
    """Inline choice like (I / me) that kids can circle on paper or tap on the tablet. Order kept as written."""
    return '<span class="pick">(' + " / ".join(f'<span class="opt">{o}</span>' for o in opts) + ')</span>'

MC_HINT = '<div class="mchint">Circle the answer (or tap it on your tablet).</div>'

def qs(items, start=1, h=24):
    """items: list of (question, nlines) for a written answer, or (question, [correct, wrong, ...]) for multiple choice."""
    out = []
    for n, (q, k) in enumerate(items):
        if isinstance(k, (list, tuple)):
            out.append(mc(q, k, start + n))
        else:
            out.append(f'<div><b>{start+n}.</b> {q}{lines(k, h) if k else ""}</div>')
    return "".join(out)

def mark_list(items, choices, start=1, cols=1):
    ch = " ".join(f'<span class="opt" style="border:1.4px solid #9aa0bb;border-radius:12px;padding:0 8px;margin-left:4px;font-size:11pt">{c}</span>' for c in choices)
    cells = "".join(f'<div style="padding:4px 0"><b>{start+n}.</b> {it} <span style="float:right">{ch}</span></div>' for n, it in enumerate(items))
    return f'<div class="grid{cols}" style="gap:2px 24px">{cells}</div>'

def fill_table(headers, rows, h=30):
    th = "".join(f"<th>{x}</th>" for x in headers)
    tr = "".join("<tr>" + "".join(f"<td style='height:{h}px'>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="t"><tr>{th}</tr>{tr}</table>'

class Subject:
    """Holds 5 days of pages + answer keys for one kid-subject."""
    def __init__(self, kid, subject, unit):
        self.kid, self.subject, self.unit = kid, subject, unit
        self.days = [None] * 5; self.keys = [""] * 5; self.titles = [""] * 5
    def set(self, i, title, body, key=""):
        self.titles[i] = title; self.keys[i] = key
        self.days[i] = page(self.kid, i, self.subject, f"{self.unit} · {title}", body)
