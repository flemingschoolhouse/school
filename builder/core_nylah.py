from core_common import *
from mathgen import *
import random

K = "Nylah"

# ---------------- MATH CRASH COURSE · Level 2 ----------------
def math():
    S = Subject(K, "Math Crash Course", "Level 2"); r = random.Random(72)
    # D1 place value to 1,000+
    nums = [r.randint(1000, 9999) for _ in range(6)]
    S.set(0, "Place Value Power",
        learnbox("<p><b>Level 2</b> rebuilds the big-number skills everything else sits on. Each place is worth <b>10 times</b> the place to its right: "
                 "ones, tens, hundreds, thousands. In <b>4,682</b> the 6 means <b>600</b>. <b>Expanded form</b> pulls a number apart by place: "
                 "4,682 = 4,000 + 600 + 80 + 2.</p>", yt("place value thousands hundreds tens ones"))
        + fill_table(["Number", "Thousands", "Hundreds", "Tens", "Ones", "Expanded form"], [[f"{n:,}", "", "", "", "", ""] for n in nums], 30)
        + qs([("What is the value of the 7 in 7,305? In 3,075?", ["7,000; 70", "7; 7", "700; 7,000"]), ("Write the number: 5,000 + 40 + 9 = ______ &nbsp; 8,000 + 300 + 6 = ______", 1),
              ("Compare: &nbsp; 3,409 __ 3,490 &nbsp;&nbsp; 6,021 __ 6,012 &nbsp;&nbsp; 1,000 __ 999", ["&lt;, &gt;, &gt;", "&gt;, &lt;, &gt;", "&lt;, &lt;, ="]),
              ("What number is 100 more than 2,950? 1,000 less than 8,204?", 1), ("Order from least to greatest: 4,310 · 4,031 · 4,301 · 4,130", ["4,031 · 4,130 · 4,301 · 4,310", "4,310 · 4,301 · 4,130 · 4,031", "4,031 · 4,301 · 4,130 · 4,310"])]),
        "Expanded: " + "; ".join(f"{n:,} = " + " + ".join(str(int(d) * 10 ** (3 - k)) for k, d in enumerate(str(n)) if d != '0') for n in nums)
        + ". 1) 7,000; 70. 2) 5,049; 8,306. 3) <, >, >. 4) 3,050; 7,204. 5) 4,031, 4,130, 4,301, 4,310.")
    # D2 addition w/ regrouping
    adds = [(r.randint(158, 689), r.randint(147, 299)) for _ in range(6)] + [(r.randint(1205, 4890), r.randint(1567, 3999)) for _ in range(4)]
    S.set(1, "Adding with Regrouping",
        learnbox("<p>Line up the places. Add the <b>ones</b> first. If a place adds up to 10 or more, keep the ones digit and <b>carry</b> the 1 ten to the next place. "
                 "<b>468 + 275:</b> 8 + 5 = 13 → write 3, carry 1. 1 + 6 + 7 = 14 → write 4, carry 1. 1 + 4 + 2 = 7. Answer <b>743</b>.</p>", yt("3 digit addition with regrouping"))
        + vgrid([(a, b, "+") for a, b in adds], 5)
        + qs([("The church collected 387 cans on Sunday and 459 cans on Wednesday. How many cans in all?", 1)], 11),
        ", ".join(f"{n+1}) {a+b:,}" for n, (a, b) in enumerate(adds)) + ", 11) 846")
    # D3 subtraction w/ regrouping, incl across zeros
    subs = [(r.randint(412, 899), r.randint(128, 399)) for _ in range(5)] + [(400, 168), (703, 259), (1000, 437), (5002, 1785), (3040, 1592)]
    S.set(2, "Subtracting with Regrouping",
        learnbox("<p>Start with the ones. If the top digit is too small, <b>borrow</b> 1 from the next place (it becomes 10 more in this place). "
                 "<b>Across zeros:</b> for 503 − 128, you can't borrow from the 0 tens, so borrow from the 5 hundreds: 5 → 4, the tens become 10, then borrow "
                 "again: tens → 9, ones → 13. 13 − 8 = 5, 9 − 2 = 7, 4 − 1 = 3. Answer <b>375</b>. Check by adding: 375 + 128 = 503.</p>", yt("subtracting across zeros"))
        + vgrid([(a, b, "−") for a, b in subs], 5)
        + qs([("Nylah read 1,200 pages this year. Naomi read 875. How many more pages did Nylah read?", 1)], 11),
        ", ".join(f"{n+1}) {a-b:,}" for n, (a, b) in enumerate(subs)) + ", 11) 325")
    # D4 rounding & word problems
    rnd = [(r.randint(101, 989)) for _ in range(6)]
    S.set(3, "Rounding & Word Problems",
        learnbox("<p><b>Rounding:</b> look at the digit to the right of the place you're rounding to. <b>5 or more → round up; 4 or less → stay.</b> "
                 "647 to the nearest ten → <b>650</b>; to the nearest hundred → <b>600</b>. Use rounding to <b>estimate</b> and check whether an answer makes sense.</p>",
                 yt("rounding to the nearest 10 and 100"))
        + fill_table(["Number", "Nearest 10", "Nearest 100"], [[str(n), "", ""] for n in rnd], 28)
        + qs([("The family drove 278 miles on Monday and 345 on Tuesday. About how many miles is that? Exactly how many?", 1),
              ("A store had 1,000 water bottles and sold 638. How many are left?", ["362", "472", "1,638"]), ("Dad bought a couch for $489 and a table for $215. Estimate the total, then find the exact total.", 1),
              ("Nylah has 352 stickers. Nayeli has 189. Titus has 76. How many in all?", ["617", "541", "607"])]),
        "Rounding: " + "; ".join(f"{n}: {(n+5)//10*10}, {(n+50)//100*100}" for n in rnd)
        + ". 1) ≈ 300 + 300 = 600 (exact 623). 2) 362. 3) ≈ $500 + $200 = $700; exact $704. 4) 617.")
    cp = ["What is the value of the 4 in 4,906?", "Expanded form of 7,058", "653 + 289", "1,476 + 2,839", "800 − 356", "4,003 − 1,867",
          "Round 846 to the nearest hundred", "Round 846 to the nearest ten", "Order least→greatest: 2,099 · 2,909 · 2,990", "925 − 488",
          "A farm had 1,250 chickens and sold 375. How many left?", "Estimate 412 + 389, then solve exactly"]
    cpa = ["4,000", "7,000 + 50 + 8", "942", "4,315", "444", "2,136", "800", "850", "2,099, 2,909, 2,990", "437", "875", "≈ 800; 801"]
    S.set(4, "Level 2 Checkpoint",
        learnbox("<p><b>Checkpoint!</b> 12 problems. Show your work. <b>Pass = 10 or more (80%)</b> → move on to Level 3 (multiplication & division). "
                 "Less than 10? We'll repeat the tricky parts next week — no big deal.</p>")
        + hgrid([e + "<div class='ln' style='height:30px'></div>" for e in cp], 2, "13pt", 4) + '<div class="big">Score: ______ / 12</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(cpa)))
    return S

def english():
    S = Subject(K, "English", "Week 2 · Parts of Speech Power-Up")
    S.set(0, "Nouns & Pronouns",
        learnbox("<p>A <b>noun</b> names a person, place, thing, or idea (<i>sister, Florida, guitar, courage</i>). <b>Common nouns</b> are general (city); "
                 "<b>proper nouns</b> name a specific one and are capitalized (Jacksonville). A <b>pronoun</b> takes the place of a noun so we don't repeat it: "
                 "<i>I, me, you, he, him, she, her, it, we, us, they, them</i>. Use <b>subject pronouns</b> (I, he, she, we, they) as the subject and "
                 "<b>object pronouns</b> (me, him, her, us, them) after verbs and prepositions. Test: <i>Naomi and (I / me) went</i> → remove “Naomi and” → “I went.”</p>",
                 yt("nouns and pronouns middle school"))
        + '<div class="lab">Underline every noun. Circle every pronoun.</div>'
        + ol(["Nylah gave her brother a book about courage.", "They drove to St. Augustine on Saturday.", "Grandma baked us a pie, and it was delicious.",
              "The dog followed me to the mailbox."])
        + '<div class="lab">Circle the correct pronoun.</div>'
        + ol([f"Mom asked Nevaeh and {pick('I', 'me')} to fold towels.", f"{pick('She', 'Her')} and Naomi sang in the choir.", f"Between you and {pick('I', 'me')}, this is the best pie.",
              f"Dad and {pick('we', 'us')} cleaned the garage.", f"The prize went to {pick('they', 'them')}."], 5)
        + qs([("Write a sentence with a proper noun, a common noun, and a pronoun. Label each.", 2)], 10),
        "1) nouns Nylah, brother, book, courage; pronoun her. 2) nouns St. Augustine, Saturday; pronoun They. 3) nouns Grandma, pie; pronouns us, it. 4) nouns dog, mailbox; pronoun me. "
        "5) me 6) She 7) me 8) we 9) them. 10) varies.")
    S.set(1, "Verbs",
        learnbox("<p>A <b>verb</b> shows action or state of being. <b>Action verbs</b> show what someone does (<i>run, think, sing</i>). <b>Linking verbs</b> connect the "
                 "subject to a word that describes it — mostly forms of <i>be</i> (am, is, are, was, were) plus <i>seem, become, feel, look, taste</i> "
                 "(<i>The soup <b>tastes</b> salty.</i>). <b>Helping verbs</b> team up with a main verb: <i>She <b>has</b> finished. We <b>will</b> leave. "
                 "They <b>were</b> laughing.</i></p>", yt("action linking helping verbs"))
        + '<div class="lab">Label the underlined verb: A (action), L (linking), or H (helping).</div>'
        + mark_list(["The baby <u>giggled</u> at the dog.", "Dinner <u>smells</u> amazing.", "We <u>are</u> going to church tonight.", "Nevaeh <u>is</u> the oldest.",
                     "Titus <u>threw</u> the ball over the fence.", "You <u>should</u> drink more water.", "The flowers <u>looked</u> wilted.", "I <u>have</u> read that book twice."],
                    ["A", "L", "H"])
        + qs([("Which sentence has a helping verb + main verb?", ["We are singing in church.", "We sang in church.", "Church was fun."]), ("Write two sentences with <i>feel</i>: one as an action verb, one as a linking verb.", 2),
              ("Change the tense of <i>Gideon blows the trumpet.</i> Which shows past, then future?", ["blew; will blow", "blowed; will blew", "blown; blows"])], 9),
        "1 A, 2 L, 3 H, 4 L, 5 A, 6 H, 7 L, 8 H. 9) We are singing in church. 10) e.g., I feel the soft blanket (action) / I feel tired (linking). 11) blew; will blow.")
    S.set(2, "Adjectives & Adverbs",
        learnbox("<p><b>Adjectives</b> describe nouns — they tell <i>which one, what kind, how many</i> (<i>three <b>small</b> puppies</i>). The articles <i>a, an, the</i> are "
                 "adjectives too. <b>Adverbs</b> describe verbs, adjectives, or other adverbs — they tell <i>how, when, where, how much</i> (<i>She sang <b>beautifully</b>. "
                 "We left <b>early</b>. It was <b>very</b> cold.</i>). Many adverbs end in <b>-ly</b>, but not all (<i>soon, never, very, here</i>). "
                 "Common mix-up: <i>good</i> is an adjective, <i>well</i> is an adverb — <i>She plays <b>well</b>.</i></p>", yt("adjectives and adverbs middle school"))
        + '<div class="lab">Write ADJ or ADV above each underlined word, then draw an arrow to the word it describes.</div>'
        + ol(["The <u>tired</u> kids walked <u>slowly</u> home.", "Grace <u>quietly</u> opened the <u>squeaky</u> door.", "It was an <u>extremely</u> <u>hot</u> afternoon.",
              "The choir sang <u>loudly</u> and <u>joyfully</u>.", "<u>Seven</u> <u>fluffy</u> chicks hatched <u>yesterday</u>."])
        + '<div class="lab">Circle the correct word.</div>' + ol([f"Nylah did {pick('good', 'well')} on her test.", f"That pie smells {pick('good', 'well')}.", f"He ran {pick('quick', 'quickly')} to the door.", f"The water is {pick('real', 'really')} cold."], 6)
        + qs([("Rewrite this boring sentence with at least two adjectives and one adverb: <i>The dog ran.</i>", 2)], 10),
        "1) tired ADJ→kids, slowly ADV→walked. 2) quietly ADV→opened, squeaky ADJ→door. 3) extremely ADV→hot, hot ADJ→afternoon. 4) loudly, joyfully ADV→sang. "
        "5) Seven, fluffy ADJ→chicks; yesterday ADV→hatched. 6) well 7) good 8) quickly 9) really. 10) varies.")
    S.set(3, "Prepositions, Conjunctions & Interjections",
        learnbox("<p>A <b>preposition</b> shows how a noun relates to another word — often location or time: <i>in, on, under, over, behind, between, during, after, "
                 "with, to, from, of</i>. It starts a <b>prepositional phrase</b> that ends with a noun: <i>under the table, after dinner</i>. A <b>conjunction</b> "
                 "joins words or ideas: <i>and, but, or, so, because, although</i>. An <b>interjection</b> shows strong feeling: <i>Wow! Oh no! Hooray!</i> "
                 "Now you know all <b>8 parts of speech</b>: noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection.</p>", yt("prepositions conjunctions interjections"))
        + '<div class="lab">Put parentheses around each prepositional phrase. Circle the conjunctions. Box the interjections.</div>'
        + ol(["Wow, the cat jumped over the fence and into the garden.", "We waited in the car because it was raining.", "After church, Nevaeh and Nylah walked to the park.",
              "Oh no! The cake fell off the counter.", "Put the books on the shelf or under the bed."])
        + qs([("Write a sentence with two prepositional phrases.", 1), ("Which sentence uses an interjection AND a conjunction?", ["Hooray, the rain stopped and we can play!", "The rain stopped at noon.", "We played under the tree."]),
              ("Which list is all 8 parts of speech?", ["noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection", "noun, verb, adjective, adverb, sentence, paragraph, comma, period", "noun, pronoun, verb, subject, predicate, clause, phrase, article"])], 6),
        "1) Wow (interj.); (over the fence) (into the garden); and. 2) (in the car); because. 3) (After church) (to the park); and. 4) Oh no (interj.); (off the counter). "
        "5) (on the shelf) (under the bed); or. 6) varies. 7) Hooray, the rain stopped and we can play! 8) noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz.</b> Label the part of speech of each underlined word. Then finish the questions. Goal: 12 of 15.</p>")
        + '<div style="font-size:13pt;line-height:2">1. <u>Wow</u>, that was close! &nbsp; 2. <u>She</u> laughed. &nbsp; 3. The <u>tall</u> tree swayed. &nbsp; 4. We ran <u>quickly</u>.<br>'
          '5. The ball rolled <u>under</u> the porch. &nbsp; 6. I like tea <u>and</u> cookies. &nbsp; 7. <u>Jacksonville</u> is big. &nbsp; 8. Dad <u>fixed</u> the sink.<br>'
          '9. The soup <u>was</u> hot. &nbsp; 10. They <u>will</u> arrive soon.</div>'
        + mark_list([f"<u>{w}</u>" for w in ["Wow", "She", "tall", "quickly", "under", "and", "Jacksonville", "fixed", "was", "will"]],
                    ["noun", "pronoun", "verb", "adj.", "adv.", "prep.", "conj.", "interj."], cols=1)
        + qs([("Fix the pronoun: <i>Him and me went fishing.</i>", ["He and I went fishing.", "Him and I went fishing.", "Me and him went fishing."]), (f"<i>You did {pick('good', 'well')} on that project.</i>", 0),
              ("Write a sentence with a linking verb and an adjective.", 1), ("Write a sentence with an adverb that does NOT end in -ly.", 1),
              ("Write a sentence using all of these: a pronoun, an action verb, a preposition.", 2)], 11),
        "1 interjection, 2 pronoun, 3 adjective, 4 adverb, 5 preposition, 6 conjunction, 7 noun (proper), 8 verb (action), 9 verb (linking), 10 verb (helping). "
        "11) He and I went fishing. 12) well. 13–15 vary.")
    return S

