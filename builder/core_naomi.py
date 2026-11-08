from core_common import *
from mathgen import *
import random

K = "Naomi"

def math():
    S = Subject(K, "Math", "Week 3 · Multiplying by One Digit"); r = random.Random(53)
    facts = [(r.randint(3, 9), r.randint(3, 9)) for _ in range(15)]
    tens = [(r.randint(2, 9), r.choice([10, 20, 30, 40, 50, 60, 70, 80, 90])) for _ in range(6)] + [(r.randint(2, 9), r.choice([100, 200, 300, 400, 500, 600, 700, 800, 900])) for _ in range(6)]
    S.set(0, "Facts, 10s & 100s",
        learnbox("<p>Strong <b>facts</b> make big multiplication easy, so warm up first! To multiply by a <b>multiple of 10 or 100</b>, multiply the "
                 "<b>basic fact</b>, then write the <b>zeros</b> on the end. 6 × 40: 6 × 4 = 24, add one zero → <b>240</b>. 7 × 300: 7 × 3 = 21, add two "
                 "zeros → <b>2,100</b>. Careful with 5s: 5 × 400 → 5 × 4 = 20, plus two zeros → <b>2,000</b> (three zeros in all!).</p>", yt("NM multiplying by multiples of 10 and 100"))
        + '<div class="lab">Part A · Facts warm-up. Write each answer.</div>'
        + hgrid([f"{a} × {b} = <span class='blank-ln' style='min-width:44px'></span>" for a, b in facts], 5, "13pt")
        + '<div class="lab">Part B · Multiply by 10s and 100s.</div>'
        + hgrid([f"{a} × {b} = <span class='blank-ln' style='min-width:70px'></span>" for a, b in tens], 3, "13.5pt", 4)
        + '<div class="lab">Part C</div>' + qs([("What is 8 × 50?", ["400", "40", "4,000"]), ("Which is the same as 9 × 600?", ["9 × 6, then add two zeros", "9 × 6, then add one zero", "9 + 600"]),
              ("A pack has 30 crackers. How many crackers are in 7 packs? Show your fact.", 2), ("Which is greater: 4 × 900 or 6 × 500?", ["4 × 900 (3,600 is more than 3,000)", "6 × 500", "They are equal."])]),
        "A: " + ", ".join(f"{n+1}) {a*b}" for n, (a, b) in enumerate(facts)) + ". B: " + ", ".join(f"{n+1}) {a*b:,}" for n, (a, b) in enumerate(tens))
        + ". C: 1) 400. 2) 9 × 6, then add two zeros (5,400). 3) 7 × 3 = 21 → 210 crackers. 4) 4 × 900 = 3,600 > 6 × 500 = 3,000.")
    easy = []
    while len(easy) < 5:
        a, b = r.randint(11, 44), r.randint(2, 4)
        if (a % 10) * b < 10 and (a // 10) * b < 10 and (a, b) not in easy: easy.append((a, b))
    hard = []
    while len(hard) < 10:
        a, b = r.randint(13, 98), r.randint(3, 9)
        if (a % 10) * b >= 10 and (a, b) not in hard: hard.append((a, b))
    p2 = easy + hard
    S.set(1, "2-Digit × 1-Digit",
        learnbox("<p>Write the bigger number on top and line up the ones. Multiply the <b>ones first</b>, then the tens. If the ones answer is 10 or more, "
                 "<b>carry</b>: write the ones digit and carry the tens digit to the top of the tens column. Multiply the tens, then <b>add</b> the carried number. "
                 "Example 47 × 6: 6 × 7 = 42 → write 2, carry 4. 6 × 4 = 24, + 4 = 28 → <b>282</b>. Problems 1–5 need no carrying.</p>", yt("NM 2 digit times 1 digit with carrying"))
        + vgrid([(a, b, "×") for a, b in p2], 5)
        + qs([("Each Sunday school class has 24 chairs. How many chairs are in 4 classes?", 1), ("When do you carry in multiplication?", ["when a place's answer is 10 or more", "every time", "only when multiplying by 9"]),
              ("In 38 × 5, after 5 × 8 = 40, what do you write and what do you carry?", ["write 0, carry 4", "write 4, carry 0", "write 40, carry nothing"]), ("Which answer makes sense for 52 × 4? (Hint: 50 × 4 = 200)", ["208", "28", "2,008"])], 16),
        ", ".join(f"{n+1}) {a*b:,}" for n, (a, b) in enumerate(p2)) + f". 16) 96 chairs. 17) when a place's answer is 10 or more. 18) write 0, carry 4 (38 × 5 = 190). 19) {52*4}.")
    p3 = [(r.randint(112, 989), r.randint(2, 9)) for _ in range(12)] + [(406, 7), (705, 4), (380, 6)]
    S.set(2, "3-Digit × 1-Digit",
        learnbox("<p>Same steps, one more place: <b>ones, tens, hundreds</b>. After each step, add the number you carried. Watch out for <b>zeros</b>: in 406 × 7, "
                 "7 × 6 = 42 → write 2, carry 4. 7 × 0 = 0, + 4 = <b>4</b> (don't forget the carry!). 7 × 4 = 28 → <b>2,842</b>. "
                 "Check: 406 is about 400, and 400 × 7 = 2,800 — close! ✔</p>", yt("NM 3 digit by 1 digit multiplication"))
        + vgrid([(a, b, "×") for a, b in p3], 5)
        + qs([("A church van drives 245 miles each month. How many miles in 6 months?", 1), ("Estimate 512 × 8 by rounding 512 to the nearest hundred.", ["500 × 8 = 4,000", "600 × 8 = 4,800", "512 + 8 = 520"]), ("A farm packs 168 strawberries in each crate. How many strawberries are in 5 crates?", 1), ("For 274 × 3, what is the first step?", ["3 × 4 = 12: write 2, carry 1", "3 × 2 = 6: write 6", "3 × 7 = 21: write 21"])], 16),
        ", ".join(f"{n+1}) {a*b:,}" for n, (a, b) in enumerate(p3)) + f". 16) {245*6:,} miles. 17) 500 × 8 = 4,000 (exact {512*8:,}). 18) {168*5} strawberries. 19) 3 × 4 = 12: write 2, carry 1 (274 × 3 = {274*3}).")
    wp = [("A box holds 24 crayons. How many crayons are in 6 boxes?", f"{24*6} crayons"),
          ("Each pew at church seats 8 people. There are 37 pews. How many people can sit down?", f"{8*37} people"),
          ("A pelican flies 128 miles a week along the coast. How many miles in 4 weeks?", f"{128*4} miles"),
          ("Mom buys 7 bags of oranges. Each bag has 15 oranges. How many oranges?", f"{7*15} oranges"),
          ("<b>Two steps:</b> Museum tickets cost $14 each. Dad buys 6 tickets and pays with a $100 bill. How much change does he get?", f"6 × $14 = ${6*14}; $100 − ${6*14} = ${100-6*14}")]
    S.set(3, "Word Problems",
        learnbox("<p>Multiply when you have <b>equal groups</b> and want the total. Clue words: <b>each, every, per, in all, times</b>. Read the problem, "
                 "circle the numbers, underline the question, solve with the standard steps, and write your answer with a <b>label</b> (crayons, miles, $). "
                 "In a <b>two-step</b> problem, solve step 1 first, then use that answer in step 2.</p>", yt("NM multiplication word problems"))
        + "".join(f'<div class="box"><b>{n+1}.</b> {q}<div class="grid2" style="margin-top:4px"><div>Work:<div class="ln" style="height:34px"></div></div><div>Answer (with label):<div class="ln" style="height:34px"></div></div></div></div>' for n, (q, a) in enumerate(wp))
        + qs([("Which clue words usually mean multiply?", ["each, every, in all", "left, fewer, take away", "share equally"]), ("A pack of gum has 5 pieces. Which number sentence finds the pieces in 9 packs?", ["9 × 5", "9 + 5", "9 − 5"])], 6),
        ", ".join(f"{n+1}) {a}" for n, (q, a) in enumerate(wp)) + ". 6) each, every, in all. 7) 9 × 5 = 45.")
    cp = ["7 × 8", "9 × 6", "40 × 7", "6 × 300", "32 × 3", "47 × 6", "253 × 4", "608 × 5",
          "A bookshelf has 5 shelves with 126 books on each. How many books?", "Naomi buys 4 packs of stickers with 25 in each. She gives away 18. How many are left?"]
    cpa = [f"{7*8}", f"{9*6}", f"{40*7}", f"{6*300:,}", f"{32*3}", f"{47*6}", f"{253*4:,}", f"{608*5:,}", f"{5*126} books", f"4 × 25 = {4*25}; {4*25} − 18 = {4*25-18} stickers"]
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz!</b> 10 problems. Write problems 5–8 up and down and show your carrying. Goal: 8 of 10 (80%).</p>")
        + hgrid([e + "<div class='ln' style='height:84px'></div>" for e in cp], 2, "13pt", 6) + '<div class="big">Score: ______ / 10</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(cpa)))
    return S

def english():
    S = Subject(K, "English", "Week 3 · All About Verbs")
    S.set(0, "Action Verbs",
        learnbox("<p>Every sentence needs a <b>verb</b>. An <b>action verb</b> tells what the subject <b>does</b>: <i>run, swim, sing, bake</i>. Some actions happen "
                 "inside your mind — <i>think, know, remember, love, pray</i> — and those are action verbs too! Test: can you put “I” or “they” in front of it? "
                 "<i>They jump</i> ✔ <i>They table</i> ✘. Strong writers pick <b>vivid</b> verbs: instead of “went,” try <i>raced, tiptoed, wandered</i>.</p>", yt("NE action verbs part 1"))
        + '<div class="lab">Is it an action verb? Circle Yes or No.</div>'
        + mark_list(["climb", "pillow", "whisper", "happy", "remember", "Jacksonville", "splash", "under"], ["Yes", "No"], cols=2)
        + '<div class="lab">Which word is the action verb?</div>'
        + qs([("The manatee nibbled the seagrass.", ["nibbled", "manatee", "seagrass"]), ("Naomi and Titus raced to the mailbox.", ["raced", "Titus", "mailbox"]),
              ("We pray before every meal.", ["pray", "every", "meal"]), ("Grandpa remembered the old hymn.", ["remembered", "Grandpa", "hymn"])], 9)
        + '<div class="lab">Replace the weak verb with a vivid one. Rewrite the sentence.</div>'
        + qs([("The dog <u>went</u> across the yard.", 1), ("The baby <u>said</u> something.", 1), ("Write a sentence about your morning with two action verbs. Underline them.", 2)], 13),
        "1) Yes 2) No 3) Yes 4) No 5) Yes 6) No 7) Yes 8) No. 9) nibbled 10) raced 11) pray 12) remembered. 13–14) vary (e.g., dashed, giggled). 15) varies — check for two underlined action verbs.")
    S.set(1, "Linking Verbs",
        learnbox("<p>A <b>linking verb</b> doesn't show action. It <b>links</b> the subject to a word that names or describes it. The most common are forms of "
                 "<b>be</b>: <i>am, is, are, was, were, be, being, been</i>. Others: <i>become, seem</i>, and the sense verbs <i>look, feel, taste, smell, sound</i>. "
                 "<i>The soup <b>tastes</b> salty</i> (linking). <i>Naomi <b>tastes</b> the soup</i> (action!). Trick: if you can swap in <b>is</b> and it still makes sense, it's linking.</p>",
                 yt("NE linking verbs part 5"))
        + '<div class="lab">Circle A for action verb or L for linking verb.</div>'
        + mark_list(["The gopher tortoise <u>is</u> slow.", "Mom <u>smelled</u> the roses.", "The roses <u>smelled</u> sweet.", "My sisters <u>were</u> excited.",
                     "Titus <u>became</u> sleepy.", "Dad <u>felt</u> the cold water.", "The music <u>sounds</u> beautiful.", "We <u>painted</u> the fence."], ["A", "L"], cols=1)
        + qs([("In “The alligator looks hungry,” which word does <i>looks</i> link to <i>alligator</i>?", ["hungry", "the", "looks"]), ("Which list has only linking verbs?", ["am, is, were, seem", "run, is, were, jump", "sing, look, kick, was"]),
              ("Write a sentence with a linking verb. Circle the linking verb and underline the word it links to.", 2), ("Use <i>feel</i> two ways: once as an action verb and once as a linking verb.", 2), ("Which sentence uses a sense verb as a <b>linking</b> verb?", ["The bread smells fresh.", "Titus smells the bread.", "Mom sniffs the bread."])], 9),
        "1) L 2) A 3) L 4) L 5) L 6) A 7) L 8) A. 9) hungry. 10) am, is, were, seem. 11) varies. 12) e.g., I feel the soft blanket (action); I feel tired (linking). 13) The bread smells fresh.")
    S.set(2, "Helping Verbs",
        learnbox("<p>A <b>helping verb</b> comes before the <b>main verb</b> and helps it. Together they make a <b>verb phrase</b>: <i>Naomi <b>is reading</b>. We <b>will visit</b> Grandma. "
                 "The kids <b>have finished</b>.</i> Learn the helping verbs in groups: <b>am, is, are, was, were, be, being, been · has, have, had · do, does, did · "
                 "can, could · will, would · shall, should · may, might, must</b>. The <b>main verb is always last</b> in the verb phrase.</p>", yt("NE helping verbs part 4"))
        + '<div class="lab">Write the helping verb and the main verb.</div>'
        + fill_table(["Sentence", "Helping verb", "Main verb"], [["The birds are singing.", "", ""], ["Mom has baked bread.", "", ""], ["We should clean our room.", "", ""],
                                                                 ["Titus can whistle.", "", ""], ["The river was rising.", "", ""]], 28)
        + '<div class="lab">Circle the helping verb that fits.</div>'
        + ol([f"Naomi {pick('is', 'are')} learning her verses.", f"They {pick('have', 'has')} gone to church.", f"I {pick('am', 'is')} helping Dad.", f"She {pick('does', 'do')} not like spiders."], 6)
        + qs([("Which sentence has a verb phrase?", ["The pelicans were diving.", "The pelicans dove.", "Pelicans eat fish."]), ("In a verb phrase, where is the main verb?", ["last", "first", "it can be anywhere"]),
              ("Write a sentence with a helping verb from the <i>can, could, should</i> group. Underline the whole verb phrase.", 2)], 10),
        "1) are / singing 2) has / baked 3) should / clean 4) can / whistle 5) was / rising. 6) is 7) have 8) am 9) does. 10) The pelicans were diving. 11) last. 12) varies.")
    vt = [("walk", "walked", "walks", "will walk"), ("jump", "jumped", "jumps", "will jump"), ("hurry", "hurried", "hurries", "will hurry"),
          ("run", "ran", "runs", "will run"), ("eat", "ate", "eats", "will eat"), ("write", "wrote", "writes", "will write")]
    S.set(3, "Verb Tenses",
        learnbox("<p>A verb's <b>tense</b> tells <b>when</b>. <b>Past</b> = already happened: most verbs add <b>-ed</b> (<i>walked</i>); if it ends in consonant + y, change y to i "
                 "(<i>hurried</i>). <b>Irregular</b> verbs change their spelling (<i>run → ran, eat → ate, go → went</i>). <b>Present</b> = now (<i>walks, walk</i>). "
                 "<b>Future</b> = will happen: use the helping verb <b>will</b> (<i>will walk</i>). Keep one tense in a story unless the time changes.</p>", yt("NE simple verb tenses part 3"))
        + '<div class="lab">Fill in the chart. (Present: use he or she.)</div>'
        + fill_table(["Verb", "Past", "Present (she…)", "Future"], [[v, "", "", ""] for v, *_ in vt], 28)
        + '<div class="lab">Circle the correct verb. Look for time clues!</div>'
        + ol([f"Yesterday we {pick('picked', 'will pick')} strawberries.", f"Tomorrow Dad {pick('will grill', 'grilled')} burgers.", f"Last week Naomi {pick('wrote', 'writes')} a letter.", f"Right now the baby {pick('sleeps', 'slept')}."], 1)
        + qs([("Which sentence is in future tense?", ["We will sing at church.", "We sang at church.", "We sing at church."]), ("Which past-tense verb is irregular?", ["went", "jumped", "played"]),
              ("Write three sentences about a trip to the beach: one past, one present, one future.", 3)], 5),
        "Chart: " + "; ".join(f"{v}: {a}, {b}, {c}" for v, a, b, c in vt) + ". 1) picked 2) will grill 3) wrote 4) sleeps. 5) We will sing at church. 6) went. 7) varies.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — verbs. Goal: 8 of 10.</p>")
        + qs([("What does an action verb tell?", ["what the subject does", "what the subject looks like", "where something is"]), ("Write the action verb: <i>The osprey snatched a fish.</i>", 1),
              ("In “The pie smells delicious,” <i>smells</i> is a…", ["linking verb", "action verb", "helping verb"]), ("Name four forms of the verb <i>be</i>.", 1),
              ("Find the verb phrase: <i>The children have planted a garden.</i>", ["have planted", "children have", "planted a garden"]), ("Write a sentence with a helping verb and underline the main verb.", 1),
              ("Past tense of <i>carry</i>:", ["carried", "carryed", "carries"]), ("Write the past and future of <i>sing</i>.", 1),
              ("Fix the tense: <i>Tomorrow I swam in the pool.</i>", ["Tomorrow I will swim in the pool.", "Tomorrow I swims in the pool.", "Tomorrow I swimmed in the pool."]), ("Use <i>taste</i> as an action verb in one sentence and as a linking verb in another.", 2)]),
        "1) what the subject does. 2) snatched. 3) linking verb. 4) any four: am, is, are, was, were, be, being, been. 5) have planted. 6) varies. 7) carried. 8) sang, will sing. "
        "9) Tomorrow I will swim in the pool. 10) e.g., I taste the cake (action); The cake tastes sweet (linking).")
    return S

