from core_common import *
from mathgen import *
import random, math as M

# ---------------- simple line icons (no fill colors -> kids color them) ----------------
def ic(body, w=90, h=80, vb="0 0 90 80"):
    return f'<svg width="{w}" height="{h}" viewBox="{vb}" fill="none" stroke="#1f2a5c" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
I = {
 "egg": ic('<path d="M10,60 C30,20 70,20 85,55 C60,70 30,70 10,60Z"/><ellipse cx="45" cy="45" rx="6" ry="8"/><path d="M20,58 L75,52"/>'),
 "caterpillar": ic("".join(f'<circle cx="{14+k*13}" cy="{50 - (8 if k==5 else 0)}" r="{8 if k<5 else 10}"/>' for k in range(6)) + '<path d="M80,32 l4,-10 M74,32 l-2,-10"/>'),
 "chrysalis": ic('<path d="M45,6 L45,14"/><path d="M45,14 C62,22 62,58 45,74 C28,58 28,22 45,14Z"/><path d="M38,40 L52,40 M39,52 L51,52"/><path d="M20,6 L70,6"/>'),
 "butterfly": ic('<path d="M45,20 L45,66"/><path d="M45,30 C20,0 2,20 12,40 C20,52 40,44 45,40Z"/><path d="M45,30 C70,0 88,20 78,40 C70,52 50,44 45,40Z"/>'
                 '<path d="M45,44 C26,46 18,66 30,72 C40,76 45,60 45,52Z"/><path d="M45,44 C64,46 72,66 60,72 C50,76 45,60 45,52Z"/><path d="M45,20 l-7,-12 M45,20 l7,-12"/>'),
 "eye": ic('<path d="M6,40 C30,10 60,10 84,40 C60,70 30,70 6,40Z"/><circle cx="45" cy="40" r="13"/><circle cx="45" cy="40" r="4"/>'),
 "ear": ic('<path d="M30,70 C30,58 22,56 22,40 C22,18 36,8 50,8 C66,8 76,22 74,36 C72,52 58,52 56,62 C54,72 40,76 30,70Z"/><path d="M40,40 C40,28 54,24 58,34 C60,42 50,44 50,50"/>'),
 "nose": ic('<path d="M44,6 C42,28 26,48 26,58 C26,68 36,70 40,64 C44,70 52,70 56,64 C60,70 70,68 70,58 C70,48 54,28 52,6"/>'),
 "mouth": ic('<path d="M8,38 C28,24 62,24 82,38 C62,64 28,64 8,38Z"/><path d="M8,38 C28,44 62,44 82,38"/><path d="M38,50 C42,62 52,62 54,50"/>'),
 "hand": ic('<path d="M28,78 C18,66 12,54 14,46 C16,40 22,42 24,50 L26,54 L24,20 C24,14 32,14 32,20 L33,42 L34,12 C34,6 42,6 42,12 L43,42 L45,15 C45,9 53,9 53,15 L52,44 L55,24 C56,18 64,19 63,25 L60,58 C59,70 54,76 50,78 Z"/>', 90, 80),
 "ship": ic('<path d="M8,58 L82,58 L72,72 L18,72Z"/><path d="M45,58 L45,8"/><path d="M45,12 L70,30 L45,30Z"/><path d="M45,34 L20,50 L45,50Z"/>'),
 "corn": ic('<path d="M45,6 C60,10 62,50 45,72 C28,50 30,10 45,6Z"/><path d="M45,72 C30,64 18,50 20,36 M45,72 C60,64 72,50 70,36"/>' + "".join(f'<path d="M36,{20+k*10} L54,{20+k*10}"/>' for k in range(4))),
 "pie": ic('<path d="M8,40 L82,40 L74,62 L16,62Z"/><path d="M8,40 C20,26 70,26 82,40"/><path d="M30,34 L36,40 M50,32 L56,40"/>'),
 "house": ic('<path d="M12,40 L45,10 L78,40"/><path d="M20,36 L20,72 L70,72 L70,36"/><path d="M38,72 L38,52 L52,52 L52,72"/>'),
}
def icon(name, scale=1.0):
    s = I[name]
    return s.replace('width="90" height="80"', f'width="{90*scale:.0f}" height="{80*scale:.0f}"')

# ======================= NARIAH (2nd) =======================
def _tstr(h, m): return f"{h}:{m:02d}"
def time_choices(h, m):
    """correct time first, then two near-misses (hands mixed up / next hour)."""
    nxt = h % 12 + 1
    alt = (m and _tstr(nxt, 30)) or _tstr(h, 30)
    swap = _tstr(nxt, 0) if m else _tstr(12 if h == 6 else (6 if h == 12 else h), 30 if h not in (6, 12) else 0)
    out = [_tstr(h, m)]
    for c in (alt, swap, _tstr(nxt, m)):
        if c not in out: out.append(c)
    return out[:3]
def clock_pick(h, m, size):
    return f'<div class="center">{clock(h, m, size)}{mc_opts(time_choices(h, m), f"clk{h}{m}{size}")}</div>'

