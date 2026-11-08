# Mom's teaching plans for the subjects taught together.
from lib import *
import geography, electives, speech, mult

def tv(vids):
    vids = [(u, l) for u, l in vids if u]
    if not vids: return ""
    return ("<div class='tvrow' style='float:right;display:flex;gap:6px;margin:0 0 4px 8px'>"
            + "".join(qr_box(u, "TV: " + l, 50) for u, l in vids) + "</div>")

def block(title, color, rows, vids=()):
    body = "".join(f"<div style='margin:2px 0'><b>{k}:</b> {v}</div>" for k, v in rows)
    return (f"<div class='box' style='padding:6px 10px;border-left:5px solid {color};overflow:hidden'>{tv(vids)}"
            f"<div class='lab' style='color:{color}'>{title}</div>{body}</div>")

GEO = [
 [("Goal", "Everyone can name and picture 5 landforms: mountain, hill, plain, valley, plateau."),
  ("Gather", "Play-dough or a pile of pillows/blankets, globe or atlas, dot markers for Titus & Nariah."),
  ("Teach (5 min)", "Build the landforms together out of play-dough (or pillows under a blanket): a tall pointy mountain, a low round hill, a flat plain, "
   "a valley between two mountains, and a plateau with a flat top. Say each word as you build it. God made the land in all these shapes!"),
  ("Do together", "Point and say: kids race to touch the one you name. Ask: which is Florida mostly like? (plains — very flat!)"),
  ("Worksheets", "Tier A (Titus & Nariah): 3 tap questions, dot the mountain and hill tops, trace “hill.” Tier B (Naomi) & C (Nevaeh, Nylah): label the pictures + questions; C adds U.S. examples and erosion."),
  ("Ask", "If you could climb any landform, which would it be and why?")],
 [("Goal", "Tell apart river, lake, ocean, bay and gulf; know fresh water from salt water."),
  ("Gather", "Two cups of water — stir salt into one (taste test!), the play-dough landforms from yesterday, blue crayons."),
  ("Teach (5 min)", "Taste test: which water is like the ocean? (salty) Rivers and most lakes are fresh. Pour a little water down a play-dough “valley” — that's a river! "
   "It starts at its source and ends at its mouth. Show a bay: water that curves into the land."),
  ("Do together", "Find the St. Johns River on a map — it runs right through Jacksonville into the Atlantic. Fresh or salt? (Fresh, but salty near the ocean.)"),
  ("Worksheets", "Tier A: color the water, 3 tap questions, trace “lake.” Tier B/C: label pictures, F/S sort; Tier C adds the Great Salt Lake question."),
  ("Ask", "Why do you think people build towns next to rivers?")],
 [("Goal", "Island, peninsula, isthmus — and Florida is a peninsula!"),
  ("Gather", "A shallow pan of water and play-dough (or a plate with blue paper), a Florida map or atlas."),
  ("Teach (5 min)", "In the pan, make an island (water all around), a peninsula (land connected on one side, water on 3 sides), and an isthmus (a skinny land bridge between two big pieces). "
   "Then show Florida on the map: water on 3 sides — a peninsula!"),
  ("Do together", "Find on the globe: Hawaii (islands), Italy (peninsula, shaped like a boot), Panama (isthmus joining North & South America)."),
  ("Worksheets", "Tier A: color the Florida map, 2 tap questions. Tier B/C: label pictures + questions; Tier C adds how being a peninsula affects Florida."),
  ("Ask", "Would you rather live on an island or a peninsula? Why?")],
 [("Goal", "Find the world's great rivers and mountains on a map."),
  ("Gather", "Globe or atlas world map, a string or yarn (to “measure” rivers)."),
  ("Teach (5 min)", "Show Mount Everest in the Himalayas (Asia) — the highest mountain, about 29,032 feet (about 5½ miles up!). Trace the Nile (Africa, longest river) "
   "and the Amazon (South America, carries the most water). Then find the Mississippi, the Rockies, and the Andes."),
  ("Do together", "Lay yarn along the Nile and the Mississippi on the globe — which is longer? (the Nile)"),
  ("Worksheets", "Tier A: dot the mountains, trace the rivers, 1 tap question, draw a mountain with a river. Tier B/C: match numbers 1–6; C adds two questions."),
  ("Ask", "What do you think it's like on top of Mount Everest? (cold, windy, little air)")],
 [("Goal", "Florida's land and water + week review."),
  ("Gather", "Globe, atlas, a Florida map if you have one."),
  ("Teach (5 min)", "Florida is a flat peninsula — its highest point, Britton Hill, is only 345 feet! Trace the St. Johns River: it flows NORTH (one of the few big U.S. rivers that does) "
   "and meets the Atlantic near Jacksonville. Find Lake Okeechobee, Florida's biggest lake."),
  ("Do together", "Review game: call out a word (mountain, peninsula, island, river, plateau, bay) — the kids make it with their hands or point to it on the globe."),
  ("Worksheets", "Tier A: trace the river, review taps, show-me checklist. Tier B/C: Florida map letters + review (8 of 10 to pass)."),
  ("Ask", "Week 3 done! Next week: weather & climate. Which landform or body of water was your favorite?")],
]

