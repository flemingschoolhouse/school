from core_common import *
from mathgen import *
import random

K = "Nylah"

def worked(rows, size="14pt"):
    """small worked-example block in monospace, right-aligned like a paper problem"""
    return (f'<div style="font-family:\'Inter\',monospace;font-size:{size};line-height:1.2;text-align:right;white-space:pre;'
            f'font-variant-numeric:tabular-nums;background:#fff;border:1.4px solid #c9cde3;border-radius:8px;padding:6px 12px">'
            + "".join(f"<div{' style=\"border-top:2px solid #111\"' if x.startswith('_') else ''}>{x.lstrip('_')}</div>" for x in rows) + '</div>')

def wbox(text, rows):
    return f'<div class="flexrow" style="align-items:center"><div class="grow">{text}</div>{worked(rows)}</div>'

# ---------------- MATH CRASH COURSE · Level 3 ----------------
def math():
    S = Subject(K, "Math Crash Course", "Level 3"); r = random.Random(73)
    # D1 meaning of multiplication + facts + x10/x100
    rep = [(r.randint(3, 5), r.randint(3, 9)) for _ in range(3)]
    facts = [(r.randint(3, 9), r.randint(3, 9)) for _ in range(20)]
    tens = [(r.randint(12, 89), 10), (r.randint(3, 9), 100), (r.randint(21, 95), 100), (r.randint(105, 480), 10), (r.randint(2, 9) * 10, 10), (r.randint(13, 60), 100)]
    S.set(0, "What Multiplication Means",
        learnbox(wbox("<p><b>Level 3</b> = multiplication &amp; division. <b>Multiplication is a fast way to add equal groups.</b> "
                      "<b>Example:</b> 4 bags with 6 apples each = 6 + 6 + 6 + 6 = 24. Instead we write <b>4 × 6 = 24</b> (“4 groups of 6”). "
                      "The numbers you multiply are <b>factors</b>; the answer is the <b>product</b>.</p>"
                      "<p><b>× 10:</b> write one zero on the end (23 × 10 = 230). <b>× 100:</b> write two zeros (23 × 100 = 2,300).</p>",
                      ["6 + 6 + 6 + 6 = 24", "4 × 6 = 24", "23 × 10 = 230", "23 × 100 = 2,300"]), yt("multiplication as repeated addition"))
        + '<div class="lab">A. Write each addition as multiplication.</div>'
        + hgrid(["<span style='white-space:nowrap'>" + " + ".join([str(b)] * a) + "</span> → <span style='white-space:nowrap'>___ × ___ = ____</span>" for a, b in rep], 3, "12pt")
        + '<div class="lab">B. Facts practice — go fast, then check.</div>'
        + hgrid([f"<span style='white-space:nowrap'>{a} × {b} = ___</span>" for a, b in facts], 5, "13pt")
        + '<div class="lab">C. Times 10 and 100</div>'
        + hgrid([f"{a:,} × {b} = ______" for a, b in tens], 3, "13pt")
        + '<div class="lab">D. Questions</div>' + qs([("Which means 5 × 3?", ["3 + 3 + 3 + 3 + 3", "5 + 3", "3 + 3 + 3"]),
              ("Nylah has 7 packs of gum with 8 pieces in each pack. How many pieces?", ["56", "15", "54"]),
              ("In 9 × 4 = 36, which number is the product?", ["36", "9", "4"])]),
        "A: " + ", ".join(f"{n+1}) {a} × {b} = {a*b}" for n, (a, b) in enumerate(rep))
        + ". B: " + ", ".join(f"{n+1}) {a*b}" for n, (a, b) in enumerate(facts))
        + ". C: " + ", ".join(f"{n+1}) {a*b:,}" for n, (a, b) in enumerate(tens))
        + ". D: 1) 3 + 3 + 3 + 3 + 3, 2) 56, 3) 36")
    # D2 2-digit x 1-digit with regrouping
    mp = []
    while len(mp) < 10:
        a, b = r.randint(14, 98), r.randint(3, 9)
        if (a % 10) * b >= 10 and (a, b) not in mp: mp.append((a, b))
    while len(mp) < 15:
        a, b = r.randint(112, 489), r.randint(3, 9)
        if (a % 10) * b >= 10: mp.append((a, b))
    S.set(1, "2-Digit × 1-Digit (Carrying)",
        learnbox(wbox("<p><b>Example: 47 × 6.</b> Multiply the <b>ones</b> first: 6 × 7 = 42. Write the <b>2</b> in the ones place and <b>carry the 4</b> "
                      "(little number above the tens). Next multiply the <b>tens</b>: 6 × 4 = 24, then <b>add the carried 4</b>: 24 + 4 = 28. Write 28. "
                      "Answer: <b>282</b>.</p><p><b>Remember:</b> multiply first, <i>then</i> add the carry. Check: 47 is about 50, and 50 × 6 = 300 — close to 282. ✔</p>",
                      ["<span style='font-size:10pt;color:#2f5bd3'>4</span><span style='visibility:hidden'>7</span>", "47", "× 6", "_282"]), yt("2 digit by 1 digit multiplication"))
        + vgrid([(a, b, "×") for a, b in mp[:10]], 5)
        + '<div class="lab">Challenge row: same steps, one more place (carry into the hundreds).</div>'
        + vgrid([(a, b, "×") for a, b in mp[10:]], 5).replace('">1.<', '">11.<').replace('">2.<', '">12.<').replace('">3.<', '">13.<').replace('">4.<', '">14.<').replace('">5.<', '">15.<')
        + qs([("The church van makes 6 trips. Each trip carries 14 people. How many people in all?", ["84", "64", "20"]),
              ("A pack holds 24 markers. How many markers are in 8 packs? Show your work.", 3)], 16),
        ", ".join(f"{n+1}) {a*b:,}" for n, (a, b) in enumerate(mp)) + ", 16) 84, 17) 192")
    # D3 division facts & fact families
    fams = []
    while len(fams) < 4:
        a, b = r.randint(3, 9), r.randint(3, 9)
        if a != b and (a, b) not in fams and (b, a) not in fams and {a, b} != {6, 7}: fams.append((a, b))
    dv = [(r.randint(3, 9), r.randint(2, 9)) for _ in range(15)]
    S.set(2, "Division Facts & Fact Families",
        learnbox(wbox("<p><b>Division splits a total into equal groups.</b> 24 ÷ 3 asks “24 split into 3 equal groups is how many in each?” → <b>8</b>. "
                      "Multiplication and division are <b>opposites</b>, so every × fact gives you ÷ facts. "
                      "<b>Example — the fact family for 3, 8, 24:</b> 3 × 8 = 24, 8 × 3 = 24, 24 ÷ 3 = 8, 24 ÷ 8 = 3. "
                      "Stuck on 42 ÷ 6? Ask: “6 times <i>what</i> is 42?” → 7.</p>",
                      ["3 × 8 = 24", "8 × 3 = 24", "24 ÷ 3 = 8", "24 ÷ 8 = 3"]), yt("multiplication and division fact families"))
        + '<div class="lab">A. Write all four facts in each family.</div>'
        + '<div class="grid2">' + "".join(f'<div class="box"><b style="color:#2f5bd3">{n+1}.</b> <b>{a}, {b}, {a*b}</b>'
                                          f'<div class="grid2" style="margin-top:4px">' + "".join('<div class="ln" style="height:24px"></div>' for _ in range(4)) + '</div></div>'
                                          for n, (a, b) in enumerate(fams)) + '</div>'
        + '<div class="lab">B. Division facts</div>'
        + hgrid([f"<span style='white-space:nowrap'>{a*b} ÷ {a} = ___</span>" for a, b in dv], 5, "13pt")
        + '<div class="lab">C. Questions</div>' + qs([("Which one is NOT in the fact family for 6, 7, 42?", ["6 + 7 = 13", "42 ÷ 6 = 7", "7 × 6 = 42"]),
              ("If 9 × 4 = 36, then 36 ÷ 4 = ?", ["9", "4", "32"]),
              ("Fill in the missing number: ____ × 7 = 56", ["8", "7", "49"])]),
        "A: " + "; ".join(f"{n+1}) {a}×{b}={a*b}, {b}×{a}={a*b}, {a*b}÷{a}={b}, {a*b}÷{b}={a}" for n, (a, b) in enumerate(fams))
        + ". B: " + ", ".join(f"{n+1}) {b}" for n, (a, b) in enumerate(dv)) + ". C: 1) 6 + 7 = 13, 2) 9, 3) 8")
    # D4 long division 1-digit divisor with remainders
    divs = []
    for k in range(9):
        b = r.randint(3, 9); q = r.randint(12, 89) if k < 3 else r.randint(21, 149); rem = 0 if k < 3 else r.randint(1, b - 1)
        divs.append((b * q + rem, b, q, rem))
    S.set(3, "Long Division (with Remainders)",
        learnbox(wbox("<p><b>Steps: Divide → Multiply → Subtract → Bring down</b> (repeat). <b>Example: 157 ÷ 4.</b> 4 can't go into 1, so use 15. "
                      "15 ÷ 4 = <b>3</b> (write 3 over the 5). 3 × 4 = 12. 15 − 12 = 3. Bring down the 7 → 37. 37 ÷ 4 = <b>9</b>. 9 × 4 = 36. "
                      "37 − 36 = <b>1</b> left over. Nothing left to bring down, so 1 is the <b>remainder</b>: <b>39 R1</b>. "
                      "<b>Check:</b> 39 × 4 = 156, + 1 = 157 ✔. The remainder must always be smaller than the divisor.</p>",
                      ["&nbsp;&nbsp;39 R1", "_4 ) 157", "− 12&nbsp;&nbsp;", "_37&nbsp;", "− 36&nbsp;", "_1&nbsp;"]), yt("long division with remainders 1 digit divisor"))
        + '<div class="grid3" style="justify-items:start">' + "".join(f'<div style="display:flex;gap:6px"><b style="color:#2f5bd3">{n+1}.</b>{longdiv(a,b)}</div>' for n, (a, b, q, rm) in enumerate(divs)) + '</div>'
        + qs([("29 kids are going on a field trip. Each car holds 4 kids. How many cars are needed so everyone can go?", ["8", "7", "7 R1"]),
              ("Grace splits 156 crayons evenly among 6 kids. How many does each kid get? Show your work.", 1),
              ("Which is the correct check for 50 ÷ 7 = 7 R1?", ["7 × 7 + 1 = 50", "7 + 7 + 1 = 15", "50 × 7 = 350"])], 10),
        ", ".join(f"{n+1}) {q}" + (f" R{rm}" if rm else "") + f" (check {q}×{b}{'+'+str(rm) if rm else ''}={a:,})" for n, (a, b, q, rm) in enumerate(divs))
        + ". 10) 8 cars (7 R1 means 1 kid left over needs another car), 11) 26, 12) 7 × 7 + 1 = 50")
    # D5 checkpoint
    c = [(r.randint(3, 9), r.randint(3, 9)), (r.randint(14, 76), 100), (r.randint(26, 89), r.randint(4, 9)), (r.randint(31, 97), r.randint(3, 8))]
    d1 = (r.randint(3, 9),); q1 = r.randint(3, 9)
    b2 = r.randint(3, 8); q2 = r.randint(32, 98); rm2 = r.randint(1, b2 - 1)
    b3 = r.randint(4, 9); q3 = r.randint(22, 89)
    cp = [f"{c[0][0]} × {c[0][1]}", f"{c[1][0]} × {c[1][1]}", f"{c[2][0]} × {c[2][1]}", f"{c[3][0]} × {c[3][1]}",
          f"{d1[0]*q1} ÷ {d1[0]}", "Write the fact family for 7, 8, 56", "Write 9 + 9 + 9 + 9 as multiplication and solve",
          f"{b3*q3} ÷ {b3}", f"{b2*q2+rm2:,} ÷ {b2}", "____ × 6 = 54",
          "A box holds 36 cans. How many cans are in 7 boxes?", "45 cookies are shared by 6 kids equally. How many each? How many left over?"]
    cpa = [f"{c[0][0]*c[0][1]}", f"{c[1][0]*c[1][1]:,}", f"{c[2][0]*c[2][1]:,}", f"{c[3][0]*c[3][1]:,}", f"{q1}",
           "7×8=56, 8×7=56, 56÷7=8, 56÷8=7", "4 × 9 = 36", f"{q3}", f"{q2} R{rm2}", "9", "252", "7 each, 3 left over (7 R3)"]
    S.set(4, "Level 3 Checkpoint",
        learnbox("<p><b>Checkpoint!</b> 12 problems. Show your work. <b>Pass = 10 or more (80%)</b> → next week is <b>Level 4: Fractions</b>. "
                 "Less than 10? We'll re-teach the tricky parts next week — no big deal. That's how a crash course works.</p>")
        + hgrid([e + "<div class='ln' style='height:30px'></div>" for e in cp], 2, "13pt", 30)
        + '<div class="big">Score: ______ / 12</div>',
        ", ".join(f"{n+1}) {a}" for n, a in enumerate(cpa)) + ". Pass = 10 of 12.")
    return S

