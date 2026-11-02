from core_common import *
from mathgen import *
import random

K = "Naomi"

def math():
    S = Subject(K, "Math", "Week 2 · Big Numbers"); r = random.Random(44)
    nums = [r.randint(10000, 999999) for _ in range(5)]
    S.set(0, "Place Value & Rounding",
        learnbox("<p>Our number system goes ones, tens, hundreds — then <b>thousands, ten thousands, hundred thousands</b>. A comma separates every three places. "
                 "In <b>352,816</b> the 5 is in the ten-thousands place and is worth <b>50,000</b>. To <b>round</b>, look at the digit just to the right: "
                 "5 or more rounds up, 4 or less stays. 352,816 → nearest thousand <b>353,000</b>; nearest ten thousand <b>350,000</b>.</p>", yt("place value to hundred thousands 4th grade"))
        + fill_table(["Number", "Word form", "Nearest thousand"], [[f"{n:,}", "", ""] for n in nums], 36)
        + qs([("Value of the 7 in 274,031? ________ &nbsp; in 702,118? ________", 1), ("Write in standard form: 400,000 + 20,000 + 3,000 + 50 + 9", 1),
              ("Compare (&lt;, &gt;, =): 46,209 __ 46,290 &nbsp;&nbsp; 108,000 __ 99,999", 1), ("Round 68,452 to the nearest ten thousand and the nearest hundred.", 1)]),
        "Nearest thousand: " + "; ".join(f"{n:,} → {(n+500)//1000*1000:,}" for n in nums) + ". 1) 70,000; 700,000. 2) 423,059. 3) <, >. 4) 70,000; 68,500.")
    adds = [(r.randint(1200, 8999), r.randint(1100, 8999)) for _ in range(6)] + [(r.randint(20000, 79999), r.randint(10000, 19999)) for _ in range(4)]
    S.set(1, "Adding Big Numbers",
        learnbox("<p>Line up the places carefully — ones under ones. Add from right to left, and <b>regroup</b> (carry) whenever a place reaches 10 or more. "
                 "Always <b>estimate first</b> so you know if your answer makes sense: 4,786 + 3,519 ≈ 5,000 + 4,000 = 9,000. Exact: <b>8,305</b>. Close! ✔</p>", yt("multi digit addition 4th grade"))
        + vgrid([(a, b, "+") for a, b in adds], 5)
        + qs([("Jacksonville's Fun Run had 12,486 runners this year and 9,758 last year. How many runners in both years?", 1)], 11),
        ", ".join(f"{n+1}) {a+b:,}" for n, (a, b) in enumerate(adds)) + ", 11) 22,244")
    subs = [(r.randint(5000, 9999), r.randint(1200, 4999)) for _ in range(6)] + [(6000, 2347), (10000, 4826), (40302, 18765), (70050, 26384)]
    S.set(2, "Subtracting Big Numbers",
        learnbox("<p>Subtract from right to left. When the top digit is smaller, <b>regroup</b> from the next place. For zeros, keep moving left until you find a digit "
                 "to borrow from: 6,000 − 2,347 → the 6 becomes 5, and the zeros become 9, 9, 10. Then 10 − 7 = 3, 9 − 4 = 5, 9 − 3 = 6, 5 − 2 = 3 → <b>3,653</b>. "
                 "<b>Check</b> by adding your answer to the number you subtracted.</p>", yt("subtracting across zeros 4th grade"))
        + vgrid([(a, b, "−") for a, b in subs], 5)
        + qs([("A library had 25,000 books and gave away 7,684. How many are left?", 1)], 11),
        ", ".join(f"{n+1}) {a-b:,}" for n, (a, b) in enumerate(subs)) + ", 11) 17,316")
    wp = [("A farmer picked 3,456 oranges on Monday and 2,879 on Tuesday. He sold 4,000. How many are left?", "2,335"),
          ("Naomi's family drove 1,248 miles to Texas and the same distance home. How many miles in all?", "2,496"),
          ("A stadium has 67,814 seats. 49,526 are filled. How many seats are empty?", "18,288"),
          ("The church raised $2,375 in May and $1,980 in June. Their goal is $5,000. How much more do they need?", "$645"),
          ("A school has 486 students. 129 are in 4th grade and 158 are in 5th. How many are in other grades?", "199")]
    S.set(3, "Two-Step Word Problems",
        learnbox("<p>Two-step problems need <b>two operations</b>. Read carefully, ask “What do I need to find first?”, solve that, then use it for step 2. "
                 "Underline the question, circle the numbers, and write a sentence answer.</p>", yt("two step word problems 4th grade"))
        + "".join(f'<div class="box"><b>{n+1}.</b> {q}<div class="grid2" style="margin-top:4px"><div>Step 1:<div class="ln"></div></div><div>Step 2:<div class="ln"></div></div></div></div>' for n, (q, a) in enumerate(wp)),
        ", ".join(f"{n+1}) {a}" for n, (q, a) in enumerate(wp)))
    cp = ["Value of the 3 in 538,104", "Round 47,862 to the nearest thousand", "Write 300,000 + 6,000 + 400 + 2 in standard form", "Compare: 61,047 __ 60,947",
          "5,678 + 2,945", "38,406 + 17,859", "9,000 − 3,462", "52,031 − 28,756", "A truck carried 4,250 pounds, then 3,875 more. How many pounds?",
          "Estimate 6,812 − 2,195 (nearest thousand)"]
    cpa = ["30,000", "48,000", "306,402", ">", "8,623", "56,265", "5,538", "23,275", "8,125", "7,000 − 2,000 = 5,000"]
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz!</b> 10 problems. Show your work. Goal: 8 or more.</p>")
        + hgrid([e + "<div class='ln' style='height:34px'></div>" for e in cp], 2, "13pt", 6) + '<div class="big">Score: ______ / 10</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(cpa)))
    return S

