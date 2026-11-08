from lib import *
from core_common import mc, qs, mark_list

TIER = {"Titus": "A", "Nariah": "A", "Naomi": "B", "Nevaeh": "C", "Nylah": "C"}
NAMES = ["Kitchen Science Lab", "Artist Study", "Musician Study", "Life Skills Club", "PE Day"]
TOPIC = ["Dancing Raisins", "Claude Monet · Water Lilies", "J. S. Bach · Soli Deo Gloria", "Emergency Ready: 9-1-1", "Backyard Relay Races"]
VID = [yt("EL dancing raisins experiment"), yt("EL how to draw Monet water lilies"),
       yt("EL Bach Jesu Joy of Man's Desiring"), yt("EL learn about 911 Emergency Ernie"), yt("EL PE relay races")]
VID2 = [None, yt("EL Claude Monet for kids"), yt("EL meet Bach for kids"), yt("EL kids safety when to call 911"), None]

def qrs(i):
    q = qr_box(VID[i], ["Experiment video", "Draw-along", "Listen here", "911 video", "Relay ideas"][i], 64)
    if VID2[i]:
        q += qr_box(VID2[i], ["", "Monet's story", "Bach's story", "When to call", ""][i], 64)
    return f'<div class="qrrow">{q}</div>'

def el_page(name, i):
    T = TIER[name]
    head = f'<div class="flexrow"><div class="learn grow">{{}}</div>{qrs(i)}</div>'
    if i == 0:
        if T == "A":
            body = (head.format('<p class="big">Drop raisins into a cup of clear soda. Watch… do they sink, float, or DANCE?! Then try raisins in plain water.</p>')
                    + '<div class="grid2"><div><div class="lab">1. Raisins in WATER — draw it!</div><div class="answer-space" style="min-height:280px"></div></div>'
                      '<div><div class="lab">2. Raisins in SODA — draw it!</div><div class="answer-space" style="min-height:280px"></div></div></div>'
                    + mc("In the soda, the raisins…", ["went up and down — they danced!", "stayed still", "turned into grapes"], 1)
                    + mc("What do you see on the raisins in the soda?", ["little bubbles", "nothing"], 2)
                    + '<div class="lab">Trace:</div>' + trace_line("bubbles", 50, 1))
        else:
            sci = ('<p><b>Why it works:</b> soda is full of dissolved <b>carbon dioxide</b> gas. A raisin is denser than the soda, so it sinks. But its wrinkly surface gives the gas '
                   'lots of spots to form bubbles. When enough bubbles stick, they act like tiny life jackets — the raisin\'s overall density drops below the soda\'s and it rises '
                   '(<b>buoyancy</b>). At the top the bubbles pop into the air, the raisin gets denser again, and down it goes. It keeps “dancing” until the soda goes flat.</p>')
            body = (head.format('<p><b>Materials:</b> 2 clear glasses, clear soda (lemon-lime or club soda), plain water, 6–8 raisins per glass.</p>'
                                + (sci if T == "C" else '<p>Bubbles of <b>carbon dioxide</b> gas stick to the wrinkly raisins and lift them up like balloons. At the top the bubbles pop, and the raisins sink again!</p>'))
                    + '<div><span class="lab">Question:</span> What will raisins do in soda compared with water?</div>'
                    + '<div><span class="lab">Hypothesis:</span> I think…' + lines(2) + '</div>'
                    + '<div><span class="lab">Observations:</span> draw both glasses after 2 minutes.</div><div class="answer-space" style="min-height:130px"></div>'
                    + qs([("What gas makes the bubbles in soda?", ["carbon dioxide", "oxygen", "steam"]),
                          ("Why did the raisins in plain water stay on the bottom?", ["There were no gas bubbles to lift them.", "The water was too cold.", "Raisins hate water."])], 1)
                    + ('<div><span class="lab">Test a variable:</span> try a smooth food (a corn kernel or a piece of pasta) next to a raisin. Which danced more? Use the word <i>density</i> to explain.' + lines(3) + '</div>'
                       if T == "C" else '<div><span class="lab">Conclusion:</span> Why did the raisins dance?' + lines(2) + '</div>'))
    elif i == 1:
        bio = ('<p><b>Claude Monet</b> (1840–1926) was a French painter and a leader of <b>Impressionism</b> — painting quick, loose brushstrokes to capture light and color in a '
               'moment instead of every tiny detail. His painting <i>Impression, Sunrise</i> (1872) gave the movement its name. At his home in Giverny he dug a pond, built a '
               'Japanese-style bridge, and planted <b>water lilies</b> — then painted them about 250 times, in morning light, afternoon light, and evening light!</p>')
        if T == "A":
            body = (head.format('<p class="big">Monet loved to paint his pond full of <b>water lilies</b> — flat round leaves (lily pads) with flowers on top. Let\'s draw them with the video!</p>')
                    + '<div class="lab">Draw-along: blue and purple water first, then green lily pads, then pink flowers. Use crayons or oil pastels and smudge with your finger like Monet\'s soft colors!</div>'
                    + '<div class="answer-space" style="min-height:520px"></div>'
                    + mc("What did Monet love to paint?", ["water lilies", "race cars", "dinosaurs"]))
        else:
            body = (head.format(bio)
                    + qs([("What does an Impressionist painter try to capture?", ["light and color in a moment", "every tiny detail, like a photo", "only people's faces"]),
                          ("Why did Monet paint the same pond again and again?", 2)], 1)
                    + '<div class="lab">Draw-along: your own water-lily pond. Water first (blues and purples, side-to-side strokes), then lily pads, then flowers. '
                      'Smudge or blend for soft light. Add the bridge if you like.</div>'
                    + '<div class="answer-space" style="min-height:330px"></div>'
                    + ('<div>Title your piece. What time of day is your light, and how did you show it with color?' + lines(2) + '</div>' if T == "C" else '<div>My art is called: <span class="blank-ln" style="min-width:250px"></span></div>'))
    elif i == 2:
        bio = ('<p><b>Johann Sebastian Bach</b> (1685–1750) was a German composer of the <b>Baroque</b> era and one of the greatest musicians who ever lived. For his last 27 years he '
               'led the music at St. Thomas Church in Leipzig, writing new music for worship almost every week. Bach often wrote <b>“S.D.G.”</b> at the end of his music — '
               '<i>Soli Deo Gloria</i>, “To God alone be the glory.” His “Jesu, Joy of Man\'s Desiring” comes from a church cantata (1723). Bach and his two wives had 20 children, '
               'and several of his sons became famous composers too.</p>')
        if T == "A":
            body = (head.format('<p class="big">Bach wrote beautiful music for church. He wrote <b>S.D.G.</b> on his music — it means “To God alone be the glory!”</p>')
                    + '<div class="lab">Draw what the music makes you think of while it plays.</div><div class="answer-space" style="min-height:360px"></div>'
                    + '<div class="big">The music was: <span class="chk"></span>fast <span class="chk"></span>slow &nbsp;&nbsp; <span class="chk"></span>loud <span class="chk"></span>soft</div>'
                    + '<div class="lab">Trace Bach\'s letters:</div>' + trace_line("S.D.G.", 52, 3))
        else:
            body = (head.format(bio)
                    + '<table class="t"><tr><th>Listen to</th><th>Fast or slow?</th><th>Loud or soft?</th><th>Instruments I hear / how it makes me feel</th></tr>'
                    + "".join(f"<tr><td>{s}</td><td></td><td></td><td style='height:52px'></td></tr>" for s in ["Jesu, Joy of Man's Desiring", "Air (from Orchestral Suite No. 3)", "Brandenburg Concerto No. 3, 1st movement"]) + '</table>'
                    + qs([("What does “Soli Deo Gloria” mean?", ["To God alone be the glory", "Music is my life", "The end of the song"]),
                          ("Bach lived during which era of music?", ["Baroque", "Romantic", "Modern"])], 1)
                    + ('<div>Bach did his work for God\'s glory. What would it look like to do your schoolwork “for God\'s glory” (1 Corinthians 10:31)?' + lines(3) + '</div>' if T == "C"
                       else '<div>Write S.D.G. at the bottom of your best paper today! What could you do this week to give God the glory?' + lines(2) + '</div>'))
    elif i == 3:
        card = ('<div class="box"><div class="lab">My Emergency Card (fill in with Mom — keep it by the phone, not on the tablet)</div>'
                + "".join(f'<div style="margin:5px 0">{t} <span class="blank-ln" style="min-width:360px"></span></div>' for t in
                          ["My full name:", "My parents' names:", "My street address:", "City, state, ZIP:", "Mom's or Dad's phone:", "Our family meeting spot outside:"]) + '</div>')
        if T == "A":
            body = (head.format('<p class="big">In a real emergency — a fire, or someone is hurt and can\'t wake up — a grown-up (or you!) calls <b>9-1-1</b>. '
                                'Never call 9-1-1 for fun. Let\'s learn our address so helpers can find us!</p>')
                    + '<div class="lab">Trace the numbers:</div>' + trace_line("911", 64, 4)
                    + '<div class="lab">Mom reads. Is it a 9-1-1 emergency?</div>'
                    + mc("The house is on fire!", ["Yes — call 9-1-1", "No"], 1)
                    + mc("My toy is lost.", ["No — tell Mom", "Yes — call 9-1-1"], 2)
                    + mc("Grandpa fell and won't wake up.", ["Yes — call 9-1-1", "No"], 3)
                    + mc("I scraped my knee.", ["No — tell Mom", "Yes — call 9-1-1"], 4)
                    + '<div class="big">Practice with Mom: say your full name <span class="star">☆</span> &nbsp; your street <span class="star">☆</span> &nbsp; Mom\'s name <span class="star">☆</span></div>'
                    + '<div class="lab">Draw a helper who comes when you call 9-1-1 (firefighter, paramedic, police officer):</div><div class="answer-space"></div>')
        else:
            body = (head.format('<p>9-1-1 is for emergencies only: a fire, someone badly hurt or not breathing, a crime or danger happening right now. On the call: stay calm, say '
                                '<b>what</b> is happening and <b>where</b> (your address), answer the dispatcher\'s questions, and <b>don\'t hang up</b> until they tell you to. '
                                'If there\'s a fire: get out, stay out, and go to the family meeting spot.</p>'
                                + ('<p>Some areas also let you text 9-1-1 if it isn\'t safe to talk — but calling is always best when you can.</p>' if T == "C" else ''))
                    + '<div class="lab">Emergency (E) or not an emergency (N)?</div>'
                    + mark_list(["Smoke is coming from the kitchen.", "The internet is down.", "A sibling is choking and can't breathe.", "A stranger is trying to break in.",
                                 "I can't find my shoes.", "Someone fell and is bleeding a lot."], ["E", "N"], 1)
                    + qs([("What should you do before you hang up?", ["Wait until the dispatcher says it's OK.", "Hang up right after saying “help.”", "Call a friend first."])], 7)
                    + card
                    + ('<div>Plan it: what are two ways out of our house if there is a fire?' + lines(2) + '</div>' if T == "C" else ''))
    else:
        races = [("Running relay", "run to the cone and back, tag the next runner"), ("Spoon relay", "carry a potato or ball on a spoon — drop it, start over"),
                 ("Sack hop", "hop inside a pillowcase"), ("Crab-walk relay", "tummy up, hands and feet"), ("Wheelbarrow", "partner holds your ankles; walk on your hands"),
                 ("Backwards walk", "walk backwards — no peeking!"), ("Ball-between-knees", "squeeze a ball between your knees and waddle")]
        if T == "A":
            body = (head.format('<p class="big">Relay race day! Run your part, then <b>tag</b> your teammate. Cheer for everybody! Color a medal when you finish each race.</p>')
                    + '<table class="t" style="font-size:14pt">' + "".join(f"<tr><td><b>{m}</b><div class='small'>{h}</div></td><td class='center'><span class='star' style='font-size:24pt'>✪</span></td></tr>" for m, h in races) + '</table>'
                    + mc("When your turn is done, you…", ["tag your teammate", "sit down and stop", "run away"], 1)
                    + '<div class="lab">My favorite race was:</div><div class="ln"></div>')
        else:
            body = (head.format('<p>Make two teams (big kids pair up with littles). Each race: one runner at a time goes to the cone and back, then tags the next teammate. '
                                'Time each team. Water break between races!' + (' Good sportsmanship counts: “let us run with endurance the race that is set before us” (Hebrews 12:1).' if T == "C" else '') + '</p>')
                    + '<table class="t"><tr><th>Race</th><th>How</th><th>Team 1 time</th><th>Team 2 time</th></tr>'
                    + "".join(f"<tr><td><b>{m}</b></td><td>{h}</td><td style='width:80px'></td><td style='width:80px'></td></tr>" for m, h in races) + '</table>'
                    + qs([("What makes a relay team fast?", ["quick, clean tags and everyone doing their part", "one fast runner doing everything", "skipping the hard races"])], 1)
                    + ('<div>Which race was hardest for your team, and what would you change next time? How did you show good sportsmanship?' + lines(3) + '</div>' if T == "C" else
                       '<div>Which race was hardest? Why?' + lines(2) + '</div>'))
    return page(name, i, "Fun Electives", f"{NAMES[i]} · {TOPIC[i]}", body)

MATERIALS = ("<b>Tue:</b> clear soda (lemon-lime or club soda), raisins, 2 clear glasses per group, water (Tier C: a few corn kernels or pasta pieces). "
             "<b>Wed:</b> white paper or cardstock, crayons or oil pastels (blues, purples, greens, pinks). "
             "<b>Thu:</b> just the QR music. <b>Fri:</b> nothing to buy — fill in the Emergency Cards together. "
             "<b>Sat:</b> backyard, 2 cones or shoes for markers, a spoon + potato/ball, pillowcases, a ball, timer, water bottles.")

KEY = ("<b>Tue:</b> A: they danced · little bubbles. B/C: 1 carbon dioxide, 2 there were no gas bubbles to lift them. "
       "<b>Wed:</b> A: water lilies. B/C: 1 light and color in a moment; 2 to capture how the light and colors changed at different times/seasons. "
       "<b>Thu:</b> B/C: 1 To God alone be the glory, 2 Baroque. "
       "<b>Fri:</b> A: yes, no (tell Mom), yes, no (tell Mom). B/C: E, N, E, E, N, E; 7 wait until the dispatcher says it's OK. "
       "<b>Sat:</b> A: tag your teammate. B/C: 1 quick, clean tags and everyone doing their part.")