def english():
    S = Subject(K, "English", "Week 3 · Sentence Building")
    S.set(0, "Complete Subjects & Predicates",
        learnbox("<p>Every complete sentence has two parts. The <b>subject</b> tells <i>who or what</i> the sentence is about. The <b>predicate</b> tells "
                 "<i>what the subject does or is</i>. The <b>complete subject</b> is ALL the words in the subject part; the <b>complete predicate</b> is ALL the words "
                 "in the predicate part. <b>Example:</b> <i>My little brother | kicked the ball over the fence.</i> Who? <i>My little brother</i> (complete subject). "
                 "Did what? <i>kicked the ball over the fence</i> (complete predicate). Draw a line <b>|</b> between them.</p>", yt("complete subject and complete predicate"))
        + '<div class="lab">Draw a line | between the complete subject and the complete predicate.</div>'
        + ol(["The tall oak tree fell during the storm.", "Our family sings in the church choir.", "The hungry puppy chewed my shoe.",
              "Nevaeh and Naomi baked cookies for the neighbors.", "A big blue truck stopped at our house."])
        + '<div class="lab">Is the underlined part the complete subject or the complete predicate?</div>'
        + mark_list(["<u>The old lighthouse</u> stands on the beach.", "Grandpa <u>told us a funny story</u>.", "<u>Every kid in the class</u> passed the test.",
                     "The baby <u>fell asleep in the car</u>."], ["subject", "predicate"], 6)
        + qs([("Which group of words is a complete sentence?", ["The girls laughed at the joke.", "The girls in the kitchen.", "Laughed at the funny joke."]),
              ("Write a sentence about your favorite food. Draw a line between the complete subject and complete predicate.", 2)], 10),
        "1) The tall oak tree | fell during the storm. 2) Our family | sings in the church choir. 3) The hungry puppy | chewed my shoe. "
        "4) Nevaeh and Naomi | baked cookies for the neighbors. 5) A big blue truck | stopped at our house. 6) subject 7) predicate 8) subject 9) predicate. "
        "10) The girls laughed at the joke. 11) varies.")
    S.set(1, "Simple Subjects & Predicates",
        learnbox("<p>Now shrink each part down to its most important word. The <b>simple subject</b> is the main noun or pronoun in the complete subject. "
                 "The <b>simple predicate</b> is the <b>verb</b> (plus any helping verbs). <b>Example:</b> <i>The tired <u>dog</u> | <u>slept</u> on the porch.</i> "
                 "Simple subject: <b>dog</b>. Simple predicate: <b>slept</b>. With a helping verb: <i>Mom <u>is baking</u> bread.</i> → simple predicate <b>is baking</b>. "
                 "Tip: find the verb first, then ask “who or what ___?”</p>", yt("simple subject and simple predicate"))
        + '<div class="lab">Underline the simple subject once. Underline the simple predicate (verb) twice.</div>'
        + ol(["The little red bird sang outside my window.", "My oldest sister drives to work.", "Seven ducks swam across the pond.",
              "Dad will fix the sink tomorrow.", "The kids in the backyard are playing tag.", "Grandma's famous peach pie won first prize.",
              "We have lived in Jacksonville for five years."])
        + '<div class="lab">Circle the simple subject.</div>'
        + ol([f"The happy baby smiled at me. {pick('happy', 'baby', 'smiled')}",
              f"A loud thunderstorm shook the house. {pick('loud', 'thunderstorm', 'shook')}",
              f"Our neighbor's cat climbed the fence. {pick('neighbor', 'cat', 'fence')}"], 8)
        + qs([("What is the simple predicate in <i>The choir has practiced all week</i>?", ["has practiced", "choir", "all week"]),
              ("Write a sentence with a helping verb. Underline the simple subject once and the simple predicate twice.", 4)], 11),
        "1) bird / sang 2) sister / drives 3) ducks / swam 4) Dad / will fix 5) kids / are playing 6) pie / won 7) We / have lived. 8) baby 9) thunderstorm 10) cat. 11) has practiced. 12) varies.")
    S.set(2, "Four Kinds of Sentences",
        learnbox("<p>Sentences have four jobs, and each job has its own end mark. A <b>declarative</b> sentence <b>tells</b> something and ends with a period (<i>We go to church on Sunday.</i>). "
                 "An <b>interrogative</b> sentence <b>asks</b> and ends with a question mark (<i>Where is my Bible?</i>). An <b>imperative</b> sentence gives a "
                 "<b>command</b> or request and usually ends with a period (<i>Please close the door.</i>) — its subject is the understood <b>“you.”</b> "
                 "An <b>exclamatory</b> sentence shows <b>strong feeling</b> and ends with an exclamation point (<i>What a beautiful sunset!</i>).</p>", yt("four types of sentences"))
        + '<div class="lab">What kind of sentence is it? Then add the end mark.</div>'
        + mark_list(["Did you feed the dog__", "Take out the trash__", "The library opens at nine__", "I can't believe we won__", "How many cookies are left__",
                     "Florida has many beaches__", "Wow, that was amazing__", "Please pass the salt__"], ["declarative", "interrogative", "imperative", "exclamatory"])
        + qs([("What is the subject of <i>Sit down.</i>?", ["you (understood)", "sit", "down"]),
              ("Write one sentence of each kind about your week: declarative, interrogative, imperative, exclamatory. Use the right end marks!", 6)], 9),
        "1) interrogative ? 2) imperative . 3) declarative . 4) exclamatory ! 5) interrogative ? 6) declarative . 7) exclamatory ! 8) imperative . 9) you (understood). 10) varies.")
    S.set(3, "Compound Sentence Parts",
        learnbox("<p>“Compound” means <b>two or more joined together</b>. A <b>compound subject</b> has two subjects sharing one verb: <i><b>Titus and Naomi</b> raced home.</i> "
                 "A <b>compound predicate</b> has two verbs sharing one subject: <i>Nylah <b>sang and danced</b>.</i> A <b>compound sentence</b> joins two complete sentences "
                 "with a <b>comma + a conjunction</b> (FANBOYS: <i>for, and, nor, but, or, yet, so</i>): <i>It rained all day<b>, so</b> we stayed inside.</i> "
                 "Test: if both sides could stand alone as sentences, it's compound — use the comma.</p>", yt("compound subjects and compound predicates"))
        + '<div class="lab">What does each sentence have?</div>'
        + mark_list(["Mom and Dad painted the kitchen.", "The puppy barked and wagged its tail.", "I wanted pizza, but we had soup.",
                     "Apples and oranges are on sale.", "We cleaned our rooms, and then we watched a movie.", "Naomi washed and dried the dishes."],
                    ["compound subject", "compound predicate", "compound sentence"])
        + '<div class="lab">Join each pair into one compound sentence (comma + conjunction).</div>'
        + qs([("The game was close. Our team won.", 1), ("We can go to the park. We can stay home.", 1)], 7)
        + qs([("Which sentence is punctuated correctly?", ["I was tired, so I went to bed.", "I was tired so, I went to bed.", "I was tired, so, I went to bed."])], 9),
        "1) compound subject 2) compound predicate 3) compound sentence 4) compound subject 5) compound sentence 6) compound predicate. "
        "7) e.g., The game was close, but our team won. 8) e.g., We can go to the park, or we can stay home. 9) I was tired, so I went to bed.")
    S.set(4, "Week Review",
        learnbox("<p><b>Review quiz</b> — sentence building. Goal: 8 of 10.</p>")
        + qs([("In <i>The kind nurse helped my grandma.</i>, what is the complete subject?", ["The kind nurse", "nurse", "helped my grandma"]),
              ("In the same sentence, what is the simple predicate?", ["helped", "helped my grandma", "nurse"]),
              ("What is the simple subject of <i>Three white horses ran across the field.</i>?", ["horses", "Three white horses", "ran"]),
              ("Which sentence is interrogative?", ["When does the game start?", "The game starts at six.", "Hurry up!"]),
              ("Which end mark goes on an exclamatory sentence?", ["!", ".", "?"]),
              ("<i>Clean your room.</i> is what kind of sentence?", ["imperative", "declarative", "exclamatory"]),
              ("Which sentence has a compound subject?", ["Nevaeh and Nylah walked to the store.", "Nylah walked and talked.", "Nylah walked, and it rained."]),
              ("Draw a line between the complete subject and complete predicate: <i>The bright full moon rose over the trees.</i>", 1),
              ("Join into a compound sentence: <i>I studied hard. I passed the test.</i>", 1),
              ("Write a sentence with a compound predicate. Circle the two verbs.", 2)]),
        "1) The kind nurse 2) helped 3) horses 4) When does the game start? 5) ! 6) imperative 7) Nevaeh and Nylah walked to the store. "
        "8) The bright full moon | rose over the trees. 9) I studied hard, so I passed the test. 10) varies.")
    return S

