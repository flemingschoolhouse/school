from core_common import *
from mathgen import *
import random
from fractions import Fraction as Fr
from math import gcd

K = "Nevaeh"
ROADMAP = ["Whole numbers & order of operations", "Fractions: all four operations", "Decimals & money", "Ratios, rates & unit rates",
           "Percents (discount, tax, tip)", "Integers & the number line", "Expressions & the distributive property",
           "One- and two-step equations & inequalities", "Exponents, square roots & scientific notation",
           "Geometry: angles, area, volume", "Slope & linear functions (graphing lines)", "Pythagorean theorem + data & statistics"]

# ---------------- fraction display helpers ----------------
def fh(n, d=None):
    """Stacked fraction (HTML). fh(Fraction) or fh(numerator, denominator) — the second form keeps it unreduced."""
    if d is None: n, d = n.numerator, n.denominator
    return ('<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.05;margin:0 2px">'
            f'<span style="border-bottom:1.3px solid currentColor;padding:0 3px">{n}</span><span>{d}</span></span>')

def mh(f):
    """Mixed number (HTML) from a Fraction."""
    w, r = divmod(f.numerator, f.denominator)
    return str(w) if r == 0 else (f"{w}" if w else "") + fh(r, f.denominator)

def mt(f):
    """Simplest-form text answer: 3/4, 2 1/3, or 5."""
    w, r = divmod(f.numerator, f.denominator)
    if r == 0: return str(w)
    return f"{r}/{f.denominator}" if w == 0 else f"{w} {r}/{f.denominator}"

def keyl(xs, start=1):
    return ", ".join(f"{start+n}) {mt(x) if isinstance(x, Fr) else x}" for n, x in enumerate(xs))

BL = "<span class='blank-ln'></span>"

def hg(items, cols=4, size="14pt", space=4, start=1):
    """hgrid with numbering that continues across sections."""
    return f'<div class="grid{cols}">' + "".join(
        f'<div style="font-size:{size};padding:6px 0 {6+space}px"><b style="color:#2f5bd3">{start+n}.</b> {it}</div>' for n, it in enumerate(items)) + '</div>'

