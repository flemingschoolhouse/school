from core_common import *
from mathgen import *
import random

K = "Nevaeh"
ROADMAP = ["Whole numbers & order of operations", "Fractions: all four operations", "Decimals & money", "Ratios, rates & unit rates",
           "Percents (discount, tax, tip)", "Integers & the number line", "Expressions & the distributive property",
           "One- and two-step equations & inequalities", "Exponents, square roots & scientific notation",
           "Geometry: angles, area, volume", "Slope & linear functions (graphing lines)", "Pythagorean theorem + data & statistics"]

# ---------------- MATH CRASH COURSE · Week 1 ----------------
def math():
    S = Subject(K, "Math Crash Course", "Week 1 of 12"); r = random.Random(81)
    # D1 multi-digit multiplication
    ps = [(r.randint(21, 89), r.randint(12, 49)) for _ in range(6)] + [(r.randint(120, 899), r.randint(12, 68)) for _ in range(4)]
    S.set(0, "Multi-Digit Multiplication",
        learnbox("<p><b>Your 12-week plan:</b> one big skill a week, building to 8th-grade math (Mom has the full roadmap). Week 1 makes sure the "
                 "whole-number skills underneath everything are rock solid.</p><p><b>Multiply 47 × 36:</b> 47 × 6 = 282 (ones). 47 × 30 = 1,410 (tens — "
                 "write a 0 placeholder first). Add: 282 + 1,410 = <b>1,692</b>. Check: estimate 50 × 36 ≈ 1,800 — close, so it's reasonable.</p>",
                 yt("multi digit multiplication standard algorithm")) + vgrid([(a, b, "×") for a, b in ps], 5)
        + '<div><b>Estimate first:</b> 312 × 48 is about ______ × ______ = ______</div>',
        "1) " + ", ".join(f"{a}×{b}={a*b:,}" for a, b in ps) + ". Estimate ≈ 300×50 = 15,000 (actual 14,976).")
    # D2 long division
    divs = []
    for k in range(9):
        b = r.choice([3, 4, 6, 7, 8, 9, 12, 15, 24]); q = r.randint(24, 320); rem = r.randint(0, b - 1) if k >= 5 else 0
        divs.append((b * q + rem, b, q, rem))
    S.set(1, "Long Division",
        learnbox("<p><b>Divide, Multiply, Subtract, Bring down</b> — repeat. <b>918 ÷ 6:</b> 6 into 9 = 1, 9 − 6 = 3, bring down 1 → 31. "
                 "6 into 31 = 5, 31 − 30 = 1, bring down 8 → 18. 6 into 18 = 3. Answer <b>153</b>. Check by multiplying: 153 × 6 = 918. "
                 "If something is left over at the end, write it as a remainder (R).</p>", yt("long division step by step"))
        + f'<div class="grid3" style="justify-items:start">' + "".join(f'<div style="display:flex;gap:6px"><b style="color:#2f5bd3">{n+1}.</b>{longdiv(a,b)}</div>' for n, (a, b, q, rm) in enumerate(divs)) + '</div>'
        + '<div><b>10.</b> 1,248 students split evenly into 24 buses. How many on each bus?' + lines(1) + '</div>',
        ", ".join(f"{n+1}) {q}" + (f" R{rm}" if rm else "") for n, (a, b, q, rm) in enumerate(divs)) + ", 10) 52")
    # D3 order of operations
    oo = ["8 + 4 × 3", "(8 + 4) × 3", "20 − 12 ÷ 4", "36 ÷ (2 + 4)", "5 × 6 − 4 × 2", "48 ÷ 8 × 3", "(15 − 3) ÷ (2 + 4)",
          "7 + 3 × (10 − 4)", "100 − 6 × 7 + 2", "[2 × (9 + 1)] ÷ 5", "18 − (3 + 9) ÷ 4", "4 × (25 − 5 × 3)"]
    ans = [20, 36, 17, 6, 22, 18, 2, 25, 60, 4, 15, 40]
    S.set(2, "Order of Operations",
        learnbox("<p><b>PEMDAS</b>: <b>P</b>arentheses (and brackets) → <b>E</b>xponents → <b>M</b>ultiply & <b>D</b>ivide left to right → "
                 "<b>A</b>dd & <b>S</b>ubtract left to right. Multiplication does NOT always come before division — whichever is first from the left goes first. "
                 "Example: 12 ÷ 3 × 2 = 4 × 2 = <b>8</b> (not 2).</p>", yt("order of operations PEMDAS explained"))
        + hgrid([f"{e} = <span class='blank-ln'></span>" for e in oo], 2, "14pt", 22)
        + '<div><b>Challenge:</b> add parentheses to make it true: &nbsp; 3 + 5 × 2 = 16 &nbsp;&nbsp;&nbsp; 24 ÷ 4 + 2 = 4</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(ans)) + ". Challenge: (3 + 5) × 2 = 16; 24 ÷ (4 + 2) = 4.")
    # D4 exponents
    ex = ["3²", "2⁵", "10³", "5² + 4", "2 × 4²", "(2 × 4)²", "6² ÷ 4", "3 + 2³ × 2", "(9 − 6)³", "10² − 8²", "4³ ÷ 2⁴", "1¹⁰ + 0⁵"]
    exa = [9, 32, 1000, 29, 32, 64, 9, 19, 27, 36, 4, 1]
    S.set(3, "Exponents",
        learnbox("<p>An <b>exponent</b> tells how many times to multiply the base by itself. 4³ = 4 × 4 × 4 = <b>64</b> (not 12!). "
                 "Read 4³ as “four cubed” and 5² as “five squared.” Exponents come right after parentheses in PEMDAS: 2 × 3² = 2 × 9 = 18, "
                 "but (2 × 3)² = 6² = 36. Powers of 10: 10³ = 1,000 — the exponent counts the zeros.</p>", yt("exponents for middle school"))
        + hgrid([f"{e} = <span class='blank-ln'></span>" for e in ex], 3, "15pt", 20)
        + '<div><b>Write in exponent form:</b> 7 × 7 × 7 × 7 = ______ &nbsp;&nbsp; 10 × 10 × 10 × 10 × 10 = ______</div>'
        + '<div><b>Explain</b> why 2⁴ and 4² have the same value but 2³ and 3² don\'t.' + lines(2) + '</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(exa)) + ". 7⁴; 10⁵. 2⁴=16=4²; 2³=8 but 3²=9.")
    # D5 checkpoint
    cp = ["58 × 34", "706 × 23", "1,512 ÷ 7", "2,046 ÷ 11", "45 − 5 × 8", "(45 − 5) × 8 ÷ 4", "3⁴", "2 × 5² − 10",
          "64 ÷ 2³ + 1", "6 + 2 × (7 − 3)²", "Write 9 × 9 × 9 in exponent form.", "A case holds 36 bottles. How many bottles in 48 cases?",
          "Eight friends share $1,016 evenly. How much each?", "Is 12 ÷ 3 × 2 equal to 2 or 8?", "Estimate 489 × 21.", "(10 − 4)² ÷ 9"]
    cpa = ["1,972", "16,238", "216", "186", "5", "80", "81", "40", "9", "38", "9³", "1,728", "$127", "8", "≈ 10,000 (500 × 20)", "4"]
    S.set(4, "Checkpoint",
        learnbox("<p><b>Checkpoint!</b> 16 problems from this week. Show your work on scratch paper. <b>Goal: 13+ correct (80%)</b>. "
                 "Anything missed gets reviewed before Week 2 (Fractions).</p>")
        + hgrid([f"{e}" + ("" if len(e) > 22 else " = ") + "<div class='ln' style='height:20px'></div>" for e in cp], 2, "13pt", 2)
        + '<div class="big">Score: ______ / 16</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(cpa)))
    return S

# ---------------- ENGLISH ----------------
def _lc(s):
    w = s.split()[0]
    return s if w in ("Titus", "Naomi", "Nevaeh", "Dad", "I") else s[0].lower() + s[1:]

def english():
    S = Subject(K, "English", "Week 2 · Building Better Sentences")
    cl = ["the storm knocked out the power", "because the bridge was closed", "when Gideon heard the dream", "Nevaeh finished her chores",
          "although the test was hard", "the puppy slept on the porch", "if you water the garden", "after the service ended"]
    S.set(0, "Clauses",
        learnbox("<p>A <b>clause</b> is a group of words with a <b>subject</b> and a <b>verb</b>. An <b>independent clause</b> is a complete thought — it can stand alone "
                 "as a sentence (<i>The choir sang.</i>). A <b>dependent clause</b> also has a subject and verb, but it starts with a word like <b>because, although, when, "
                 "if, since, while, after, before, unless</b> — so it leaves you hanging (<i>When the choir sang…</i> what happened?).</p>", yt("independent and dependent clauses"))
        + '<div class="lab">Mark each clause I (independent) or D (dependent). Underline the subject once and the verb twice.</div>'
        + mark_list(cl, ["I", "D"])
        + '<div class="lab">Turn these dependent clauses into complete sentences by adding an independent clause.</div>'
        + qs([("Which is a complete sentence?", ["Because the bridge was closed, we took the long way home.", "Because the bridge was closed.", "Because the bridge was closed and the long way."]),
              ("Which is a complete sentence?", ["If you water the garden, the tomatoes will grow.", "If you water the garden.", "If you water the garden every day this week."]),
              ("Write your own sentence that has one dependent clause:", 2)], 9),
        "I, D, D, I, D, I, D, D. 9) Because the bridge was closed, we took the long way home. 10) If you water the garden, the tomatoes will grow. 11) varies.")
    pairs = [("I wanted to go outside.", "It started to rain.", "but"), ("Naomi can read the story.", "She can listen to the audiobook.", "or"),
             ("The oven was hot.", "We put the bread in.", "so"), ("Dad mowed the yard.", "Titus raked the clippings.", "and"),
             ("He didn't like peas.", "He didn't like carrots either.", "nor"), ("We stayed home.", "The roads were flooded.", "for")]
    S.set(1, "Compound Sentences",
        learnbox("<p>A <b>compound sentence</b> joins two independent clauses with a comma and a <b>coordinating conjunction</b>. Remember them with "
                 "<b>FANBOYS</b>: <b>F</b>or, <b>A</b>nd, <b>N</b>or, <b>B</b>ut, <b>O</b>r, <b>Y</b>et, <b>S</b>o. "
                 "<i>The dog barked, <b>so</b> I opened the door.</i> The comma goes <b>before</b> the conjunction. You can also join them with a semicolon: "
                 "<i>The dog barked; I opened the door.</i></p>", yt("compound sentences FANBOYS"))
        + '<div class="lab">Which compound sentence is written correctly? Watch the comma!</div>'
        + qs([(f"{a} {b} <span class='pill'>{c}</span>",
               [f"{a[:-1]}, {c} {_lc(b)}", f"{a[:-1]} {c}, {_lc(b)}", f"{a[:-1]}, {_lc(b)}"]) for a, b, c in pairs[:3]])
        + '<div class="lab">Now combine these yourself.</div>'
        + qs([(f"{a} {b} <span class='pill'>{c}</span>", 1) for a, b, c in pairs[3:]], 4)
        + qs([("Write a compound sentence using <b>yet</b>:", 1), ("Rewrite #4 using a semicolon instead:", 1)], 7),
        "1) I wanted to go outside, but it started to rain. 2) Naomi can read the story, or she can listen to the audiobook. 3) The oven was hot, so we put the bread in. "
        "4) Dad mowed the yard, and Titus raked the clippings. 5) He didn't like peas, nor did he like carrots. 6) We stayed home, for the roads were flooded. "
        "7) varies. 8) Dad mowed the yard; Titus raked the clippings.")
    cx = [("We ate dinner.", "Dad got home.", "after"), ("I'll bring an umbrella.", "It might rain.", "since"), ("She kept running.", "Her legs were tired.", "although"),
          ("You can have dessert.", "You finish your vegetables.", "if"), ("The baby slept.", "We folded laundry.", "while")]
    S.set(2, "Complex Sentences",
        learnbox("<p>A <b>complex sentence</b> has one independent clause and at least one dependent clause, joined by a <b>subordinating conjunction</b> "
                 "(after, although, as, because, before, if, since, though, unless, until, when, while). <b>Comma rule:</b> if the dependent clause comes "
                 "<b>first</b>, put a comma after it. If it comes second, usually no comma.<br><i>When the bell rang, we went inside.</i> &nbsp;·&nbsp; "
                 "<i>We went inside when the bell rang.</i></p>", yt("complex sentences subordinating conjunctions"))
        + '<div class="lab">Which complex sentence is combined and punctuated correctly?</div>'
        + qs([("<i>After Dad got home + We ate dinner.</i>", ["After Dad got home, we ate dinner.", "After Dad got home we ate dinner.", "After, Dad got home we ate dinner."]),
              ("<i>Since it might rain + I'll bring an umbrella.</i>", ["Since it might rain, I'll bring an umbrella.", "Since it might rain I'll, bring an umbrella.", "Since, it might rain I'll bring an umbrella."]),
              ("<i>Although her legs were tired + She kept running.</i>", ["Although her legs were tired, she kept running.", "Although her legs were tired. She kept running.", "Although, her legs were tired she kept running."])])
        + '<div class="lab">Combine using the word given. Write it twice — dependent clause first (with a comma), then second.</div>'
        + qs([(f"{a} {b} <span class='pill'>{c}</span>", 2) for a, b, c in cx[3:]], 4)
        + qs([("Simple, compound, or complex? <i>Although we were late, Pastor waited for us.</i>", ["complex", "compound", "simple"])], 6),
        "1) After Dad got home, we ate dinner. / We ate dinner after Dad got home. 2) Since it might rain, I'll bring an umbrella. 3) Although her legs were tired, she kept running. "
        "4) If you finish your vegetables, you can have dessert. 5) While we folded laundry, the baby slept. 6) complex.")
    fr = ["Running down the hallway with a muddy dog.", "I finished my math I started my essay.", "Because the store was closed.",
          "The sun set behind the trees, and the crickets started singing.", "We baked cookies, they were delicious.", "Whenever Grandma visits.",
          "My brother fixed the bike.", "The rain stopped we went outside to play."]
    S.set(3, "Fragments & Run-Ons",
        learnbox("<p>A <b>fragment</b> is missing a subject, a verb, or a complete thought (<i>Because I was tired.</i>). A <b>run-on</b> jams two independent "
                 "clauses together with nothing between them (<i>I was tired I went to bed.</i>). A <b>comma splice</b> joins them with only a comma "
                 "(<i>I was tired, I went to bed.</i>). <b>Fix</b> run-ons and splices with a period, a semicolon, or a comma + FANBOYS.</p>", yt("fragments and run on sentences"))
        + '<div class="lab">Label each: F (fragment), RO (run-on), CS (comma splice), or C (correct).</div>'
        + mark_list(fr, ["F", "RO", "CS", "C"])
        + '<div class="lab">Fix three of the broken ones (#1, #2, #5):</div>' + qs([("", 1), ("", 1), ("", 1)], 9),
        "1 F, 2 RO, 3 F, 4 C, 5 CS, 6 F, 7 C, 8 RO. Fixes vary (e.g., I finished my math, so I started my essay. / We baked cookies; they were delicious.)")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz.</b> Use everything from this week: clauses, compound and complex sentences, fragments and run-ons. Goal: 8 of 10.</p>")
        + qs([("What is an independent clause?", ["a clause with a subject and verb that is a complete thought", "a clause that starts with because or when", "a group of words with no verb"]),
              ("<i>We stayed inside until the storm passed.</i> Which word is the subordinating conjunction?", ["until", "inside", "passed"]),
              ("Which list is the FANBOYS?", ["for, and, nor, but, or, yet, so", "for, and, not, but, or, yes, so", "if, and, nor, but, or, yet, since"]), ("Fix the comma splice: <i>The phone rang, nobody answered it.</i>", 1),
              ("Fix the fragment: <i>Since the library was open late.</i>", 1), ("Where does the comma go? <i>If you hear thunder go inside.</i>", ["after thunder", "after If", "after go"]),
              ("Simple, compound, or complex? <i>Nylah practiced piano, and Naomi read.</i>", ["compound", "complex", "simple"]),
              ("Simple, compound, or complex? <i>The tall oak tree fell during the storm.</i>", ["simple", "compound", "complex"]),
              ("Write a complex sentence about something you did this week. Put the dependent clause first.", 2),
              ("Write a compound sentence about Gideon using <b>but</b>.", 2)]),
        "1) a clause with a subject & verb that expresses a complete thought. 2) until. 3) for, and, nor, but, or, yet, so. 4) The phone rang, but nobody answered it. "
        "5) e.g., We studied there since the library was open late. 6) after thunder (If you hear thunder, go inside). 7) compound. 8) simple. 9–10 vary.")
    return S

# ---------------- SCIENCE ----------------
def science():
    S = Subject(K, "Science", "Week 2 · Atoms & the Periodic Table")
    S.set(0, "Inside an Atom",
        learnbox("<p>All matter is made of <b>atoms</b> — so small that millions could fit across the period at the end of this sentence. Each atom has a center called the "
                 "<b>nucleus</b>, which holds <b>protons</b> (positive charge, +) and <b>neutrons</b> (no charge, 0). Whizzing around the nucleus in the "
                 "<b>electron cloud</b> are <b>electrons</b> (negative charge, −), which are far lighter. In a neutral atom, the number of electrons equals the "
                 "number of protons, so the charges balance.</p>", yt("parts of an atom for middle school"))
        + fill_table(["Particle", "Charge", "Where is it?"], [["Proton", "", ""], ["Neutron", "", ""], ["Electron", "", ""]])
        + qs([("What part of the atom holds most of its mass?", ["the nucleus — protons and neutrons are much heavier than electrons", "the electron cloud — it takes up the most space", "the electrons — there are more of them"]), ("Why is a neutral atom's overall charge zero?", ["It has equal numbers of + protons and − electrons.", "Neutrons cancel out all the charges.", "Atoms never have any charge."])])
        + '<div class="lab">Draw a helium atom: 2 protons, 2 neutrons, 2 electrons. Label the nucleus and electron cloud.</div><div class="answer-space" style="min-height:190px"></div>',
        "Proton + nucleus; Neutron 0 nucleus; Electron − electron cloud. 1) the nucleus. 2) equal + protons and − electrons.")
    els = [("Carbon", "C", 6, 12), ("Oxygen", "O", 8, 16), ("Sodium", "Na", 11, 23), ("Aluminum", "Al", 13, 27), ("Chlorine", "Cl", 17, 35), ("Gold", "Au", 79, 197)]
    S.set(1, "Atomic Number & Mass",
        learnbox("<p>Every element has its own <b>atomic number</b> = the number of <b>protons</b>. Change the protons and you change the element! "
                 "The <b>mass number</b> = protons + neutrons. So: <b>neutrons = mass number − atomic number</b>. In a neutral atom, "
                 "<b>electrons = protons</b>. Example: Nitrogen (N) has atomic number 7 and mass number 14 → 7 protons, 7 electrons, 14 − 7 = 7 neutrons.</p>",
                 yt("atomic number mass number protons neutrons electrons"))
        + fill_table(["Element", "Symbol", "Atomic #", "Mass #", "Protons", "Neutrons", "Electrons"],
                     [[n, s, str(a), str(m), "", "", ""] for n, s, a, m in els], 32)
        + qs([("An atom has 15 protons and 16 neutrons. What is its mass number? (It's phosphorus.)", ["31", "15", "1"]),
              ("Why is gold's symbol Au instead of G? (Hint: Latin <i>aurum</i>.)", ["Some symbols come from Latin names.", "G was already taken by gas.", "Au stands for “all useful.”"]),
              ("If an atom gains an extra proton, what happens to it?", ["It becomes a different element.", "It becomes heavier but stays the same element.", "Nothing changes."])]),
        "C 6/6/6, O 8/8/8, Na 11/12/11, Al 13/14/13, Cl 17/18/17, Au 79/118/79 (protons/neutrons/electrons). 1) 31. 2) symbols can come from Latin names. 3) it becomes a different element.")
    S.set(2, "The Periodic Table",
        learnbox("<p>The <b>periodic table</b> lists all known elements in order of atomic number. The rows are <b>periods</b> (7 of them); the columns are "
                 "<b>groups</b> (18). Elements in the same group act alike because they have the same number of outer electrons. <b>Metals</b> (shiny, conduct "
                 "electricity) are on the left and middle; <b>nonmetals</b> are on the right; <b>metalloids</b> sit along the zig-zag “staircase” between them. "
                 "Group 1 metals react wildly with water; Group 18 <b>noble gases</b> (helium, neon, argon) barely react at all. Use any periodic table "
                 "(online or in a book) for today's questions.</p>", yt("how to read the periodic table"))
        + qs([("What is the difference between a period and a group?", ["A period is a row; a group is a column of elements that act alike.", "A period is a column; a group is a row.", "There is no difference."]), ("Which element has atomic number 1, and where is it?", ["hydrogen — period 1, group 1", "helium — period 1, group 18", "oxygen — period 2, group 16"]),
              ("Name two noble gases. Why are they called “noble”?", 2), ("Sulfur (S), Silicon (Si), Iron (Fe) — which list is right?", ["nonmetal, metalloid, metal", "metal, metal, metal", "metalloid, nonmetal, metal"]),
              ("Sodium and potassium are in the same group. Will potassium react with water?", ["Yes — elements in the same group act alike.", "No — only sodium reacts with water.", "Only if the water is frozen."]),
              ("Find the symbols: Calcium ____ Potassium ____ Silver ____ Lead ____ Neon ____ Iron ____", 1)]),
        "1) period = row, group = column (shared properties). 2) hydrogen — period 1, group 1. 3) e.g., helium, neon, argon — they rarely react/combine. "
        "4) nonmetal; metalloid; metal. 5) yes — same group, similar properties (it reacts even more strongly). 6) Ca, K, Ag, Pb, Ne, Fe.")
    things = ["water (H₂O)", "oxygen gas (O₂)", "salt water", "gold", "carbon dioxide (CO₂)", "trail mix", "table salt (NaCl)", "air", "iron", "sugar (C₁₂H₂₂O₁₁)"]
    S.set(3, "Elements, Compounds & Mixtures",
        learnbox("<p>An <b>element</b> is made of only one kind of atom (gold, iron, oxygen). A <b>compound</b> is two or more elements <b>chemically bonded</b> in a fixed "
                 "ratio — and it acts completely different from its parts. Sodium is an explosive metal and chlorine is a poisonous gas, but bonded together they make "
                 "table salt! A <b>mixture</b> is substances physically mixed but not bonded, so they can be separated (sand and iron filings, salt water). "
                 "A <b>chemical formula</b> shows the atoms in a compound: H₂O = 2 hydrogen + 1 oxygen.</p>", yt("elements compounds and mixtures"))
        + '<div class="lab">Classify each: E (element), C (compound), or M (mixture).</div>' + mark_list(things, ["E", "C", "M"], cols=2)
        + qs([("How many atoms total are in one molecule of sugar, C₁₂H₂₂O₁₁?", ["45", "3", "12"]),
              ("How could you separate salt from salt water? Why does that prove it's a mixture?", 2),
              ("God made over 100 elements and combined them into everything you see. Name 3 things in your kitchen and guess whether each is an element, compound, or mixture.", 2)], 11),
        "water C, oxygen E, salt water M, gold E, CO₂ C, trail mix M, NaCl C, air M, iron E, sugar C. 11) 45 (12 C + 22 H + 11 O). 12) evaporate the water — the parts kept their own properties and separated physically. 13) varies.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — atoms and the periodic table. Goal: 8 of 10. Periodic table allowed for #6–7.</p>")
        + qs([("Which shows the three particles and their charges?", ["proton +, neutron 0, electron −", "proton −, neutron +, electron 0", "proton 0, neutron −, electron +"]), ("What does the atomic number tell you?", ["the number of protons", "the number of neutrons", "how heavy the atom is"]),
              ("Mass number 40, atomic number 20. How many neutrons?", ["20", "40", "60"]), ("A period is a ____ and a group is a ____.", ["row; column", "column; row", "metal; gas"]),
              ("Where are metals found on the periodic table?", ["left and middle", "far right only", "top row only"]), ("Write the symbol: Helium ____ Copper ____ Nitrogen ____", 1),
              ("Element with 8 protons: ________ Element with 26 protons: ________", 1), ("Lemonade, neon, H₂O — which list is right?", ["mixture, element, compound", "compound, mixture, element", "element, compound, mixture"]),
              ("Why does table salt behave differently from sodium and chlorine?", 2), ("Explain the difference between a compound and a mixture with an example of each.", 2)]),
        "1) proton +, neutron 0, electron −. 2) number of protons (identity). 3) 20. 4) row / column. 5) left and middle. 6) He, Cu, N. 7) oxygen, iron. 8) mixture, element, compound. "
        "9) chemical bonding forms a new substance with new properties. 10) compound bonded (water), mixture not bonded (salad, salt water).")
    return S

# ---------------- HISTORY ----------------
def history():
    S = Subject(K, "History", "Week 2 · The Thirteen Colonies")
    S.set(0, "Jamestown, 1607",
        learnbox("<p>In 1607, the Virginia Company of London sent about 100 men to build <b>Jamestown</b> — the first <b>permanent English settlement</b> in North America. "
                 "They chose swampy land, many came hoping for gold rather than to farm, and disease and hunger killed most of them. Captain <b>John Smith</b> "
                 "enforced a rule: “he that will not work shall not eat.” The winter of 1609–10, called the <b>Starving Time</b>, nearly wiped the colony out. "
                 "Jamestown survived when <b>John Rolfe</b> began growing <b>tobacco</b> to sell in England. In 1619, Virginia formed the <b>House of Burgesses</b>, "
                 "the first elected lawmaking body in the colonies — and that same year the first enslaved Africans were brought to Virginia, beginning a terrible "
                 "injustice that would last for 250 years.</p>", yt("Jamestown colony history for kids"))
        + qs([("Who sponsored Jamestown, and what did many settlers hope to find?", ["the Virginia Company of London — gold", "the King of Spain — spices", "the Pilgrims — religious freedom"]), ("List two reasons Jamestown almost failed.", 2),
              ("What crop saved Jamestown's economy?", ["tobacco", "cotton", "wheat"]), ("Why was the House of Burgesses important?", ["It was the first elected lawmaking body in the colonies.", "It was the first church in America.", "It ended slavery in Virginia."]),
              ("John Smith's rule echoes 2 Thessalonians 3:10. Do you think it was fair? Explain.", 3)]),
        "1) Virginia Company of London; gold/riches. 2) swampy land/disease, hunger/Starving Time, settlers unwilling to farm. 3) tobacco. 4) first representative (elected) government in the colonies. 5) opinion.")
    S.set(1, "Plymouth & New England",
        learnbox("<p>In 1620 the <b>Pilgrims</b>, who wanted to separate from the Church of England, sailed on the <b>Mayflower</b>. Before landing they signed the "
                 "<b>Mayflower Compact</b>, agreeing to make fair laws and obey them — an early step toward self-government. In 1630 the <b>Puritans</b>, who "
                 "wanted to purify the church, founded <b>Massachusetts Bay Colony</b>; their leader John Winthrop hoped they'd be “a city upon a hill.” "
                 "When <b>Roger Williams</b> argued that government should not force religion, he was banished and founded <b>Rhode Island</b> (1636) "
                 "with religious freedom. New England's rocky soil and cold winters made farming hard, so people turned to <b>fishing, shipbuilding, "
                 "lumber, and trade</b>, and governed through <b>town meetings</b>.</p>", yt("New England colonies history"))
        + qs([("What was the Mayflower Compact?", ["an agreement to make and obey fair laws — early self-government", "a trade deal with England for tobacco", "a peace treaty with the Wampanoag"]), ("How were the Pilgrims and Puritans different?", 2),
              ("Why did Roger Williams start Rhode Island?", ["for religious freedom", "to grow tobacco", "to fight the Spanish"]), ("How did geography shape the New England economy?", 2),
              ("Winthrop's “city upon a hill” comes from Matthew 5:14. What did he hope the colony would be?", 2)]),
        "1) agreement to make and obey fair laws — early self-government. 2) Pilgrims separated from the church; Puritans wanted to reform it. 3) for religious freedom / separation of church and state. "
        "4) rocky soil, cold → fishing, shipbuilding, lumber, trade. 5) a godly example the world would watch.")
    S.set(2, "The Middle Colonies",
        learnbox("<p>The <b>Middle Colonies</b> — <b>New York, New Jersey, Pennsylvania, and Delaware</b> — had fertile soil and a milder climate. They grew so much "
                 "wheat, corn, and rye that they were called the <b>“breadbasket colonies.”</b> New York began as the Dutch colony of New Netherland; the English "
                 "took it in 1664. <b>William Penn</b>, a <b>Quaker</b>, founded Pennsylvania in 1681 as a “holy experiment” where people of any faith could worship "
                 "freely. He made peace treaties with the Lenape people, and Philadelphia (“city of brotherly love”) grew into the largest city in the colonies. "
                 "The Middle Colonies were the most <b>diverse</b> — Dutch, English, German, Swedish, Scots-Irish, and more lived side by side.</p>", yt("Middle colonies history"))
        + qs([("Which are the four Middle Colonies?", ["New York, New Jersey, Pennsylvania, Delaware", "Virginia, Maryland, Georgia, Delaware", "Massachusetts, New York, Rhode Island, Connecticut"]), ("Why were they called the “breadbasket colonies”?", ["Fertile soil grew lots of grain.", "They baked bread for England.", "They traded in baskets."]), ("What was William Penn's “holy experiment”?", 2),
              ("Who controlled New York before the English?", ["the Dutch", "the Spanish", "the French"]), ("Why might religious freedom attract more settlers?", 2)])
        + '<div class="lab">Compare: New England vs. Middle Colonies</div>' + fill_table(["", "New England", "Middle"], [["Soil/climate", "", ""], ["Main jobs", "", ""], ["Religion", "", ""]], 34),
        "1) NY, NJ, PA, DE. 2) fertile soil grew lots of grain. 3) a colony with religious freedom for all and fair treatment. 4) the Dutch. 5) people persecuted elsewhere could worship freely. "
        "Table: rocky/cold vs fertile/mild; fishing, shipbuilding, trade vs farming grain, trade; mostly Puritan vs diverse/tolerant.")
    S.set(3, "The Southern Colonies",
        learnbox("<p>The <b>Southern Colonies</b> — <b>Maryland, Virginia, North Carolina, South Carolina, and Georgia</b> — had long growing seasons and rich soil. "
                 "Huge farms called <b>plantations</b> grew <b>cash crops</b> to sell: tobacco, rice, and indigo (a blue dye). Planters relied more and more on the "
                 "forced labor of <b>enslaved Africans</b>, a deep evil that treated people made in God's image as property. Maryland (1634) was founded by Lord "
                 "Baltimore as a refuge for Catholics. <b>Georgia</b> (1732), the last colony, was founded by James Oglethorpe as a fresh start for debtors and as a "
                 "<b>buffer</b> to protect South Carolina from the Spanish in <b>Florida</b> — just north of us!</p>", yt("Southern colonies history"))
        + qs([("Which are the five Southern Colonies?", ["Maryland, Virginia, North Carolina, South Carolina, Georgia", "Virginia, Florida, Georgia, Texas, Maryland", "Delaware, Virginia, North Carolina, Georgia, Alabama"]), ("What is a cash crop? Name three grown in the South.", 2),
              ("Why did Georgia's location matter to the English?", ["It was a buffer against Spanish Florida.", "It had the best gold mines.", "It was closest to England."]), ("Why was Maryland founded?", ["as a refuge for Catholics", "as a home for debtors", "as a Quaker colony"]),
              ("Genesis 1:27 says every person is made in God's image. How does that truth condemn slavery?", 3)])
        + mc("Which colony bordered Spanish Florida?", ["Georgia", "Virginia", "Pennsylvania"], 6),
        "1) MD, VA, NC, SC, GA. 2) a crop grown to sell; tobacco, rice, indigo. 3) buffer against Spanish Florida. 4) refuge for Catholics. 5) every person has equal God-given worth and cannot be owned. Florida bordered Georgia.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — the Thirteen Colonies. Goal: 8 of 10.</p>")
        + '<div class="lab">Sort all 13 colonies into regions.</div>' + fill_table(["New England (4)", "Middle (4)", "Southern (5)"], [["", "", ""]], 120)
        + qs([("First permanent English settlement and year:", ["Jamestown, 1607", "Plymouth, 1620", "St. Augustine, 1565"]), ("Document the Pilgrims signed before landing:", ["the Mayflower Compact", "the Constitution", "the Declaration of Independence"]), ("Founder of Pennsylvania and his religion:", ["William Penn, Quaker", "John Winthrop, Puritan", "Lord Baltimore, Catholic"]),
              ("Colony founded for religious freedom by Roger Williams:", ["Rhode Island", "Georgia", "New York"]), ("Main economy of New England:", 1), ("Nickname for the Middle Colonies:", 1),
              ("Two cash crops of the South:", 1), ("Last colony founded, and one reason:", 1), ("Which region would you have wanted to live in? Give two reasons.", 2)]),
        "New England: MA, NH, CT, RI. Middle: NY, NJ, PA, DE. Southern: MD, VA, NC, SC, GA. Jamestown 1607; Mayflower Compact; William Penn, Quaker; Rhode Island; fishing/shipbuilding/trade; breadbasket; tobacco/rice/indigo; Georgia — debtors/buffer vs Spanish Florida; opinion.")
    return S

def build():
    return [math(), english(), science(), history()]