def science():
    S = Subject(K, "Science", "Week 3 · Habitats & Adaptations")
    S.set(0, "Habitats",
        learnbox("<p>A <b>habitat</b> is the home where a plant or animal lives. It gives four things: <b>food, water, shelter, and space</b>. "
                 "<b>Forests</b> have many trees (deer, owls, squirrels). <b>Deserts</b> get less than 10 inches of rain a year (camels, lizards, cactus). "
                 "<b>Oceans</b> are salt water (sea turtles, dolphins, coral). <b>Wetlands</b> are land soaked with water, like marshes and swamps (herons, alligators). "
                 "<b>Grasslands</b> are wide open fields of grass (bison, zebras, prairie dogs). Last week's food webs all live inside habitats!</p>", yt("NS habitats polar desert forest grassland aquatic"))
        + '<div class="lab">Circle the habitat: F forest · D desert · O ocean · W wetland · G grassland.</div>'
        + mark_list(["camel", "bison", "sea turtle", "great blue heron", "black bear", "dolphin", "saguaro cactus", "zebra", "alligator", "woodpecker"], ["F", "D", "O", "W", "G"], cols=2)
        + qs([("What four things does every habitat give?", ["food, water, shelter, space", "toys, food, water, sun", "only food and water"]), ("Which habitat gets less than 10 inches of rain a year?", ["desert", "wetland", "forest"]),
              ("Why couldn't a dolphin live in a desert?", 2)], 11)
        + '<div class="lab">Your backyard is a habitat! Draw it and label one source of food, water, shelter, and space.</div><div class="answer-space" style="min-height:140px"></div>',
        "camel D, bison G, sea turtle O, heron W, bear F, dolphin O, cactus D, zebra G, alligator W, woodpecker F. 11) food, water, shelter, space. 12) desert. 13) it needs water to live/breathe and swim; no water or fish to eat.")
    S.set(1, "Physical Adaptations",
        learnbox("<p>An <b>adaptation</b> is a feature that helps a living thing survive in its habitat. <b>Physical adaptations</b> are body parts or body features: "
                 "a duck's <b>webbed feet</b> paddle; a camel's <b>hump</b> stores fat and its long eyelashes block sand; a polar bear's thick fur and <b>blubber</b> keep it warm; "
                 "a cactus's <b>spines</b> protect it and its waxy stem holds water. <b>Camouflage</b> is coloring that blends in (a flounder on sand). "
                 "<b>Mimicry</b> means looking like something dangerous — Florida's harmless scarlet kingsnake looks like a venomous coral snake!</p>", yt("NS physical adaptations in animals"))
        + '<div class="lab">How does each adaptation help?</div>'
        + fill_table(["Animal", "Adaptation", "How it helps"], [["duck", "webbed feet", ""], ["owl", "big eyes", ""], ["porcupine", "sharp quills", ""], ["polar bear", "white fur", ""]], 32)
        + qs([("Which is a physical adaptation?", ["a pelican's pouch", "a bird flying south", "a bear sleeping all winter"]), ("What does a camel's hump store?", ["fat", "water", "sand"]),
              ("What is mimicry?", ["looking like something dangerous", "changing habitats", "eating plants"]), ("Why do many desert plants have thick, waxy stems?", ["to hold water", "to catch fish", "to stay warm in snow"])], 5)
        + '<div class="lab">Invent an animal for a wetland. Draw it and label 3 physical adaptations.</div><div class="answer-space" style="min-height:150px"></div>',
        "duck: paddles in water; owl: sees at night; porcupine: protects from predators; polar bear: camouflage in snow. 5) a pelican's pouch. 6) fat. 7) looking like something dangerous. 8) to hold water.")
    S.set(2, "Behavioral Adaptations",
        learnbox("<p><b>Behavioral adaptations</b> are things an animal <b>does</b> to survive. <b>Migration</b>: moving to a new place each season — monarch butterflies fly to Mexico, "
                 "and American white pelicans spend the winter in Florida. <b>Hibernation</b>: a deep winter sleep where the body slows way down (groundhogs, some bats). "
                 "Opossums <b>play dead</b>; fish swim in <b>schools</b>; many animals hunt at night (<b>nocturnal</b>). Camouflage works best with a behavior: "
                 "a rabbit <b>freezes</b> so its brown fur hides it. Many behaviors are <b>instincts</b> — God built them in, no one teaches them.</p>", yt("NS behavioral adaptations in animals"))
        + '<div class="lab">Circle P (physical) or B (behavioral).</div>'
        + mark_list(["a monarch flies to Mexico", "a duck's webbed feet", "a groundhog hibernates", "an opossum plays dead", "a turtle's hard shell",
                     "a bat hunts at night", "a fish swims in a school", "an alligator's strong jaws"], ["P", "B"], cols=1)
        + qs([("Why do some birds migrate south in fall?", ["to find warmer weather and food", "to visit other birds", "to lay eggs in snow"]), ("What happens to an animal's body during hibernation?", ["it slows way down", "it grows a new tail", "it speeds up"]),
              ("What is an instinct?", ["a behavior an animal is born knowing", "a trick an animal is taught", "a kind of habitat"]), ("Pick one animal. Describe one physical AND one behavioral adaptation it has.", 3)], 9),
        "1) B 2) P 3) B 4) B 5) P 6) B 7) B 8) P. 9) to find warmer weather and food. 10) it slows way down. 11) a behavior it is born knowing. 12) varies.")
    S.set(3, "Florida Habitats",
        learnbox("<p>Florida is full of habitats! The <b>St. Johns River</b> is Florida's longest river (about 310 miles) and one of the few that flows <b>north</b> — "
                 "right through Jacksonville to the Atlantic. Its <b>wetlands</b> clean water and are nurseries for fish. The <b>manatee</b> is a gentle herbivore that eats seagrass; "
                 "cold water below about 68°F can make it sick, so in winter it <b>migrates</b> to warm springs like Blue Spring on the St. Johns. The <b>alligator</b> has eyes and "
                 "nostrils on <b>top</b> of its head so it can hide underwater and still see and breathe. The <b>gopher tortoise</b> lives in dry, sandy uplands and uses shovel-like "
                 "front legs to dig burrows about <b>15 feet long</b> — more than 350 other kinds of animals use them!</p>", yt("NS exploring Florida's wetlands"))
        + fill_table(["Animal", "Habitat", "Physical adaptation", "Behavioral adaptation"], [["manatee", "", "", ""], ["alligator", "", "", ""], ["gopher tortoise", "", "", ""]], 62)
        + qs([("Which way does the St. Johns River flow?", ["north", "south", "west"]), ("Why do manatees gather at warm springs in winter?", ["cold water can make them sick", "to find sand to dig in", "to hunt fish"]),
              ("How does the alligator's head help it hunt?", ["eyes and nostrils on top let it hide underwater", "it has a beak", "it has a long neck"]), ("Why is the gopher tortoise's burrow important to other animals?", 2),
              ("Name a Florida habitat near your home and one animal you have seen there.", 2)]),
        "Table: manatee — river/springs/coast; flippers/paddle tail, thick body; migrates to warm springs. Alligator — wetlands/rivers; eyes + nostrils on top, strong jaws; basks in sun, hides underwater. "
        "Gopher tortoise — dry sandy uplands; shovel-like legs, hard shell; digs burrows. 1) north. 2) cold water can make them sick. 3) eyes and nostrils on top. 4) 350+ animals use it for shelter. 5) varies.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — habitats and adaptations. Goal: 8 of 10.</p>")
        + qs([("What is a habitat?", ["the home where a living thing lives", "a kind of food", "an animal's body part"]), ("Name the four things a habitat gives.", 1),
              ("Which habitat is land soaked with water?", ["wetland", "desert", "grassland"]), ("What is an adaptation?", 1),
              ("A duck's webbed feet are a…", ["physical adaptation", "behavioral adaptation", "habitat"]), ("Migration means…", ["moving to a new place each season", "sleeping all winter", "blending in"]),
              ("Give one example of camouflage.", 1), ("Why do manatees swim to warm springs in winter?", ["cold water can make them sick", "to lay eggs", "to find gopher tortoises"]),
              ("Where does the gopher tortoise live?", ["dry, sandy uplands", "the deep ocean", "the Arctic"]), ("Job 12:7 says, “Ask the beasts, and they will teach you.” What has an animal taught you about God's design?", 2)]),
        "1) the home where a living thing lives. 2) food, water, shelter, space. 3) wetland. 4) a feature or behavior that helps it survive. 5) physical adaptation. 6) moving to a new place each season. "
        "7) e.g., a flounder on sand, a rabbit's brown fur. 8) cold water can make them sick. 9) dry, sandy uplands. 10) opinion.")
    return S