# ---------------- MATH CRASH COURSE · Week 2 ----------------
def math():
    S = Subject(K, "Math Crash Course", "Week 2 of 12"); r = random.Random(82)

    def proper(dmax=12, dmin=2):
        d = r.randint(dmin, dmax); n = r.randint(1, d - 1); g = gcd(n, d); return n // g, d // g

    # D1 equivalent fractions, simplifying, improper <-> mixed
    simp, seen = [], set()
    while len(simp) < 8:
        n, d = proper(10, 3); k = r.randint(2, 8)
        if (n * k, d * k) not in seen and d > 1: seen.add((n * k, d * k)); simp.append((n, d, k))
    eqv = []
    while len(eqv) < 3:
        n, d = proper(9, 3); k = r.randint(2, 6)
        if d > 1 and (n, d) not in [(a, b) for a, b, c in eqv]: eqv.append((n, d, k))
    imp = []
    for _ in range(4):
        d = r.randint(3, 9); w = r.randint(1, 6); rem = r.randint(1, d - 1); imp.append(Fr(d * w + rem, d) if gcd(rem, d) == 1 else Fr(d * w + 1, d))
    mix = []
    while len(mix) < 4:
        d = r.randint(3, 9); w = r.randint(1, 7); rem = r.choice([x for x in range(1, d) if gcd(x, d) == 1])
        if Fr(w * d + rem, d) not in mix: mix.append(Fr(w * d + rem, d))
    eq_items = [f"{fh(n, d)} = {fh('?', d * k)}" for n, d, k in eqv[:2]] + [f"{fh(eqv[2][0], eqv[2][1])} = {fh(eqv[2][0] * eqv[2][2], '?')}"]
    eq_key = [str(eqv[0][0] * eqv[0][2]), str(eqv[1][0] * eqv[1][2]), str(eqv[2][1] * eqv[2][2])]
    S.set(0, "Equivalent & Simplest Form",
        learnbox("<p><b>Equivalent fractions</b> name the same amount: multiply or divide the top and bottom by the <b>same</b> number. "
                 f"{fh(2, 3)} = {fh(8, 12)} (× 4). <b>Simplest form:</b> divide top and bottom by the <b>GCF</b> (greatest common factor). "
                 f"{fh(18, 24)}: GCF of 18 and 24 is 6 → {fh(3, 4)}. <b>Improper → mixed:</b> divide. {fh(17, 5)} → 17 ÷ 5 = 3 R2 → {mh(Fr(17, 5))}. "
                 f"<b>Mixed → improper:</b> whole × bottom + top. {mh(Fr(17, 5))} → 3 × 5 + 2 = 17 → {fh(17, 5)}.</p>", yt("simplify fractions GCF"))
        + '<div class="lab">A. Write in simplest form.</div>'
        + hg([f"{fh(n * k, d * k)} = {BL}" for n, d, k in simp])
        + '<div class="lab">B. Find the missing number.</div>' + hg([e + f" &nbsp;? = {BL}" for e in eq_items], 3, space=2, start=9)
        + '<div class="lab">C. Change improper fractions to mixed numbers (simplest form), and mixed numbers to improper fractions.</div>'
        + hg([f"{fh(f.numerator, f.denominator)} = {BL}" for f in imp] + [f"{mh(f)} = {BL}" for f in mix], start=12)
        + qs([("Which fraction is equivalent to 3/5?", ["9/15", "6/8", "5/3"]), ("What is the GCF of 18 and 30?", ["6", "3", "9"]),
              ("Which fraction is already in simplest form?", ["8/15", "6/9", "10/12"]), ("Which is the same as 4 1/2?", ["9/2", "5/2", "6/2"])], 20),
        "A) " + keyl([Fr(n, d) for n, d, k in simp]) + " (GCFs: " + ", ".join(str(k) for n, d, k in simp) + "). "
        "B) " + keyl(eq_key, 9) + ". C) " + keyl(imp, 12) + ", " + ", ".join(f"{16+n}) {f.numerator}/{f.denominator}" for n, f in enumerate(mix))
        + ". 20) 9/15. 21) 6. 22) 8/15. 23) 9/2.")

    # D2 add / subtract unlike denominators (incl. mixed numbers)
    dens = [(2, 3), (3, 4), (4, 6), (5, 10), (6, 8), (3, 5), (2, 7), (4, 5), (6, 9), (8, 12), (3, 8), (5, 6)]
    r.shuffle(dens)
    def pf(d): return Fr(r.choice([x for x in range(1, d) if gcd(x, d) == 1]), d)
    adds, subs = [], []
    for a, b in dens[:4]: adds.append((pf(a), pf(b)))
    for a, b in dens[4:8]:
        x, y = pf(a), pf(b)
        while x == y: x, y = pf(a), pf(b)
        subs.append((max(x, y), min(x, y)))
    madd, msub = [], []
    for a, b in dens[8:10]:
        x, y = pf(a) + r.randint(1, 5), pf(b) + r.randint(1, 4); madd.append((x, y))
    for a, b in dens[10:12]:            # borrowing: first fraction part smaller than second
        p, q = pf(a), pf(b)
        while p == q: p, q = pf(a), pf(b)
        lo, hi = min(p, q), max(p, q); msub.append((lo + r.randint(4, 8), hi + r.randint(1, 3)))
    d2 = ([f"{fh(x)} + {fh(y)} = " for x, y in adds] + [f"{fh(x)} − {fh(y)} = " for x, y in subs]
          + [f"{mh(x)} + {mh(y)} = " for x, y in madd] + [f"{mh(x)} − {mh(y)} = " for x, y in msub])
    d2k = [x + y for x, y in adds] + [x - y for x, y in subs] + [x + y for x, y in madd] + [x - y for x, y in msub]
    wp2 = Fr(11, 4) - Fr(4, 3)
    S.set(1, "Adding & Subtracting Fractions",
        learnbox("<p>You can only add or subtract fractions with the <b>same denominator</b>. Find the <b>LCD</b> (least common denominator), rename each "
                 f"fraction, then add or subtract the numerators. Keep the denominator. Simplify. {fh(1, 4)} + {fh(2, 3)}: LCD = 12 → {fh(3, 12)} + {fh(8, 12)} = {fh(11, 12)}.<br>"
                 "<b>Mixed numbers:</b> do the fractions, then the whole numbers. If you can't subtract the fractions, <b>borrow</b> 1 whole: "
                 f"{mh(Fr(37, 6))} − {mh(Fr(11, 4))} → 6{fh(2, 12)} − 2{fh(9, 12)} → 5{fh(14, 12)} − 2{fh(9, 12)} = <b>{mh(Fr(37, 6) - Fr(11, 4))}</b>.</p>",
                 yt("add subtract fractions unlike denominators"))
        + '<div class="lab">Show your work. Answers in simplest form (change improper answers to mixed numbers).</div>'
        + hgrid([e + "<div style='height:44px'></div>" for e in d2], 4, "14pt", 4)
        + qs([("What is the LCD of 6 and 8?", ["24", "48", "14"]), ("1/2 + 1/3 = ?", ["5/6", "2/5", "2/6"]),
              ("To subtract 3 1/5 − 1 3/5, you first need to…", ["borrow 1 from the 3 (3 1/5 = 2 6/5)", "subtract 3/5 − 1/5", "add the wholes"]),
              (f"A recipe needs 2 3/4 cups of flour. You have 1 1/3 cups. How much more do you need?", 2)], 13),
        keyl(d2k) + f". 13) 24. 14) 5/6. 15) borrow (3 1/5 = 2 6/5). 16) 2 3/4 − 1 1/3 = 33/12 − 16/12 = {mt(wp2)} cups.")

    # D3 multiply fractions & mixed numbers
    mf = [(pf(r.randint(2, 9)), pf(r.randint(2, 10))) for _ in range(5)]
    wf = [(r.randint(3, 12), pf(r.choice([3, 4, 5, 6, 8]))) for _ in range(2)]
    mm = [(pf(r.randint(2, 6)) + r.randint(1, 3), pf(r.randint(2, 6)) + r.randint(1, 2)) for _ in range(2)] + [(pf(r.choice([3, 4, 5])) + r.randint(1, 4), pf(r.choice([3, 4, 5, 6])))]
    d3 = [f"{fh(x)} × {fh(y)} = " for x, y in mf] + [f"{w} × {fh(y)} = " for w, y in wf] + [f"{mh(x)} × {mh(y)} = " for x, y in mm]
    d3k = [x * y for x, y in mf] + [w * y for w, y in wf] + [x * y for x, y in mm]
    S.set(2, "Multiplying Fractions",
        learnbox("<p><b>Multiply</b> the numerators, <b>multiply</b> the denominators, then simplify. No common denominator needed! "
                 f"{fh(2, 3)} × {fh(9, 10)} = {fh(18, 30)} = <b>{fh(3, 5)}</b>. You may also simplify (cancel) a top and a bottom number by a common factor <b>before</b> you multiply. "
                 f"<b>Whole numbers:</b> write over 1 — 4 × {fh(2, 3)} = {fh(4, 1)} × {fh(2, 3)} = {fh(8, 3)} = {mh(Fr(8, 3))}. "
                 f"<b>Mixed numbers:</b> change to improper fractions first — {mh(Fr(3, 2))} × {mh(Fr(8, 3))} = {fh(3, 2)} × {fh(8, 3)} = {fh(24, 6)} = <b>4</b>.</p>",
                 yt("multiplying fractions and mixed numbers"))
        + '<div class="lab">Show your work. Answers in simplest form.</div>'
        + hgrid([e + "<div style='height:34px'></div>" for e in d3], 4, "14pt", 4)
        + qs([(f"3/4 × 2/5 = ?", [mt(Fr(3, 4) * Fr(2, 5)), "5/9", "6/9"]),
              ("Before you multiply 2 1/3 × 3/4, you should…", ["change 2 1/3 to 7/3", "find a common denominator", "multiply 2 × 3 only"]),
              ("When you multiply two fractions less than 1, the answer is…", ["smaller than both", "bigger than both", "always 1"]),
              ("Our co-op has 24 kids, and 3/4 of them came on the field trip. How many came?", 1),
              ("A board is 5 1/2 feet long. Dad uses 2/3 of it. How many feet does he use?", 1)], 11),
        keyl(d3k) + f". 11) {mt(Fr(3, 4) * Fr(2, 5))}. 12) change 2 1/3 to 7/3. 13) smaller than both. 14) {mt(24 * Fr(3, 4))} kids. 15) {mt(Fr(11, 2) * Fr(2, 3))} feet.")

    # D4 divide fractions — multiply by the reciprocal
    dv = []
    while len(dv) < 5:
        x, y = pf(r.randint(3, 9)), pf(r.randint(2, 8))
        if x != y: dv.append((x, y))
    wd = [(r.randint(2, 9), pf(r.choice([3, 4, 5, 6])))]
    md = [(pf(r.randint(2, 6)) + r.randint(1, 4), pf(r.randint(2, 5)) + r.randint(1, 2)) for _ in range(2)] + [(pf(r.choice([3, 4, 5])) + r.randint(2, 5), r.randint(2, 4))]
    d4 = [f"{fh(x)} ÷ {fh(y)} = " for x, y in dv] + [f"{w} ÷ {fh(y)} = " for w, y in wd] + [f"{mh(x)} ÷ {mh(Fr(y))} = " for x, y in md]
    d4k = [x / y for x, y in dv] + [w / y for w, y in wd] + [x / y for x, y in md]
    S.set(3, "Dividing Fractions",
        learnbox("<p>The <b>reciprocal</b> of a fraction is the fraction flipped: {0} ↔ {1}. To <b>divide</b> fractions, keep the first fraction, change ÷ to ×, "
                 "and multiply by the <b>reciprocal</b> of the second fraction. {2} ÷ {3} = {2} × {4} = {5} = <b>{6}</b>. "
                 "Change mixed numbers and whole numbers to improper fractions <b>first</b>: {7} ÷ 2 = {8} ÷ {9} = {8} × {10} = <b>{11}</b>. "
                 "Check: the answer × the divisor should give you back the first number.</p>".format(
                     fh(3, 4), fh(4, 3), fh(2, 3), fh(4, 5), fh(5, 4), fh(10, 12), fh(5, 6), mh(Fr(9, 4)), fh(9, 4), fh(2, 1), fh(1, 2), mh(Fr(9, 8))),
                 yt("dividing fractions reciprocal"))
        + '<div class="lab">Show your work. Answers in simplest form.</div>'
        + hgrid([e + "<div style='height:34px'></div>" for e in d4], 3, "14pt", 4)
        + qs([("What is the reciprocal of 2 1/2?", ["2/5", "5/2", "1/2"]), ("What is the reciprocal of 7?", ["1/7", "7", "7/7"]),
              ("To divide 3/8 ÷ 1/4 you…", ["multiply 3/8 × 4/1", "multiply 8/3 × 1/4", "find a common denominator and subtract"]),
              ("You have 3 3/4 yards of ribbon. Each bow takes 5/8 yard. How many bows can you make?", 1),
              ("Mom splits a 2/3-pound bag of trail mix evenly into 4 snack bags. How much is in each bag?", 1)], 10),
        keyl(d4k) + f". 10) 2/5. 11) 1/7. 12) multiply 3/8 × 4/1 (= {mt(Fr(3, 8) / Fr(1, 4))}). 13) {mt(Fr(15, 4) / Fr(5, 8))} bows. 14) {mt(Fr(2, 3) / 4)} pound.")

    # D5 checkpoint
    cp = [(f"Simplify {fh(24, 36)}", Fr(24, 36)), (f"Write {fh(29, 6)} as a mixed number", Fr(29, 6)), (f"Write {mh(Fr(23, 7))} as an improper fraction", "23/7"),
          (f"{fh(5, 6)} + {fh(3, 4)}", Fr(5, 6) + Fr(3, 4)), (f"{fh(7, 8)} − {fh(1, 6)}", Fr(7, 8) - Fr(1, 6)),
          (f"{mh(Fr(17, 5))} + {mh(Fr(11, 2))}", Fr(17, 5) + Fr(11, 2)), (f"{mh(Fr(25, 4))} − {mh(Fr(8, 3))}", Fr(25, 4) - Fr(8, 3)),
          (f"{fh(4, 9)} × {fh(3, 8)}", Fr(4, 9) * Fr(3, 8)), (f"{mh(Fr(9, 4))} × {mh(Fr(4, 3))}", Fr(9, 4) * Fr(4, 3)),
          (f"{fh(5, 6)} ÷ {fh(2, 3)}", Fr(5, 6) / Fr(2, 3)), (f"{mh(Fr(7, 2))} ÷ {fh(7, 8)}", Fr(7, 2) / Fr(7, 8))]
    S.set(4, "Week 2 Checkpoint",
        learnbox("<p><b>Checkpoint!</b> 15 problems from this week. Show your work in the space or on scratch paper, and give every answer in simplest form. "
                 "<b>Goal: 12 of 15 (80%) to pass.</b> If you score less than 12, that's okay — Mom will re-teach the skills you missed at the start of next week "
                 "before we move on to Week 3 (Decimals & Money).</p>")
        + hgrid([f"{q} = <div style='height:40px'></div>" for q, a in cp], 3, "14pt", 2)
        + qs([("Which is equivalent to 4/10?", ["2/5", "4/5", "1/4"]), ("What is the LCD of 4 and 10?", ["20", "40", "14"]),
              ("What is the reciprocal of 3/7?", ["7/3", "3/7", "−3/7"]),
              ("A pan of brownies is 3/4 full. Nevaeh eats 1/3 of what's left. How much of the whole pan did she eat?", ["1/4", "1/3", "5/12"])], 12)
        + '<div class="big">Score: ______ / 15 &nbsp;&nbsp; Passed (12+)? &nbsp;Yes / Not yet</div>',
        keyl([a for q, a in cp]) + f". 12) 2/5. 13) 20. 14) 7/3. 15) {mt(Fr(3, 4) * Fr(1, 3))}. Pass = 12+/15; below 12 → re-teach missed skills next week.")
    return S