def science():
    S = Subject(K, "Science", "Week 3 · Human Body Systems")
    S.set(0, "Skeletal & Muscular Systems",
        learnbox("<p>Last week you learned <b>cells → tissues → organs → organ systems → organism</b>. This week we tour your organ systems! "
                 "The <b>skeletal system</b> is your bones — an adult has <b>206</b>. Bones <b>support</b> your body, <b>protect</b> organs (the skull guards the brain, "
                 "the ribs guard the heart and lungs), <b>store minerals</b> like calcium, and <b>make blood cells</b> in the marrow. Bones meet at <b>joints</b>. "
                 "The <b>muscular system</b> moves you. Muscles can only <b>pull</b>, so they work in <b>pairs</b>: your biceps pulls to bend your arm; your triceps pulls to straighten it. "
                 "<b>Tendons</b> attach muscles to bones. There are three muscle types: <b>skeletal</b> (you control it), <b>smooth</b> (stomach, blood vessels), and <b>cardiac</b> (heart only).</p>",
                 yt("skeletal and muscular systems for kids"))
        + '<div class="lab">Put these in order from smallest (1) to largest (5).</div>'
        + mark_list(["muscle tissue", "your whole body", "a muscle cell", "muscular system", "the biceps (a muscle organ)"], ["1", "2", "3", "4", "5"])
        + qs([("How many bones does an adult have?", ["206", "106", "650"]), ("Which bone protects the brain?", ["skull", "ribs", "femur"]),
              ("Which type of muscle is found only in the heart?", ["cardiac", "smooth", "skeletal"]), ("What connects a muscle to a bone?", ["a tendon", "a joint", "marrow"]),
              ("Explain why muscles have to work in pairs. Use your arm as an example.", 2),
              ("Name two jobs of the skeletal system besides holding you up.", 2)], 6),
        "Order: a muscle cell 1, muscle tissue 2, the biceps 3, muscular system 4, your whole body 5. 6) 206 7) skull 8) cardiac 9) a tendon. "
        "10) muscles can only pull, so one pulls to bend (biceps) and the other pulls to straighten (triceps). 11) protect organs, make blood cells, store minerals (calcium).")
    S.set(1, "Circulatory System",
        learnbox("<p>The <b>circulatory system</b> is your body's delivery service. The <b>heart</b>, a muscle about the size of your fist, pumps <b>blood</b> through "
                 "<b>blood vessels</b>. The heart has <b>4 chambers</b>: two upper <b>atria</b> and two lower <b>ventricles</b>. <b>Arteries</b> carry blood <b>away</b> from "
                 "the heart; <b>veins</b> carry blood <b>back</b> to the heart; tiny <b>capillaries</b> connect them and trade oxygen and nutrients for wastes. "
                 "Blood has <b>red blood cells</b> (carry oxygen), <b>white blood cells</b> (fight germs), <b>platelets</b> (help clots form to stop bleeding), and liquid <b>plasma</b>. "
                 "Your heart beats about <b>100,000 times a day</b>!</p>", yt("circulatory system for kids"))
        + fill_table(["Part", "Job"], [["Heart", ""], ["Arteries", ""], ["Veins", ""], ["Capillaries", ""]], 24)
        + '<div class="lab">Which part of the blood does each job?</div>'
        + mark_list(["carries oxygen", "fights germs", "helps a scrape stop bleeding", "the liquid part of blood"], ["red blood cells", "white blood cells", "platelets", "plasma"])
        + qs([("How many chambers does the heart have?", ["4", "2", "6"]), ("Which vessels carry blood away from the heart?", ["arteries", "veins", "capillaries"]),
              ("Which blood vessels are so tiny that blood cells pass through them in single file?", ["capillaries", "arteries", "veins"]),
              ("Why does your heart beat faster when you run? Use the word <i>oxygen</i>.", 2),
              ("Find your pulse on your wrist. Count beats for 15 seconds, × 4. Resting: _____ per minute. After 30 jumping jacks: _____ per minute.", 0)], 5),
        "Table: heart pumps blood; arteries carry blood away from the heart; veins carry blood back to the heart; capillaries tiny vessels that trade oxygen/nutrients for wastes. "
        "1) red blood cells 2) white blood cells 3) platelets 4) plasma. 5) 4 6) arteries 7) capillaries 8) muscles need more oxygen, so the heart pumps blood faster to deliver it. 9) varies (about 60–100 resting; higher after exercise).")
    S.set(2, "Respiratory System",
        learnbox("<p>The <b>respiratory system</b> brings <b>oxygen</b> in and sends <b>carbon dioxide</b> out. Air enters your <b>nose or mouth</b>, travels down the "
                 "<b>trachea</b> (windpipe), splits into two <b>bronchi</b>, and fills your two <b>lungs</b>. Inside the lungs are millions of tiny air sacs called "
                 "<b>alveoli</b>, wrapped in capillaries. There, oxygen moves into the blood and carbon dioxide moves out — that's how the respiratory and circulatory systems "
                 "<b>work together</b>. A dome-shaped muscle under your lungs, the <b>diaphragm</b>, pulls down to help you breathe in and relaxes up to help you breathe out.</p>",
                 yt("respiratory system for kids"))
        + '<div class="lab">Number the path air takes, from 1 (first) to 5 (last).</div>'
        + mark_list(["bronchi", "nose or mouth", "alveoli", "trachea", "lungs"], ["1", "2", "3", "4", "5"])
        + qs([("What gas do we breathe IN that our cells need?", ["oxygen", "carbon dioxide", "nitrogen"]), ("What gas do we breathe OUT?", ["carbon dioxide", "oxygen", "helium"]),
              ("What are alveoli?", ["tiny air sacs in the lungs", "the windpipe", "the muscle under the lungs"]), ("What does the diaphragm do?", ["pulls down to help you breathe in", "pumps blood", "filters food"]),
              ("Explain how the respiratory and circulatory systems work together.", 3),
              ("Put your hand on your belly and breathe deeply 5 times. What did you feel move, and why?", 2)], 6),
        "Path: nose or mouth 1, trachea 2, bronchi 3, lungs 4, alveoli 5. 6) oxygen 7) carbon dioxide 8) tiny air sacs in the lungs 9) pulls down to help you breathe in. "
        "10) lungs put oxygen into the blood in the alveoli; the heart and blood carry it to the cells and bring carbon dioxide back to the lungs to breathe out. 11) belly rises and falls — the diaphragm moving.")
    S.set(3, "Digestive System",
        learnbox("<p>The <b>digestive system</b> breaks food into nutrients small enough to get into your blood. Digestion starts in the <b>mouth</b>: teeth chew and "
                 "<b>saliva</b> begins breaking food down. The <b>esophagus</b> squeezes food down to the <b>stomach</b>, which churns it with acid. Next comes the "
                 "<b>small intestine</b> — about 20 feet long! — where most nutrients are absorbed into the blood. The <b>liver</b> (makes bile) and <b>pancreas</b> "
                 "(makes digestive juices) help here. The <b>large intestine</b> absorbs water, and leftover waste leaves the body.</p>", yt("digestive system for kids"))
        + '<div class="lab">Number the path food takes, from 1 (first) to 5 (last).</div>'
        + mark_list(["stomach", "large intestine", "mouth", "small intestine", "esophagus"], ["1", "2", "3", "4", "5"])
        + '<div class="lab">Which organ does each job?</div>'
        + mark_list(["churns food with acid", "absorbs most nutrients", "absorbs water", "makes bile"], ["stomach", "small intestine", "large intestine", "liver"], 6)
        + qs([("Where does digestion begin?", ["the mouth", "the stomach", "the small intestine"]),
              ("Which system carries the nutrients from the small intestine to the rest of your body?", ["circulatory", "respiratory", "skeletal"]),
              ("About how long is the small intestine?", ["about 20 feet", "about 2 feet", "about 200 feet"]),
              ("1 Corinthians 6:19–20 says our bodies are a temple of the Holy Spirit, so we honor God with them. Name two ways you can take care of your digestive system.", 2)], 10),
        "Path: mouth 1, esophagus 2, stomach 3, small intestine 4, large intestine 5. 6) stomach 7) small intestine 8) large intestine 9) liver. "
        "10) the mouth 11) circulatory 12) about 20 feet 13) e.g., eat fruits and vegetables, drink water, chew well, don't overeat.")
    S.set(4, "Nervous System + Review",
        learnbox("<p><b>One more system:</b> the <b>nervous system</b> is the control center — the <b>brain</b>, the <b>spinal cord</b>, and <b>nerves</b> made of nerve cells "
                 "(<b>neurons</b>). Nerves carry messages between your body and brain super fast, so you can feel, think, and move. "
                 "<b>Review quiz</b> — body systems. Goal: 8 of 10.</p>")
        + qs([("Put in order: organ, cell, organ system, tissue.", ["cell, tissue, organ, organ system", "tissue, cell, organ system, organ", "organ, organ system, cell, tissue"]),
              ("Which system is made of the brain, spinal cord, and nerves?", ["nervous", "digestive", "muscular"]),
              ("Which system includes the heart and blood vessels?", ["circulatory", "respiratory", "skeletal"]),
              ("Which carry blood back to the heart?", ["veins", "arteries", "alveoli"]),
              ("Where does oxygen enter the blood?", ["alveoli in the lungs", "the stomach", "the trachea"]),
              ("Where are most nutrients absorbed?", ["small intestine", "large intestine", "esophagus"]),
              ("What do red blood cells do?", ["carry oxygen", "fight germs", "make bile"]),
              ("Why do muscles work in pairs?", ["They can only pull, not push.", "They are too weak alone.", "Bones push them."]),
              ("Name two jobs of the skeletal system.", 1),
              ("Pick two systems and explain how they work together.", 3)]),
        "1) cell, tissue, organ, organ system 2) nervous 3) circulatory 4) veins 5) alveoli in the lungs 6) small intestine 7) carry oxygen "
        "8) They can only pull, not push. 9) support, protect organs, make blood cells, store minerals. 10) e.g., respiratory + circulatory: lungs load oxygen into blood, heart pumps it to cells.")
    return S