def fl_history():
    S = Subject(K, "Florida History", "Week 3 · Spanish & French Florida")
    S.set(0, "Ponce de León, 1513",
        learnbox("<p><b>Juan Ponce de León</b> sailed with Christopher Columbus on his second voyage in <b>1493</b> and later ruled Puerto Rico. In <b>April 1513</b> "
                 "he landed on Florida's east coast — no one knows the exact spot. It was the <b>Easter season</b>, called <i>Pascua Florida</i> (“flowery Easter”) in Spanish, "
                 "and the land was full of flowers, so he named it <b>La Florida</b>. The “Fountain of Youth” story was mostly added <b>later</b>."
                 " In <b>1521</b> he came back to start a colony on the southwest coast, but the <b>Calusa</b> fought back and he was wounded by an arrow. "
                 "He died soon after in Cuba.</p>", yt("NF learning about Ponce de Leon"))
        + '<div class="lab">Fact or legend? Circle F (fact) or L (legend).</div>'
        + mark_list(["Ponce de León reached Florida in 1513.", "He drank from a magic Fountain of Youth.", "He named the land La Florida.", "He sailed with Columbus in 1493.", "He was wounded fighting the Calusa."], ["F", "L"], cols=1)
        + qs([("Why did he choose the name La Florida?", ["It was the Easter season and full of flowers.", "He found gold there.", "His ship was named Florida."]), ("Which country did Ponce de León sail for?", ["Spain", "France", "England"]),
              ("What happened when he returned in 1521?", ["The Calusa fought back and he was wounded.", "He founded St. Augustine.", "He built a stone fort."]), ("How can you tell the difference between a fact and a legend in history?", 2)], 6)
        + '<div class="lab">Draw Ponce de León\'s ship arriving at a flowery Florida coast.</div><div class="answer-space" style="min-height:60px"></div>',
        "1) F 2) L 3) F 4) F 5) F. 6) Easter season (Pascua Florida) and flowers. 7) Spain. 8) Calusa fought back; wounded, died in Cuba. 9) facts can be proven with records/evidence; legends are stories added later.")
    S.set(1, "Fort Caroline — French in Jacksonville",
        learnbox("<p>France wanted a piece of the New World too. In <b>1562</b> <b>Jean Ribault</b> sailed into the mouth of the St. Johns River, called it the <i>River May</i>, "
                 "and set up a stone column to claim the land for France. In <b>June 1564</b> <b>René de Laudonnière</b> brought about 200 settlers and built <b>Fort Caroline</b>, "
                 "a triangle-shaped fort of earth and wood on the St. Johns — in today's <b>Jacksonville</b>! Many were <b>Huguenots</b> (French Protestants) hoping for a place to "
                 "worship freely. The Timucua chief <b>Saturiwa</b> helped them at first, but the settlers ran short of food and struggled. Today you can visit "
                 "<b>Fort Caroline National Memorial</b> on the river (the fort there is a model — the real spot has never been found).</p>", yt("NF Fort Caroline National Memorial virtual tour"))
        + fill_table(["Question", "Answer"], [["Who claimed the river for France in 1562?", ""], ["Who built Fort Caroline, and when?", ""], ["What shape was the fort?", ""], ["Which Timucua chief helped the French?", ""]], 30)
        + qs([("Who were the Huguenots?", ["French Protestants", "Spanish soldiers", "a Florida tribe"]), ("What did the French call the St. Johns River?", ["River May", "River of Flowers", "Saint Augustine River"]),
              ("Why did many Huguenots want to come to Florida?", ["to worship God freely", "to find the Fountain of Youth", "to trade with England"]), ("What problem did the Fort Caroline settlers have?", ["They ran short of food.", "It snowed too much.", "They had no river nearby."]),
              ("Fort Caroline was built more than 450 years ago! If you visited the Memorial, what would you want to see? Why?", 2)], 5),
        "1) Jean Ribault. 2) René de Laudonnière, June 1564. 3) triangle. 4) Saturiwa. 5) French Protestants. 6) River May. 7) to worship freely. 8) ran short of food. 9) opinion.")
    S.set(2, "Menéndez & St. Augustine",
        learnbox("<p>King Philip II of Spain was angry that France was building in Florida, so he sent <b>Pedro Menéndez de Avilés</b>. Menéndez sighted land on <b>August 28, 1565</b> — "
                 "the feast day of <b>St. Augustine</b>, so that became the town's name. On <b>September 8, 1565</b>, he came ashore near a Timucua village, held a church service, and "
                 "shared a meal — 56 years before the Pilgrims' Thanksgiving. The French under Ribault sailed south to attack, but a <b>hurricane</b> wrecked their ships. Menéndez "
                 "marched his soldiers about 40 miles north through the storm and captured <b>Fort Caroline</b> on <b>September 20, 1565</b>, renaming it <b>San Mateo</b>. Many "
                 "French were killed, and Spain took control of Florida.</p>", yt("NF St Augustine 1565 Pedro Menendez"))
        + '<div class="lab">Number the events in order (1–5).</div>'
        + "".join(f'<div class="prob"><span class="blank-ln" style="min-width:40px"></span> {e}</div>' for e in
                  ["A hurricane wrecks the French ships.", "Menéndez sights land on St. Augustine's feast day.", "French Huguenots build Fort Caroline.", "Menéndez captures Fort Caroline.", "Menéndez comes ashore and founds St. Augustine."])
        + qs([("Why was the city named St. Augustine?", ["Land was sighted on the feast day of St. Augustine.", "Menéndez's son was named Augustine.", "A Timucua chief chose it."]), ("On what date was St. Augustine founded?", ["September 8, 1565", "April 2, 1513", "July 4, 1776"]),
              ("What helped Menéndez defeat the French?", ["A hurricane wrecked the French fleet.", "The French gave up without a fight.", "England sent help."]), ("What did Spain rename Fort Caroline?", ["San Mateo", "San Marcos", "La Florida"]),
              ("St. Augustine is the oldest continuously lived-in European city in the continental U.S. Why do you think it lasted when Fort Caroline didn't?", 2)], 6),
        "Order (top to bottom): 4, 2, 1, 5, 3 — Fort Caroline built 1564 → land sighted Aug 28 → St. Augustine founded Sept 8 → hurricane → Fort Caroline captured Sept 20. "
        "6) feast day of St. Augustine. 7) September 8, 1565. 8) a hurricane wrecked the French fleet. 9) San Mateo. 10) opinion (Spain was stronger, more soldiers/supplies, a good harbor, help from Spain).")
    S.set(3, "Missions & the Castillo",
        learnbox("<p>In the 1600s, Spanish <b>Franciscan friars</b> built <b>missions</b> across north Florida to teach the Timucua, Guale, and Apalachee people about Christianity "
                 "(you can visit rebuilt <b>Mission San Luis</b> in Tallahassee). St. Augustine had only wooden forts, and in <b>1668</b> the English pirate <b>Robert Searles</b> raided the town. "
                 "So Spain built a stone fort: the <b>Castillo de San Marcos</b>, from <b>1672 to 1695</b>. It is made of <b>coquina</b> — a rock of tiny shells stuck together — dug on "
                 "Anastasia Island. Cannonballs sank into the soft stone instead of cracking it! In <b>1702</b> English soldiers from Carolina burned the town, but about 1,500 people "
                 "sheltered inside for nearly two months and the Castillo never fell. It is the oldest masonry (stone) fort in the continental U.S.</p>", yt("NF Castillo de San Marcos castle made of coquina"))
        + '<svg width="640" height="80" style="align-self:center"><line x1="20" y1="40" x2="620" y2="40" stroke="#8a3ab9" stroke-width="3"/>'
          + "".join(f'<circle cx="{x}" cy="40" r="7" fill="#8a3ab9"/><text x="{x}" y="70" text-anchor="middle" font-size="15" font-weight="700" fill="#1f2a5c">{y}</text>' for x, y in [(40, 1513), (130, 1564), (220, 1565), (380, 1668), (450, 1672), (530, 1695), (600, 1702)])
          + '</svg>'
        + fill_table(["Year", "What happened?"], [["1668", ""], ["1672", ""], ["1695", ""], ["1702", ""]], 30)
        + qs([("What is coquina?", ["rock made of tiny shells stuck together", "a kind of wood", "Spanish for brick"]), ("Why did Spain build a stone fort?", ["The wooden forts weren't strong enough after a pirate raid.", "They had too much stone.", "France asked them to."]),
              ("What happened when cannonballs hit the coquina walls?", ["They sank into the stone instead of cracking it.", "They bounced back at the ship.", "The walls fell down."]), ("What was the purpose of the Spanish missions?", 2)], 1),
        "1668 pirate Robert Searles raids St. Augustine; 1672 Castillo construction begins; 1695 Castillo finished; 1702 English siege — town burned, Castillo holds. 1) rock of tiny shells. "
        "2) wooden forts weren't strong enough after the raid. 3) they sank in. 4) to teach Native people about Christianity (and to strengthen Spain's hold on Florida).")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — Spanish & French Florida. Goal: 8 of 10.</p>")
        + qs([("Who named La Florida, and in what year?", ["Ponce de León, 1513", "Menéndez, 1565", "Ribault, 1562"]), ("What does <i>Pascua Florida</i> mean?", 1),
              ("Who built Fort Caroline in 1564?", ["French Huguenots", "Spanish friars", "English pirates"]), ("Where was Fort Caroline?", 1),
              ("Who founded St. Augustine, and on what date?", 1), ("How did a hurricane help Spain in 1565?", ["It wrecked the French ships.", "It destroyed St. Augustine.", "It blew Menéndez home."]),
              ("What did Spanish friars build across north Florida?", ["missions", "railroads", "lighthouses"]), ("The Castillo de San Marcos was built from ___ to ___.", 1),
              ("What is coquina made of?", ["tiny shells", "sand and wood", "red clay"]), ("Explain why the Castillo was never captured.", 2)]),
        "1) Ponce de León, 1513. 2) flowery Easter. 3) French Huguenots. 4) on the St. Johns River in today's Jacksonville. 5) Pedro Menéndez de Avilés, September 8, 1565. 6) it wrecked the French ships. "
        "7) missions. 8) 1672 to 1695. 9) tiny shells. 10) strong coquina walls absorbed cannonballs; people sheltered inside during sieges.")
    return S

def build():
    return [math(), english(), science(), fl_history()]