def nariah_math():
    S = Subject("Nariah", "Math", "Level 1 · Regrouping & Time"); r = random.Random(22)
    adds = [(r.randint(13, 69), r.randint(13, 29)) for _ in range(30)]
    adds = [(a, b) for a, b in adds if (a % 10 + b % 10) >= 10 and a + b < 100][:10]
    S.set(0, "Adding with Regrouping",
        learnbox("<p class='big'>When the <b>ones</b> add up to 10 or more, trade 10 ones for <b>1 ten</b>! "
                 "<b>38 + 25:</b> 8 + 5 = 13 → write <b>3</b>, carry the <b>1</b> ten. 1 + 3 + 2 = <b>6</b>. Answer: <b>63</b>.</p>", yt("2 digit addition with regrouping 2nd grade"))
        + f'<div class="flexrow" style="align-items:flex-end;gap:24px"><div class="center">{blocks(38)}<div class="big">38</div></div><div class="huge">+</div>'
          f'<div class="center">{blocks(25)}<div class="big">25</div></div><div class="big">Circle 10 ones to make a new ten!</div></div>'
        + vgrid([(a, b, "+") for a, b in adds], 5),
        ", ".join(f"{n+1}) {a+b}" for n, (a, b) in enumerate(adds)))
    subs = []
    while len(subs) < 10:
        a, b = r.randint(31, 95), r.randint(12, 49)
        if a % 10 < b % 10 and a > b: subs.append((a, b))
    S.set(1, "Subtracting with Regrouping",
        learnbox("<p class='big'>If the top ones digit is too small, <b>borrow</b> a ten! <b>52 − 17:</b> 2 is less than 7, so trade 1 ten for 10 ones. "
                 "Now it's 4 tens and 12 ones. 12 − 7 = <b>5</b>. 4 − 1 = <b>3</b>. Answer: <b>35</b>.</p>", yt("2 digit subtraction with regrouping 2nd grade"))
        + f'<div class="flexrow" style="align-items:flex-end;gap:20px"><div class="center">{blocks(52)}<div class="big">52</div></div>'
          '<div class="big">Cross out 17. Break a ten into 10 ones when you need to!</div></div>'
        + vgrid([(a, b, "−") for a, b in subs], 5),
        ", ".join(f"{n+1}) {a-b}" for n, (a, b) in enumerate(subs)))
    times = [(3, 0), (7, 30), (11, 0), (1, 30), (9, 30), (5, 0)]
    S.set(2, "Telling Time: Hour & Half Hour",
        learnbox("<p class='big'>The <b>short</b> hand shows the <b>hour</b>. The <b>long</b> hand shows the <b>minutes</b>. Long hand on <b>12</b> → “o'clock” (3:00). "
                 "Long hand on <b>6</b> → “thirty” — half past (3:30). At half past, the short hand sits halfway between two numbers.</p>", yt("telling time hour and half hour 2nd grade"))
        + '<div class="lab">What time is it? Circle the time.</div><div class="grid3" style="justify-items:center">'
        + "".join(clock_pick(h, m, 130) for h, m in times) + '</div>'
        + '<div class="lab">Draw the hands.</div><div class="grid3" style="justify-items:center">'
        + "".join(f'<div class="center">{clock(0, 0, 130, False)}<div class="big"><b>{t}</b></div></div>' for t in ["4:00", "8:30", "12:30"]) + '</div>',
        "3:00, 7:30, 11:00, 1:30, 9:30, 5:00. Drawn: 4:00 (short on 4, long on 12), 8:30 (short between 8 & 9, long on 6), 12:30 (short between 12 & 1, long on 6).")
    mix = [(46, 37, "+"), (71, 28, "−"), (58, 25, "+"), (60, 24, "−"), (29, 49, "+"), (83, 56, "−")]
    S.set(3, "Mix It Up!",
        learnbox("<p class='big'>Look at the sign first! <b>+</b> means add, <b>−</b> means subtract. Then check: do I need to regroup?</p>")
        + vgrid([(a, b, op) for a, b, op in mix], 6)
        + '<div class="lab">Circle the time.</div><div class="grid3" style="justify-items:center">' + "".join(clock_pick(h, m, 120) for h, m in [(2, 30), (10, 0), (6, 30)]) + '</div>'
        + qs([("Nariah had 45 stickers. She got 28 more. How many now?", ["73", "63", "17"]), ("There were 62 cookies. The family ate 35. How many are left?", ["27", "37", "97"]),
              ("School starts at 9:00. Lunch is at 12:00. How many hours apart?", ["3 hours", "4 hours", "12 hours"])], 7),
        "83, 43, 83, 36, 78, 27. Clocks 2:30, 10:00, 6:30. 7) 73 8) 27 9) 3 hours.")
    cp = [(37, 48, "+"), (65, 19, "+"), (54, 27, "−"), (90, 36, "−"), (28, 28, "+"), (73, 45, "−")]
    S.set(4, "Checkpoint",
        learnbox("<p class='big'><b>Checkpoint!</b> 12 questions. Goal: <b>10 right</b>. You can do it!</p>")
        + vgrid([(a, b, op) for a, b, op in cp], 6)
        + '<div class="lab">Circle the time.</div><div class="grid3" style="justify-items:center">' + "".join(clock_pick(h, m, 120) for h, m in [(4, 30), (8, 0), (12, 30)]) + '</div>'
        + '<div class="grid3" style="justify-items:center">' + "".join(f'<div class="center">{clock(0, 0, 120, False)}<div class="big"><b>{t}</b></div></div>' for t in ["6:00", "2:30", "11:30"]) + '</div>'
        + '<div class="big">Score: ______ / 12</div>',
        "85, 84, 27, 54, 56, 28. Clocks 4:30, 8:00, 12:30. Drawn 6:00, 2:30, 11:30 — check hands.")
    return S

