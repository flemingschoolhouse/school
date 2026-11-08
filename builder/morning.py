from lib import *
from core_common import mc, MC_HINT

VERSE = ("And we know that for those who love God all things work together for good, for those who are "
         "called according to his purpose.")
VERSE_SHORT = "For those who love God all things work together for good."
REF = "Romans 8:28 (ESV)"
SONG = yt("Romans 8:28 ESV song")
STORYVID = yt("Joseph Bible story for kids")
THEME = "Joseph"

D = [
 dict(ref="Genesis 37:1–11", title="The Robe & the Dreams",
  story="Joseph was seventeen, and his father Jacob loved him more than his other sons. Jacob made him a robe of many colors, "
        "and his brothers hated him for it. Then Joseph had two dreams: his brothers' bundles of grain bowed down to his bundle, and "
        "the sun, moon, and eleven stars bowed down to him. When he told the dreams, his brothers hated him even more — and they were jealous. "
        "But his father kept the saying in mind. God was already at work in Joseph's story.",
  kid="Jacob gave his son Joseph a beautiful robe of many colors. Joseph had dreams that his family would bow down to him. "
      "His brothers got very jealous and angry.",
  q_teen=["Why did Joseph's brothers hate him? Give two reasons from the passage.",
          "What did the sun, moon, and eleven stars stand for in Joseph's second dream?"],
  q_mid=["What special gift did Jacob give Joseph?", "How did Joseph's brothers feel about him?"],
  q_early="What did Jacob give Joseph?",
  greek=("ζῆλος", "zēlos", "jealousy; also zeal, strong feeling", "James 3:16 — “where jealousy and selfish ambition exist, there will be disorder.”"),
  word="LOVE", wdef="caring for others the way God cares for us — not being jealous",
  theo="Sin often starts in the heart. The brothers' jealousy grew quietly until it led to something terrible — so we bring our feelings to God early.",
  j_teen="Jealousy grew in the brothers until it took over. Is there anyone you're tempted to be jealous of? Write a prayer giving that to God.",
  j_mid="Write about a time you felt jealous. What could you do next time instead?",
  k_trace="God loves me", draw="Draw Joseph's robe of many colors."),
 dict(ref="Genesis 37:12–36", title="Sold by His Brothers",
  story="Jacob sent Joseph to check on his brothers, who were far away with the sheep. When they saw him coming, they plotted to kill him. "
        "Reuben talked them into throwing him into an empty pit instead, hoping to rescue him later. Then Judah said, “Let's sell him,” "
        "and they sold Joseph to traders for twenty pieces of silver. They dipped his robe in goat's blood, and Jacob believed a wild animal had killed his son. "
        "Joseph was taken to Egypt as a slave — but he was not forgotten by God.",
  kid="Joseph's brothers threw him into a deep pit. Then they sold him to traders going to Egypt! "
      "Joseph was far from home, but God was still with him.",
  q_teen=["Which brother tried to save Joseph, and which brother suggested selling him?",
          "How could Joseph have hope in Egypt even though everything went wrong? Explain."],
  q_mid=["Where did the brothers throw Joseph?", "How much did the traders pay for Joseph?"],
  q_early="Where did the brothers put Joseph?",
  greek=("ἐλπίς", "elpis", "hope — a sure expectation of good from God", "Romans 5:5 — “hope does not put us to shame.”"),
  word="HOPE", wdef="trusting that God will bring good, even when it's hard",
  theo="Nothing that happens to God's children is outside His care. Joseph's worst day was still part of God's good plan.",
  j_teen="Joseph's family turned against him. Write about how Romans 8:28 could help someone on their worst day.",
  j_mid="Write about a hard day you had. How was God with you?",
  k_trace="God is with me", draw="Draw Joseph in the pit."),
 dict(ref="Genesis 39", title="Faithful in Egypt",
  story="Joseph was bought by Potiphar, an officer of Pharaoh. “The LORD was with Joseph,” and everything he did went well, so Potiphar put him "
        "in charge of his whole house. When Potiphar's wife tried again and again to get him to sin, Joseph refused: “How then can I do this great "
        "wickedness and sin against God?” She lied about him, and Joseph was thrown into prison for doing right. But even in prison "
        "the LORD was with him, and the keeper of the prison put Joseph in charge.",
  kid="Joseph worked hard in Egypt and always did what was right. Someone told a lie about him, and he was put in jail. "
      "But even in jail, the LORD was with Joseph!",
  q_teen=["What did Joseph say when he was tempted to sin? (39:9)",
          "Joseph did right and still ended up in prison. What does that teach about obeying God?"],
  q_mid=["What was the name of the Egyptian officer who bought Joseph?", "Who was with Joseph even in prison?"],
  q_early="Who was with Joseph in jail?",
  greek=("πειρασμός", "peirasmos", "temptation, testing", "1 Corinthians 10:13 — “God is faithful, and he will not let you be tempted beyond your ability.”"),
  word="FAITHFUL", wdef="doing what is right again and again, even when no one sees",
  theo="Joseph saw sin as sin against God first. Faithfulness means pleasing God whether we are rewarded or not.",
  j_teen="Joseph stayed faithful when it cost him. Where is it hardest for you to do right when no one is watching? What will you do?",
  j_mid="Write one way you can be faithful at home this week, even when no one sees.",
  k_trace="I do right", draw="Draw Joseph working hard."),
 dict(ref="Genesis 41", title="Pharaoh's Dreams",
  story="Pharaoh had two dreams no one could explain: seven fat cows eaten by seven thin cows, and seven full ears of grain swallowed by seven thin ones. "
        "Joseph was brought from prison and said, “It is not in me; God will give Pharaoh a favorable answer.” God showed him the meaning: "
        "seven years of plenty, then seven years of famine. Joseph told Pharaoh to store up grain in the good years. Pharaoh put Joseph — "
        "now thirty years old — in charge of all Egypt.",
  kid="Pharaoh, the king, had strange dreams about cows and grain. God helped Joseph tell what they meant: seven years of lots of food, "
      "then seven years of no food. Pharaoh made Joseph a ruler to save the food!",
  q_teen=["What did the seven fat cows and seven thin cows stand for?",
          "Joseph said, “It is not in me.” Why is that answer important? What does it show about him?"],
  q_mid=["What animals were in Pharaoh's first dream?", "What job did Pharaoh give Joseph?"],
  q_early="Who helped Joseph know what the dreams meant?",
  greek=("σοφία", "sophia", "wisdom", "James 1:5 — “If any of you lacks wisdom, let him ask God, who gives generously to all.”"),
  word="WISDOM", wdef="knowing the right thing to do — a gift from God",
  theo="Every good gift comes from God. Joseph gave God the credit, and God used Joseph's wisdom to save many lives.",
  j_teen="Joseph pointed Pharaoh to God instead of himself. What gift or talent has God given you? How can you use it to point people to Him?",
  j_mid="God gave Joseph wisdom. Write something you need wisdom for, and ask God for it.",
  k_trace="God helps me", draw="Draw seven fat cows (or a big pile of grain)."),
 dict(ref="Genesis 45:1–15; 50:20", title="God Meant It for Good",
  story="The famine came, and Joseph's brothers went to Egypt to buy grain. They bowed before the ruler — not knowing it was Joseph! "
        "Finally Joseph wept and said, “I am your brother, Joseph, whom you sold into Egypt.” He forgave them and brought the whole family to Egypt. Years later he told them, “As for you, you meant evil against me, but God meant it for good, "
        "to bring it about that many people should be kept alive.”",
  kid="Joseph's brothers came to Egypt for food. Joseph said, “I am your brother!” He hugged them and forgave them. "
      "Joseph said, “God meant it for good!”",
  q_teen=["What did Joseph say in Genesis 50:20?",
          "How does Joseph's whole story show Romans 8:28 is true? Use at least two events from this week."],
  q_mid=["Why did the brothers come to Egypt?", "What did Joseph do when he saw his brothers?"],
  q_early="What did Joseph do for his brothers?",
  greek=("ἄφεσις", "aphesis", "forgiveness — a sending away of a debt", "Ephesians 1:7 — “In him we have redemption through his blood, the forgiveness of our trespasses.”"),
  word="FORGIVE", wdef="letting go of getting even, like God lets go of our sins",
  theo="Joseph points us to Jesus: rejected by His brothers, He suffered, and God turned it into salvation for many. We forgive because we are forgiven.",
  j_teen="Look back at Joseph's whole story. Write the one thing God taught you through it this week.",
  j_mid="Is there someone you need to forgive? Write what you could say to them.",
  k_trace="God is good", draw="Draw Joseph hugging his brothers."),
]