def english():
    S = Subject(K, "English", "Week 2 · All About Nouns")
    S.set(0, "Common & Proper Nouns",
        learnbox("<p>A <b>noun</b> names a person, place, thing, or idea. A <b>common noun</b> is a general name: <i>girl, city, river, church</i>. "
                 "A <b>proper noun</b> is the name of a specific one and always starts with a <b>capital letter</b>: <i>Naomi, Jacksonville, St. Johns River, "
                 "Bethel Church</i>. Days, months, holidays, and book titles are proper nouns too.</p>", yt("common and proper nouns for kids"))
        + '<div class="lab">Write C for common or P for proper.</div>'
        + mark_list(["dog", "Florida", "Tuesday", "teacher", "Bible", "ocean", "Atlantic Ocean", "November"], ["C", "P"], cols=2)
        + '<div class="lab">Write a proper noun for each common noun.</div>'
        + fill_table(["Common noun", "Proper noun"], [["state", ""], ["sister", ""], ["holiday", ""], ["street", ""], ["book", ""]], 26)
        + qs([("Fix the capitals: <i>on thanksgiving, aunt maria drove from georgia to jacksonville.</i>", 2)], 9),
        "C, P, P, C, P, C, P, P. Proper nouns vary. 9) On Thanksgiving, Aunt Maria drove from Georgia to Jacksonville.")
    pl = ["cat", "box", "baby", "leaf", "child", "dish", "toy", "mouse", "city", "tooth", "bus", "sheep"]
    S.set(1, "Plural Nouns",
        learnbox("<p><b>Plural</b> means more than one. Most nouns add <b>-s</b> (cats). Nouns ending in <b>s, x, z, ch, sh</b> add <b>-es</b> (boxes, dishes). "
                 "Consonant + <b>y</b>: change y to i and add -es (baby → babies), but vowel + y just adds -s (toy → toys). Some <b>f/fe</b> words change to -ves "
                 "(leaf → leaves). And some are <b>irregular</b> — they change completely or not at all: child → children, mouse → mice, tooth → teeth, sheep → sheep.</p>",
                 yt("plural nouns rules for kids"))
        + '<div class="grid3">' + "".join(f'<div class="prob">{w} → <span class="blank-ln" style="min-width:110px"></span></div>' for w in pl) + '</div>'
        + qs([("Write a sentence using two plural nouns from above.", 2), ("Naomi lost a tooth in August. If she loses two more, she will have lost three ______.", 1),
              ("Which rule do <i>fox</i>, <i>church</i>, and <i>glass</i> follow?", 1)]),
        "cats, boxes, babies, leaves, children, dishes, toys, mice, cities, teeth, buses, sheep. 1) varies. 2) teeth. 3) add -es.")
    S.set(2, "Possessive Nouns",
        learnbox("<p>A <b>possessive noun</b> shows who owns something. For one owner, add <b>'s</b>: <i>the dog's bone, Naomi's book</i>. For a plural noun "
                 "that ends in s, add just an <b>apostrophe</b>: <i>the girls' room</i> (more than one girl). For irregular plurals, add 's: "
                 "<i>the children's toys</i>. Don't use an apostrophe just to make a plural!</p>", yt("possessive nouns for kids"))
        + '<div class="lab">Rewrite using a possessive noun.</div>'
        + qs([("the hat that belongs to Dad", 1), ("the bikes that belong to the boys", 1), ("the leash of the puppy", 1), ("the toys of the children", 1),
              ("the nest of the birds", 1), ("the Bible of Grandma", 1)])
        + '<div class="lab">Circle the correct word.</div>'
        + ol(["My (sisters / sister's) bed is next to mine.", "All three (sisters / sisters') shoes were by the door.", "We have two (cats / cat's).", "The (teachers / teacher's) desk is clean."], 7),
        "1) Dad's hat 2) the boys' bikes 3) the puppy's leash 4) the children's toys 5) the birds' nest 6) Grandma's Bible. 7) sister's 8) sisters' 9) cats 10) teacher's")
    S.set(3, "Writing with Nouns",
        learnbox("<p>Strong writers choose <b>specific nouns</b>. Instead of “a bird,” say “a <b>pelican</b>.” Instead of “food,” say “<b>Papa John's pizza</b>.” "
                 "Today you'll write a paragraph about your family using specific common and proper nouns. Remember: a paragraph has a <b>topic sentence</b>, "
                 "3–4 <b>detail sentences</b>, and a <b>closing sentence</b>.</p>")
        + '<div class="lab">Make these nouns more specific.</div>'
        + fill_table(["Plain noun", "Specific noun"], [["a tree", ""], ["a car", ""], ["a game", ""], ["a song", ""]], 26)
        + '<div class="lab">Write a paragraph: “My Family.” Use at least 3 proper nouns, 2 plural nouns, and 1 possessive noun. Underline them!</div>' + lines(10, 28)
        + '<div class="small">Checklist: <span class="chk"></span>topic sentence <span class="chk"></span>3 proper nouns <span class="chk"></span>2 plural <span class="chk"></span>1 possessive <span class="chk"></span>capitals & periods</div>',
        "Answers vary — check for capitalized proper nouns, correct plurals/possessives, and a topic + closing sentence.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — nouns. Goal: 8 of 10.</p>")
        + qs([("What is a noun?", 1), ("Circle the proper nouns: <i>girl · Tuesday · river · Pastor Mike · Jacksonville</i>", 1),
              ("Plural of: berry ______ bench ______ goose ______", 1), ("Plural of: knife ______ day ______ fox ______", 1),
              ("Make it possessive: the wings of the butterfly", 1), ("Make it possessive: the coats of the women", 1),
              ("Fix it: <i>The dog's are barking at the mailman.</i>", 1), ("Write a sentence with a plural possessive noun.", 1),
              ("Fix the capitals: <i>my brother titus was born in july.</i>", 1), ("Replace the plain noun with a specific one: <i>We ate food at the place.</i>", 1)]),
        "1) person, place, thing, or idea. 2) Tuesday, Pastor Mike, Jacksonville. 3) berries, benches, geese. 4) knives, days, foxes. 5) the butterfly's wings. 6) the women's coats. "
        "7) The dogs are barking at the mailman. 8) varies (e.g., the girls' room). 9) My brother Titus was born in July. 10) varies.")
    return S