EL = [
 [("Gather", "2 clear glasses per group, clear soda (lemon-lime or club soda — freshly opened), plain water, raisins (Tier C: a few corn kernels or pasta pieces)."),
  ("Before", "Ask: what will raisins do in soda? In water? Everyone predicts (Tier A draws it)."),
  ("Steps", "1) Fill one glass with water and one with soda. 2) Drop 6–8 raisins into each. 3) Watch for 2 minutes — look at the bubbles collecting on the soda raisins. "
   "4) Record. 5) Tier C: add a smooth food to test whether the wrinkles matter."),
  ("Explain", "Soda has carbon dioxide gas dissolved in it. Bubbles grab onto the wrinkly raisins like little life jackets and float them up. At the top the bubbles pop, "
   "the raisins sink — and they repeat until the soda goes flat. In water there's no gas, so they just sit."),
  ("Tiers", "A: draw both glasses, 2 taps, trace “bubbles.” B: hypothesis, observations, 2 taps, conclusion. C: full explanation (density, buoyancy) + variable test.")],
 [("Gather", "White paper or cardstock, crayons or oil pastels (blues, purples, greens, pinks), paper towels for smudging. The draw-along video is the TV link up top."),
  ("Before", "Play the Monet story video. Show a Water Lilies painting (search “Monet Water Lilies” in a museum site or book) — ask: is it sharp like a photo or soft and blurry? Why?"),
  ("Steps", "1) Water first: side-to-side strokes of blue and purple. 2) Lily pads: green ovals with a little notch. 3) Flowers: pink and white petals on a few pads. "
   "4) Smudge with a finger or towel for soft light. 5) Optional: add the Japanese bridge across the top."),
  ("Talk about", "Impressionists painted light and color in a moment. Monet painted his pond about 250 times because the light kept changing — God's world looks new every hour!"),
  ("Tiers", "A: draw-along + 1 tap. B: 2 questions + pond + title. C: same plus explaining time of day / light.")],
 [("Gather", "The music video (TV link up top). Optional: scarves for the littles."),
  ("Before", "Tell Bach's story in 1 minute (or play the “Meet Bach” video). Show them S.D.G. — “To God alone be the glory.” Remind them it's the same idea as our “All For His Glory.”"),
  ("Steps", "1) Play “Jesu, Joy of Man's Desiring” — eyes closed. Ask: is it fast or slow? Can you hum the flowing notes? 2) Play it again: littles draw, big kids fill in the "
   "listening table. 3) Big kids look up and listen to “Air (on the G String)” and Brandenburg Concerto No. 3 if time allows."),
  ("Fun fact", "Bach had 20 children, and many of his musical sons became composers too. He wrote new music for church nearly every week in Leipzig."),
  ("Tiers", "A: draw to the music, fast/slow & loud/soft, trace S.D.G. B: listening table + 2 taps + S.D.G. at the bottom of their best paper. C: same + 1 Corinthians 10:31 reflection.")],
 [("Gather", "Your phone (powered OFF or in airplane mode for practice!), pencils. Have each kid's Emergency Card filled in with your real address and phone — keep the cards by the phone, not on the tablets."),
  ("Before", "Watch the Emergency Ernie video. Ask: what is an emergency? What is NOT an emergency?"),
  ("Steps", "1) Sort the emergencies together. 2) Role-play a 9-1-1 call with the phone OFF: you are the dispatcher — “9-1-1, what is your emergency? What is your address?” "
   "3) Each kid practices saying their full name, address and a parent's phone number. 4) Walk outside to pick a family meeting spot (mailbox, a tree) for a fire."),
  ("Tiers", "A: trace 911, 4 taps, say name/street/Mom's name, draw a helper. B: E/N sort, tap question, Emergency Card. C: same + two ways out of the house.")],
 [("Gather", "Backyard, 2 cones (or shoes) as markers, a spoon and potato or small ball, pillowcases, a ball, timer, water bottles."),
  ("Before", "Warm up: 20 jumping jacks, high knees, arm circles. Make 2 teams — pair big kids with littles so it's fair."),
  ("Steps", "Run each relay: running, spoon, sack hop, crab walk, wheelbarrow (big kid holds a little's ankles gently), backwards walk, ball-between-knees. "
   "Time each team. Water break every 2 races. Cheer for both teams!"),
  ("Cool down", "Slow walk around the yard, then stretch. Talk about good sportsmanship: shake hands, “good game,” encourage each other."),
  ("Tiers", "A: medal checklist + 1 tap + favorite race. B: time table + tap + hardest race. C: time table + sportsmanship reflection (Hebrews 12:1).")],
]