# ---------------- ENGLISH ----------------
def english():
    S = Subject(K, "English", "Week 3 · Punctuation Power")
    cm = [("We packed sandwiches, apples, and water bottles.", "C"), ("Yes I finished my history page.", "N"),
          ("On July 4, 1776, Congress adopted the Declaration.", "C"), ("My cousin lives in Orlando Florida.", "N"),
          ("However, the rain stopped before lunch.", "C"), ("Bring your Bible a pencil and a notebook.", "N")]
    S.set(0, "Commas",
        learnbox("<p><b>Comma rules:</b> ① <b>Series</b> of 3+ items: <i>eggs, milk, and bread.</i> ② After <b>introductory words/phrases</b>: <i>Yes, … Well, … However, … After lunch, …</i> "
                 "③ <b>Dates</b>: between day and year, and after the year mid-sentence: <i>On November 10, 2026, we started Week 3.</i> "
                 "④ <b>Places</b>: between city and state, and after the state mid-sentence: <i>Jacksonville, Florida, is our home.</i></p>", yt("comma rules middle school"))
        + '<div class="lab">Mark each sentence C (correct) or N (needs a comma).</div>' + mark_list([a for a, b in cm], ["C", "N"])
        + qs([("Which date is punctuated correctly?", ["The fair opened on Friday, March 6, 2026, at noon.", "The fair opened on Friday March 6 2026 at noon.", "The fair opened on, Friday March 6, 2026 at noon."]),
              ("Which sentence is correct?", ["We drove to Savannah, Georgia, for the weekend.", "We drove to Savannah Georgia, for the weekend.", "We drove, to Savannah, Georgia for the weekend."])], 7)
        + '<div class="lab">Rewrite each sentence with the missing commas.</div>'
        + qs([("Well I think we should leave at 8:00.", 1), ("Nylah Naomi and Titus fed the chickens.", 1),
              ("Grandma was born on May 12 1968 in Atlanta Georgia.", 1)], 9),
        "1 C, 2 N (Yes,), 3 C, 4 N (Orlando, Florida), 5 C, 6 N (Bible, a pencil, and). 7) Friday, March 6, 2026, at noon. 8) Savannah, Georgia, for. "
        "9) Well, I think… 10) Nylah, Naomi, and Titus… 11) May 12, 1968, in Atlanta, Georgia.")
    sc = [("I have one goal ___ finish the race.", ":"), ("The bus was late ___ we missed the first song.", ";"), ("We need three things ___ eggs, milk, and flour.", ":"),
          ("Titus loves trucks ___ Nayeli loves dolls.", ";"), ("Church starts at 10 ___ 30 on Sunday.", ":"), ("It was cold ___ however, we still went swimming.", ";"),
          ("Read Psalm 23 ___ 1 before bed.", ":"), ("The puppy was tired ___ it fell asleep on the rug.", ";")]
    S.set(1, "Semicolons & Colons",
        learnbox("<p>A <b>semicolon ( ; )</b> joins two <b>complete sentences</b> that are closely related, without a FANBOYS word: <i>The power went out; we lit candles.</i> "
                 "With words like <b>however</b> or <b>therefore</b>, use a semicolon before and a comma after: <i>It rained; however, we still played.</i><br>"
                 "A <b>colon ( : )</b> comes after a complete sentence to introduce a <b>list</b> or an <b>explanation</b>: <i>Bring three things: a pencil, a ruler, and an eraser.</i> "
                 "Colons also go in <b>times</b> (8:30) and <b>Bible references</b> (John 3:16). Don't put a colon right after <i>are</i> or <i>include</i>.</p>", yt("semicolons and colons"))
        + '<div class="lab">Which mark belongs in the blank? Circle ; or :</div>' + mark_list([a for a, b in sc], [";", ":"])
        + qs([("Which uses a colon correctly?", ["My favorite fruits are these: mango, kiwi, and pears.", "My favorite fruits are: mango, kiwi, and pears.", "My: favorite fruits are mango, kiwi, and pears."]),
              ("Which uses a semicolon correctly?", ["The power went out; we lit candles.", "The power went out; and we lit candles.", "The power; went out we lit candles."]),
              ("Join with a semicolon and <b>however</b>: <i>I studied hard. The test was still tricky.</i>", 1),
              ("Write a sentence that uses a colon to introduce a list of your favorite foods.", 1),
              ("Write a sentence where a semicolon joins two related ideas about your week.", 1)], 9),
        "1 :, 2 ;, 3 :, 4 ;, 5 : (10:30), 6 ;, 7 : (Psalm 23:1), 8 ;. 9) My favorite fruits are these: mango, kiwi, and pears. 10) The power went out; we lit candles. "
        "11) I studied hard; however, the test was still tricky. 12–13 vary.")
    S.set(2, "Quotation Marks & Dialogue",
        learnbox("<p><b>Quotation marks</b> go around a speaker's <b>exact words</b>. Capitalize the first word of the quote. Commas, periods, question marks, and "
                 "exclamation points go <b>inside</b> the closing marks.<br><i>Mom said, “Wash your hands.”</i> &nbsp;·&nbsp; <i>“Wash your hands,” Mom said.</i> &nbsp;·&nbsp; "
                 "<i>“Did you finish?” asked Dad.</i><br>A <b>split quote</b>: <i>“When you finish,” Mom said, “bring me your page.”</i> In a story, start a <b>new paragraph</b> "
                 "every time the speaker changes. Titles of <b>short works</b> (songs, poems, chapters) also go in quotation marks: “Amazing Grace.”</p>", yt("punctuating dialogue quotation marks"))
        + qs([("Which is punctuated correctly?", ["“Let's go to the park,” said Naomi.", "“Let's go to the park”, said Naomi.", "“Let's go to the park,” Said Naomi."]),
              ("Which is punctuated correctly?", ["Dad asked, “Who left the gate open?”", "Dad asked, “Who left the gate open”?", "Dad asked “who left the gate open?”"]),
              ("Which split quote is correct?", ["“If it rains,” Titus said, “we'll play inside.”", "“If it rains,” Titus said, “We'll play inside.”", "“If it rains” Titus said “we'll play inside.”"]),
              ("Which sentence uses quotation marks for a title correctly?", ["We sang “Amazing Grace” at church.", "We sang Amazing “Grace” at church.", "“We sang Amazing Grace at church.”"])])
        + '<div class="lab">Rewrite with correct quotation marks, commas, and capitals.</div>'
        + qs([("pastor james said remember to bring your Bible", 1), ("can I help with dinner asked Nevaeh", 1)], 5)
        + '<div class="lab">7. Write a short dialogue (4 lines) between you and a friend planning a fun day. New speaker = new line.</div>' + lines(4, 23),
        "1) “Let's go to the park,” said Naomi. 2) Dad asked, “Who left the gate open?” 3) “If it rains,” Titus said, “we'll play inside.” 4) We sang “Amazing Grace” at church. "
        "5) Pastor James said, “Remember to bring your Bible.” 6) “Can I help with dinner?” asked Nevaeh. 7) varies — check marks, commas inside, new line per speaker.")
    ap = [("The cat licked", ("its", "it's"), "paw."), ("", ("They're", "Their", "There"), "coming over after lunch."), ("I can't find", ("Dad's", "Dads'"), "keys."),
          ("Both", ("girls'", "girl's"), "jackets were on the floor."), ("", ("It's", "Its"), "going to be a sunny day."), ("The", ("children's", "childrens'"), "choir sang first."),
          ("", ("Whose", "Who's"), "shoes are these?"), ("We bought three", ("apples", "apple's"), "at the market.")]
    S.set(3, "Apostrophes",
        learnbox("<p>Apostrophes do two jobs.<br>① <b>Contractions</b> — the apostrophe replaces missing letters: <i>do not → don't, it is → it's, they are → they're, will not → won't.</i><br>"
                 "② <b>Possessives</b> (ownership): one owner → add <b>'s</b> (<i>the dog's bowl</i>). Plural ending in s → add just <b>'</b> (<i>the dogs' bowls</i>). "
                 "Plural not ending in s → add <b>'s</b> (<i>the children's books</i>).<br><b>Never</b> use an apostrophe for possessive pronouns (<i>its, yours, hers, theirs, whose</i>) "
                 "or for plain plurals (<i>two apples</i>, not <i>apple's</i>).</p>", yt("apostrophes possessives contractions"))
        + '<div class="lab">Circle the correct word.</div>'
        + '<div class="grid2">' + "".join(f'<div style="padding:3px 0"><b>{n+1}.</b> {a} {pick(*o)} {b}</div>' for n, (a, o, b) in enumerate(ap)) + '</div>'
        + '<div class="lab">Write the contraction.</div>'
        + hg([f"{w} → {BL}" for w in ["can not", "I would", "we have", "should not"]], 4, "12pt", 0, 9)
        + '<div class="lab">Write it as a possessive (example: the bowl of the dog → the dog\'s bowl).</div>'
        + hg([f"{w}<br>{BL}" for w in ["the nest of the bird", "the bikes belonging to my brothers", "the toys of the children"]], 3, "12pt", 0, 13)
        + qs([("Which sentence is correct?", ["The Smiths' van is in the driveway.", "The Smith's van is in the driveway.", "The Smiths van' is in the driveway."]),
              ("Write one sentence that uses BOTH <i>its</i> and <i>it's</i> correctly.", 1)], 16),
        "1) its 2) They're 3) Dad's 4) girls' 5) It's 6) children's 7) Whose 8) apples. 9) can't 10) I'd 11) we've 12) shouldn't. 13) the bird's nest 14) my brothers' bikes "
        "15) the children's toys. 16) The Smiths' van… 17) varies (e.g., It's sad that the dog hurt its paw).")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — commas, semicolons, colons, quotation marks, and apostrophes. Goal: 8 of 10.</p>")
        + qs([("Which sentence is punctuated correctly?", ["We visited St. Augustine, Florida, on June 3, 2025.", "We visited St. Augustine Florida, on June 3 2025.", "We visited, St. Augustine, Florida on June 3, 2025."]),
              ("Where does the comma go? <i>After church we ate lunch at Grandma's.</i>", ["after church", "after we", "after lunch"]),
              ("Which mark belongs in the blank? <i>I packed two snacks ___ crackers and grapes.</i>", ["colon ( : )", "semicolon ( ; )", "no mark"]),
              ("Which joins the sentences correctly?", ["The game was over; we headed home.", "The game was over, we headed home.", "The game was over: and we headed home."]),
              ("Which is punctuated correctly?", ["“Are you ready?” asked Mom.", "“Are you ready”? asked Mom.", "“Are you ready,” asked Mom?"]),
              ("Which word means “it is”?", ["it's", "its", "its'"]),
              ("Fix it: <i>The dogs bowl is empty and the two cats bowls are too.</i>", 1),
              ("Rewrite with quotation marks: <i>Titus shouted look at that huge rainbow</i>", 1),
              ("Write a sentence with a semicolon and the word <b>therefore</b>.", 1),
              ("Write a sentence that uses a colon before a list of three things you'd pack for a trip.", 1)]),
        "1) We visited St. Augustine, Florida, on June 3, 2025. 2) after church (After church, we…). 3) colon. 4) The game was over; we headed home. 5) “Are you ready?” asked Mom. "
        "6) it's. 7) The dog's bowl is empty, and the two cats' bowls are too. 8) Titus shouted, “Look at that huge rainbow!” 9) varies (…; therefore, …). 10) varies (complete sentence + colon + list with commas).")
    return S

