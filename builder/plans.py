# Mom's teaching plans for the subjects taught together.
from lib import *
import geography, electives, speech, mult

def block(title, color, rows):
    body = "".join(f"<div style='margin:2px 0'><b>{k}:</b> {v}</div>" for k, v in rows)
    return f"<div class='box' style='padding:6px 10px;border-left:5px solid {color}'><div class='lab' style='color:{color}'>{title}</div>{body}</div>"

GEO = [
 [("Goal", "Everyone can name and point to the 7 continents."),
  ("Gather", "Globe, atlas, the Geography page for each kid, dot markers for Titus & Nariah."),
  ("Teach (5 min)", "Spin the globe: “Land or water?” Explain a continent is a giant piece of land. Point to each continent and say its name together "
   "(North America, South America, Europe, Asia, Africa, Australia, Antarctica). Point out that Europe and Asia are one big piece of land with a border drawn between them."),
  ("Do together", "Continent call-out: you name one, the kids race to touch it on the globe. Big kids answer: biggest? (Asia) smallest? (Australia) coldest? (Antarctica)"),
  ("Worksheets", "Tier A (Titus & Nariah): dot each continent while you say the names, trace 7, color North America. Tier B (Naomi) & C (Nevaeh, Nylah): label the map; Tier C adds the fast-facts table."),
  ("Ask", "Which continent do we live on? Which one would you like to visit and why?")],
 [("Goal", "Name the 5 oceans and know the Atlantic is ours."),
  ("Gather", "Globe, a bowl of water with salt (let them taste a drop!), blue crayons."),
  ("Teach (5 min)", "Ocean water is salty — taste test! Oceans cover about 71% of Earth (spin the globe — mostly blue!). Name the 5: Pacific, Atlantic, Indian, Arctic, Southern. "
   "They're all connected — one big world ocean with 5 names."),
  ("Do together", "Trace a finger from Jacksonville across the Atlantic to Africa. Then find the Pacific — the biggest. Ask: which ocean is frozen? (Arctic) Which circles Antarctica? (Southern)"),
  ("Worksheets", "Tier A: color the water blue while you say the ocean names, trace “ocean.” Tier B/C: label oceans A–E; Tier C adds the fast-facts table."),
  ("Ask", "If you sailed east from our beach, what ocean would you be on? What would you reach?")],
 [("Goal", "Understand the equator, prime meridian, and the four hemispheres."),
  ("Gather", "Globe, an orange (or ball) and a marker, a knife for Mom."),
  ("Teach (5 min)", "Draw a line around the middle of the orange — the equator, like a belt. Cut along it: two halves = Northern and Southern Hemispheres. "
   "On another orange, draw a line top to bottom — the prime meridian — and cut: Eastern and Western Hemispheres. Every place is in one N/S half AND one E/W half."),
  ("Do together", "Find Florida on the globe: north or south of the equator? (North) East or west of the prime meridian? (West) Repeat with Australia and Japan."),
  ("Worksheets", "Tier A: trace the equator belt and color North/South. Tier B/C: hemisphere table; Tier C adds the explain question."),
  ("Ask", "Why is it summer in Australia when it's winter here? (Older kids — tilt of the Earth; preview for later.)")],
 [("Goal", "Use grid lines to find places; older kids read latitude and longitude."),
  ("Gather", "Globe or atlas world map with grid lines; painter's tape optional for a floor grid."),
  ("Teach (5 min)", "Make a grid on the floor with tape or chairs: rows A–C and columns 1–3. Hide a toy at “B2” and let kids find it. That's how map lines work! "
   "Latitude lines run side to side (like a ladder's rungs) and tell how far north or south. Longitude lines run top to bottom and tell how far east or west. Say latitude first."),
  ("Do together", "Find 30°N, 82°W on the globe — that's us! Then let older kids pick a coordinate for the little ones to find."),
  ("Worksheets", "Tier A: grid treasure hunt. Tier B/C: read the coordinates of points A–E; Tier C adds the hemisphere challenge."),
  ("Ask", "Why do pilots and ship captains need latitude and longitude?")],
 [("Goal", "Put it all together: describe exactly where we live."),
  ("Gather", "Globe, atlas, a Florida or Jacksonville map if you have one."),
  ("Teach (5 min)", "Play “zoom in”: Earth → North America → United States → Florida → Jacksonville → our street. Point out the St. Johns River running through Jacksonville "
   "and the Atlantic Ocean to the east."),
  ("Do together", "Quick review game: you call out a word (continent, ocean, equator, Pacific, Asia, prime meridian) and the kids point to it on the globe."),
  ("Worksheets", "Tier A: color North America, find the star, trace Florida, show-me checklist. Tier B/C: the “where we live” table; Tier C adds three challenge questions."),
  ("Ask", "Week 2 done! Which was hardest — continents, oceans, hemispheres, or coordinates?")],
]