def civics():
    S = Subject(K, "Civics", "Week 3 · The Bill of Rights")
    S.set(0, "Why We Have a Bill of Rights",
        learnbox("<p>When the Constitution was written in 1787, many Americans were worried. The <b>Anti-Federalists</b> feared a strong national government could take "
                 "away people's freedoms, the way the British king had. They wanted a written list of rights the government could never take away. "
                 "To win their support, <b>James Madison</b> — often called the “Father of the Constitution” — wrote amendments and introduced them in the First Congress in <b>1789</b>. "
                 "Congress sent 12 amendments to the states, and 10 were approved (ratified) on <b>December 15, 1791</b>. Those first ten amendments are called the "
                 "<b>Bill of Rights</b>. An <b>amendment</b> is a change or addition to the Constitution.</p>", yt("bill of rights for kids"))
        + qs([("What is an amendment?", ["a change or addition to the Constitution", "a law passed by a state", "a court case"]),
              ("Who feared a strong national government and demanded a Bill of Rights?", ["the Anti-Federalists", "the British king", "the Supreme Court"]),
              ("Who wrote the amendments that became the Bill of Rights?", ["James Madison", "George Washington", "Benjamin Franklin"]),
              ("When was the Bill of Rights ratified?", ["December 15, 1791", "July 4, 1776", "September 17, 1787"]),
              ("How many amendments are in the Bill of Rights?", ["10", "12", "27"]),
              ("Why do you think the Anti-Federalists wanted rights <b>written down</b> instead of just trusting leaders to be fair?", 3),
              ("If you could add one right to a list for your family, what would it be and why?", 2)]),
        "1) a change or addition to the Constitution 2) the Anti-Federalists 3) James Madison 4) December 15, 1791 5) 10. "
        "6) e.g., written rights can't easily be ignored or taken away; leaders might misuse power. 7) opinion.")
    S.set(1, "1st Amendment Freedoms",
        learnbox("<p>The <b>1st Amendment</b> protects five freedoms. <b>Religion:</b> the government can't set up an official church, and you may worship (or not) freely. "
                 "<b>Speech:</b> you can share your ideas and opinions. <b>Press:</b> newspapers and media can report news and criticize the government. "
                 "<b>Assembly:</b> people can gather peacefully. <b>Petition:</b> you can ask the government to change something. Memory trick: <b>R-A-P-P-S</b> "
                 "(Religion, Assembly, Press, Petition, Speech). These freedoms protect your family's right to go to church and share your faith.</p>", yt("first amendment five freedoms"))
        + '<div class="lab">Which 1st Amendment freedom is being used?</div>'
        + mark_list(["A family worships at the church of their choice.", "Neighbors sign a letter asking the city for a stop sign.", "A newspaper writes that the mayor made a mistake.",
                     "A group holds a peaceful rally at the park.", "A girl writes a blog post sharing her opinion.", "Kids pray before lunch on their own."],
                    ["religion", "speech", "press", "assembly", "petition"])
        + qs([("What does “peaceably assemble” mean?", ["gather peacefully as a group", "build something together", "vote in an election"]),
              ("Which freedom lets you ask the government to fix a problem?", ["petition", "press", "assembly"]),
              ("Which 1st Amendment freedom do you think is most important? Defend your answer.", 3)], 7),
        "1) religion 2) petition 3) press 4) assembly 5) speech 6) religion. 7) gather peacefully as a group 8) petition 9) opinion.")
    S.set(2, "The 2nd, 3rd & 4th Amendments",
        learnbox("<p>The <b>2nd Amendment</b> protects “the right of the people to keep and bear arms” and mentions a “well regulated militia” (citizen soldiers). "
                 "The <b>3rd Amendment</b> says the government can't force you to let soldiers live in your house in peacetime without your permission — the British had done this "
                 "(it was called <b>quartering</b>). The <b>4th Amendment</b> protects you from <b>unreasonable searches and seizures</b>. Usually, police need a "
                 "<b>warrant</b> — permission from a judge — based on <b>probable cause</b> (a good reason to believe evidence of a crime is there).</p>", yt("bill of rights amendments 1 to 10"))
        + fill_table(["Amendment", "What it protects (your own words)"], [["2nd", ""], ["3rd", ""], ["4th", ""]], 34)
        + '<div class="lab">Which amendment is this about?</div>'
        + mark_list(["Soldiers can't move into your home in peacetime without your OK.", "Police need a warrant to search your house.", "The right to keep and bear arms.",
                     "A judge must see probable cause before signing a warrant."], ["2nd", "3rd", "4th"])
        + qs([("What is a warrant?", ["a judge's written permission to search or arrest", "a type of weapon", "a soldier's uniform"]),
              ("Why did the colonists care so much about the 3rd Amendment?", ["British soldiers had been quartered in their homes.", "They wanted bigger houses.", "Soldiers paid them rent."]),
              ("Why do you think the Founders wanted police to get a judge's permission before searching a home?", 2)], 5),
        "Table: 2nd — right to keep and bear arms; 3rd — no quartering soldiers in homes in peacetime without consent; 4th — no unreasonable searches/seizures, warrants need probable cause. "
        "1) 3rd 2) 4th 3) 2nd 4) 4th. 5) a judge's written permission to search or arrest 6) British soldiers had been quartered in their homes. 7) protects privacy; stops searches without a good reason.")
    S.set(3, "Rights of the Accused",
        learnbox("<p>Amendments 5–8 protect people accused of crimes, so trials are fair. <b>5th:</b> you can't be tried twice for the same crime (<b>double jeopardy</b>), "
                 "you can't be forced to testify against yourself (“pleading the Fifth”), and you can't lose life, liberty, or property without <b>due process</b> (fair legal steps). "
                 "<b>6th:</b> a <b>speedy and public trial</b> by an impartial jury, the right to know the charges, to question witnesses, and to have a <b>lawyer</b>. "
                 "<b>7th:</b> a jury trial in many <b>civil</b> cases (disagreements over money or property, not crimes). "
                 "<b>8th:</b> no <b>excessive bail</b> or fines and no <b>cruel and unusual punishment</b>.</p>", yt("rights of the accused 5th 6th 8th amendments"))
        + '<div class="lab">Which amendment protects this?</div>'
        + mark_list(["A man found not guilty can't be tried again for the same crime.", "An accused woman gets a lawyer.", "Bail can't be set at a million dollars for a small crime.",
                     "Two neighbors arguing over a fence get a jury.", "A suspect doesn't have to answer questions that could prove him guilty.", "A trial can't be kept secret or delayed for years.",
                     "A punishment can't be cruel and unusual."], ["5th", "6th", "7th", "8th"])
        + qs([("What is double jeopardy?", ["being tried twice for the same crime", "two crimes at once", "a game show"]),
              ("What is a civil case?", ["a disagreement over money or property", "a serious crime like robbery", "a case about the President"]),
              ("Proverbs 31:9 says, “Open your mouth, judge righteously, defend the rights of the poor and needy” (ESV). How do the 5th–8th Amendments help protect people who can't protect themselves?", 3)], 8),
        "1) 5th 2) 6th 3) 8th 4) 7th 5) 5th 6) 6th 7) 8th. 8) being tried twice for the same crime 9) a disagreement over money or property 10) e.g., everyone gets a lawyer and a fair trial, even if poor.")
    S.set(4, "9th & 10th + Review",
        learnbox("<p><b>Last two:</b> the <b>9th Amendment</b> says that just because a right isn't listed doesn't mean people don't have it. The <b>10th Amendment</b> says "
                 "powers not given to the national government (and not forbidden to the states) belong to the <b>states or the people</b>. "
                 "<b>Review quiz</b> — Bill of Rights. Goal: 8 of 10.</p>", yt("bill of rights review for kids"))
        + qs([("Who wrote the Bill of Rights?", ["James Madison", "Thomas Jefferson", "John Adams"]), ("What year was it ratified?", ["1791", "1787", "1776"]),
              ("Which is NOT one of the 1st Amendment's five freedoms?", ["freedom to vote", "freedom of the press", "freedom of assembly"]),
              ("Which amendment protects the right to keep and bear arms?", ["2nd", "4th", "8th"]),
              ("Which amendment requires warrants and stops unreasonable searches?", ["4th", "3rd", "6th"]),
              ("Which amendment gives a speedy, public trial and a lawyer?", ["6th", "5th", "10th"]),
              ("Which amendment bans cruel and unusual punishment?", ["8th", "7th", "1st"]),
              ("Which amendment gives leftover powers to the states or the people?", ["10th", "9th", "2nd"]),
              ("Name all five freedoms of the 1st Amendment.", 1),
              ("Which right in the Bill of Rights matters most to your family? Explain.", 3)]),
        "1) James Madison 2) 1791 3) freedom to vote 4) 2nd 5) 4th 6) 6th 7) 8th 8) 10th 9) religion, speech, press, assembly, petition 10) opinion.")
    return S

def build():
    return [math(), english(), science(), civics()]
