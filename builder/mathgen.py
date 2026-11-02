from lib import *
import random, math

def vert(a, b, op):
    return (f'<div class="vert"><div>{a:,}</div><div class="bar" style="border-top:none">{op} {b:,}</div>'
            f'<div class="bar">&nbsp;</div></div>')

def vgrid(probs, cols=5):
    return f'<div class="grid{cols}" style="justify-items:center">' + "".join(
        f'<div style="display:flex;gap:4px"><span class="q" style="font-size:10pt;color:#2f5bd3;font-weight:700">{n+1}.</span>{vert(a,b,op)}</div>'
        for n, (a, b, op) in enumerate(probs)) + '</div>'

def hgrid(items, cols=2, size="13.5pt", space=0):
    return f'<div class="grid{cols}">' + "".join(
        f'<div style="font-size:{size};padding:6px 0 {6+space}px"><b style="color:#2f5bd3">{n+1}.</b> {it}</div>' for n, it in enumerate(items)) + '</div>'

def longdiv(a, b):
    return (f'<div style="display:inline-flex;align-items:flex-start;font-family:Inter;font-size:16pt;padding-bottom:70px">'
            f'<span style="padding:4px 4px 0 0">{b}</span><span style="border-left:2px solid #111;border-top:2px solid #111;'
            f'border-top-left-radius:10px;padding:2px 8px 0 8px">{a:,}</span></div>')

def clock(h, m, size=120, hands=True):
    c = size / 2; r = c - 4
    t = "".join(f'<text x="{c + (r-14)*math.sin(math.radians(k*30)):.1f}" y="{c - (r-14)*math.cos(math.radians(k*30)) + 5:.1f}" '
                f'text-anchor="middle" font-size="{size/9:.0f}" font-weight="600" fill="#1f2a5c">{k or 12}</text>' for k in range(12))
    ticks = "".join(f'<line x1="{c + (r-3)*math.sin(math.radians(k*6)):.1f}" y1="{c - (r-3)*math.cos(math.radians(k*6)):.1f}" '
                    f'x2="{c + r*math.sin(math.radians(k*6)):.1f}" y2="{c - r*math.cos(math.radians(k*6)):.1f}" stroke="#1f2a5c" stroke-width="{2 if k%5==0 else 0.8}"/>' for k in range(60))
    hd = ""
    if hands:
        ma = math.radians(m * 6); ha = math.radians((h % 12) * 30 + m * 0.5)
        hd = (f'<line x1="{c}" y1="{c}" x2="{c + r*0.5*math.sin(ha):.1f}" y2="{c - r*0.5*math.cos(ha):.1f}" stroke="#111" stroke-width="5" stroke-linecap="round"/>'
              f'<line x1="{c}" y1="{c}" x2="{c + r*0.78*math.sin(ma):.1f}" y2="{c - r*0.78*math.cos(ma):.1f}" stroke="#2f5bd3" stroke-width="3" stroke-linecap="round"/>')
    return (f'<svg width="{size}" height="{size}"><circle cx="{c}" cy="{c}" r="{r}" fill="#fff" stroke="#1f2a5c" stroke-width="3"/>{ticks}{t}{hd}'
            f'<circle cx="{c}" cy="{c}" r="4" fill="#111"/></svg>')

def blocks(n, unit=11):
    """base-ten picture: tens rods + ones cubes"""
    t, o = divmod(n, 10); x = 2; s = ""
    for _ in range(t):
        s += "".join(f'<rect x="{x}" y="{2+k*unit}" width="{unit}" height="{unit}" fill="#eef1fb" stroke="#2f5bd3" stroke-width="1.2"/>' for k in range(10)); x += unit + 5
    for k in range(o):
        s += f'<rect x="{x + (k%2)*(unit+3)}" y="{2 + (k//2)*(unit+3)}" width="{unit}" height="{unit}" fill="#f1ebfd" stroke="#6d28d9" stroke-width="1.2"/>'
    w = x + 2 * (unit + 3) + 4
    return f'<svg width="{w}" height="{10*unit+6}">{s}</svg>'

def objs(n, shape="circle", per_row=5, sz=34):
    s = ""
    for k in range(n):
        r, c = divmod(k, per_row); x, y = 4 + c * (sz + 8), 4 + r * (sz + 8)
        if shape == "circle":
            s += f'<circle cx="{x+sz/2}" cy="{y+sz/2}" r="{sz/2-2}" fill="#fff" stroke="#6d28d9" stroke-width="2.5"/>'
        elif shape == "star":
            pts = " ".join(f"{x+sz/2+ (sz/2-2 if j%2==0 else sz/5)*math.sin(j*math.pi/5):.1f},{y+sz/2- (sz/2-2 if j%2==0 else sz/5)*math.cos(j*math.pi/5):.1f}" for j in range(10))
            s += f'<polygon points="{pts}" fill="#fff" stroke="#2f5bd3" stroke-width="2.5"/>'
        else:
            s += f'<rect x="{x+2}" y="{y+2}" width="{sz-4}" height="{sz-4}" rx="5" fill="#fff" stroke="#a21caf" stroke-width="2.5"/>'
    rows = (n + per_row - 1) // per_row
    return f'<svg width="{per_row*(sz+8)+4}" height="{rows*(sz+8)+4}">{s}</svg>'