def nariah_english():
    S = Subject("Nariah", "English", "Week 2 · Vowels, Nouns & Verbs")
    def sort_tbl(cols, words):
        return (f'<div>Word bank: ' + "".join(f'<span class="pill" style="font-size:13pt">{w}</span>' for w in words) + '</div>'
                + fill_table([f"short {c}" for c in cols], [[""] * len(cols)] * 4, 34))
    S.set(0, "Short a & Short e",
        learnbox("<p class='big'>Short <b>a</b> says /a/ like in <b>cat</b>. Short <b>e</b> says /e/ like in <b>bed</b>. Say each word slowly and listen for the middle sound.</p>", yt("short a short e phonics song"))
        + '<div class="lab">Short a or short e? Circle the sound you hear.</div>' + mark_list(["map", "hen", "jam", "pet", "bag", "web", "fan", "ten"], ["short a", "short e"], cols=2)
        + '<div class="lab">Trace and write.</div>' + trace_line("cat", 46, 2) + trace_line("bed", 46, 2)
        + '<div class="box big"><b>Read it:</b> The red hen sat in a bag. Ted had a hat and a pet cat.</div>'
        + '<div class="lab">Circle every short a word above. Underline every short e word.</div>',
        "short a: map, jam, bag, fan; short e: hen, pet, web, ten. Reading: a — sat, bag, had, hat, cat (and 'a'); e — red, hen, Ted, pet.")
    S.set(1, "Short i, o & u",
        learnbox("<p class='big'>Short <b>i</b> — <b>pig</b>. Short <b>o</b> — <b>dog</b>. Short <b>u</b> — <b>sun</b>. Tap the sounds on your fingers: p-i-g!</p>", yt("short i o u phonics song"))
        + '<div class="lab">Which vowel makes a real word? Circle it.</div>'
        + '<div class="grid3">' + "".join(f'<div class="big">{w.replace("_", "__")} {pick("i", "o", "u")}</div>' for w in ["p_g", "h_t", "b_s", "d_g", "c_p", "f_x", "s_n", "w_g", "m_d", "l_ck", "f_sh", "dr_m"]) + '</div>'
        + '<div class="lab">Short i, o, or u? Circle the sound you hear.</div>' + mark_list(["fish", "mop", "bug", "lip", "log", "cup", "sit", "hot", "mud"], ["i", "o", "u"], cols=2)
        + '<div class="box big"><b>Read it:</b> A big bug sat on a log in the hot sun. It hid in a cup!</div>',
        "Possible: pig/pug, hit/hot/hut, bus, dig/dog/dug, cop/cup, fox/fix, sun/son, wig, mud/mid, lick/lock/luck, fish, drum. Sort i: fish, lip, sit; o: mop, log, hot; u: bug, cup, mud.")
    S.set(2, "Nouns",
        learnbox("<p class='big'>A <b>noun</b> is a <b>person</b>, <b>place</b>, or <b>thing</b>. <i>Mom</i> is a person. <i>Park</i> is a place. <i>Ball</i> is a thing.</p>", yt("nouns song for kids"))
        + '<div class="lab">Is it a person, place, or thing? Circle one.</div>'
        + mark_list(["sister", "church", "apple", "baker", "beach", "book", "Dad", "zoo", "shoe"], ["person", "place", "thing"], cols=1)
        + '<div class="lab">Circle the nouns in each sentence.</div>'
        + '<div class="big" style="line-height:2">1. The dog ran to the park.<br>2. My brother has a red truck.<br>3. Mom put the pie on the table.</div>'
        + '<div class="lab">Write a noun:</div><div class="grid3"><div>person: <span class="blank-ln" style="min-width:100px"></span></div><div>place: <span class="blank-ln" style="min-width:100px"></span></div><div>thing: <span class="blank-ln" style="min-width:100px"></span></div></div>',
        "Person: sister, baker, Dad. Place: church, beach, zoo. Thing: apple, book, shoe. 1) dog, park 2) brother, truck 3) Mom, pie, table.")
    S.set(3, "Verbs",
        learnbox("<p class='big'>A <b>verb</b> is an <b>action</b> word — something you can <b>do</b>! <i>run, jump, sing, eat, read</i>. Can you act it out? Then it's a verb!</p>", yt("verbs song for kids"))
        + '<div class="lab">Can you do it? Circle verb or not a verb.</div>'
        + mark_list(["hop", "cat", "swim", "blue", "clap", "tree", "kick", "sing"], ["verb", "not a verb"], cols=2)
        + '<div class="lab">Circle the verb that finishes the sentence.</div>'
        + qs([("The bird can ______.", ["fly", "tree", "green"]), ("I like to ______ with my sister.", ["play", "table", "red"]),
              ("Fish ______ in the pond.", ["swim", "fins", "wet"]), ("We ______ to God at church.", ["sing", "pew", "loud"])])
        + '<div class="lab">Act it out! Mom says a verb, you do it: hop · wiggle · stomp · tiptoe · spin</div>'
        + '<div class="lab">Draw yourself doing your favorite verb.</div><div class="answer-space"></div>',
        "Verbs: hop, swim, clap, kick, sing (cat, blue, tree = not a verb). 1) fly 2) play 3) swim 4) sing.")
    S.set(4, "Review & Read",
        learnbox("<p class='big'>Read the story. Then answer the questions.</p>")
        + '<div class="box" style="font-size:15pt;line-height:1.6">Nan has a big red dog named Gus. Gus can run and dig. One hot day, Gus dug a pit in the mud. '
          'Nan got a tub and gave Gus a bath. Gus did not like it! He shook and got Nan wet. Nan had to laugh.</div>'
        + qs([("What is the dog's name?", ["Gus", "Nan", "Red"]), ("What did Gus dig in?", ["mud", "sand", "a tub"]), ("What did Nan use to give Gus a bath?", ["a tub", "a cup", "a pit"]),
              ("Which word is a noun?", ["dog", "dig", "run"]), ("Which word is a verb?", ["dig", "mud", "tub"]), ("Which word has a short u?", ["mud", "dog", "wet"])])
        + '<div class="lab">Write one word from the story that has a short a.</div>' + lines(1, 30),
        "1) Gus 2) mud 3) a tub 4) dog 5) dig 6) mud. Short a word: Nan, has, bath, had.")
    return S