EL = [
 [("Gather", "Shallow plates (one per kid or pair), milk (whole is best), food coloring, dish soap in a small cup, cotton swabs, paper towels."),
  ("Before", "Ask: what do you think will happen when soap touches the milk? Have everyone predict (Tier A draws it)."),
  ("Steps", "1) Pour milk just to cover the plate. 2) Add 4–6 drops of different colors near the center. 3) Dip a swab in soap and touch the middle — hold it there 10 seconds. "
   "4) Watch! 5) Try touching other spots. 6) Older kids: repeat with skim milk or water and compare."),
  ("Explain", "Milk's surface is like a stretched skin (surface tension). Soap weakens it where it touches, so the colors get pulled away. Soap also chases the fat in the milk, "
   "which keeps it swirling — that's why whole milk works best."),
  ("Tiers", "A: predict & draw, slow/fast checkbox, trace “milk.” B: hypothesis, observations, conclusion. C: full explanation + variable test.")],
 [("Gather", "Colored paper (or let kids paint plain paper with watercolors first and let it dry), scissors, glue sticks, cardstock. Search “Matisse The Snail” to show the real piece."),
  ("Before", "Play the Matisse story QR. Show The Snail and ask: what shapes do you see? How do they make a spiral?"),
  ("Steps", "1) Cut freely — no drawing first (Matisse “drew with scissors”). 2) Make at least 8 shapes: leaves, stars, squiggles, rectangles. "
   "3) Arrange them on the page BEFORE gluing; move things around. 4) Glue. 5) Give the piece a title."),
  ("Talk about", "Organic shapes (curvy, like leaves) vs geometric shapes (squares, triangles). Matisse kept making art after his illness — God gives creativity in every season."),
  ("Tiers", "A: free collage in the box. B: why cut-outs + organic vs geometric + title. C: same plus explain one design choice.")],
 [("Gather", "The QR music on your phone or TV; scarves or ribbons for the littles (optional)."),
  ("Before", "Tell the Nutcracker story in 1 minute (or play the story QR): Clara, the nutcracker, the Mouse King, the Land of Sweets."),
  ("Steps", "1) Play “Dance of the Sugar Plum Fairy” — eyes closed. Ask: what instrument sounds like tiny bells? (the celesta) 2) Play it again: littles draw or tiptoe, "
   "big kids fill in the listening table. 3) Play “Russian Dance (Trepak)” — fast and loud! Everyone dance. 4) End with “Waltz of the Flowers.”"),
  ("Fun fact", "Tchaikovsky found the celesta in Paris and kept it a secret so other composers wouldn't use it first."),
  ("Tiers", "A: draw to the music, fast/slow & loud/soft. B: listening table + celesta question + draw the Land of Sweets. C: listening table + how music tells a story.")],
 [("Gather", "Blank cards or folded paper, envelopes, a stamp or two, your address book."),
  ("Before", "Let each kid choose a real person to thank (grandparent, Sunday school teacher, Pastor, a friend who gave a gift). Show them a thank-you note you've received if you have one."),
  ("Steps", "1) Go over the 5 parts: greeting, thank them for the specific thing, how you used it/why it mattered, a kind sentence, closing + name. 2) Draft on the worksheet. "
   "3) Copy onto the real card. 4) Address the envelope together: return address top left, their address in the center, stamp top right. 5) Mail them this week!"),
  ("Tiers", "A: trace “Thank you,” draw a picture, trace name to sign — you write the words. B: draft with the 5 parts + practice envelope. C: same with formal titles & abbreviations.")],
 [("Gather", "Backyard, a timer, water bottles. Mark a start and finish line."),
  ("Before", "Warm up: 20 jumping jacks, arm circles. Older kids take their pulse (count 15 seconds × 4)."),
  ("Steps", "Run each event: bear crawl, crab walk, frog jumps, inchworm, flamingo balance, kangaroo hops, bunny hops, gorilla shuffle. Round 1 for a score, water break, "
   "then Round 2 to try to beat it. Older kids record times/counts; littles earn a medal on their sheet for each one."),
  ("Cool down", "Slow walk around the yard, then stretch. Older kids take their pulse again and compare."),
  ("Tiers", "A: medal checklist + favorite animal. B: score table + hardest walk. C: score table + heart rate + muscles worked.")],
]

