from lib import *

def learnbox(html_, vid=None, label="Watch"):
    q = qr_box(vid, label, 62) if vid else ""
    return f'<div class="flexrow"><div class="learn grow">{html_}</div>{q}</div>'

def qs(items, start=1, h=24):
    """items: list of (question, nlines)"""
    return "".join(f'<div><b>{start+n}.</b> {q}{lines(k, h) if k else ""}</div>' for n, (q, k) in enumerate(items))

def mark_list(items, choices, start=1, cols=1):
    ch = " ".join(f'<span class="opt" style="border:1.4px solid #9aa0bb;border-radius:4px;padding:0 6px;margin-left:4px;font-size:10pt">{c}</span>' for c in choices)
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
