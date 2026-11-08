from lib import *

# Speech Stars Week 3 — "Tongue Peek" (TH). Comes after Week 2 Bunny Teeth & Tails (F/V, final K).
WK = 3
VID = [yt("SP voiceless th sound phonics"), yt("SP voiced th sound phonics"), yt("SP th articulation words"),
       yt("SP th speech sound activities"), yt("SP teaching th sound Charli")]
TITLES = ["Tongue Peek: Quiet TH", "Buzzy TH", "TH at the End", "Phrases & Sentences", "Game Board Review"]
TH_QUIET = ["thumb", "think", "thank", "thin", "three", "thirty", "thorn", "thirsty", "thunder", "Thursday"]
TH_BUZZ = ["the", "this", "that", "they", "them", "there", "then", "those", "mother", "feather"]
TH_END = ["bath", "math", "tooth", "teeth", "mouth", "path", "moth", "north", "south", "both"]
PHRASES = ["thank you", "three teeth", "this bath", "brush my teeth", "my mother",
           "think of that", "a thin moth", "the north path", "both thumbs", "thirty three"]
SENT = ["Thank you for the bath.", "I brush my teeth.", "This moth is thin.",
        "Three birds sat on the path.", "My mother and father love me."]
def tracker(words, cols=2, n=5):
    rows = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1.2px solid #e0e2ee;padding:9px 2px">'
                   f'<span class="word" style="font-size:17pt">{esc(w)}</span><span class="star" style="font-size:17pt">{"☆"*n}</span></div>' for w in words)
    return f'<div class="grid{cols}" style="gap:2px 22px">{rows}</div>'

GYM = ('<div class="box"><span class="lab">Mouth Gym warm-up (1 min):</span> tongue elevator up & down ×5 · tongue peek '
       '(tip just between your teeth) ×5 · smile–kiss ×5</div>')

def head(text, v):
    return f'<div class="flexrow"><div class="grow"><div class="learn"><p class="big">{text}</p></div>{GYM}</div>{v}</div>'

def speech_page(name, i):
    v = qr_box(VID[i], "Watch & copy", 62)
    if i == 0:
        body = (head('<b>Tongue peek!</b> Put the tip of your tongue just between your teeth — let it peek out a tiny bit, like a turtle '
                     'peeking out of its shell. Now blow air: “thhh.” That\'s the <b>quiet TH</b>. Check in the mirror — can you see your tongue?', v)
                + '<div class="grid2"><div class="box center"><div class="huge">thhh</div><div>tongue peeks out · quiet air</div></div>'
                  '<div class="box center"><div class="huge">not “f” or “s”</div><div>no bunny teeth · no snake</div></div></div>'
                + '<div class="lab">Quiet TH at the start. Mom says it, you copy with a tongue peek. Color a star each time!</div>' + tracker(TH_QUIET, 2))
    elif i == 1:
        body = (head('<b>Buzzy TH!</b> Same tongue peek — but turn your voice ON so your tongue tickles: “thhh-uh.” '
                     'Hand on your throat — feel the buzz? Lots of little words use buzzy TH: <b>the, this, that</b>.', v)
                + '<div class="grid2"><div class="box center"><div class="huge">thhh</div><div>quiet — just air (thumb)</div></div>'
                  '<div class="box center"><div class="huge">thhh~</div><div>buzzy — voice on (this)</div></div></div>'
                + tracker(TH_BUZZ, 2))
    elif i == 2:
        body = (head('TH at the <b>end</b>! Finish every word with a tongue peek — don\'t turn it into “f” (“baf”) or drop it. '
                     'ba-<b>th</b>, too-<b>th</b>, mou-<b>th</b>.', v)
                + tracker(TH_END, 2)
                + '<div class="lab">Mirror check: does your tongue peek out at the END of “tooth”? <span class="chk"></span> yes!</div>'
                + '<div class="lab">Silly practice: point to your tooth, your teeth, your mouth, and your thumb — and say each one!</div>')
    elif i == 3:
        body = (head('Now put TH in <b>phrases</b>. Go slow — tongue peek every time you see “th”!', v)
                + tracker(PHRASES, 2, 3)
                + '<div class="lab">Sentence challenge (Nariah reads; Titus & Nayeli echo Mom):</div>'
                + "".join(f'<div class="big" style="margin:2px 0">{n+1}. {esc(s)} <span class="star" style="font-size:15pt">☆☆☆</span></div>' for n, s in enumerate(SENT)))
    else:
        words = TH_QUIET[:5] + TH_BUZZ[:5] + TH_END[:5] + PHRASES[:5]
        sq = ""
        for k, w in enumerate(words):
            r, c = divmod(k, 5)
            if r % 2: c = 4 - c
            x, y = 6 + c * 136, 6 + r * 96
            sq += (f'<rect x="{x}" y="{y}" width="128" height="88" rx="10" fill="{"#f1ebfd" if k%2 else "#eef1fb"}" stroke="#a21caf" stroke-width="2"/>'
                   f'<text x="{x+64}" y="{y+52}" text-anchor="middle" font-size="{19 if len(w)<9 else 14}" font-weight="700" fill="#1f2a5c">{esc(w)}</text>'
                   f'<text x="{x+10}" y="{y+20}" font-size="12" fill="#a21caf">{k+1}</text>')
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big"><b>Game day!</b> Roll a die and move your button. Say the word on your square with a '
                f'tongue peek. Miss it? Try again! First to 20 wins.</p></div>{v}</div>'
                f'<svg width="690" height="392" style="align-self:center">{sq}</svg>'
                '<div class="big center">START at 1 → FINISH at 20 ★</div>'
                '<div class="box"><span class="lab">Mom\'s check:</span> quiet TH <span class="chk"></span> &nbsp; buzzy TH <span class="chk"></span> '
                '&nbsp; TH at end <span class="chk"></span> &nbsp; Needs more practice: ____________</div>')
    return page(name, i, "Speech Stars", f"Week {WK} · {TITLES[i]}", body)

MOM = ("<p><b>Speech Stars Week 3 — Tongue Peek (TH)</b> (10 minutes a day). After Bunny Teeth & Tails (F/V, final K), this week teaches TH: "
       "the tongue tip peeks between the teeth. Quiet TH (thumb) is just air; buzzy TH (this) has the voice on. Common swaps to listen for: "
       "“f” for TH (“fumb,” “baf”), “d” for buzzy TH (“dis”), or “s” (“sank you”). A small mirror helps a lot.</p>")