CELL = ('<svg width="330" height="230" viewBox="0 0 330 230"><ellipse cx="165" cy="115" rx="158" ry="104" fill="#fff" stroke="#1f2a5c" stroke-width="3"/>'
        '<circle cx="150" cy="110" r="38" fill="#f1ebfd" stroke="#6d28d9" stroke-width="2.5"/><circle cx="158" cy="104" r="11" fill="#d9ccf5" stroke="#6d28d9"/>'
        '<ellipse cx="250" cy="80" rx="26" ry="12" fill="#eef1fb" stroke="#2f5bd3" stroke-width="2"/><path d="M230,80 q8,-9 14,0 t14,0 t14,0" fill="none" stroke="#2f5bd3"/>'
        '<ellipse cx="80" cy="160" rx="24" ry="11" fill="#eef1fb" stroke="#2f5bd3" stroke-width="2"/><path d="M60,160 q7,-8 13,0 t13,0 t13,0" fill="none" stroke="#2f5bd3"/>'
        '<circle cx="245" cy="150" r="14" fill="#fff" stroke="#a21caf" stroke-width="2"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#1f2a5c"/>' for x, y in [(95, 70), (110, 60), (205, 175), (215, 168), (120, 185), (270, 115), (200, 50)])
        + "".join(f'<text x="{x}" y="{y}" font-size="15" font-weight="700" fill="#a21caf">{t}</text>' for t, x, y in
                  [("1", 6, 70), ("2", 146, 66), ("3", 205, 125), ("4", 280, 72), ("5", 92, 56), ("6", 262, 160)]) + '</svg>')