def science():
    S = Subject(K, "Science", "Week 2 · Food Chains & Food Webs")
    S.set(0, "Producers & Consumers",
        learnbox("<p>Every living thing needs energy. <b>Producers</b> make their own food from sunlight — plants, algae, and seagrass. <b>Consumers</b> eat other living things. "
                 "<b>Herbivores</b> eat only plants (manatee, deer). <b>Carnivores</b> eat only animals (alligator, osprey). <b>Omnivores</b> eat both (raccoon, bear, people!). "
                 "God designed it so that all the energy in a food chain starts with the <b>sun</b>.</p>", yt("producers and consumers for kids"))
        + '<div class="lab">Sort each: P (producer), H (herbivore), C (carnivore), O (omnivore).</div>'
        + mark_list(["oak tree", "manatee", "alligator", "raccoon", "seagrass", "white-tailed deer", "osprey", "black bear", "algae", "bobcat"], ["P", "H", "C", "O"], cols=2)
        + qs([("Where does all the energy in a food chain start?", 1), ("Why are plants called producers?", 1), ("Are you a herbivore, carnivore, or omnivore? How do you know?", 2)], 11),
        "oak P, manatee H, alligator C, raccoon O, seagrass P, deer H, osprey C, bear O, algae P, bobcat C. 11) the sun. 12) they make their own food from sunlight. 13) omnivore — eat plants and animals.")
    S.set(1, "Food Chains",
        learnbox("<p>A <b>food chain</b> shows who eats whom. The arrows point in the direction the <b>energy moves</b> — from the thing being eaten to the thing that eats it. "
                 "Example from a Florida pond: <b>algae → mosquito larva → small fish → largemouth bass → alligator</b>. The first link is always a producer. "
                 "The animal at the end with no predators is the <b>top predator</b>.</p>", yt("food chains for kids"))
        + '<div class="lab">Put each chain in order with arrows.</div>'
        + qs([("snake · grass · hawk · grasshopper · frog", 2), ("tiger shark · seagrass · sea turtle", 2),
              ("acorn · owl · mouse", 2)])
        + '<div class="lab">Draw your own Florida food chain with at least 4 links. Label the producer and the top predator.</div><div class="answer-space" style="min-height:170px"></div>'
        + qs([("What would happen to the hawk if all the grass died? Explain.", 2)], 4),
        "1) grass → grasshopper → frog → snake → hawk. 2) seagrass → sea turtle → tiger shark. 3) acorn → mouse → owl. 4) the hawk would lose food because every animal below it depends on the grass.")
    S.set(2, "Food Webs",
        learnbox("<p>In real life, animals eat more than one thing, so food chains overlap into a <b>food web</b>. In Florida's wetlands, a <b>raccoon</b> might eat crayfish, "
                 "eggs, fish, and berries. If one living thing disappears, it can affect the whole web. Look at the web below and answer the questions.</p>", yt("food web for kids"))
        + '<svg width="640" height="250" style="align-self:center">'
          + "".join(f'<rect x="{x-58}" y="{y-16}" width="116" height="32" rx="8" fill="#fff" stroke="#4338ca" stroke-width="2"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" font-weight="600" fill="#1f2a5c">{t}</text>'
                    for t, x, y in [("alligator", 320, 26), ("great blue heron", 140, 110), ("raccoon", 500, 110), ("bass (fish)", 320, 130),
                                    ("crayfish", 120, 200), ("small fish", 320, 220), ("berries", 520, 220)])
          + "".join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#4338ca" stroke-width="2" marker-end="url(#ar)"/>' for a, b, c, d in
                    [(120, 184, 135, 128), (300, 204, 160, 128), (330, 204, 325, 148), (140, 186, 470, 128), (500, 204, 500, 128), (320, 114, 320, 44), (160, 94, 290, 40), (480, 94, 350, 40)])
          + '<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#4338ca"/></marker></defs></svg>'
        + qs([("Name everything the heron eats in this web.", 1), ("What eats the raccoon?", 1), ("Which living thing is the producer?", 1),
              ("Write one complete food chain from this web.", 1), ("If all the crayfish disappeared, which two animals would be affected first? Why?", 2),
              ("Why is a food web more realistic than a food chain?", 2)]),
        "1) crayfish, small fish. 2) alligator. 3) berries. 4) e.g., small fish → bass → alligator. 5) heron and raccoon — they eat crayfish. 6) animals eat many things, so energy paths overlap.")
    S.set(3, "Decomposers",
        learnbox("<p>When plants and animals die, who cleans up? <b>Decomposers</b>! Bacteria, fungi (mushrooms and mold), and helpers like earthworms break down dead things and "
                 "waste and return nutrients to the soil. Then producers use those nutrients to grow, and the cycle starts again. Without decomposers, the earth "
                 "would be piled with dead leaves and the soil would run out of nutrients. Try it: look under a log or in the leaf pile in the backyard!</p>", yt("decomposers for kids"))
        + qs([("Name three decomposers.", 1), ("What do decomposers give back to the soil?", 1), ("What would happen if there were no decomposers?", 2)])
        + '<div class="lab">Backyard hunt: look under a log, rock, or leaf pile (with Mom). Draw and label what you find.</div><div class="answer-space" style="min-height:190px"></div>'
        + '<div class="lab">Draw the cycle: sun → producer → consumer → decomposer → soil → producer</div><div class="answer-space" style="min-height:150px"></div>',
        "1) bacteria, fungi/mushrooms, earthworms (also mold). 2) nutrients. 3) dead things would pile up and soil would lose nutrients.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — food chains and webs. Goal: 8 of 10.</p>")
        + qs([("What is a producer? Give an example.", 1), ("What is a consumer? Give an example.", 1), ("Herbivore, carnivore, or omnivore: manatee ______ osprey ______ raccoon ______", 1),
              ("In a food chain, which way do the arrows point?", 1), ("Put in order: fish · algae · pelican", 1), ("What is a food web?", 1),
              ("What do decomposers do?", 1), ("Name a decomposer.", 1), ("Where does the energy in every food chain begin?", 1),
              ("Psalm 104:27 says all creatures look to God “to give them their food in due season.” How does a food web show God's care?", 2)]),
        "1) makes its own food (plant). 2) eats other living things (animal). 3) herbivore, carnivore, omnivore. 4) direction energy moves (toward the eater). 5) algae → fish → pelican. "
        "6) overlapping food chains. 7) break down dead things, return nutrients. 8) e.g., fungi. 9) the sun. 10) opinion.")
    return S

