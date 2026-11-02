from lib import *

TIER = {"Titus": "A", "Nariah": "A", "Naomi": "B", "Nevaeh": "C", "Nylah": "C"}
NAMES = ["Kitchen Science Lab", "Artist Study", "Musician Study", "Life Skills Club", "PE Day"]
TOPIC = ["Magic Milk", "Henri Matisse · Painting with Scissors", "Tchaikovsky · The Nutcracker", "Thank-You Notes & Envelopes", "Animal Walk Olympics"]
VID = [yt("magic milk experiment for kids"), yt("Matisse cut outs art lesson for kids"),
       yt("Dance of the Sugar Plum Fairy Tchaikovsky"), yt("how to address an envelope for kids"), yt("animal walks exercise for kids")]
VID2 = [None, yt("Henri Matisse for kids biography"), yt("Nutcracker story for kids"), yt("how to write a thank you note for kids"), None]

def qrs(i):
    q = qr_box(VID[i], ["Experiment video", "Art lesson", "Listen here", "How-to video", "Animal walks"][i], 64)
    if VID2[i]:
        q += qr_box(VID2[i], ["", "Matisse's story", "Nutcracker story", "Thank-you notes", ""][i], 64)
    return f'<div class="qrrow">{q}</div>'

def el_page(name, i):
    T = TIER[name]
    head = f'<div class="flexrow"><div class="learn grow">{{}}</div>{qrs(i)}</div>'
    if i == 0:
        if T == "A":
            body = (head.format('<p class="big">Pour milk on a plate. Add drops of food coloring. Touch the middle with a soapy cotton swab… what happens?!</p>')
                    + '<div class="grid2"><div><div class="lab">1. I think the colors will…</div><div class="answer-space" style="min-height:300px"></div></div>'
                      '<div><div class="lab">2. Draw what REALLY happened!</div><div class="answer-space" style="min-height:300px"></div></div></div>'
                    + '<div class="big">The colors moved: &nbsp; <span class="chk"></span>slow &nbsp; <span class="chk"></span>FAST &nbsp; <span class="chk"></span>not at all</div>'
                    + '<div class="lab">Trace:</div>' + trace_line("milk", 50, 2))
        else:
            sci = ('<p><b>Why it works:</b> milk is mostly water with tiny bits of fat and protein floating in it. The surface of the milk is pulled tight '
                   'like a stretched skin — that\'s <b>surface tension</b>. Soap weakens that pull right where it touches, so the tighter surface around it '
                   'yanks outward, dragging the colors. Soap molecules also grab onto fat, and as they chase the fat around, the swirling keeps going.</p>')
            body = (head.format('<p><b>Materials:</b> a shallow plate, milk (whole works best), food coloring, dish soap, cotton swabs.</p>'
                                + (sci if T == "C" else '<p>Soap breaks the milk\'s <b>surface tension</b> — the invisible “skin” on top — and the colors race away!</p>'))
                    + '<div><span class="lab">Question:</span> What will happen when soap touches the milk?</div>'
                    + '<div><span class="lab">Hypothesis:</span> I think…' + lines(2) + '</div>'
                    + '<div><span class="lab">Observations:</span> draw and describe what you saw.</div><div class="answer-space" style="min-height:150px"></div>'
                    + ('<div><span class="lab">Test a variable:</span> try skim milk or water instead of whole milk. Which swirled the most? Why do you think so?' + lines(3) + '</div>'
                       if T == "C" else '<div><span class="lab">Conclusion:</span> Why did the colors move?' + lines(2) + '</div>'))
    elif i == 1:
        bio = ('<p><b>Henri Matisse</b> (1869–1954) was a French artist famous for bold, bright colors. Late in life, after a serious illness, he often '
               'couldn\'t stand at an easel — so he invented a new way to make art. Assistants painted big sheets of paper, and Matisse “drew with scissors,” '
               'cutting out leaves, stars, swirls and wavy shapes, then arranging them on the wall. He called them <b>cut-outs</b>. One famous one, '
               '<i>The Snail</i> (1953), is a spiral of colorful paper rectangles.</p>')
        if T == "A":
            body = (head.format('<p class="big">Matisse was an artist who made pictures with <b>scissors</b>! He cut out fun shapes and glued them down.</p>')
                    + '<div class="lab">Cut out shapes from colored paper (leaves, stars, squiggles!) and glue them in the box. Make a snail spiral if you want!</div>'
                    + '<div class="answer-space" style="min-height:560px"></div>')
        else:
            body = (head.format(bio)
                    + '<div class="grid2"><div>Why did Matisse start making cut-outs?' + lines(2) + '</div><div>What is an “organic” shape (like a leaf) vs. a “geometric” shape (like a square)? Draw one of each.<div class="answer-space" style="min-height:60px"></div></div></div>'
                    + '<div class="lab">Your cut-out: use painted or colored paper, cut at least 8 shapes, arrange them before you glue. Glue it here or on cardstock.</div>'
                    + '<div class="answer-space" style="min-height:300px"></div>'
                    + ('<div>Title your piece and explain one choice you made about color or placement:' + lines(2) + '</div>' if T == "C" else '<div>My art is called: <span class="blank-ln" style="min-width:250px"></span></div>'))
    elif i == 2:
        bio = ('<p><b>Pyotr Ilyich Tchaikovsky</b> (1840–1893) was a Russian composer. His ballet <b>The Nutcracker</b> (1892) tells of a girl named Clara '
               'whose Christmas gift, a nutcracker, comes to life, defeats the Mouse King, and takes her to the Land of Sweets. In the “Dance of the Sugar Plum '
               'Fairy” you hear the <b>celesta</b> — a keyboard instrument whose hammers strike metal bars for a twinkly, music-box sound. '
               'Tchaikovsky discovered it in Paris and kept it secret so other composers wouldn\'t use it first!</p>')
        if T == "A":
            body = (head.format('<p class="big">Tchaikovsky wrote music for <b>The Nutcracker</b>. Listen to the “Sugar Plum Fairy” — it sounds like twinkly bells!</p>')
                    + '<div class="lab">Draw what the music makes you think of while it plays.</div><div class="answer-space" style="min-height:420px"></div>'
                    + '<div class="big">The music was: <span class="chk"></span>fast <span class="chk"></span>slow &nbsp;&nbsp; <span class="chk"></span>loud <span class="chk"></span>soft</div>'
                    + '<div class="big">Tiptoe like a fairy while it plays again! <span class="star">☆</span></div>')
        else:
            body = (head.format(bio)
                    + '<table class="t"><tr><th>Listen to</th><th>Fast or slow?</th><th>Loud or soft?</th><th>Instruments I hear / how it makes me feel</th></tr>'
                    + "".join(f"<tr><td>{s}</td><td></td><td></td><td style='height:52px'></td></tr>" for s in ["Dance of the Sugar Plum Fairy", "Russian Dance (Trepak)", "Waltz of the Flowers"]) + '</table>'
                    + '<div>What is a celesta, and why did Tchaikovsky keep it a secret?' + lines(2) + '</div>'
                    + ('<div>A ballet tells a story without words. How does the music help tell the story? Give one example.' + lines(3) + '</div>' if T == "C"
                       else '<div>Draw the Land of Sweets.<div class="answer-space" style="min-height:120px"></div></div>'))
    elif i == 3:
        env = ('<svg width="460" height="230" style="align-self:center"><rect x="2" y="2" width="456" height="226" rx="6" fill="#fff" stroke="#1f2a5c" stroke-width="2"/>'
               '<rect x="388" y="14" width="56" height="62" fill="none" stroke="#a21caf" stroke-dasharray="4,3" stroke-width="2"/><text x="416" y="50" font-size="11" text-anchor="middle" fill="#a21caf">stamp</text>'
               + "".join(f'<line x1="16" x2="170" y1="{24+k*20}" y2="{24+k*20}" stroke="#9aa0bb"/>' for k in range(3))
               + '<text x="16" y="88" font-size="10" fill="#555566">your (return) address</text>'
               + "".join(f'<line x1="150" x2="380" y1="{124+k*28}" y2="{124+k*28}" stroke="#9aa0bb"/>' for k in range(3))
               + '<text x="150" y="210" font-size="10" fill="#555566">who it goes to: name · street · city, state ZIP</text></svg>')
        if T == "A":
            body = (head.format('<p class="big">When someone is kind to us, we say <b>thank you</b>! Let\'s make a thank-you card for someone special.</p>')
                    + '<div class="lab">Trace:</div>' + trace_line("Thank you", 50, 1)
                    + '<div class="lab">Who is your card for? Mom writes their name:</div><div class="ln"></div>'
                    + '<div class="lab">Draw a picture for them!</div><div class="answer-space" style="min-height:360px"></div>'
                    + '<div class="lab">Trace your name to sign it:</div>' + trace_line(name, 46, 1))
        else:
            parts = ["Greeting — Dear ___,", "Thank them for the specific gift or kindness", "Say how you used it or why it mattered",
                     "Add a kind sentence about them", "Closing — Love, / Sincerely, and your name"]
            body = (head.format('<p>A handwritten thank-you note is a lost art — and people keep them for years! A good note has five parts and fits on one small card.</p>'
                                + ('<p>Addresses go in the center of the envelope; your return address goes top left; the stamp goes top right. '
                                   'Use the two-letter state abbreviation (FL) and the ZIP code. Formal titles: Mr., Mrs., Ms., Dr., Pastor.</p>' if T == "C" else ''))
                    + '<div class="lab">The 5 parts:</div>' + ol([esc(p) for p in parts])
                    + '<div class="lab">Draft your note here, then copy it onto a real card:</div>' + lines(7)
                    + '<div class="lab">Practice addressing this envelope (use a real person!):</div>' + env)
    else:
        moves = [("Bear crawl", "hands & feet, hips high", "across the yard"), ("Crab walk", "tummy up, walk on hands & feet", "across the yard"),
                 ("Frog jumps", "squat low, leap forward", "10 jumps"), ("Inchworm", "walk hands out to plank, walk feet in", "5 times"),
                 ("Flamingo balance", "stand on one foot", "count how long!"), ("Kangaroo hops", "feet together, big hops", "15 hops"),
                 ("Bunny hops", "tiny quick hops", "20 hops"), ("Gorilla shuffle", "squat, knuckles down, shuffle sideways", "across & back")]
        if T == "A":
            body = (head.format('<p class="big">Today we move like ANIMALS! Mom calls out an animal — you do the walk. Color a medal when you finish each one!</p>')
                    + '<table class="t" style="font-size:14pt">' + "".join(f"<tr><td><b>{m}</b><div class='small'>{h}</div></td><td>{d}</td><td class='center'><span class='star' style='font-size:24pt'>✪</span></td></tr>" for m, h, d in moves) + '</table>'
                    + '<div class="lab">My favorite animal walk was:</div><div class="ln"></div>')
        else:
            body = (head.format('<p>Animal walks build strength, balance, and coordination — no equipment needed. Run the Olympics in the backyard: each event, try to beat your first score '
                                'on round 2. Water break between rounds!' + (' Take your pulse (count 15 seconds × 4) before and after the round.' if T == "C" else '') + '</p>')
                    + '<table class="t"><tr><th>Event</th><th>How</th><th>Goal</th><th>Round 1</th><th>Round 2</th></tr>'
                    + "".join(f"<tr><td><b>{m}</b></td><td>{h}</td><td>{d}</td><td style='width:70px'></td><td style='width:70px'></td></tr>" for m, h, d in moves) + '</table>'
                    + ('<div class="grid2"><div>Heart rate before: ______ bpm</div><div>Heart rate after: ______ bpm</div></div>'
                       '<div>Which animal walk was hardest? Which muscles did it work?' + lines(2) + '</div>' if T == "C" else
                       '<div>Which animal walk was hardest? Why?' + lines(2) + '</div>'))
    return page(name, i, "Fun Electives", f"{NAMES[i]} · {TOPIC[i]}", body)

MATERIALS = ("<b>Tue:</b> milk (whole is best), shallow plates, food coloring, dish soap, cotton swabs. "
             "<b>Wed:</b> colored or kid-painted paper, scissors, glue sticks, cardstock. "
             "<b>Thu:</b> just the QR music. <b>Fri:</b> blank cards or folded paper, envelopes, stamps if mailing. "
             "<b>Sat:</b> backyard, timer, water bottles.")