# ---------------- SCIENCE ----------------
import re
_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
def chem(eq):
    """'2H2 + O2 -> 2H2O' -> pretty text with subscripts (coefficients stay full size)."""
    out = []
    for t in eq.split():
        if t == "->": out.append("→")
        elif t == "+": out.append("+")
        else:
            m = re.match(r"(\d*)(.*)", t); out.append(m.group(1) + m.group(2).translate(_SUB))
    return " ".join(out)

def atoms(side):
    """Count atoms on one side of an equation, e.g. '2H2 + O2'."""
    tot = {}
    for t in side.split(" + "):
        m = re.match(r"(\d*)(.*)", t.strip()); c = int(m.group(1) or 1)
        for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", m.group(2)):
            tot[el] = tot.get(el, 0) + c * int(n or 1)
    return tot

def science():
    S = Subject(K, "Science", "Week 3 · Matter & Its Changes")
    S.set(0, "States of Matter",
        learnbox("<p>All matter is made of tiny particles (atoms and molecules) that are <b>always moving</b>. In a <b>solid</b>, particles are packed tightly and only "
                 "<b>vibrate</b> in place, so a solid keeps its own shape and volume. In a <b>liquid</b>, particles are close but <b>slide past</b> each other, so a liquid "
                 "has a set volume but takes the shape of its container. In a <b>gas</b>, particles are <b>far apart</b> and move fast in every direction, so a gas spreads "
                 "out to fill any container. Adding thermal energy (heat) makes particles move faster — that's what causes <b>phase changes</b>: melting (solid → liquid), "
                 "freezing (liquid → solid), evaporation/boiling (liquid → gas), condensation (gas → liquid), and sublimation (solid → gas, like dry ice). "
                 "Water melts at 0 °C (32 °F) and boils at 100 °C (212 °F) at sea level.</p>", yt("states of matter particle theory"))
        + fill_table(["State", "Definite shape? (yes/no)", "Definite volume? (yes/no)", "How do the particles move?"], [["Solid", "", "", ""], ["Liquid", "", "", ""], ["Gas", "", "", ""]], 30)
        + '<div class="lab">Name the phase change.</div>'
        + qs([("An ice cube in your lemonade gets smaller.", ["melting", "freezing", "condensation"]),
              ("Drops of water form on the outside of a cold glass on a hot Florida day.", ["condensation", "evaporation", "melting"]),
              ("A puddle disappears after the sun comes out.", ["evaporation", "condensation", "sublimation"]),
              ("Dry ice turns straight into a foggy gas without melting.", ["sublimation", "evaporation", "freezing"]),
              ("Water in an ice-cube tray turns solid in the freezer.", ["freezing", "condensation", "melting"]),
              ("When you heat a liquid, its particles…", ["move faster and spread apart", "slow down and pack together", "stop moving"]),
              ("Use particles to explain why the smell of cookies baking spreads through the whole house.", 2)]),
        "Solid: yes, yes, packed tight & vibrate in place. Liquid: no, yes, close but slide past each other. Gas: no, no, far apart, fast, every direction. "
        "1) melting 2) condensation 3) evaporation 4) sublimation 5) freezing 6) move faster & spread apart 7) gas particles from the cookies move fast and spread out to fill the space.")
    ch = [("Chopping firewood", "P"), ("Burning firewood", "C"), ("An iron gate rusting", "C"), ("Ice melting", "P"), ("Baking a cake", "C"),
          ("Dissolving sugar in tea", "P"), ("Milk going sour", "C"), ("Tearing paper", "P"), ("A banana turning brown", "C"), ("Boiling water", "P")]
    S.set(1, "Physical vs. Chemical Changes",
        learnbox("<p>A <b>physical property</b> can be observed without changing what the substance is: color, hardness, density, melting point, whether it's magnetic, "
                 "whether it dissolves. A <b>chemical property</b> describes how a substance can change into a <b>new</b> substance: flammability (can it burn?), "
                 "ability to rust, reacting with acid.<br>A <b>physical change</b> changes size, shape, or state, but it is still the same stuff (cutting, melting, dissolving). "
                 "A <b>chemical change</b> makes a <b>new substance</b> with new properties (burning, rusting, cooking, digesting). Physical changes are often easy to "
                 "undo; chemical changes usually are not.</p>", yt("physical and chemical changes"))
        + '<div class="lab">Mark each P (physical change) or C (chemical change).</div>' + mark_list([a for a, b in ch], ["P", "C"], cols=2)
        + qs([("Which is a <b>chemical property</b> of wood?", ["It can burn.", "It is brown.", "It floats on water."]),
              ("Which is a <b>physical property</b> of copper?", ["It is shiny and orange-brown.", "It turns green when it reacts with air over time.", "It reacts with nitric acid."]),
              ("Dissolving salt in water is a physical change because…", ["the salt is still salt — you can get it back by evaporating the water", "a new substance forms", "it gives off light"]),
              ("A marshmallow over a campfire turns black and crispy. Physical or chemical? How do you know?", 2),
              ("Name one physical change and one chemical change that happen in your kitchen.", 2)], 11),
        "1 P, 2 C, 3 C, 4 P, 5 C, 6 P, 7 C, 8 P, 9 C, 10 P. 11) It can burn. 12) shiny and orange-brown. 13) salt is still salt / can be recovered. "
        "14) chemical — a new black substance (carbon) forms; you can't undo it. 15) varies (e.g., boiling water / toasting bread).")
    rx = ["4Fe + 3O2 -> 2Fe2O3", "CH4 + 2O2 -> CO2 + 2H2O", "NaHCO3 + HCl -> NaCl + H2O + CO2"]
    S.set(2, "Chemical Reactions",
        learnbox("<p>In a <b>chemical reaction</b>, atoms rearrange to make new substances. The starting substances are the <b>reactants</b>; the new ones are the "
                 "<b>products</b>. A chemical equation shows them with an arrow that means “yields”: &nbsp;<b>reactants → products</b>. "
                 f"Rust: {chem(rx[0])} (iron + oxygen → iron oxide).<br><b>Signs a reaction happened:</b> ① gas bubbles (not from boiling), ② color change, "
                 "③ temperature change or light given off, ④ a <b>precipitate</b> (a solid forms when two liquids mix), ⑤ a new odor. "
                 "Baking soda + vinegar fizzes because it makes carbon dioxide gas.</p>", yt("signs of a chemical reaction"))
        + '<div class="lab">For each equation, list the reactants and the products.</div>'
        + "".join(f'<div><b>{n+1}.</b> {chem(e)}<div style="display:flex;gap:16px;margin-top:4px"><span style="flex:1">Reactants: {BL}</span><span style="flex:1">Products: {BL}</span></div></div>' for n, e in enumerate(rx))
        + qs([("Which is a sign of a chemical reaction?", ["Bubbles form when you drop an antacid tablet in water.", "Water boils into steam.", "Butter melts in a pan."]),
              ("Which is NOT a sign of a chemical reaction?", ["Ice cubes melting in a cup", "A sparkler giving off light and heat", "A cloudy solid forming when two clear liquids mix"]),
              ("A solid that forms when two liquids are mixed is called a…", ["precipitate", "reactant", "solution"]),
              ("In an equation, the arrow means…", ["yields (makes)", "equals exactly", "subtract"]),
              ("Glow sticks give off light when you snap them. Which sign of a reaction is that?", ["light given off", "gas bubbles", "a precipitate"]),
              ("Bread dough rises and bakes into a loaf. List two signs that chemical changes happened.", 2)], 4),
        "1) Reactants: iron (Fe), oxygen (O₂); Product: iron oxide (Fe₂O₃). 2) Reactants: methane (CH₄), oxygen (O₂); Products: carbon dioxide (CO₂), water (H₂O). "
        "3) Reactants: sodium bicarbonate (NaHCO₃), hydrochloric acid (HCl); Products: sodium chloride (NaCl), water, carbon dioxide. "
        "4) antacid bubbles. 5) ice melting. 6) precipitate. 7) yields. 8) light given off. 9) e.g., gas bubbles (dough rises), color change (browns), new smell.")
    eqs = ["2H2 + O2 -> 2H2O", "CH4 + 2O2 -> CO2 + 2H2O", "2Mg + O2 -> 2MgO", "N2 + 3H2 -> 2NH3"]
    def cnt(e):
        L, R = [atoms(x) for x in e.split(" -> ")]
        return ", ".join(f"{el} {L[el]}/{R.get(el, 0)}" for el in L)
    rows = [[f"<b>{i+1}.</b> " + chem(e), "  ".join(f"{el}: ___" for el in atoms(e.split(' -> ')[0])), "  ".join(f"{el}: ___" for el in atoms(e.split(' -> ')[0])), ""] for i, e in enumerate(eqs)]
    sug = atoms("2C6H12O6"); h2o3 = atoms("3H2O")
    S.set(3, "Conservation of Mass",
        learnbox("<p>The <b>law of conservation of mass</b>: in a chemical reaction, matter is not created or destroyed — atoms are only <b>rearranged</b>. So the total mass "
                 "of the reactants equals the total mass of the products (in a closed container). French chemist <b>Antoine Lavoisier</b> showed this in the late 1700s.<br><b>Counting atoms:</b> a <b>subscript</b> (small number) counts the atoms of the element just "
                 f"before it: H₂O has 2 H and 1 O. A <b>coefficient</b> (big number in front) multiplies the whole molecule: 3H₂O has {h2o3['H']} H and {h2o3['O']} O. "
                 "An equation is <b>balanced</b> when every element has the same number of atoms on both sides.</p>", yt("conservation of mass counting atoms"))
        + '<div class="lab">Count the atoms on each side. Is it balanced?</div>'
        + fill_table(["Equation", "Reactant side (left)", "Product side (right)", "Balanced?"], rows, 30)
        + qs([("How many atoms of each element are in 2C₆H₁₂O₆ (two sugar molecules)?", 1),
              ("Is H₂ + O₂ → H₂O balanced?", ["No — 2 oxygen atoms on the left but only 1 on the right", "Yes — it has H and O on both sides", "Yes — there are 3 molecules"]),
              ("In a sealed bag, 10 g of baking soda reacts with 50 g of vinegar. What is the mass of everything in the bag afterward?", ["60 g", "50 g", "less than 60 g, because gas formed"]),
              ("If you do the same reaction in an open cup, the cup weighs less afterward. Why?", ["Carbon dioxide gas escaped into the air.", "Atoms were destroyed.", "The vinegar evaporated instantly."]),
              ("Explain in your own words why the number of atoms must be the same on both sides of an equation.", 2)], 5),
        "Table (left/right): " + "; ".join(f"{i+1}) {cnt(e)} — balanced" for i, e in enumerate(eqs)) + ". "
        f"5) C {sug['C']}, H {sug['H']}, O {sug['O']} ({sum(sug.values())} atoms). 6) No — O 2 vs 1. 7) 60 g. 8) CO₂ gas escaped. 9) atoms are rearranged, never created or destroyed (conservation of mass).")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — matter and its changes. Goal: 8 of 10.</p>")
        + qs([("In which state do particles only vibrate in place?", ["solid", "liquid", "gas"]),
              ("A gas takes the shape and volume of its container because its particles…", ["are far apart and move freely", "are packed tightly", "do not move"]),
              ("Water vapor turning into dew on the grass is…", ["condensation", "evaporation", "sublimation"]),
              ("Which is a chemical change?", ["Frying an egg", "Freezing juice into popsicles", "Cutting paper into snowflakes"]),
              ("Which is a chemical property?", ["flammability", "color", "density"]),
              ("In A + B → C, what are A and B?", ["reactants", "products", "precipitates"]),
              ("How many oxygen atoms are in 2CO₂?", ["4", "2", "3"]),
              ("List three signs that a chemical reaction may have happened.", 1),
              ("Count the atoms: is 2Na + Cl₂ → 2NaCl balanced? Show the counts.", 1),
              ("Explain the law of conservation of mass and give an example.", 2)]),
        f"1) solid 2) far apart & move freely 3) condensation 4) frying an egg 5) flammability 6) reactants 7) {atoms('2CO2')['O']}. 8) any 3: gas bubbles, color change, temperature change/light, precipitate, new odor. "
        "9) Yes — Na " + "/".join(str(atoms(x)['Na']) for x in ['2Na + Cl2', '2NaCl']) + ", Cl " + "/".join(str(atoms(x)['Cl']) for x in ['2Na + Cl2', '2NaCl'])
        + ". 10) Mass is not created or destroyed in a reaction; atoms rearrange (e.g., sealed bag of baking soda + vinegar weighs the same before and after).")
    return S