def fl_history():
    S = Subject(K, "Florida History", "Week 2 · Florida's First Peoples")
    S.set(0, "The First Floridians",
        learnbox("<p>People have lived in Florida for a very long time — archaeologists believe more than <b>12,000 years</b>. Back then Florida was cooler and drier, the "
                 "coastline stretched much farther out, and giant animals like <b>mammoths</b> and <b>mastodons</b> roamed. The first Floridians hunted, fished, and "
                 "gathered plants. Over thousands of years they built villages, made pottery, and piled up huge mounds of shells called <b>middens</b> — some are still "
                 "standing today! By the time Europeans arrived, about <b>350,000</b> Native people lived in Florida.</p>", yt("Florida first people history for kids"))
        + qs([("About how long have people lived in Florida?", 1), ("Name two giant animals the first Floridians may have seen.", 1),
              ("What is a shell midden?", 2), ("How was Florida different long ago?", 2), ("How do archaeologists learn about people who didn't leave written records?", 2)])
        + '<div class="lab">Draw a village of Florida\'s first people.</div><div class="answer-space" style="min-height:150px"></div>',
        "1) more than 12,000 years. 2) mammoths, mastodons. 3) a large mound of discarded shells. 4) cooler, drier, bigger coastline, giant animals. 5) by studying things they left behind — tools, pottery, mounds.")
    S.set(1, "The Timucua — Our Neighbors!",
        learnbox("<p>The <b>Timucua</b> (tee-MOO-kwah) lived in northeast and north-central Florida — right where <b>Jacksonville</b> is today! They lived in villages of round "
                 "houses made of poles and palm thatch, with a large council house in the center. They <b>farmed</b> corn, beans, and squash, and also fished, hunted "
                 "deer, and gathered oysters along the St. Johns River in <b>dugout canoes</b>. Timucua leaders often had elaborate tattoos to show their rank. "
                 "Sadly, after Europeans arrived, war and new diseases caused the Timucua population to shrink until they disappeared by the 1700s.</p>", yt("Timucua people Florida for kids"))
        + qs([("Where did the Timucua live?", 1), ("Describe a Timucua house.", 2), ("Name three foods the Timucua ate.", 1),
              ("What did they use to travel on the river?", 1), ("What happened to the Timucua after Europeans came?", 2),
              ("Jacksonville has a preserve named after them — the Timucuan Ecological and Historic Preserve. Why do you think it's important to remember them?", 2)]),
        "1) northeast/north-central Florida incl. Jacksonville. 2) round, poles + palm thatch. 3) corn, beans, squash (also fish, deer, oysters). 4) dugout canoes. 5) war and disease made them disappear by the 1700s. 6) opinion.")
    S.set(2, "Calusa & Apalachee",
        learnbox("<p>The <b>Calusa</b> (kah-LOO-sah) lived in southwest Florida. They were called “the shell people” because they built whole islands and canals out of shells. "
                 "Unlike most tribes, the Calusa didn't need to farm — the rich waters gave them plenty of fish, shellfish, and turtles. They were powerful, and many "
                 "other tribes paid them tribute. The <b>Apalachee</b> (ap-uh-LATCH-ee) lived in the panhandle near today's Tallahassee. They were skilled "
                 "<b>farmers</b> with large fields of corn, and they played a rough ball game with a small deerskin ball.</p>", yt("Calusa and Apalachee for kids"))
        + fill_table(["", "Timucua", "Calusa", "Apalachee"], [["Part of Florida", "", "", ""], ["Farmed or not?", "", "", ""], ["Main foods", "", "", ""], ["One interesting fact", "", "", ""]], 40)
        + qs([("Why didn't the Calusa need to farm?", 2), ("Which tribe lived closest to Tallahassee?", 1), ("Which of the three would you most like to learn more about? Why?", 2)]),
        "Timucua: NE Florida, farmed, corn/beans/squash/fish; Calusa: SW, did not farm, fish/shellfish; Apalachee: panhandle, farmed, corn. 1) the sea gave plenty of food. 2) Apalachee. 3) opinion.")
    S.set(3, "Europeans Arrive",
        learnbox("<p>In <b>1513</b>, Spanish explorer <b>Juan Ponce de León</b> landed on the east coast and named the land <b>La Florida</b> — “land of flowers.” "
                 "In <b>1564</b>, French Protestants (Huguenots) built <b>Fort Caroline</b> on the St. Johns River — in what is now <b>Jacksonville</b>! Spain wanted Florida "
                 "for itself, so in <b>1565</b> <b>Pedro Menéndez de Avilés</b> founded <b>St. Augustine</b> and soon destroyed Fort Caroline. St. Augustine is the "
                 "<b>oldest continuously inhabited city</b> founded by Europeans in the United States — older than Jamestown by 42 years!</p>", yt("St Augustine history for kids"))
        + '<div class="lab">Make a timeline.</div>'
        + '<svg width="640" height="80" style="align-self:center"><line x1="20" y1="40" x2="620" y2="40" stroke="#8a3ab9" stroke-width="3"/>'
          + "".join(f'<circle cx="{x}" cy="40" r="7" fill="#8a3ab9"/><text x="{x}" y="70" text-anchor="middle" font-size="15" font-weight="700" fill="#1f2a5c">{y}</text>' for x, y in [(80, 1513), (300, 1564), (430, 1565), (590, 1607)])
          + '</svg>'
        + fill_table(["Year", "What happened?"], [["1513", ""], ["1564", ""], ["1565", ""], ["1607", "(Hint: last week Nevaeh learned this one!)"]], 32)
        + qs([("What does “La Florida” mean?", 1), ("Why did Spain attack Fort Caroline?", 2), ("Why is St. Augustine special?", 2)]),
        "1513 Ponce de León names La Florida; 1564 French build Fort Caroline (Jacksonville); 1565 Menéndez founds St. Augustine; 1607 Jamestown. 1) land of flowers. 2) Spain wanted to control Florida. 3) oldest continuously inhabited European-founded city in the U.S.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — Florida's first peoples. Goal: 8 of 10.</p>")
        + qs([("About how long have people lived in Florida?", 1), ("What is a midden?", 1), ("Which tribe lived where Jacksonville is today?", 1),
              ("Name three crops the Timucua grew.", 1), ("Which tribe was known as “the shell people”?", 1), ("Which tribe lived in the panhandle?", 1),
              ("Who named Florida, and when?", 1), ("What was Fort Caroline, and where was it?", 1), ("Who founded St. Augustine, and when?", 1),
              ("Explain one way life changed for Florida's Native peoples after Europeans arrived.", 2)]),
        "1) 12,000+ years. 2) a mound of shells. 3) Timucua. 4) corn, beans, squash. 5) Calusa. 6) Apalachee. 7) Ponce de León, 1513. 8) French fort on the St. Johns River (Jacksonville), 1564. 9) Pedro Menéndez de Avilés, 1565. 10) disease, war, loss of land/population.")
    return S

def build():
    return [math(), english(), science(), fl_history()]