def nariah_science():
    S = Subject("Nariah", "Science", "Week 2 · The Butterfly Life Cycle")
    VB = [yt("BF egg"), yt("BF caterpillar"), yt("BF chrysalis"), yt("BF butterfly"), yt("BF review")]
    S.set(0, "Stage 1: Egg",
        learnbox("<p class='big'>A mother <b>monarch butterfly</b> lays tiny eggs on a <b>milkweed</b> leaf. Each egg is about the size of a pin head! "
                 "Monarchs pick milkweed because it's the only plant their babies can eat. After 3–5 days, the egg hatches.</p>", VB[0])
        + f'<div class="center">{icon("egg", 2.2)}</div>'
        + qs([("What plant does a monarch lay her eggs on?", ["milkweed", "oak tree", "grass"]), ("How big is a monarch egg?", ["about the size of a pin head", "as big as a grape", "as big as your hand"]), ("How many days until it hatches?", ["3–5 days", "1 day", "30 days"])], 1, 30)
        + '<div class="lab">Trace:</div>' + trace_line("egg", 48, 3),
        "1) milkweed 2) about the size of a pin head 3) 3–5 days")
    S.set(1, "Stage 2: Caterpillar",
        learnbox("<p class='big'>Out comes a tiny <b>caterpillar</b> (also called a <b>larva</b>). First it eats its own eggshell, then it munches milkweed all day long! "
                 "It grows so fast it gets too big for its skin, so it <b>molts</b> — splits its skin and crawls out with a new one. It molts several times in about 2 weeks.</p>", VB[1])
        + f'<div class="center">{icon("caterpillar", 2.2)}</div>'
        + qs([("What is another name for a caterpillar?", ["larva", "pupa", "egg"]), ("What is the first thing it eats?", ["its eggshell", "a flower", "a bug"]), ("What does “molt” mean?", ["shed its old skin", "go to sleep", "fly away"])], 1, 30)
        + '<div class="lab">Trace:</div>' + trace_line("larva", 48, 2),
        "1) larva 2) its eggshell 3) shedding its old skin")
    S.set(2, "Stage 3: Chrysalis",
        learnbox("<p class='big'>When the caterpillar is big, it hangs upside down in a “J” shape and forms a <b>chrysalis</b> (KRIS-uh-lis) — also called a <b>pupa</b>. "
                 "A monarch chrysalis is green with tiny gold dots. Inside, God is doing something amazing: the caterpillar is changing into a butterfly! "
                 "This takes about 1–2 weeks.</p>", VB[2])
        + f'<div class="center">{icon("chrysalis", 2.2)}</div>'
        + qs([("What shape does the caterpillar hang in?", ["a J", "an O", "a T"]), ("What is another name for the chrysalis?", ["pupa", "larva", "nest"]), ("What is happening inside?", ["The caterpillar is changing into a butterfly.", "The caterpillar is sleeping all winter.", "A new egg is growing."])], 1, 30)
        + '<div class="lab">Trace:</div>' + trace_line("pupa", 48, 3),
        "1) a J 2) pupa 3) the caterpillar is changing into a butterfly")
    S.set(3, "Stage 4: Butterfly",
        learnbox("<p class='big'>The chrysalis cracks open and an <b>adult butterfly</b> squeezes out! Its wings are wet and crumpled, so it pumps them and waits a few hours "
                 "until they're dry. Then it flies off to drink nectar from flowers with a straw-like tongue. Fall monarchs fly all the way to <b>Mexico</b>! "
                 "Then the cycle starts over.</p>", VB[3])
        + f'<div class="center">{icon("butterfly", 2.2)}</div>'
        + qs([("Why can't the butterfly fly right away?", ["Its wings are wet and crumpled.", "It is too hungry.", "It is too cold."]), ("What does a butterfly drink?", ["nectar", "milk", "rain"]), ("Where do fall monarchs fly?", ["Mexico", "the North Pole", "the ocean"])], 1, 30)
        + '<div class="box big">2 Corinthians 5:17 — “if anyone is in Christ, he is a new creation.” How is a butterfly like a new creation?</div>' + lines(2, 30),
        "1) its wings are wet/crumpled 2) nectar 3) Mexico. Reflection varies.")
    S.set(4, "The Whole Cycle",
        learnbox("<p class='big'>Put the life cycle together! Circle the right number (1–4) under each stage, then draw arrows to make a circle.</p>", VB[4])
        + '<div class="grid4" style="justify-items:center">' + "".join(f'<div class="center">{icon(n, 1.4)}<div class="big">{pick("1", "2", "3", "4")}</div></div>' for n in ["butterfly", "egg", "chrysalis", "caterpillar"]) + '</div>'
        + '<div class="lab">Draw the life cycle as a circle with arrows.</div><div class="answer-space" style="min-height:260px"></div>'
        + qs([("What plant do monarchs need?", ["milkweed", "corn", "roses"]), ("Which stage eats the most?", ["caterpillar", "egg", "chrysalis"])], 1, 30),
        "butterfly 4, egg 1, chrysalis 3, caterpillar 2. 1) milkweed 2) caterpillar.")
    return S

