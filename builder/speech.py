from lib import *

# Speech Stars Week 2 (continued) — "Bunny Teeth & Tails". Lesson 1 (bunny teeth F) already done.
VID = [yt("v sound speech therapy for kids"), yt("f and v sound at end of words speech practice"),
       yt("final k sound speech therapy for kids"), yt("f v k sound sentences speech practice kids"), yt("speech therapy game f v k sounds")]
TITLES = ["Bunny Teeth Buzz: V", "Bunny Tails: F & V at the End", "Kitty Tails: K at the End", "Phrases & Sentences", "Game Board Review"]
V_START = ["van", "vest", "vase", "vine", "vet", "very", "visit", "violin", "voice", "volcano"]
FV_END = ["leaf", "off", "roof", "knife", "laugh", "five", "give", "glove", "stove", "wave"]
K_END = ["book", "duck", "cake", "rock", "sock", "bike", "milk", "lake", "snack", "truck"]
PHRASES = ["five ducks", "a big leaf", "give me the book", "my purple glove", "a red truck",
           "very good snack", "wave to the van", "off the roof", "a pink sock", "I love cake"]
SENT = ["I gave five ducks a snack.", "The van drove to the lake.", "Put the glove in the truck.",
        "A leaf fell off the roof.", "I love my purple bike."]

def tracker(words, cols=2, n=5):
    rows = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1.2px solid #e0e2ee;padding:9px 2px">'
                   f'<span class="word" style="font-size:17pt">{esc(w)}</span><span class="star" style="font-size:17pt">{"☆"*n}</span></div>' for w in words)
    return f'<div class="grid{cols}" style="gap:2px 22px">{rows}</div>'

GYM = ('<div class="box"><span class="lab">Mouth Gym warm-up (1 min):</span> tongue elevator up & down ×5 · bunny teeth '
       '(top teeth gently on bottom lip) ×5 · smile–kiss ×5</div>')

def head(text, v):
    return f'<div class="flexrow"><div class="grow"><div class="learn"><p class="big">{text}</p></div>{GYM}</div>{v}</div>'

def speech_page(name, i):
    v = qr_box(VID[i], "Watch & copy", 62)
    if i == 0:
        body = (head('<b>Bunny teeth</b> again — top teeth gently on your bottom lip! For <b>F</b> just blow air: “fff.” For <b>V</b>, turn your voice ON so your lip '
                     '<b>buzzes</b>: “vvvv.” Put your hand on your throat — feel the buzz?', v)
                + '<div class="grid2"><div class="box center"><div class="huge">fff</div><div>quiet — just air</div></div>'
                  '<div class="box center"><div class="huge">vvv</div><div>buzzy — voice on</div></div></div>'
                + '<div class="lab">V at the start. Mom says it, you copy with bunny teeth. Color a star each time!</div>' + tracker(V_START, 2))
    elif i == 1:
        body = (head('Bunny <b>tails</b>! The F or V sound comes at the <b>end</b> of the word. Don\'t drop it — finish with bunny teeth: '
                     'lea-<b>f</b>, fi-<b>ve</b>.', v)
                + tracker(FV_END, 2)
                + '<div class="lab">Mirror check: are your bunny teeth showing at the END of “five”? <span class="chk"></span> yes!</div>')
    elif i == 2:
        body = (head('Kitty tails! <b>K</b> at the end is made in the <b>back</b> of your mouth — like a little cough: “k!” Don\'t let it disappear: '
                     'boo-<b>k</b>, du-<b>ck</b>. Hold your chin and feel the back of your tongue pop up.', v)
                + tracker(K_END, 2)
                + '<div class="lab">Silly practice: say “k-k-k” like a clock ticking, then like a chicken pecking!</div>')
    elif i == 3:
        body = (head('Now put the sounds in <b>phrases</b>. Go slow — bunny teeth for F and V, kitty tail for K!', v)
                + tracker(PHRASES, 2, 3)
                + '<div class="lab">Sentence challenge (Nariah reads; Titus & Nayeli echo Mom):</div>'
                + "".join(f'<div class="big" style="margin:2px 0">{n+1}. {esc(s)} <span class="star" style="font-size:15pt">☆☆☆</span></div>' for n, s in enumerate(SENT)))
    else:
        words = FV_END[:5] + V_START[:5] + K_END[:5] + PHRASES[:5]
        sq = ""
        for k, w in enumerate(words):
            r, c = divmod(k, 5)
            if r % 2: c = 4 - c
            x, y = 6 + c * 136, 6 + r * 96
            sq += (f'<rect x="{x}" y="{y}" width="128" height="88" rx="10" fill="{"#f1ebfd" if k%2 else "#eef1fb"}" stroke="#a21caf" stroke-width="2"/>'
                   f'<text x="{x+64}" y="{y+52}" text-anchor="middle" font-size="{19 if len(w)<9 else 14}" font-weight="700" fill="#1f2a5c">{esc(w)}</text>'
                   f'<text x="{x+10}" y="{y+20}" font-size="12" fill="#a21caf">{k+1}</text>')
        body = (f'<div class="flexrow"><div class="learn grow"><p class="big"><b>Game day!</b> Roll a die and move your button. Say the word on your square — bunny teeth '
                f'for F and V, kitty tail for K. Miss it? Try again! First to 20 wins.</p></div>{v}</div>'
                f'<svg width="690" height="392" style="align-self:center">{sq}</svg>'
                '<div class="big center">START at 1 → FINISH at 20 ★</div>'
                '<div class="box"><span class="lab">Mom\'s check:</span> V <span class="chk"></span> &nbsp; F/V at end <span class="chk"></span> '
                '&nbsp; K at end <span class="chk"></span> &nbsp; Needs more practice: ____________</div>')
    return page(name, i, "Speech Stars", f"Week 2 · {TITLES[i]}", body)

MOM = ("<p><b>Speech Stars Week 2, continued — Bunny Teeth & Tails</b> (10 minutes a day). You finished Lesson 1 (bunny teeth F), so this week picks up "
       "with V, then F/V and K at the ends of words. TH (“tongue peek”) moves to a later week.</p>")
