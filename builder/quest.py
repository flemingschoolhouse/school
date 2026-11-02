"""Chore Quest — daily game-style checklists for each kid (not weekly; lives at the site root as quest-<kid>.html).

Edit the lists, chores, XP, levels and rewards in the CONFIG section below, then run:  python3 quest.py
It writes quest-<kid>.html + quest-<kid>.webmanifest + icons/quest-<kid>.png into the repo root,
and MOM_BOARD (imported by mompage.py) adds the Chore Quest scoreboard to Mom's Corner.

Saving: uses the same Google Apps Script API as the school pages (no script changes needed):
  kid=<Kid>, week="quest-stats"  -> progress = today's summary + team chores claimed today; answers = day history
  kid=<Kid>, week="questmom"     -> answers = {date: 1} for each day Mom tapped "Inspection passed"
"""
import json, os, sys
sys.path.insert(0, "/home/claude")

API = "https://script.google.com/macros/s/AKfycbzgvfEOWoBFQHBeHmbvklVpT-UCOSJUHCx3rcUvQVwzFDg9CfIY0UC6UlDvA9kr3ZeIaQ/exec"
REPO = "/home/claude/school"

# ============================ CONFIG ============================
TUE_SAT = [2, 3, 4, 5, 6]          # JS getDay(): 0 Sun … 6 Sat — school days

def P(id, text, emoji, xp=5, days=None, link=None, special=False):
    return dict(id=id, text=text, emoji=emoji, xp=xp, days=days, link=link, special=special)

# Grace's Master Cleaning Checklist — shared by everyone every day. easy=True chores are starred for the littles.
def C(id, text, xp, easy=False):
    return dict(id=id, text=text, xp=xp, easy=easy)
TEAM = [
 dict(room="Kitchen", emoji="🍳", chores=[C("k1", "Clean off counters", 10), C("k2", "Wipe off counters", 10), C("k3", "Clean off table", 10, True),
      C("k4", "Wipe off table", 5, True), C("k5", "Wipe down cabinets", 10), C("k6", "Wipe down chairs and benches", 10, True),
      C("k7", "Load dishwasher", 15), C("k8", "Unload dishwasher", 15), C("k9", "Wipe out / down sink", 10),
      C("k10", "Pick up all THINGS off floor", 10, True), C("k11", "Vacuum", 15)]),
 dict(room="Living Room", emoji="🛋️", chores=[C("l1", "Put up all things on couch", 5, True), C("l2", "Put up all things on rocking chair", 5, True),
      C("l3", "Throw away all trash", 5, True), C("l4", "Put up laundry", 10), C("l5", "Organize shelf", 10), C("l6", "Wipe down / dust shelf", 10),
      C("l7", "Fold blankets in corner of couch", 5, True), C("l8", "Live-Barbie / Library area", 10, True)]),
 dict(room="Bathroom", emoji="🛁", chores=[C("b1", "Wipe down sink", 10), C("b2", "Wipe down back and bottom of toilet", 15), C("b3", "Clean inside of toilet", 20),
      C("b4", "Wipe down cabinet", 10), C("b5", "Put all dirty laundry in hamper", 5, True), C("b6", "Throw away all trash", 5, True),
      C("b7", "Empty trash can", 10), C("b8", "Vacuum", 15)]),
 dict(room="Sleeping Room", emoji="🛏️", chores=[C("s1", "Make beds", 10, True), C("s2", "Put up ALL clean clothes", 15), C("s3", "Put (ONLY the actual dirty) clothes in laundry", 5, True),
      C("s4", "Pick up / put up all things on floor (toys, books, purses, etc.)", 10, True), C("s5", "Straighten / organize clothes baskets", 10),
      C("s6", "Put normal wear shoes in shoe holder", 5, True), C("s7", "Stack all other shoes in tote (closet)", 5, True),
      C("s8", "Straighten / dust tops of shelves", 10), C("s9", "Vacuum", 15)]),
 dict(room="Playroom", emoji="🧸", chores=[C("p1", "Put up ALL electronics in their homes (headsets, Nintendos, remotes, game cards…)", 10, True),
      C("p2", "Put toys in proper toy bin", 5, True), C("p3", "Throw away any and all trash", 5, True), C("p4", "Dust shelves", 10),
      C("p5", "Straighten / clean / organize TV stand", 10)]),
 dict(room="Extras", emoji="⭐", chores=[C("e1", "Clean up hallway", 10, True), C("e2", "Clean van", 25)]),
]

TEEN_AM = [P("teeth", "Brush teeth", "🪥"), P("face", "Wash face", "🧼"), P("deo", "Put on deodorant", "✨"), P("dress", "Get dressed", "👕"),
           P("hair", "Do your hair", "💇‍♀️"), P("bed", "Make your bed", "🛏️"), P("bfast", "Eat breakfast", "🥣")]
TEEN_PM = [P("shower", "Shower", "🚿"), P("teeth2", "Brush teeth", "🪥"), P("hamper", "Dirty clothes in the hamper", "🧺"),
           P("layout", "Lay out tomorrow's clothes", "👚"), P("charge", "Charge your tablet", "🔌"), P("bible", "Family Bible study", "📖")]