def nariah_ss():
    S = Subject("Nariah", "Social Studies", "Week 2 · The First Thanksgiving")
    S.set(0, "The Mayflower",
        learnbox("<p class='big'>In <b>1620</b>, a group called the <b>Pilgrims</b> wanted to worship God freely. They sailed from England across the <b>Atlantic Ocean</b> "
                 "on a ship called the <b>Mayflower</b>. The trip took 66 days! About 102 people were crowded on board, with storms and seasickness.</p>", yt("Mayflower Pilgrims for kids"))
        + f'<div class="center">{icon("ship", 2.0)}</div>'
        + qs([("What was the name of the Pilgrims' ship?", ["the Mayflower", "the Titanic", "the Ark"]), ("Why did the Pilgrims come?", ["to worship God freely", "to find gold", "to go on vacation"]), ("What ocean did they cross? (Hint: it's by our house!)", ["the Atlantic Ocean", "the Pacific Ocean", "the Arctic Ocean"])], 1, 30)
        + '<div class="lab">Trace:</div>' + trace_line("Mayflower", 44, 1),
        "1) the Mayflower 2) to worship God freely 3) the Atlantic Ocean")
    S.set(1, "The Wampanoag & Squanto",
        learnbox("<p class='big'>The Pilgrims landed in a cold place they called <b>Plymouth</b>. The first winter was very hard and many got sick. In the spring, they met the "
                 "<b>Wampanoag</b> (WAHM-puh-noh-ag) people. A man named <b>Squanto</b> spoke English and showed the Pilgrims how to plant <b>corn</b> with a "
                 "fish in each hole to help it grow, and where to fish and hunt.</p>", yt("Squanto story for kids"))
        + f'<div class="center">{icon("corn", 2.0)}</div>'
        + qs([("Who did the Pilgrims meet in the spring?", ["the Wampanoag", "the King", "pirates"]), ("Who helped the Pilgrims?", ["Squanto", "Gideon", "Columbus"]), ("What did he put in each hole with the corn?", ["a fish", "a rock", "a shell"])], 1, 30)
        + '<div class="lab">Trace:</div>' + trace_line("corn", 46, 3),
        "1) the Wampanoag 2) Squanto 3) a fish")
    S.set(2, "The Harvest Feast, 1621",
        learnbox("<p class='big'>In the fall of <b>1621</b>, the Pilgrims had a good harvest! They held a <b>feast</b> to give thanks. About <b>90</b> Wampanoag men and "
                 "their leader <b>Massasoit</b> joined about <b>50</b> Pilgrims. The feast lasted <b>3 days</b>! They probably ate deer, wild birds, fish, corn, "
                 "and squash. They also played games and races.</p>", yt("first Thanksgiving 1621 for kids"))
        + f'<div class="center">{icon("pie", 2.0)}</div>'
        + qs([("What year was the harvest feast?", ["1621", "1492", "2021"]), ("How many days did it last?", ["3 days", "1 day", "10 days"]), ("Which two foods did they probably eat?", ["deer and corn", "pizza and tacos", "ice cream and cake"])], 1, 30)
        + '<div class="lab">Draw the feast!</div><div class="answer-space"></div>',
        "1) 1621 2) 3 days 3) deer, birds, fish, corn, squash")
    S.set(3, "Giving Thanks to God",
        learnbox("<p class='big'>The Pilgrims thanked God for keeping them alive and giving them food. Thanksgiving is a time for us to thank God too! "
                 "<b>Psalm 107:1</b> says, “Oh give thanks to the LORD, for he is good, for his steadfast love endures forever!”</p>", yt("Psalm 107:1 song for kids"))
        + '<div class="lab">Trace:</div>' + trace_line("Thank you God", 44, 1)
        + '<div class="lab">Write or draw 5 things you are thankful for.</div>'
        + "".join(f'<div class="flexrow" style="align-items:center"><div class="huge" style="color:#8a3ab9">{n}</div><div class="grow ln" style="height:40px"></div></div>' for n in range(1, 6))
        + '<div class="lab">Make it a prayer! Read your list to God tonight at Bible study.</div>',
        "Answers vary.")
    S.set(4, "Review",
        learnbox("<p class='big'>Show what you know about the first Thanksgiving!</p>")
        + '<div class="lab">Draw a line from the word to what it means.</div>'
        + '<svg width="640" height="250" style="align-self:center">'
          + "".join(f'<text x="20" y="{40+k*52}" font-size="19" font-weight="700" fill="#1f2a5c">{w}</text><circle cx="190" cy="{34+k*52}" r="6" fill="#8a3ab9"/>' for k, w in enumerate(["Mayflower", "Squanto", "Wampanoag", "1621", "Pilgrims"]))
          + "".join(f'<circle cx="270" cy="{34+k*52}" r="6" fill="#8a3ab9"/><text x="290" y="{40+k*52}" font-size="16" fill="#1f2a5c">{w}</text>' for k, w in enumerate(["the year of the harvest feast", "the people who sailed from England", "the Pilgrims' ship", "the Native people who lived there", "showed them how to plant corn"]))
          + '</svg>'
        + qs([("Why did the Pilgrims have a feast?", ["to thank God for the harvest", "for a birthday", "because it was Christmas"]), ("What is one way our family gives thanks?", 2)], 1, 30),
        "Mayflower–ship; Squanto–planted corn; Wampanoag–Native people; 1621–harvest feast; Pilgrims–sailed from England. 1) to thank God for the harvest. 2) varies.")
    return S