# Multiple-choice versions (correct answer first; order is shuffled when built). Keyed by day, then question index.
MC_TEEN = {0: {1: ["his father, mother, and eleven brothers", "the kings of Egypt", "the twelve tribes' enemies"]},
           1: {0: ["Reuben tried to save him; Judah suggested selling him", "Judah tried to save him; Reuben suggested selling him", "Benjamin tried to save him; Levi suggested selling him"]},
           2: {0: ["“How then can I do this great wickedness and sin against God?”", "“No one will ever find out.”", "“I will ask Potiphar first.”"]},
           3: {0: ["seven years of plenty, then seven years of famine", "seven good kings, then seven bad kings", "seven wars Egypt would win"]},
           4: {0: ["“You meant evil against me, but God meant it for good.”", "“I will never forgive you.”", "“Go home and never come back.”"]}}
MC_MID = [{0: ["a robe of many colors", "a golden crown", "a new sword"], 1: ["jealous and angry", "proud and happy", "they didn't care"]},
          {0: ["into an empty pit", "into a river", "into a lion's den"], 1: ["twenty pieces of silver", "one gold coin", "a camel"]},
          {0: ["Potiphar", "Pharaoh", "Pilate"], 1: ["the LORD", "nobody", "his brothers"]},
          {0: ["cows", "lions", "camels"], 1: ["ruler over all Egypt", "baker for the king", "shepherd of Pharaoh's sheep"]},
          {0: ["to buy grain (food)", "to visit the pyramids", "to fight Egypt"], 1: ["He forgave them.", "He threw them in prison forever.", "He sent them away hungry."]}]