KID_AM = [P("teeth", "Brush teeth", "🪥"), P("dress", "Get dressed", "👕"), P("hair", "Brush your hair", "🪮"), P("bed", "Make your bed", "🛏️"), P("bfast", "Eat breakfast", "🥣")]
KID_PM = [P("bath", "Bath or shower", "🛁"), P("teeth2", "Brush teeth", "🪥"), P("pjs", "Put on pajamas", "🌙"),
          P("hamper", "Dirty clothes in the hamper", "🧺"), P("bible", "Family Bible study", "📖")]
def school(kid): return [P("school", "Do today's school pages", "✏️", 15, TUE_SAT, f"{kid.lower()}.html")]

KIDS = {
 "Nevaeh": dict(style="teen", color="#6d28d9", team_goal=4, am=TEEN_AM, school=school("Nevaeh"), pm=TEEN_PM),
 "Nylah":  dict(style="teen", color="#2f5bd3", team_goal=4, am=TEEN_AM, school=school("Nylah"), pm=TEEN_PM),
 "Naomi":  dict(style="kid", color="#8a3ab9", team_goal=3, read=False, am=KID_AM, school=school("Naomi"), pm=KID_PM,
                own=[P("micro", "Clean the microwave — your special job!", "🌟", 15, special=True)]),
 "Nariah": dict(style="kid", color="#d6336c", team_goal=3, read=True, am=KID_AM, school=school("Nariah"), pm=KID_PM),
 "Titus":  dict(style="kid", color="#2f5bd3", team_goal=2, read=True,
                am=[P("teeth", "Brush teeth", "🪥"), P("dress", "Get dressed", "👕"), P("bed", "Make your bed", "🛏️"), P("shoes", "Shoes in the shoe holder", "👟"), P("bfast", "Eat breakfast", "🥣")],
                school=school("Titus"), pm=[P("bath", "Take a bath", "🛁"), P("teeth2", "Brush teeth", "🪥"), P("pjs", "Put on pajamas", "🌙"), P("hamper", "Clothes in the hamper", "🧺"), P("bible", "Family Bible study", "📖")]),
 "Nayeli": dict(style="kid", color="#a21caf", team_goal=1, read=True,
                am=[P("teeth", "Brush teeth", "🪥"), P("dress", "Get dressed", "👗"), P("hands", "Wash hands", "🧼"), P("shoes", "Shoes in the shoe holder", "👟")],
                school=[P("school", "My school pages", "✏️", 15, TUE_SAT, "nayeli.html")],
                pm=[P("bath", "Take a bath", "🛁"), P("pjs", "Put on pajamas", "🌙"), P("teeth2", "Brush teeth", "🪥"), P("bible", "Bible study — sit and listen", "📖")]),
}

# Level N needs LEVELS[N-1] total XP (after the list, every level is +900 more).
LEVELS = [0, 100, 250, 450, 700, 1000, 1400, 1900, 2500, 3200]
TEEN_TITLES = ["Rookie", "Apprentice", "Helper Pro", "Tidy Tactician", "Clean Captain", "Chore Champion", "Home Hero", "Elite", "Master", "Legend"]
KID_TITLES = ["Little Helper", "Busy Helper", "Super Helper", "Star Helper", "Mighty Helper", "Awesome Helper", "Hero Helper", "Champion Helper", "Master Helper", "Legendary Helper"]
PETS = [("🥚", "Egg"), ("🐣", "Hatchling"), ("🐥", "Chick"), ("🦜", "Parrot"), ("🦚", "Peacock"), ("🦄", "Unicorn"), ("🐉", "Dragon")]  # stage = min(level-1, last)
# Rewards Grace can change any time (level -> reward). "Show Mom to claim!"
REWARDS = {2: "Pick tonight's dessert 🍪", 3: "Choose the family movie 🎬", 4: "Stay up 30 minutes late 🌙", 5: "Pick the pizza on church night 🍕",
           6: "Skip one chore of your choice 🎟️", 7: "One-on-one time with Mom or Dad 💜", 8: "Ice cream trip 🍦", 9: "Pick game night's game 🎲", 10: "Big surprise reward 🎁"}
XP_RULES = dict(day_bonus=25, streak_step=3, streak_cap=30, inspect=25)
BADGES = [  # id, emoji, name, how to earn (checked in JS by stat >= n)
 ("first", "🏁", "First Quest", "Finish a whole day", "complete", 1),
 ("st3", "🔥", "On Fire", "3-day streak", "beststreak", 3),
 ("st7", "⚡", "Week Warrior", "7-day streak", "beststreak", 7),
 ("st14", "🌟", "Unstoppable", "14-day streak", "beststreak", 14),
 ("st30", "👑", "Royal Streak", "30-day streak", "beststreak", 30),
 ("team10", "🤝", "Team Player", "10 team chores", "team", 10),
 ("team50", "🧽", "Clean Machine", "50 team chores", "team", 50),
 ("team150", "🏠", "House Hero", "150 team chores", "team", 150),
 ("kitchen20", "🍳", "Kitchen Hero", "20 kitchen chores", "kitchen", 20),
 ("bath10", "🚽", "Brave Bathroom Boss", "10 bathroom chores", "bath", 10),
 ("vac10", "🌀", "Vacuum Pro", "Vacuum 10 times", "vacuum", 10),
 ("early5", "🐓", "Early Bird", "Morning list done by 9:30, 5 times", "early", 5),
 ("insp5", "🏆", "Inspection Ace", "Pass Mom's inspection 5 times", "inspect", 5),
 ("micro10", "🌟", "Microwave Master", "Clean the microwave 10 times", "micro", 10),
]
# ================================================================