# ---------------- HISTORY ----------------
def history():
    S = Subject(K, "History", "Week 3 · The Road to Revolution")
    S.set(0, "The French & Indian War",
        learnbox("<p>Last week we met the Thirteen Colonies. By the 1750s, Britain and France both claimed the rich <b>Ohio River Valley</b>. In 1754, a 22-year-old Virginia "
                 "officer named <b>George Washington</b> clashed with the French there and had to surrender at <b>Fort Necessity</b>. That started the <b>French and Indian War "
                 "(1754–1763)</b> — Britain and its colonists against France and its Native American allies. Britain finally won, and in the <b>Treaty of Paris (1763)</b> France "
                 "gave up Canada and its land east of the Mississippi River. Spain, France's ally, gave <b>Florida</b> to Britain! But the war nearly <b>doubled Britain's debt</b>. "
                 "Parliament decided the colonists should help pay for it — and for the soldiers left to guard them. The <b>Proclamation of 1763</b> also forbade colonists to settle "
                 "west of the <b>Appalachian Mountains</b>, which made many of them angry.</p>", yt("French and Indian War for kids"))
        + qs([("What land did Britain and France both want?", ["the Ohio River Valley", "the Florida Keys", "New England"]),
              ("Who fought on each side?", ["Britain & the colonists vs. France & its Native American allies", "Britain vs. the colonists", "France & the colonists vs. Spain"]),
              ("What happened to Florida in the Treaty of Paris (1763)?", ["Spain gave it to Britain.", "France bought it.", "It became the 14th colony to join the war."]),
              ("Why was Britain short on money after the war, and how did it plan to fix that?", 2),
              ("What did the Proclamation of 1763 forbid?", ["settling west of the Appalachian Mountains", "trading with France", "building new churches"]),
              ("Imagine you are a colonist who fought in the war. How would you feel about the Proclamation of 1763? Explain.", 3)]),
        "1) Ohio River Valley. 2) Britain & colonists vs. France & Native allies. 3) Spain gave Florida to Britain. 4) the war nearly doubled its debt; it planned to tax the colonists. "
        "5) settling west of the Appalachians. 6) opinion (e.g., angry — they fought for that land and were then kept out of it).")
    S.set(1, "The Stamp Act, 1765",
        learnbox("<p>To pay its war debt, Parliament passed the <b>Sugar Act (1764)</b> and then the <b>Stamp Act (1765)</b>, the first tax placed <b>directly</b> on the colonists. "
                 "Newspapers, legal documents, licenses, pamphlets, and even playing cards had to carry a paid tax stamp. Colonists were furious — not mostly about the money, but "
                 "because they had <b>no representatives in Parliament</b>. Their cry: <b>“No taxation without representation!”</b> Groups called the <b>Sons of Liberty</b> "
                 "protested, sometimes violently. Nine colonies sent delegates to the <b>Stamp Act Congress</b>, and merchants <b>boycotted</b> (refused to buy) British goods. "
                 "Parliament <b>repealed</b> the Stamp Act in 1766 — but passed the <b>Declaratory Act</b>, saying it could make laws for the colonies “in all cases whatsoever.” "
                 "In 1767 the <b>Townshend Acts</b> taxed glass, lead, paint, paper, and tea.</p>", yt("Stamp Act no taxation without representation"))
        + qs([("What did the Stamp Act tax?", ["printed paper like newspapers, legal documents, and playing cards", "only sugar and molasses", "land and houses"]),
              ("What did “no taxation without representation” mean?", ["Only a government where colonists had elected representatives should tax them.", "Colonists should never pay any taxes.", "Only the king could set taxes."]),
              ("What is a boycott?", ["refusing to buy goods to protest", "a ship that carries tea", "a law passed by Parliament"]),
              ("Why did Parliament repeal the Stamp Act, and why didn't that end the conflict?", 2),
              ("Which items did the Townshend Acts tax?", ["glass, lead, paint, paper, and tea", "sugar and coffee", "guns and gunpowder"]),
              ("Romans 13:7 (ESV) says, “Pay to all what is owed to them: taxes to whom taxes are owed.” The colonists didn't refuse all taxes; they objected to taxes passed without "
               "their consent. Do you think peaceful protest like a boycott was a fair response? Explain.", 3)]),
        "1) printed paper (newspapers, documents, cards). 2) only a government with their elected representatives could tax them. 3) refusing to buy goods. "
        "4) the boycott hurt British merchants; but the Declaratory Act claimed Parliament could still make any laws for the colonies (and new taxes followed). 5) glass, lead, paint, paper, tea. 6) opinion.")
    S.set(2, "Boston Massacre & Tea Party",
        learnbox("<p>Britain sent soldiers to keep order in Boston, and tension grew. On <b>March 5, 1770</b>, a crowd taunted and threw snowballs at British soldiers, who fired "
                 "into it and killed <b>five colonists</b>, including <b>Crispus Attucks</b>, a man of African and Native American descent. Patriots called it the "
                 "<b>Boston Massacre</b>, and Paul Revere's famous engraving spread anger through the colonies. Yet lawyer <b>John Adams</b> defended the soldiers in court because "
                 "he believed everyone deserved a fair trial; most were found not guilty. Parliament dropped the Townshend taxes — except the tax on <b>tea</b>. "
                 "After the <b>Tea Act (1773)</b>, on <b>December 16, 1773</b>, Sons of Liberty disguised as Mohawk Indians boarded three ships and dumped <b>342 chests</b> of tea into "
                 "Boston Harbor: the <b>Boston Tea Party</b>.</p>", yt("Boston Massacre and Boston Tea Party"))
        + qs([("When was the Boston Massacre, and how many colonists were killed?", ["March 5, 1770 — five", "July 4, 1776 — fifty", "December 16, 1773 — none"]),
              ("Who was Crispus Attucks?", ["one of the five colonists killed in the Boston Massacre", "the British captain who gave the order", "the lawyer who defended the soldiers"]),
              ("Why did Paul Revere's engraving matter?", ["It spread anger by showing the event as a cruel attack.", "It was used as evidence to free the soldiers.", "It was a map of Boston Harbor."]),
              ("Exodus 23:2 (ESV) says, “You shall not fall in with the many to do evil… siding with a majority, so as to pervert justice.” How did John Adams live this out?", 2),
              ("What happened at the Boston Tea Party?", ["Colonists dumped 342 chests of British tea into Boston Harbor.", "Colonists threw a party to welcome British soldiers.", "British troops burned the colonists' tea."]),
              ("Was the Boston Tea Party right or wrong? Give one reason for each side, then your opinion.", 3)]),
        "1) March 5, 1770 — five. 2) one of the five colonists killed. 3) it spread anger (propaganda). 4) he defended unpopular soldiers so they would get a fair trial, even though the crowd was against them. "
        "5) dumped 342 chests of tea into Boston Harbor. 6) opinion (for: protest against unfair tax; against: destroyed others' property, about £9,000+ of tea).")
    S.set(3, "1774–1775: War Begins",
        learnbox("<p>Parliament punished Boston with the <b>Coercive Acts (1774)</b> — colonists called them the <b>Intolerable Acts</b>. They <b>closed Boston Harbor</b> until the tea "
                 "was paid for, cut back Massachusetts' self-government, and let troops be housed in colonists' buildings. Other colonies sent Boston help. In "
                 "<b>September 1774</b>, delegates from 12 colonies (all but Georgia) met in Philadelphia as the <b>First Continental Congress</b>. They agreed to boycott British "
                 "goods and petition King George III. On the night of <b>April 18, 1775</b>, <b>Paul Revere</b> and <b>William Dawes</b> rode to "
                 "warn that British troops were marching to seize weapons at Concord. On <b>April 19, 1775</b>, militia (“minutemen”) faced the British at <b>Lexington</b> and "
                 "<b>Concord</b> — the first battles of the American Revolution, the “shot heard round the world.”</p>", yt("Intolerable Acts Lexington and Concord"))
        + qs([("What did the Intolerable Acts do to Boston?", ["closed Boston Harbor until the tea was paid for", "made Boston the capital of the colonies", "lowered the tax on tea"]),
              ("Which colony did NOT send delegates to the First Continental Congress?", ["Georgia", "Virginia", "Massachusetts"]),
              ("Name two things the First Continental Congress decided to do.", 1),
              ("Why were the British marching to Concord?", ["to seize the colonists' weapons and gunpowder", "to sign a peace treaty", "to collect the Stamp Act tax"]),
              ("What happened on April 19, 1775?", ["The battles of Lexington and Concord began the Revolution.", "The Declaration of Independence was signed.", "The Boston Tea Party took place."]),
              ("Why do you think colonies that weren't punished still helped Boston?", 1)])
        + '<div class="lab">Number these events in order (1–4).</div>'
        + mark_list(["Lexington and Concord", "Intolerable Acts", "Boston Tea Party", "First Continental Congress"], ["1", "2", "3", "4"], 7, cols=2),
        "1) closed Boston Harbor. 2) Georgia. 3) boycott British goods; petition King George III (also: meet again in May 1775). 4) to seize weapons/gunpowder. 5) Lexington & Concord began the war. "
        "6) e.g., they feared they could be next / unity among colonies. Order: Tea Party 1, Intolerable Acts 2, First Continental Congress 3, Lexington & Concord 4 "
        "(so: #7 Lexington = 4, #8 Intolerable = 2, #9 Tea Party = 1, #10 Congress = 3).")
    ev = [("Stamp Act", "1765"), ("Lexington & Concord", "1775"), ("French & Indian War begins", "1754"), ("Boston Tea Party", "1773"),
          ("Boston Massacre", "1770"), ("First Continental Congress", "1774")]
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — the road to revolution. Goal: 8 of 10.</p>")
        + '<div class="lab">1. Timeline: write the year next to each event, then number them in order 1–6.</div>'
        + fill_table(["Event", "Year", "Order", "Event", "Year", "Order"], [[ev[i][0], "", "", ev[i + 3][0], "", ""] for i in range(3)], 24)
        + qs([("Main reason Britain began taxing the colonies:", ["to pay debt from the French and Indian War", "to build a new navy for the colonies", "to punish the Sons of Liberty"]),
              ("“No taxation without representation” protested…", ["taxes passed by a Parliament where colonists had no vote", "all taxes of every kind", "Spanish taxes in Florida"]),
              ("Who defended the British soldiers after the Boston Massacre?", ["John Adams", "Samuel Adams", "Paul Revere"]),
              ("Colonists' name for the Coercive Acts:", ["the Intolerable Acts", "the Townshend Acts", "the Declaratory Acts"]),
              ("Who rode to warn that the British were coming on April 18, 1775?", ["Paul Revere and William Dawes", "George Washington and John Adams", "Crispus Attucks and Samuel Adams"]),
              ("What country gained Florida in 1763?", ["Britain", "France", "Spain"]),
              ("What was the purpose of a boycott?", ["to pressure Britain by refusing to buy its goods", "to raise money for the king", "to train soldiers"]),
              ("Which event do you think did the most to push the colonies toward war? Defend your answer.", 2)], 2),
        "1) Timeline: French & Indian War 1754 (1), Stamp Act 1765 (2), Boston Massacre 1770 (3), Boston Tea Party 1773 (4), First Continental Congress 1774 (5), Lexington & Concord 1775 (6). "
        "2) pay war debt. 3) taxes passed without colonists' representation. 4) John Adams. 5) Intolerable Acts. 6) Paul Revere and William Dawes. 7) Britain. "
        "8) pressure Britain economically by refusing to buy its goods. 9) opinion with reasons.")
    return S

def build():
    return [math(), english(), science(), history()]