# ======================= TITUS (K) =======================
def titus_math():
    S = Subject("Titus", "Math", "Level 1 · Numbers to 20")
    def count_box(n, shape):
        return f'<div class="box center">{objs(n, shape, 5, 30)}<div class="big">How many? <span class="blank-ln" style="min-width:50px"></span></div></div>'
    S.set(0, "Numbers 11–15",
        learnbox("<p class='big'>Teen numbers are <b>10 and some more</b>! 13 is 10 and 3 more. Count the shapes, then dot each one with your dot marker as you count.</p>", yt("teen numbers song for kids"))
        + f'<div class="grid2">{count_box(11, "circle")}{count_box(14, "star")}{count_box(12, "square")}{count_box(15, "circle")}</div>'
        + '<div class="lab">Trace the numbers.</div>' + '<div class="trow" style="gap:16px">' + "".join(school_print(str(n), 62, "trace") for n in range(11, 16)) + '</div>',
        "11, 14, 12, 15")
    S.set(1, "Numbers 16–20",
        learnbox("<p class='big'>Keep counting! 16, 17, 18, 19, <b>20</b>! 20 is two groups of 10. Count and dot!</p>", yt("count to 20 song for kids"))
        + f'<div class="grid2">{count_box(16, "star")}{count_box(18, "circle")}{count_box(20, "square")}{count_box(17, "star")}</div>'
        + '<div class="lab">Trace the numbers.</div>' + '<div class="trow" style="gap:16px">' + "".join(school_print(str(n), 62, "trace") for n in range(16, 21)) + '</div>',
        "16, 18, 20, 17")
    def add_row(a, b, shape):
        return (f'<div class="flexrow" style="align-items:center;gap:12px">{objs(a, shape, 5, 30)}<div class="huge">+</div>{objs(b, shape, 5, 30)}'
                f'<div class="huge" style="margin-left:auto">{a} + {b} = <span class="blank-ln" style="min-width:50px"></span></div></div>')
    S.set(2, "Adding: Put Together",
        learnbox("<p class='big'><b>Adding</b> means putting groups together. Count ALL the shapes to find how many in all!</p>", yt("addition song for kindergarten"))
        + add_row(3, 2, "circle") + add_row(4, 4, "star") + add_row(5, 3, "square") + add_row(6, 2, "circle") + add_row(5, 5, "star")
        + '<div class="big">Use counting bears: 2 bears + 7 bears = ______</div>',
        "5, 8, 8, 8, 10, 9")
    def sub_row(a, b):
        sz = 30; s = ""
        for k in range(a):
            x = 4 + k * (sz + 8)
            s += f'<circle cx="{x+sz/2}" cy="{sz/2+4}" r="{sz/2-2}" fill="#fff" stroke="#6d28d9" stroke-width="2.5"/>'
            if k >= a - b:
                s += f'<line x1="{x+2}" y1="{6}" x2="{x+sz-2}" y2="{sz+2}" stroke="#111" stroke-width="3"/>'
        return (f'<div class="flexrow" style="align-items:center"><svg width="{a*(sz+8)+6}" height="{sz+10}">{s}</svg>'
                f'<div class="huge" style="margin-left:auto">{a} − {b} = <span class="blank-ln" style="min-width:50px"></span></div></div>')
    S.set(3, "Taking Away",
        learnbox("<p class='big'><b>Taking away</b> means some go away! Count the ones that are <b>left</b> (not crossed out).</p>", yt("subtraction song for kindergarten"))
        + sub_row(5, 2) + sub_row(7, 3) + sub_row(9, 4) + sub_row(6, 1) + sub_row(10, 5)
        + '<div class="big">Use 8 bears. Take away 3. How many left? ______</div>',
        "3, 4, 5, 5, 5, 5")
    S.set(4, "Review Day",
        learnbox("<p class='big'>Show Mom what you learned! Count, add, and take away.</p>")
        + f'<div class="grid2">{count_box(13, "circle")}{count_box(19, "star")}</div>'
        + add_row(4, 3, "square") + sub_row(8, 2)
        + '<div class="lab">Count to 20 out loud for Mom! <span class="star">☆</span> &nbsp; Trace 1–20:</div>'
        + '<div class="trow" style="gap:8px">' + "".join(school_print(str(n), 44, "trace", False) for n in range(1, 21)) + '</div>',
        "13, 19, 7, 6")
    return S