def level_table(n=40):
    t = list(LEVELS)
    while len(t) < n: t.append(t[-1] + 900)
    return t

PAGE_CSS = r"""
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;font-family:Poppins,sans-serif;min-height:100vh;padding-bottom:40px}
body.kid{background:linear-gradient(180deg,#f3ecff 0%,#e8f0ff 60%,#fdeef6 100%);color:#1f2a5c}
body.teen{background:radial-gradient(circle at 20% 0%,#2a1f5c 0%,#12142e 55%,#0b0c1f 100%);color:#eef0ff}
.wrap{max-width:720px;margin:0 auto;padding:14px}
.hero{border-radius:24px;padding:16px;display:flex;gap:14px;align-items:center;position:relative;overflow:hidden}
.kid .hero{background:#fff;box-shadow:0 4px 0 rgba(31,42,92,.12)}
.teen .hero{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);backdrop-filter:blur(6px)}
.av{width:92px;height:92px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:56px;flex:none;position:relative}
.kid .av{background:var(--c)}.teen .av{background:linear-gradient(135deg,var(--c),#0b0c1f);font-size:30px;font-weight:800;color:#fff;border:3px solid rgba(255,255,255,.3)}
.av .lv{position:absolute;bottom:-4px;right:-4px;background:#1f2a5c;color:#fff;font:800 14px Poppins;border-radius:12px;padding:2px 8px;border:2px solid #fff}
.hi{flex:1;min-width:0}.hi h1{margin:0;font-size:26px;line-height:1.1}.hi .ti{font-weight:600;opacity:.8;font-size:15px}
.bar{height:16px;border-radius:10px;margin:8px 0 3px;overflow:hidden}.kid .bar{background:#e6e1f5}.teen .bar{background:rgba(255,255,255,.12)}
.bar i{display:block;height:100%;border-radius:10px;background:linear-gradient(90deg,var(--c),#2f5bd3);transition:width .6s}
.small{font-size:12.5px;opacity:.8}
.chips{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.chip{border-radius:16px;padding:5px 12px;font-weight:700;font-size:14px}.kid .chip{background:#f1ebfd}.teen .chip{background:rgba(255,255,255,.1)}
.today{margin:14px 0 4px;display:flex;align-items:center;gap:12px;border-radius:20px;padding:12px 16px}
.kid .today{background:#fff}.teen .today{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1)}
.ring{width:64px;height:64px;flex:none}.today b{font-size:17px}
h2{font-size:19px;margin:20px 4px 8px;display:flex;align-items:center;gap:8px}
.sec{border-radius:20px;padding:6px}.kid .sec{background:#fff;box-shadow:0 3px 0 rgba(31,42,92,.08)}.teen .sec{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08)}
.it{display:flex;align-items:center;gap:12px;padding:10px;border-radius:14px;cursor:pointer;user-select:none;transition:background .15s}
.it+.it{border-top:1px dashed rgba(127,127,160,.25)}
.it .em{font-size:28px;width:40px;text-align:center;flex:none}
.it .tx{flex:1;font-size:17px;font-weight:500;line-height:1.25}.kid.big .it .tx{font-size:20px;font-weight:600}
.it .xp{font-size:12px;font-weight:700;opacity:.7;white-space:nowrap}
.box{width:38px;height:38px;border-radius:12px;border:3px solid var(--c);flex:none;display:flex;align-items:center;justify-content:center;font-size:24px;color:#fff;transition:transform .15s}
.it.on .box{background:var(--c);transform:scale(1.08)}.it.on .tx{text-decoration:line-through;opacity:.55}
.it.on{background:rgba(109,40,217,.07)}
.it.lock{cursor:default;opacity:.55}.it.lock .box{border-style:dashed}
.say{border:0;background:#f1ebfd;border-radius:50%;width:36px;height:36px;font-size:18px;flex:none;cursor:pointer}
.go{font-size:12px;font-weight:700;color:#fff;background:#4338ca;border-radius:12px;padding:4px 10px;text-decoration:none;white-space:nowrap}
.who{font-size:12px;font-weight:700;border-radius:10px;padding:2px 8px;background:#e4f6e7;color:#1d6b33;white-space:nowrap}
.teen .who{background:rgba(80,200,120,.2);color:#9ff0b9}
.star{font-size:12px;color:#8a3ab9;font-weight:700}
.room{border-radius:16px;margin:6px 0;overflow:hidden}.kid .room{background:#faf8ff}.teen .room{background:rgba(255,255,255,.04)}
.room summary{list-style:none;cursor:pointer;padding:12px 14px;font-weight:700;font-size:17px;display:flex;align-items:center;gap:10px}
.room summary::-webkit-details-marker{display:none}.room summary .ct{margin-left:auto;font-size:13px;opacity:.7}
.goal{border-radius:16px;padding:10px 14px;margin:0 0 6px;font-weight:600;font-size:15px}.kid .goal{background:#f1ebfd}.teen .goal{background:rgba(109,40,217,.25)}
.badges{display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:8px}
.bd{border-radius:16px;padding:10px 6px;text-align:center;font-size:12px;font-weight:600}.bd .e{font-size:34px;display:block}
.kid .bd{background:#fff}.teen .bd{background:rgba(255,255,255,.06)}.bd.no{opacity:.35;filter:grayscale(1)}
.rw{display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:14px;font-weight:600}
.rw+.rw{border-top:1px dashed rgba(127,127,160,.25)}.rw .l{font-weight:800;min-width:70px}.rw.got{background:rgba(80,200,120,.15)}.rw.no{opacity:.5}
.pop{position:fixed;inset:0;background:rgba(10,12,30,.75);display:none;align-items:center;justify-content:center;z-index:20;padding:20px}
.pop.on{display:flex}.card{background:#fff;color:#1f2a5c;border-radius:28px;padding:26px 22px;text-align:center;max-width:380px;width:100%;animation:bounce .5s}
.card .big{font-size:84px;line-height:1}.card h3{font-size:28px;margin:8px 0 4px}.card p{margin:4px 0 14px;font-size:16px}
.card button{border:0;background:var(--c);color:#fff;font:700 18px Poppins;border-radius:22px;padding:12px 28px;cursor:pointer}
@keyframes bounce{0%{transform:scale(.6)}60%{transform:scale(1.06)}100%{transform:scale(1)}}
#fx{position:fixed;inset:0;pointer-events:none;z-index:30}
.float{position:fixed;font:800 20px Poppins;color:#6d28d9;pointer-events:none;z-index:31;animation:up 1s forwards}
.teen .float{color:#c4b5fd}
@keyframes up{from{opacity:1;transform:translateY(0)}to{opacity:0;transform:translateY(-60px)}}
.sync{text-align:center;font-size:12px;opacity:.6;margin-top:18px}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.top a{color:inherit;font-weight:600;font-size:14px;text-decoration:none;opacity:.8}
"""