MC_EARLY = [["a robe of many colors", "a puppy", "a bike"],
            ["in a pit", "in a boat", "in a tree"],
            ["God", "nobody"],
            ["God", "a cow", "Pharaoh"],
            ["He forgave them.", "He got mad.", "He ran away."]]

def _verse_block(short=False, copy_lines=0):
    v = VERSE_SHORT if short else VERSE
    out = f'<div class="flexrow"><div class="grow verse">“{esc(v)}”<div class="small" style="margin-top:3px">{REF} · memory verse</div></div>'
    out += qr_box(SONG, "Verse song", 66) + '</div>'
    if copy_lines:
        out += f'<div class="small">Copy the verse:</div>' + lines(copy_lines, 24)
    return out

def page_for(level, name, i):
    d = D[i]
    t = f"{THEME} · {d['title']}"
    if level == "teen":
        g = d["greek"]
        body = (_verse_block(copy_lines=0)
          + f'<div class="box"><span class="lab">Read:</span> {d["ref"]}<p style="margin-top:4px">{esc(d["story"])}</p></div>'
          + "".join(mc(esc(q), MC_TEEN[i][n], n + 1) if n in MC_TEEN.get(i, {}) else f'<div><b>{n+1}.</b> {esc(q)}{lines(2,24)}</div>' for n, q in enumerate(d["q_teen"]))
          + f'<div class="grid2"><div class="box"><span class="lab">Greek word of the day</span>'
            f'<div style="font-size:18pt;margin:2px 0">{g[0]} <span style="font-size:12pt;color:#555">({g[1]})</span></div>'
            f'<div><b>Means:</b> {esc(g[2])}</div><div class="small" style="margin-top:3px">{esc(g[3])}</div></div>'
            f'<div class="box"><span class="lab">Theology fact</span><p style="margin-top:3px">{esc(d["theo"])}</p></div></div>'
          + f'<div><span class="lab">Journal:</span> {esc(d["j_teen"])}{lines(5,24)}</div>')
    elif level == "mid":
        body = (_verse_block(copy_lines=2)
          + f'<div class="box"><span class="lab">Bible story · {d["ref"]}</span><p style="margin-top:4px">{esc(d["story"])}</p></div>'
          + "".join(mc(esc(q), MC_MID[i][n], n + 1) for n, q in enumerate(d["q_mid"]))
          + f'<div class="grid2"><div class="box"><span class="lab">Bible word of the day</span><div class="word">{d["word"]}</div>'
            f'<div>{esc(d["wdef"])}</div></div><div class="box"><span class="lab">Theology fact</span><p style="margin-top:3px">{esc(d["theo"])}</p></div></div>'
          + f'<div><span class="lab">Journal:</span> {esc(d["j_mid"])}{lines(4,26)}</div>')
    elif level == "early":
        body = (_verse_block()
          + f'<div class="box"><span class="lab">Bible story · {d["ref"]}</span><p class="big" style="margin-top:4px">{esc(d["kid"])}</p></div>'
          + mc(f'<b>Question:</b> {esc(d["q_early"])}', MC_EARLY[i])
          + f'<div class="box"><span class="lab">Word of the day:</span> <b>{d["word"].title()}</b> — {esc(d["wdef"])}'
            f'{trace_line(d["word"].lower(), 46, 2)}</div>'
          + f'<div class="lab">{esc(d["draw"])}</div><div class="answer-space"></div>')
    elif level == "k":
        body = (f'<div class="lab">Trace your name:</div>{trace_line("Titus", 52, 2)}'
          + _verse_block(short=True)
          + f'<div class="box"><span class="lab">Mom reads:</span><p class="big" style="margin-top:4px">{esc(d["kid"])}</p></div>'
          + f'<div class="lab">Trace it:</div>{trace_line(d["k_trace"], 48, 1)}'
          + f'<div class="lab">{esc(d["draw"])}</div><div class="answer-space"></div>')
    else:  # pk
        body = (f'<div class="lab">Trace your name:</div>{trace_line("Nayeli", 56, 1)}'
          + f'<div class="box"><span class="lab">Mom reads:</span><p class="big" style="margin-top:4px">{esc(d["kid"])}</p>'
            f'<p class="big"><b>Say it with me:</b> “{esc(VERSE_SHORT)}”</p></div>'
          + f'<div class="lab">Trace the word:</div>{trace_line(d["word"].lower(), 56, 2)}'
          + f'<div class="lab">{esc(d["draw"])}</div><div class="answer-space"></div>')
    return page(name, i, "Morning Work", "Our school day has begun!", f'<div class="small" style="margin-top:-4px">{esc(t)}</div>' + body)

def mom_notes():
    rows = "".join(f"<tr><td><b>Day {i+1}</b></td><td>{d['ref']}</td><td>{esc(d['title'])}</td><td>{d['greek'][1]} · {d['word'].title()}</td></tr>" for i, d in enumerate(D))
    return (f'<p>Theme this week: <b>{THEME}</b>. Memory verse for everyone: <b>{REF}</b> — the littles say the shorter part.</p>'
            f'<table class="t"><tr><th>Day</th><th>Reading</th><th>Story</th><th>Greek · Word</th></tr>{rows}</table>'
            f'<div class="qrrow" style="margin-top:6px">{qr_box(SONG,"Romans 8:28 ESV song")}{qr_box(STORYVID,"Joseph story video")}</div>')