def titus_letters():
    S = Subject("Titus", "Letters & Writing", "Week 2 · Mm and Ss")
    mw = ["moon", "mop", "sun", "milk", "map", "dog", "mouse", "cat"]
    sw = ["sock", "fish", "sun", "seal", "bed", "six", "soap", "cup"]
    def listen(words, letter):
        return ('<div class="lab">Mom reads each word. Does it START with /' + letter + '/? Color the ' + letter.upper() + ' for yes, the X for no.</div>'
                '<div class="grid4">' + "".join(f'<div class="box center"><div class="small">{n+1}. (Mom: “{w}”)</div><span class="huge" style="color:#c9cde3">{letter.upper()}</span> &nbsp; <span class="huge" style="color:#c9cde3">✗</span></div>' for n, w in enumerate(words)) + '</div>')
    S.set(0, "Big M, Little m",
        learnbox("<p class='big'><b>M</b> says /m/ — like <b>mmm</b>, yummy! <b>m</b>oon, <b>m</b>ilk, <b>M</b>om!</p>", yt("letter M song for kids"))
        + '<div class="lab">Trace big M.</div>' + trace_line("M", 66, 5) + '<div class="lab">Trace little m.</div>' + trace_line("m", 66, 6)
        + '<div class="lab">Trace the word:</div>' + trace_line("Mom", 66, 2),
        "—")
    S.set(1, "M Words",
        learnbox("<p class='big'>Listen for the <b>/m/</b> sound at the start of words. Put your lips together and hum: mmm!</p>", yt("letter M sound words for kids"))
        + listen(mw, "m") + '<div class="lab">Trace:</div>' + trace_line("map", 60, 2) + trace_line("mop", 60, 2),
        "Yes: moon, mop, milk, map, mouse. No: sun, dog, cat.")
    S.set(2, "Big S, Little s",
        learnbox("<p class='big'><b>S</b> says /s/ — like a snake: <b>sssss</b>! <b>s</b>un, <b>s</b>ock, <b>s</b>ix!</p>", yt("letter S song for kids"))
        + '<div class="lab">Trace big S.</div>' + trace_line("S", 66, 6) + '<div class="lab">Trace little s.</div>' + trace_line("s", 66, 7)
        + '<div class="lab">Trace the word:</div>' + trace_line("sun", 66, 2),
        "—")
    S.set(3, "S Words",
        learnbox("<p class='big'>Listen for <b>/s/</b> at the start. Smile and let the air hiss out: sss!</p>", yt("letter S sound words for kids"))
        + listen(sw, "s") + '<div class="lab">Trace:</div>' + trace_line("sat", 60, 2) + trace_line("sit", 60, 2),
        "Yes: sock, sun, seal, six, soap. No: fish, bed, cup.")
    S.set(4, "Review: M, S & My Name",
        learnbox("<p class='big'>Show what you know! Trace your letters and your name.</p>")
        + '<div class="lab">Trace:</div>' + trace_line("Mm", 60, 3) + trace_line("Ss", 60, 3)
        + '<div class="lab">My name:</div>' + trace_line("Titus", 66, 2)
        + '<div class="lab">Now write your name by yourself:</div>' + school_print("", 66, "blank", extra_w=600)
        + '<div class="big">Mom asks: what sound does M make? <span class="star">☆</span> &nbsp; What sound does S make? <span class="star">☆</span></div>',
        "—")
    return S

def titus_science():
    S = Subject("Titus", "Science", "Week 2 · My Five Senses")
    VS = [yt("SN sight"), yt("SN hearing"), yt("SN smell taste"), yt("SN touch"), yt("SN all")]
    S.set(0, "I Can See!",
        learnbox("<p class='big'>God gave us <b>5 senses</b>! Today: <b>seeing</b>. We see with our <b>eyes</b>. Play I Spy with Mom: “I spy something purple…”</p>", VS[0])
        + f'<div class="center">{icon("eye", 2.4)}</div>'
        + '<div class="lab">Go on a walk. Draw 3 things you SEE.</div><div class="answer-space" style="min-height:300px"></div>'
        + '<div class="lab">Trace:</div>' + trace_line("see", 56, 3), "—")
    S.set(1, "I Can Hear!",
        learnbox("<p class='big'>We <b>hear</b> with our <b>ears</b>. Close your eyes and be very quiet. What do you hear? Birds? A car? The baby?</p>", VS[1])
        + f'<div class="center">{icon("ear", 2.4)}</div>'
        + '<div class="lab">Mom makes a sound behind your back (clap, shake keys, crinkle paper, ring a bell). Guess what it is!</div>'
        + '<table class="t" style="font-size:15pt">' + "".join(f"<tr><td style='height:44px'>Sound {k}</td><td>I guessed: </td><td class='center'><span class='chk'></span> right!</td></tr>" for k in range(1, 5)) + '</table>'
        + '<div class="lab">Trace:</div>' + trace_line("hear", 56, 2), "—")
    S.set(2, "I Can Smell & Taste!",
        learnbox("<p class='big'>We <b>smell</b> with our <b>nose</b> and <b>taste</b> with our <b>tongue</b>. Some foods are sweet, some sour, some salty!</p>", VS[2])
        + f'<div class="flexrow" style="justify-content:center;gap:40px">{icon("nose", 1.8)}{icon("mouth", 1.8)}</div>'
        + '<div class="lab">Taste test with Mom! Try a tiny bite and color the face.</div>'
        + '<table class="t" style="font-size:15pt"><tr><th>Food</th><th>Sweet, sour, or salty?</th><th>I like it! / No thanks</th></tr>'
        + "".join(f"<tr><td style='height:46px'>{f}</td><td></td><td class='center' style='font-size:22pt'>☺ &nbsp; ☹</td></tr>" for f in ["banana or apple", "lemon", "pretzel or cracker", "pickle"]) + '</table>', "—")
    S.set(3, "I Can Touch!",
        learnbox("<p class='big'>We feel with our <b>skin</b> — especially our <b>hands</b>! Things can feel soft, hard, bumpy, smooth, warm, or cold.</p>", VS[3])
        + f'<div class="center">{icon("hand", 2.2)}</div>'
        + '<div class="lab">Mystery bag! Mom puts things in a bag. Feel without looking. Is it soft or hard?</div>'
        + '<div class="grid2"><div class="box" style="min-height:200px"><div class="huge center">SOFT</div><div class="small center">draw soft things</div></div>'
          '<div class="box" style="min-height:200px"><div class="huge center">HARD</div><div class="small center">draw hard things</div></div></div>'
        + '<div class="lab">Trace:</div>' + trace_line("soft", 56, 2), "—")
    S.set(4, "My 5 Senses",
        learnbox("<p class='big'>Match each body part to its sense. Draw a line!</p>", VS[4])
        + '<div class="flexrow" style="justify-content:space-between;align-items:stretch"><div style="display:flex;flex-direction:column;gap:6px">'
        + "".join(icon(n, 0.95) for n in ["eye", "ear", "nose", "mouth", "hand"])
        + '</div><div style="display:flex;flex-direction:column;justify-content:space-around;font-size:22pt;font-weight:700;color:#1f2a5c">'
        + "".join(f"<div>{w}</div>" for w in ["touch", "taste", "see", "hear", "smell"]) + '</div></div>'
        + '<div class="big">Thank You, God, for my 5 senses! <span class="star">☆☆☆☆☆</span></div>',
        "eye–see, ear–hear, nose–smell, mouth–taste, hand–touch")
    return S