def science():
    S = Subject(K, "Science", "Week 2 · Cells: Building Blocks of Life")
    S.set(0, "Cell Theory",
        learnbox("<p>In 1665, <b>Robert Hooke</b> looked at a thin slice of cork under an early microscope and saw tiny boxes. He called them <b>cells</b>. "
                 "Over the next 200 years, scientists discovered that every living thing is built from cells. This became the <b>cell theory</b>: "
                 "<b>(1)</b> all living things are made of one or more cells; <b>(2)</b> the cell is the basic unit of structure and function in living things; "
                 "<b>(3)</b> all cells come from other cells. Some living things are a single cell (<b>unicellular</b>, like bacteria); you are "
                 "<b>multicellular</b> — about 30 trillion cells, all working together!</p>", yt("cell theory for middle school"))
        + qs([("Who first named cells, and what was he looking at?", ["Robert Hooke — a slice of cork", "Isaac Newton — an apple", "Louis Pasteur — milk"]), ("Write the three parts of the cell theory in your own words.", 4),
              ("Which is true?", ["Bacteria are unicellular; people are multicellular.", "Bacteria are multicellular; people are unicellular.", "Both bacteria and people are one cell."]),
              ("Psalm 139:14 says we are “fearfully and wonderfully made.” How does knowing you're made of trillions of cooperating cells connect to that verse?", 3)]),
        "1) Robert Hooke, cork. 2) all living things are made of cells; cell is the basic unit; cells come from cells. 3) Bacteria are unicellular; people are multicellular. 4) opinion.")
    S.set(1, "Parts of an Animal Cell",
        learnbox("<p>Cells have tiny parts called <b>organelles</b>, each with a job — like rooms in a house. The <b>cell membrane</b> is the flexible outer edge that controls what "
                 "goes in and out. The <b>nucleus</b> is the control center holding DNA (the instructions). <b>Cytoplasm</b> is the jelly-like fluid where everything "
                 "floats. <b>Mitochondria</b> are the powerhouses that turn food into energy. <b>Ribosomes</b> build proteins. <b>Vacuoles</b> store water and "
                 "nutrients. <b>Lysosomes</b> break down waste.</p>", yt("animal cell organelles for kids"))
        + f'<div class="flexrow" style="align-items:center">{CELL}<div class="grow"><div class="lab">Label the diagram.</div>'
        + "".join(f'<div style="padding:3px 0"><b>{n}.</b> <span class="blank-ln" style="min-width:170px"></span></div>' for n in range(1, 7)) + '</div></div>'
        + '<div class="lab">Match the organelle to its job.</div>'
        + fill_table(["Job", "Organelle"], [["Control center with DNA", ""], ["Makes energy", ""], ["Controls what enters and leaves", ""], ["Builds proteins", ""], ["Cleans up waste", ""]], 26),
        "Diagram: 1 cell membrane, 2 nucleus, 3 cytoplasm, 4 mitochondria, 5 ribosomes, 6 vacuole (accept lysosome). "
        "Jobs: nucleus, mitochondria, cell membrane, ribosomes, lysosomes.")
    S.set(2, "Plant Cells",
        learnbox("<p>Plant cells have everything animal cells have, plus three extras. A stiff <b>cell wall</b> outside the membrane gives support (that's why celery is crunchy). "
                 "<b>Chloroplasts</b> contain green chlorophyll and use sunlight to make food — <b>photosynthesis</b>. And plant cells have one huge "
                 "<b>central vacuole</b> that stores water; when it's full the plant stands tall, and when it empties the plant wilts. Plant cells are usually "
                 "boxy; animal cells are rounder.</p>", yt("plant cell vs animal cell"))
        + '<div class="lab">Compare: write each part in the right section.</div>'
        + '<svg width="620" height="250" style="align-self:center"><circle cx="220" cy="125" r="118" fill="none" stroke="#2f5bd3" stroke-width="2.5"/>'
          '<circle cx="400" cy="125" r="118" fill="none" stroke="#6d28d9" stroke-width="2.5"/><text x="150" y="20" font-size="15" font-weight="700" fill="#2f5bd3">Animal only</text>'
          '<text x="400" y="20" font-size="15" font-weight="700" fill="#6d28d9">Plant only</text><text x="282" y="125" font-size="13" font-weight="700" fill="#1f2a5c">Both</text></svg>'
        + '<div>Word bank: <span class="pill">cell wall</span><span class="pill">nucleus</span><span class="pill">chloroplasts</span><span class="pill">cell membrane</span>'
          '<span class="pill">mitochondria</span><span class="pill">large central vacuole</span><span class="pill">small vacuoles</span><span class="pill">cytoplasm</span><span class="pill">ribosomes</span></div>'
        + qs([("Why does a plant wilt when it isn't watered?", ["Its central vacuole loses water, so the cells go limp.", "Its chloroplasts fall out.", "Its cell wall melts."]), ("Why don't animal cells need chloroplasts?", 2)]),
        "Animal only: small vacuoles (lysosomes). Plant only: cell wall, chloroplasts, large central vacuole. Both: nucleus, cell membrane, mitochondria, cytoplasm, ribosomes. "
        "1) central vacuole loses water so cells lose firmness. 2) animals get energy by eating food instead of making it from sunlight.")
    S.set(3, "Levels of Organization",
        learnbox("<p>In multicellular living things, cells are organized in levels, from smallest to largest: <b>cells → tissues → organs → organ systems → organism</b>. "
                 "A <b>tissue</b> is a group of similar cells doing the same job (muscle tissue). An <b>organ</b> is made of different tissues working together "
                 "(the heart). An <b>organ system</b> is a group of organs with one big job (the circulatory system: heart, blood vessels, blood). All the systems "
                 "together make an <b>organism</b> — you!</p>", yt("levels of organization cells tissues organs"))
        + '<div class="lab">Number each in order from smallest (1) to largest (5).</div>'
        + mark_list(["organ system", "cell", "organism", "tissue", "organ"], ["1", "2", "3", "4", "5"], cols=1)
        + '<div class="lab">Circle what each example is.</div>'
        + mark_list(["stomach", "a red blood cell", "digestive system", "a golden retriever", "muscle tissue", "lungs", "nervous system", "a single skin cell"], ["cell", "tissue", "organ", "system", "organism"], cols=1)
        + qs([("Choose one organ system. Name it, list two organs in it, and tell its job.", 3)], 14),
        "Order: cell 1, tissue 2, organ 3, organ system 4, organism 5. stomach organ; red blood cell cell; digestive system organ system; golden retriever organism; "
        "muscle tissue tissue; lungs organ; nervous system organ system; skin cell cell. 14) e.g., respiratory: lungs, trachea — brings in oxygen.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — cells. Goal: 8 of 10.</p>")
        + qs([("State the three parts of the cell theory.", 3), ("Who named the cell?", ["Robert Hooke", "Charles Darwin", "Albert Einstein"]), ("Which organelle is the control center?", ["nucleus", "mitochondria", "vacuole"]),
              ("Which organelle releases energy from food?", ["mitochondria", "ribosomes", "cell wall"]), ("Which three parts do plant cells have that animal cells don't?", ["cell wall, chloroplasts, large central vacuole", "nucleus, cytoplasm, ribosomes", "mitochondria, lysosomes, cell membrane"]),
              ("What does the cell membrane do?", ["controls what enters and leaves", "makes food from sunlight", "stores DNA"]), ("What is photosynthesis, and where does it happen?", 2),
              ("Put in order: organ, cell, organism, tissue, organ system.", ["cell, tissue, organ, organ system, organism", "organism, organ system, organ, tissue, cell", "cell, organ, tissue, organism, organ system"]), ("Is a bacterium unicellular or multicellular?", ["unicellular", "multicellular"]),
              ("Give an example of a tissue and an organ.", 1)]),
        "1) all living things are made of cells; basic unit; cells come from cells. 2) Robert Hooke. 3) nucleus. 4) mitochondria. 5) cell wall, chloroplasts, large central vacuole. "
        "6) controls what enters and leaves. 7) making food from sunlight; in chloroplasts. 8) cell, tissue, organ, organ system, organism. 9) unicellular. 10) e.g., muscle tissue; heart.")
    return S