PAGE_JS = r"""
(function(){
var C=window.QUEST, KID=C.kid, API=C.api, LS='quest-'+KID;
var ROOMOF={},CH={};C.team.forEach(function(r){r.chores.forEach(function(c){ROOMOF[c.id]=r.room;CH[c.id]=c})});
function today(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function dkey(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
var S={days:{},base:{}},INSP={},CLAIMS={},TODAY=today();
try{var l=JSON.parse(localStorage.getItem(LS)||'null');if(l&&l.days)S=l}catch(e){}
if(!S.base)S.base={};
function day(k){k=k||TODAY;if(!S.days[k])S.days[k]={p:[],t:[]};return S.days[k]}
function personal(dateStr){var wd=new Date(dateStr+'T12:00:00').getDay(),out=[];
  ['am','school','own','pm'].forEach(function(s){(C[s]||[]).forEach(function(it){if(!it.days||it.days.indexOf(wd)>=0)out.push(it)})});return out}
function dayXP(k,d){var x=0,its={};personal(k).forEach(function(i){its[i.id]=i});
  d.p.forEach(function(id){x+=(its[id]?its[id].xp:5)});d.t.forEach(function(id){x+=(CH[id]?CH[id].xp:5)});return x}
function complete(k,d){var ps=personal(k);for(var i=0;i<ps.length;i++)if(d.p.indexOf(ps[i].id)<0)return false;return d.t.length>=C.goal}
function stats(){
  var keys=Object.keys(S.days).sort(),b=S.base,st={xp:b.xp||0,complete:b.complete||0,team:b.team||0,kitchen:b.kitchen||0,bath:b.bath||0,vacuum:b.vacuum||0,
    early:b.early||0,micro:b.micro||0,inspect:0,beststreak:b.beststreak||0,streak:0};
  var run=0,prev=null;
  keys.forEach(function(k){var d=S.days[k],c=complete(k,d);st.xp+=dayXP(k,d);
    d.t.forEach(function(id){st.team++;if(ROOMOF[id]=='Kitchen')st.kitchen++;if(ROOMOF[id]=='Bathroom')st.bath++;if(/vacuum/i.test(CH[id]?CH[id].text:''))st.vacuum++});
    if(d.p.indexOf('micro')>=0)st.micro++; if(d.early)st.early++;
    if(c){st.complete++;var gap=prev?Math.round((new Date(k)-new Date(prev))/864e5):1;run=(gap==1)?run+1:1;prev=k;
      st.xp+=C.rules.day_bonus+Math.min(run*C.rules.streak_step,C.rules.streak_cap);st.beststreak=Math.max(st.beststreak,run)}});
  // current streak: ends today or yesterday
  var y=new Date();y.setDate(y.getDate()-1);
  st.streak=(prev==TODAY||prev==dkey(y))?run:0;
  for(var k in INSP){st.inspect++;st.xp+=C.rules.inspect}
  var L=1;while(L<C.levels.length&&st.xp>=C.levels[L])L++;st.level=L;st.lo=C.levels[L-1];st.hi=C.levels[L]||st.lo+900;return st}
// ---------- sound & fx ----------
var AC=null;function tone(f,t,dur){try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();var o=AC.createOscillator(),g=AC.createGain();
  o.frequency.value=f;o.type='triangle';g.gain.setValueAtTime(.18,AC.currentTime+t);g.gain.exponentialRampToValueAtTime(.001,AC.currentTime+t+dur);
  o.connect(g);g.connect(AC.destination);o.start(AC.currentTime+t);o.stop(AC.currentTime+t+dur)}catch(e){}}
function ding(){tone(880,0,.15);tone(1320,.08,.2)}
function fanfare(){[523,659,784,1047].forEach(function(f,i){tone(f,i*.12,.3)})}
function floatXP(el,n){var r=el.getBoundingClientRect(),f=document.createElement('div');f.className='float';f.textContent='+'+n+' XP';
  f.style.left=(r.right-90)+'px';f.style.top=(r.top)+'px';document.body.appendChild(f);setTimeout(function(){f.remove()},1000)}
var cv=document.getElementById('fx'),cx=cv.getContext('2d'),parts=[];
function confetti(n){cv.width=innerWidth;cv.height=innerHeight;var cols=['#6d28d9','#2f5bd3','#d6336c','#8a3ab9','#22a3c4','#4338ca'];
  for(var i=0;i<n;i++)parts.push({x:innerWidth/2,y:innerHeight/3,vx:(Math.random()-.5)*14,vy:Math.random()*-12-4,s:6+Math.random()*6,c:cols[i%6],r:Math.random()*6,life:120});
  if(parts.length==n)loop()}
function loop(){cx.clearRect(0,0,cv.width,cv.height);parts.forEach(function(p){p.vy+=.35;p.x+=p.vx;p.y+=p.vy;p.r+=.2;p.life--;
  cx.save();cx.translate(p.x,p.y);cx.rotate(p.r);cx.fillStyle=p.c;cx.fillRect(-p.s/2,-p.s/4,p.s,p.s/2);cx.restore()});
  parts=parts.filter(function(p){return p.life>0&&p.y<innerHeight+20});if(parts.length)requestAnimationFrame(loop);else cx.clearRect(0,0,cv.width,cv.height)}
function popup(big,title,text){var p=document.getElementById('pop');p.querySelector('.big').textContent=big;p.querySelector('h3').textContent=title;
  p.querySelector('p').textContent=text;p.classList.add('on');if(C.read)say(title+'. '+text)}
document.getElementById('pop').addEventListener('click',function(e){if(e.target.tagName=='BUTTON'||e.target.id=='pop')this.classList.remove('on')});
function say(t){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t.replace(/[^\w\s.,!?'’-]/g,' '));u.rate=.9;speechSynthesis.speak(u)}catch(e){}}
// ---------- render ----------
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function item(it,on,extra,lock){
  return '<div class="it'+(on?' on':'')+(lock?' lock':'')+'" data-id="'+it.id+'" data-kind="'+(it.room?'t':'p')+'"><div class="em">'+(it.emoji||'')+'</div><div class="tx">'+esc(it.text)+
    (it.easy&&C.style=='kid'?' <span class="star">⭐ easy</span>':'')+'</div>'+(extra||'')+
    (C.read?'<button class="say" data-say="'+esc(it.text)+'">🔊</button>':'')+'<span class="xp">+'+it.xp+'</span><div class="box">'+(on?'✓':'')+'</div></div>'}
var lastLevel=null,lastComplete=null;
function render(){
  var d=day(),st=stats(),ps=personal(TODAY),done=0;ps.forEach(function(i){if(d.p.indexOf(i.id)>=0)done++});
  var tot=ps.length+C.goal,cnt=done+Math.min(d.t.length,C.goal),pct=tot?cnt/tot:0,comp=complete(TODAY,d);
  // hero
  var pet=C.pets[Math.min(st.level-1,C.pets.length-1)];
  document.getElementById('av').innerHTML=(C.style=='kid'?pet[0]:KID.charAt(0))+'<span class="lv">Lv '+st.level+'</span>';
  document.getElementById('title').textContent='Level '+st.level+' · '+C.titles[Math.min(st.level-1,C.titles.length-1)]+(C.style=='kid'?' · pet: '+pet[1]:'');
  document.getElementById('xpbar').style.width=Math.min(100,(st.xp-st.lo)/(st.hi-st.lo)*100)+'%';
  document.getElementById('xptx').textContent=st.xp+' XP · '+(st.hi-st.xp)+' to Level '+(st.level+1);
  document.getElementById('chips').innerHTML='<span class="chip">🔥 '+st.streak+' day streak</span><span class="chip">🏆 best '+st.beststreak+'</span><span class="chip">🧽 '+st.team+' team chores</span>';
  // ring
  var R=26,Cc=2*Math.PI*R;document.getElementById('ring').innerHTML='<circle cx="32" cy="32" r="'+R+'" fill="none" stroke="rgba(127,127,160,.25)" stroke-width="8"/>'+
    '<circle cx="32" cy="32" r="'+R+'" fill="none" stroke="'+C.color+'" stroke-width="8" stroke-linecap="round" stroke-dasharray="'+(Cc*pct)+' '+Cc+'" transform="rotate(-90 32 32)"/>'+
    '<text x="32" y="38" text-anchor="middle" font-size="16" font-weight="800" fill="currentColor">'+Math.round(pct*100)+'%</text>';
  document.getElementById('todaytx').innerHTML=comp?'<b>Quest complete! 🎉</b><div class="small">Everything done today. You earned your day bonus!</div>':
    '<b>'+cnt+' of '+tot+' done today</b><div class="small">Finish your list + '+C.goal+' team chore'+(C.goal>1?'s':'')+' to complete today\'s quest.</div>';
  // personal sections
  var secs=[['am','☀️ Morning'],['school','✏️ School'],['own','🌟 My special job'],['pm','🌙 Evening']],h='';
  var wd=new Date().getDay();
  secs.forEach(function(s){var its=(C[s[0]]||[]).filter(function(i){return !i.days||i.days.indexOf(wd)>=0});if(!its.length)return;
    h+='<h2>'+s[1]+'</h2><div class="sec">'+its.map(function(i){return item(i,d.p.indexOf(i.id)>=0,i.link?'<a class="go" href="'+i.link+'">Open ↗</a>':'')}).join('')+'</div>';
    if(s[0]=='school'){h+=teamHTML(d)}});
  if(!(C.school||[]).some(function(i){return !i.days||i.days.indexOf(wd)>=0}))h=h.replace('<h2>🌙 Evening</h2>',teamHTML(d)+'<h2>🌙 Evening</h2>');
  document.getElementById('lists').innerHTML=h;
  // badges
  document.getElementById('badges').innerHTML=C.badges.filter(function(b){return b[0]!='micro10'||C.own}).map(function(b){var got=(st[b[4]]||0)>=b[5];
    return '<div class="bd'+(got?'':' no')+'"><span class="e">'+b[1]+'</span>'+b[2]+'<div class="small">'+b[3]+'</div></div>'}).join('');
  // rewards
  document.getElementById('rewards').innerHTML=Object.keys(C.rewards).map(function(l){l=+l;return '<div class="rw '+(st.level>=l?'got':'no')+'"><span class="l">Level '+l+'</span><span>'+C.rewards[l]+'</span>'+(st.level>=l?'<span style="margin-left:auto">✅ show Mom!</span>':'')+'</div>'}).join('');
  if(lastLevel!==null&&st.level>lastLevel){fanfare();confetti(160);var r=C.rewards[st.level];
    popup(C.style=='kid'?pet[0]:'⚡','Level '+st.level+'!',C.titles[Math.min(st.level-1,C.titles.length-1)]+(r?' — Reward unlocked: '+r+' Show Mom!':''))}
  else if(lastComplete===false&&comp){fanfare();confetti(120);popup('🎉','Quest complete!','You finished everything today! +'+C.rules.day_bonus+' bonus XP'+(st.streak>1?' · '+st.streak+' day streak 🔥':''))}
  lastLevel=st.level;lastComplete=comp;
}
function teamHTML(d){
  var h='<h2>🧽 Team Chores</h2><div class="goal">Pick at least <b>'+C.goal+'</b> chore'+(C.goal>1?'s':'')+' from the family chart today ('+Math.min(d.t.length,C.goal)+'/'+C.goal+'). Extra chores = extra XP!</div><div class="sec">';
  C.team.forEach(function(r){var mine=0,doneR=0;r.chores.forEach(function(c){if(d.t.indexOf(c.id)>=0)mine++;if(d.t.indexOf(c.id)>=0||CLAIMS[c.id])doneR++});
    h+='<details class="room"'+(mine?' open':'')+'><summary><span style="font-size:24px">'+r.emoji+'</span>'+r.room+'<span class="ct">'+doneR+'/'+r.chores.length+' done</span></summary>'+
      r.chores.map(function(c){var on=d.t.indexOf(c.id)>=0,other=!on&&CLAIMS[c.id];c.room=r.room;
        return item(c,on,other?'<span class="who">✓ '+CLAIMS[c.id].join(' & ')+'</span>':'',!!other)}).join('')+'</details>'});
  return h+'</div>'}
// ---------- interactions ----------
document.getElementById('lists').addEventListener('click',function(e){
  var s=e.target.closest('.say');if(s){e.stopPropagation();say(s.dataset.say);return}
  if(e.target.closest('a'))return;var el=e.target.closest('.it');if(!el||el.classList.contains('lock'))return;
  var d=day(),arr=el.dataset.kind=='t'?d.t:d.p,id=el.dataset.id,i=arr.indexOf(id);
  if(i>=0){arr.splice(i,1)}else{arr.push(id);ding();var xp=+(el.querySelector('.xp').textContent.replace('+',''));floatXP(el,xp);confetti(18);
    if(C.read)say(el.querySelector('.tx').textContent.replace('⭐ easy',''));
    var am=(C.am||[]).every(function(x){return d.p.indexOf(x.id)>=0});if(am&&!d.early&&new Date().getHours()*60+new Date().getMinutes()<=570)d.early=1}
  var open=[].map.call(document.querySelectorAll('details.room[open]'),function(x){return x.querySelector('summary').textContent});
  save();render();
  document.querySelectorAll('details.room').forEach(function(x){if(open.indexOf(x.querySelector('summary').textContent)>=0)x.open=true})});
// ---------- sync ----------
var st_;function rollup(){var keys=Object.keys(S.days).sort();if(keys.length<=60)return;var before=stats().xp,b=S.base;
  b.beststreak=Math.max(b.beststreak||0,stats().beststreak);
  while(keys.length>60){var k=keys.shift(),d=S.days[k];if(complete(k,d))b.complete=(b.complete||0)+1;
  d.t.forEach(function(id){b.team=(b.team||0)+1;if(ROOMOF[id]=='Kitchen')b.kitchen=(b.kitchen||0)+1;if(ROOMOF[id]=='Bathroom')b.bath=(b.bath||0)+1;if(/vacuum/i.test(CH[id]?CH[id].text:''))b.vacuum=(b.vacuum||0)+1});
  if(d.p.indexOf('micro')>=0)b.micro=(b.micro||0)+1;if(d.early)b.early=(b.early||0)+1;delete S.days[k]}
  b.xp=(b.xp||0)+before-stats().xp}
function save(){rollup();try{localStorage.setItem(LS,JSON.stringify(S))}catch(e){}clearTimeout(st_);st_=setTimeout(push,1500)}
function push(){if(!API)return;var st=stats(),d=day(),ps=personal(TODAY),dn=ps.filter(function(i){return d.p.indexOf(i.id)>=0}).length;
  var body={kid:KID,week:'quest-stats',progress:{date:TODAY,team:d.t,done:dn,total:ps.length,goal:C.goal,complete:complete(TODAY,d)?1:0,
    level:st.level,xp:st.xp,streak:st.streak,best:st.beststreak,title:C.titles[Math.min(st.level-1,C.titles.length-1)]},answers:S};
  try{fetch(API,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body)}).then(function(){mark('Saved ✓')})}catch(e){}}
function mark(t){document.getElementById('sync').textContent=t+' · '+new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})}
function merge(remote){if(!remote||!remote.days)return;for(var k in remote.days){var r=remote.days[k],l=S.days[k];
  if(!l){S.days[k]=r;continue}['p','t'].forEach(function(f){(r[f]||[]).forEach(function(id){if(l[f].indexOf(id)<0)l[f].push(id)})});if(r.early)l.early=1}
  var rb=remote.base||{};for(var f in rb){if((rb[f]||0)>(S.base[f]||0))S.base[f]=rb[f]}}
function pull(first){if(!API)return;
  fetch(API+'?action=all&week=quest-stats').then(function(r){return r.json()}).then(function(j){CLAIMS={};
    (j.rows||[]).forEach(function(r){if(r.kid==KID){if(first)merge(r.answers);return}var p=r.progress||{};
      if(p.date==TODAY)(p.team||[]).forEach(function(id){(CLAIMS[id]=CLAIMS[id]||[]).push(r.kid)})});
    return fetch(API+'?action=get&kid='+encodeURIComponent(KID)+'&week=questmom')}).then(function(r){return r.json()}).then(function(j){
    var before=Object.keys(INSP).length;INSP=j.answers||{};if(!first&&Object.keys(INSP).length>before&&INSP[TODAY]){fanfare();confetti(140);popup('🏆','Inspection passed!','Mom checked your work. Amazing job! +'+C.rules.inspect+' XP')}
    var open=[].map.call(document.querySelectorAll('details.room[open]'),function(x){return x.querySelector('summary').textContent});
    render();document.querySelectorAll('details.room').forEach(function(x){if(open.indexOf(x.querySelector('summary').textContent)>=0)x.open=true});
    mark('Synced');if(first)save()}).catch(function(){mark('Offline — saved on this tablet')})}
render();pull(true);
setInterval(function(){if(document.visibilityState!='visible')return;if(today()!=TODAY){TODAY=today();lastComplete=null;render()}pull(false)},45000);
document.addEventListener('visibilitychange',function(){if(document.visibilityState=='visible')pull(false);else{clearTimeout(st_);push()}});
})();
"""