MULT = [
 "Chant the 5s table together 3 times (clap on each answer). Cover it and go around the room — each kid says the next fact. Then pages. Titus & Nayeli: count by 10s on their Skip Count Stars page.",
 "Chant the 10s table 3 times. Quick oral quiz: you say “10 times 7,” they shout the answer. Then pages. Titus & Nayeli: count by 5s and dot the numbers that end in 5 or 0.",
 "Chant both tables once. Flash-card round with 0s, 1s, 2s, 5s, 10s. Then the 30-fact page — have them circle and re-write any they hesitated on. Titus & Nayeli: hands count by 5s.",
 "Read the word problems out loud together for Nariah. Then time the 2-minute speed drill and write the time on the page. Titus & Nayeli: ten-frame towers.",
 "Checkpoint: 40 facts, 4 minutes. 32+ = pass. Note any missed facts for Monday practice. Titus & Nayeli: dot-to-dot by 10s, then count to 100 by 10s and 50 by 5s for you.",
]

SPEECH = [
 "Mouth Gym (1 min). Review bunny-teeth F from last time: “fff” ×5. Then V: same bunny teeth, voice on — hands on throats to feel the buzz. Go down the V word list; color a star for each good one. Mirror helps.",
 "Mouth Gym. Bunny tails — the sound comes at the END. Say each word slowly, stretching the last sound (lea-fff, fi-vvv). Watch for dropped endings (“lea” for leaf).",
 "Mouth Gym. Kitty tails — K at the end, made at the back of the mouth. Model a crisp “k!” Watch for dropped K (“boo” for book) or T instead of K (“boot”). Clock/chicken game for fun.",
 "Mouth Gym. Phrases — slow and clear. Nariah reads the sentences; Titus & Nayeli echo after you. Praise effort, not just perfect sounds.",
 "Game day! Roll and move; say the word on the square. Fill in your check at the bottom: which sounds are solid, which need more practice next week.",
]

def day_plan(i):
    d, wd, dt = DAYS[i]
    return ("<div class='small'>Order of the day for together subjects: Multiplication → Speech → Geography → Elective. About 10–15 minutes each.</div>"
            + block(f"Multiplication Mastery · {mult.TITLES[i]}", "#6d28d9", [("Plan", MULT[i])])
            + block(f"Speech Stars · {speech.TITLES[i]} (Nariah, Titus, Nayeli)", "#a21caf", [("Plan", SPEECH[i])])
            + block(f"Geography · {geography.TITLES[i]}", "#2f5bd3", GEO[i])
            + block(f"{electives.NAMES[i]} · {electives.TOPIC[i]}", "#b02fc9", EL[i]))