MULT = [
 "Chant the 3s table together 3 times (clap on each answer). Cover it and go around the room — each kid says the next fact. Then pages. Titus & Nayeli: count by 2s and dot the 2s on 1–20.",
 "Chant the 4s table 3 times. Quick oral quiz: you say “4 times 7,” they shout the answer. Drill the tricky ones (4×6, 4×7, 4×8). Then pages. Titus & Nayeli: pairs of socks by 2s.",
 "Chant both tables once. Flash-card round with 0s, 1s, 2s, 3s, 4s, 5s, 10s. Then the 30-fact page — have them circle and re-write any they hesitated on. Titus & Nayeli: froggy hops by 2s.",
 "Read the word problems out loud together for Nariah. Then time the 2-minute speed drill and write the time on the page. Titus & Nayeli: review 2s, 5s, 10s with counting bears.",
 "Checkpoint: 40 facts, 4 minutes. 32+ = pass. Note any missed facts for Monday practice. Titus & Nayeli: dot-to-dot by 2s, then count to 20 by 2s, 50 by 5s, and 100 by 10s for you.",
]

SPEECH = [
 "Mouth Gym (1 min). Teach the tongue peek: tongue tip just between the teeth, blow air — “thhh.” Use the mirror so they can see it. Go down the quiet TH list (thumb, think…); color a star for each good one. Listen for “f” (“fumb”).",
 "Mouth Gym. Buzzy TH: same tongue peek, voice on — hands on throats to feel the buzz. Little words: the, this, that, they. Listen for “d” (“dis,” “dat”).",
 "Mouth Gym. TH at the end: bath, tooth, mouth. Stretch the last sound and keep the tongue peeking. Listen for “f” at the end (“baf,” “toof”). Point-and-say game: tooth, teeth, mouth, thumb.",
 "Mouth Gym. Phrases — slow and clear. Nariah reads the sentences; Titus & Nayeli echo after you. Praise effort, not just perfect sounds.",
 "Game day! Roll and move; say the word on the square. Fill in your check at the bottom: which TH sounds are solid, which need more practice next week.",
]

def day_plan(i):
    d, wd, dt = DAYS[i]
    return ("<div class='small'>Order of the day for together subjects: Multiplication → Speech → Geography → Elective. About 10–15 minutes each.</div>"
            + block(f"Multiplication Mastery · {mult.TITLES[i]}", "#6d28d9", [("Plan", MULT[i])],
                    ([(mult.VID[i], "Song")] if i < 4 else []) + [(mult.VIDSC[i], "Skip count")])
            + block(f"Speech Stars · {speech.TITLES[i]} (Nariah, Titus, Nayeli)", "#a21caf", [("Plan", SPEECH[i])], [(speech.VID[i], "Watch & copy")])
            + block(f"Geography · {geography.TITLES[i]}", "#2f5bd3", GEO[i], [(geography.VID[i], "Geography")])
            + block(f"{electives.NAMES[i]} · {electives.TOPIC[i]}", "#b02fc9", EL[i], [(electives.VID[i], "Video"), (electives.VID2[i], "Story")]))