def page_html(kid, cfg):
    conf = dict(kid=kid, api=API, style=cfg["style"], color=cfg["color"], goal=cfg["team_goal"], read=cfg.get("read", False),
                am=cfg["am"], school=cfg["school"], pm=cfg["pm"], own=cfg.get("own"), team=TEAM, levels=level_table(),
                titles=TEEN_TITLES if cfg["style"] == "teen" else KID_TITLES, pets=PETS, rewards=REWARDS, rules=XP_RULES, badges=BADGES)
    big = " big" if kid in ("Titus", "Nayeli") else ""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{kid}'s Quest</title><meta name="theme-color" content="{cfg['color']}"><meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="{kid}'s Quest"><link rel="manifest" href="quest-{kid.lower()}.webmanifest">
<link rel="icon" href="icons/quest-{kid.lower()}.png"><link rel="apple-touch-icon" href="icons/quest-{kid.lower()}.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">
<style>{PAGE_CSS}</style></head>
<body class="{cfg['style']}{big}" style="--c:{cfg['color']}"><canvas id="fx"></canvas><div class="wrap">
<div class="top"><a href="index.html">🏠 School home</a><a href="{kid.lower()}.html">✏️ My school pages</a></div>
<div class="hero"><div class="av" id="av"></div><div class="hi"><h1>{kid}'s Quest</h1><div class="ti" id="title"></div>
<div class="bar"><i id="xpbar"></i></div><div class="small" id="xptx"></div><div class="chips" id="chips"></div></div></div>
<div class="today"><svg class="ring" id="ring" viewBox="0 0 64 64"></svg><div id="todaytx"></div></div>
<div id="lists"></div>
<h2>🏅 Badges</h2><div class="badges" id="badges"></div>
<h2>🎁 Level rewards</h2><div class="sec" id="rewards"></div>
<div class="sync" id="sync">Loading…</div></div>
<div class="pop" id="pop"><div class="card"><div class="big"></div><h3></h3><p></p><button>Yay! ✨</button></div></div>
<script>window.QUEST={json.dumps(conf, ensure_ascii=False)};</script><script>{PAGE_JS}</script></body></html>"""

def make_icon(kid, color, path):
    from PIL import Image, ImageDraw, ImageFont
    S = 512; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
    d.rounded_rectangle([0, 0, S - 1, S - 1], 110, fill=c)
    try: f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 250)
    except Exception: f = ImageFont.load_default()
    d.text((S * 0.36, S * 0.47), kid[0], font=f, fill="white", anchor="mm")
    d.line([(300, 270), (350, 330), (440, 190)], fill="white", width=38, joint="curve")
    d.text((S / 2, S * 0.84), "QUEST", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64) if f else None, fill="white", anchor="mm")
    im.save(path)

def write_all(repo=REPO):
    os.makedirs(f"{repo}/icons", exist_ok=True)
    for kid, cfg in KIDS.items():
        k = kid.lower()
        open(f"{repo}/quest-{k}.html", "w").write(page_html(kid, cfg))
        make_icon(kid, cfg["color"], f"{repo}/icons/quest-{k}.png")
        man = dict(name=f"{kid}'s Quest", short_name=f"{kid}'s Quest", start_url=f"quest-{k}.html", scope="./", display="standalone",
                   background_color="#ffffff", theme_color=cfg["color"], icons=[dict(src=f"icons/quest-{k}.png", sizes="512x512", type="image/png")])
        open(f"{repo}/quest-{k}.webmanifest", "w").write(json.dumps(man, indent=1))

# ---------------- Mom's Corner scoreboard ----------------
MOM_BOARD = r"""<div class="mhead" id="quest"><h2>🎮 Chore Quest — today</h2><div id="qb">Loading…</div>
<p class="small">Tap <b>Inspection passed</b> after you check a kid's work — they get +__INSP__ XP and a trophy pop-up on their tablet.
Kids' quest pages: __LINKS__</p></div>
<style>#qb table{width:100%;border-collapse:collapse;font:14px Poppins,sans-serif}#qb td,#qb th{border:1px solid #d6d6e0;padding:6px;text-align:center}
#qb th{background:#eef1fb}#qb .kid{font-weight:700;text-align:left}#qb button{border:0;border-radius:14px;padding:6px 10px;font:600 13px Poppins;background:#6d28d9;color:#fff;cursor:pointer}
#qb button.done{background:#2b8a3e}#qb .tm{text-align:left;font:13px Poppins;margin-top:8px}</style>
<script>
(function(){var API='__API__',KIDS=['Nevaeh','Nylah','Naomi','Nariah','Titus','Nayeli'],NAMES=__NAMES__;
function today(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
var T=today(),INS={};
function load(){Promise.all([fetch(API+'?action=all&week=quest-stats').then(function(r){return r.json()}),fetch(API+'?action=all&week=questmom').then(function(r){return r.json()})]).then(function(a){
 var rows={};(a[0].rows||[]).forEach(function(r){rows[r.kid]=r});(a[1].rows||[]).forEach(function(r){INS[r.kid]=r.answers||{}});
 var h='<table><tr><th>Kid</th><th>Level</th><th>🔥 Streak</th><th>Today</th><th>Team chores today</th><th></th></tr>',tm={};
 KIDS.forEach(function(k){var r=rows[k],p=r?r.progress:{};var td=p.date==T;
  (td?p.team||[]:[]).forEach(function(id){(tm[id]=tm[id]||[]).push(k)});
  var ok=(INS[k]||{})[T];
  h+='<tr><td class="kid">'+k+'</td><td>'+(r?'Lv '+p.level+'<div style="font-size:11px">'+p.xp+' XP · '+(p.title||'')+'</div>':'—')+'</td><td>'+(r?(p.streak||0):'—')+'</td>'+
   '<td>'+(td?(p.complete?'✅ done':p.done+'/'+p.total):'not started')+'</td><td>'+(td?(p.team||[]).length+' / goal '+p.goal:'—')+'</td>'+
   '<td><button data-k="'+k+'" class="'+(ok?'done':'')+'">'+(ok?'🏆 Passed':'Inspection passed')+'</button></td></tr>'});
 var list=Object.keys(tm).map(function(id){return '<li>'+(NAMES[id]||id)+' — '+tm[id].join(' & ')+'</li>'}).join('');
 document.getElementById('qb').innerHTML=h+'</table><div class="tm"><b>Team chores done today:</b>'+(list?'<ul>'+list+'</ul>':' none yet')+'</div>';
}).catch(function(){document.getElementById('qb').textContent='Could not load Chore Quest right now — try refreshing.'})}
document.getElementById('qb').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var k=b.dataset.k,a=INS[k]||{};
 if(a[T])delete a[T];else a[T]=1;INS[k]=a;b.textContent=a[T]?'🏆 Passed':'Inspection passed';b.className=a[T]?'done':'';
 fetch(API,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain'},body:JSON.stringify({kid:k,week:'questmom',progress:{},answers:a})})});
load();setInterval(load,60000);})();
</script>"""
_names = {c["id"]: f'{r["room"]}: {c["text"]}' for r in TEAM for c in r["chores"]}
MOM_BOARD = (MOM_BOARD.replace("__API__", API).replace("__INSP__", str(XP_RULES["inspect"])).replace("__NAMES__", json.dumps(_names, ensure_ascii=False))
             .replace("__LINKS__", " · ".join(f'<a href="quest-{k.lower()}.html">{k}</a>' for k in KIDS)))

if __name__ == "__main__":
    write_all()
    print("quest pages written")