# ======================= NAYELI (Pre-K) =======================
SHAPES = ["circle", "square", "triangle", "rectangle", "star"]
def shape_path(name, cx, cy, s):
    if name == "circle": return f'<circle cx="{cx}" cy="{cy}" r="{s}"/>'
    if name == "square": return f'<rect x="{cx-s}" y="{cy-s}" width="{2*s}" height="{2*s}"/>'
    if name == "triangle": return f'<polygon points="{cx},{cy-s} {cx+s*1.1},{cy+s*0.85} {cx-s*1.1},{cy+s*0.85}"/>'
    if name == "rectangle": return f'<rect x="{cx-s*1.4}" y="{cy-s*0.75}" width="{2.8*s}" height="{1.5*s}"/>'
    pts = " ".join(f"{cx + (s if j%2==0 else s*0.42)*M.sin(j*M.pi/5):.1f},{cy - (s if j%2==0 else s*0.42)*M.cos(j*M.pi/5):.1f}" for j in range(10))
    return f'<polygon points="{pts}"/>'

def dots_on(name, cx, cy, s, n=14):
    # sample points along the outline for dot-marker circles
    import itertools
    pts = []
    if name == "circle":
        pts = [(cx + s*M.cos(2*M.pi*k/n), cy + s*M.sin(2*M.pi*k/n)) for k in range(n)]
    else:
        if name == "square": V = [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)]
        elif name == "triangle": V = [(cx, cy-s), (cx+s*1.1, cy+s*0.85), (cx-s*1.1, cy+s*0.85)]
        elif name == "rectangle": V = [(cx-s*1.4, cy-s*0.75), (cx+s*1.4, cy-s*0.75), (cx+s*1.4, cy+s*0.75), (cx-s*1.4, cy+s*0.75)]
        else: V = [(cx + (s if j%2==0 else s*0.42)*M.sin(j*M.pi/5), cy - (s if j%2==0 else s*0.42)*M.cos(j*M.pi/5)) for j in range(10)]
        per = max(1, n // len(V))
        for a, b in zip(V, V[1:] + V[:1]):
            for t in range(per):
                f = t / per; pts.append((a[0] + (b[0]-a[0])*f, a[1] + (b[1]-a[1])*f))
    return "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="21" fill="#fff" stroke="#a21caf" stroke-width="2.5"/>' for x, y in pts)

def nayeli_pages(i):
    sh = SHAPES[i]; Nm = "Nayeli"
    p1 = page(Nm, i, "Pre-K", f"Shape of the Day · {sh.title()}",
        f'<div class="center huge">This is a {sh}!</div><div class="big center">Dot every circle with your dot marker.</div>'
        f'<svg width="680" height="560" style="align-self:center">{dots_on(sh, 340, 290, 220 if sh not in ("rectangle",) else 170, 16 if sh!="star" else 20)}</svg>'
        f'<div class="big center">Say it with Mom: “{sh}!” <span class="star">☆</span></div>')
    rows = ""
    for r in range(3):
        rows += f'<svg width="680" height="170" fill="none" stroke="#9a9aa8" stroke-width="5" stroke-dasharray="2,11" stroke-linecap="round">' + "".join(shape_path(sh, 95 + k * 165, 85, 60) for k in range(4)) + '</svg>'
    p2 = page(Nm, i, "Pre-K", f"Trace the {sh.title()}s",
        f'<div class="big center">Start at the dot and trace each {sh} with your finger, then a crayon!</div>'
        f'<svg width="680" height="170" fill="none" stroke="#a21caf" stroke-width="6" style="align-self:center">' + "".join(shape_path(sh, 95 + k * 165, 85, 60) for k in range(1)) + '</svg>' + rows)
    r = random.Random(100 + i); items = ""
    picks = [sh] * 5 + r.sample([x for x in SHAPES if x != sh] * 3, 7); r.shuffle(picks)
    for k, nm in enumerate(picks):
        rr, cc = divmod(k, 4)
        items += f'<g fill="#fff" stroke="#1f2a5c" stroke-width="4">{shape_path(nm, 90 + cc * 170, 90 + rr * 175, 55)}</g>'
    p3 = page(Nm, i, "Pre-K", f"Find the {sh.title()}s",
        f'<div class="big center">Put a sticker on every <b>{sh}</b>. Then color them!</div>'
        f'<svg width="680" height="540" style="align-self:center">{items}</svg><div class="big center">How many {sh}s? Count with Mom: ______</div>')
    return [p1, p2, p3]