def civics():
    S = Subject(K, "Civics", "Week 2 · The Three Branches")
    S.set(0, "The Constitution",
        learnbox("<p>After winning independence, America first tried the Articles of Confederation, but the national government was too weak. In <b>1787</b>, delegates met in "
                 "Philadelphia and wrote the <b>U.S. Constitution</b>, the supreme law of the land. It begins with the <b>Preamble</b> — “We the People” — showing "
                 "that power comes from the citizens. To keep any one group from getting too powerful, the Constitution splits power three ways: "
                 "<b>separation of powers</b>. The <b>Legislative</b> branch makes the laws, the <b>Executive</b> branch carries out the laws, and the "
                 "<b>Judicial</b> branch interprets the laws. The first 10 amendments, the <b>Bill of Rights</b>, protect freedoms like speech and religion.</p>",
                 yt("three branches of government for kids"))
        + fill_table(["Branch", "Main job", "Who is in it?"], [["Legislative", "", ""], ["Executive", "", ""], ["Judicial", "", ""]], 34)
        + qs([("Why did the Articles of Confederation need to be replaced?", ["The national government was too weak.", "The king wanted them gone.", "They gave the President too much power."]), ("What do the words “We the People” tell us?", ["Power comes from the citizens.", "Only the people in Philadelphia could vote.", "The President speaks for everyone."]),
              ("Why did the Founders divide power into three branches?", 2), ("Jeremiah 17:9 says the human heart is deceitful. How might that truth explain why the Founders didn't want to trust any one person with all the power?", 3)]),
        "Table: make laws — Congress; carry out laws — President/VP/Cabinet; interpret laws — Supreme Court & federal courts. 1) national government too weak. 2) power comes from the people. "
        "3) to stop any one group from getting too much power. 4) people are sinful, so power needs limits.")
    S.set(1, "Legislative Branch",
        learnbox("<p>Article I creates <b>Congress</b>, which has two houses. The <b>Senate</b> has <b>100</b> senators — <b>2 per state</b> — who serve <b>6-year</b> terms. "
                 "The <b>House of Representatives</b> has <b>435</b> members, divided among states by <b>population</b>, who serve <b>2-year</b> terms. "
                 "Florida, with a big population, has 28 representatives. Congress writes and passes laws, collects taxes, declares war, and approves the budget. "
                 "A <b>bill</b> must pass <b>both</b> houses and then be signed by the President to become a law.</p>", yt("how a bill becomes a law"))
        + fill_table(["", "Senate", "House of Representatives"], [["Number of members", "", ""], ["How seats are divided", "", ""], ["Length of term", "", ""], ["Florida's members", "", ""]], 30)
        + qs([("Why do you think the Founders gave every state the same number of senators but divided House seats by population?", 3),
              ("Which shows the steps for a bill to become a law?", ["passes the House → passes the Senate → President signs", "President writes it → Supreme Court signs it", "passes the Senate → Supreme Court votes → states sign"]), ("Name two powers of Congress.", 1)]),
        "Senate 100 / 2 per state / 6 yrs / 2; House 435 / by population / 2 yrs / 28. 1) balance big & small states (the Great Compromise). "
        "2) bill introduced → passes House → passes Senate → President signs (or veto/override). 3) make laws, tax, declare war, budget.")
    S.set(2, "Executive Branch",
        learnbox("<p>Article II creates the <b>executive branch</b>, led by the <b>President</b>, who carries out and enforces the laws. The President serves a <b>4-year term</b> "
                 "and can be elected only <b>twice</b>. To run, a person must be at least <b>35</b>, a <b>natural-born citizen</b>, and a U.S. resident for 14 years. "
                 "The President is <b>Commander in Chief</b> of the military, makes treaties (with Senate approval), appoints judges, and can <b>veto</b> (reject) bills. "
                 "The <b>Vice President</b> takes over if needed and leads the Senate. The <b>Cabinet</b> — heads of departments like Education and Defense — advises the President.</p>",
                 yt("executive branch for kids"))
        + qs([("Which are the three requirements to be President?", ["at least 35, natural-born citizen, U.S. resident 14 years", "at least 21, a lawyer, lived in D.C.", "at least 40, served in Congress, owns land"]), ("How long is a term? How many terms can a President serve?", ["4 years; two terms", "6 years; one term", "2 years; no limit"]),
              ("What is a veto?", ["the President rejecting a bill passed by Congress", "a new law", "a court ruling"]), ("What does “Commander in Chief” mean?", ["leader of the armed forces", "leader of the Senate", "head of the Supreme Court"]), ("What does the Cabinet do?", 2),
              ("1 Timothy 2:1–2 tells Christians to pray for “kings and all who are in high positions.” Write a short prayer for our nation's leaders.", 4)]),
        "1) 35+, natural-born citizen, 14 years resident. 2) 4 years; two terms. 3) rejecting a bill passed by Congress. 4) leader of the armed forces. 5) heads departments and advises the President. 6) varies.")
    S.set(3, "Judicial Branch + Checks & Balances",
        learnbox("<p>Article III creates the <b>judicial branch</b>: the <b>Supreme Court</b> and lower federal courts. The Supreme Court has <b>9 justices</b> who serve "
                 "<b>for life</b> so they can decide cases fairly without worrying about re-election. Courts decide what laws mean, and through "
                 "<b>judicial review</b> they can strike down a law that goes against the Constitution. <b>Checks and balances</b> let each branch limit the others: "
                 "the President can veto a bill; Congress can override a veto with a 2/3 vote; the Senate approves judges; courts can rule laws unconstitutional.</p>",
                 yt("checks and balances for kids"))
        + '<div class="lab">Which branch is checking which?</div>'
        + fill_table(["Check", "Branch doing the check", "Branch being checked"],
                     [["President vetoes a bill", "", ""], ["Congress overrides a veto", "", ""], ["Court rules a law unconstitutional", "", ""],
                      ["Senate rejects a Supreme Court nominee", "", ""], ["President appoints a judge", "", ""]], 28)
        + qs([("How many justices are on the Supreme Court? How long do they serve?", ["9, for life", "12, for 6 years", "100, for 4 years"]), ("What is judicial review?", ["courts deciding whether a law follows the Constitution", "Congress reviewing the budget", "the President reviewing judges"]), ("Why are checks and balances important?", 2)]),
        "veto: Exec → Leg; override: Leg → Exec; unconstitutional: Jud → Leg (or Exec); reject nominee: Leg → Exec/Jud; appoint judge: Exec → Jud. "
        "1) 9, for life. 2) courts deciding whether a law follows the Constitution. 3) keeps any branch from getting too much power.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — the Constitution and three branches. Goal: 8 of 10.</p>")
        + qs([("What year was the Constitution written?", ["1787", "1776", "1607"]), ("What are the first 10 amendments called?", ["the Bill of Rights", "the Preamble", "the Articles"]), ("Which branch makes laws? What is it called?", ["legislative — Congress", "executive — the Cabinet", "judicial — the Supreme Court"]),
              ("How many senators? Representatives?", ["100; 435", "50; 100", "435; 100"]), ("How old must the President be?", ["at least 35", "at least 18", "at least 50"]), ("What is a veto, and how can Congress override one?", 2),
              ("How many Supreme Court justices are there?", ["9", "7", "12"]), ("What is separation of powers?", 2), ("Give one example of checks and balances.", 1),
              ("Which branch do you think is most important? Defend your answer.", 3)]),
        "1) 1787. 2) Bill of Rights. 3) legislative — Congress. 4) 100; 435. 5) 35. 6) rejecting a bill; 2/3 vote of both houses. 7) 9. 8) dividing power among three branches. 9) e.g., veto. 10) opinion.")
    return S

def build():
    return [math(), english(), science(), civics()]
