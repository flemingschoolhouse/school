import sys, os, re
sys.path.insert(0, "/home/claude")
import lib; lib.WEB["on"] = True
import build
from lib import CSS, DAYS, esc

WEBCSS = """
html,body{background:#e9ebf4;margin:0}
.page{background:#fff;margin:14px auto;box-shadow:0 2px 10px rgba(0,0,0,.12);border-radius:6px;page-break-after:auto}
.page.blank{display:none}
.vidbtn{display:inline-flex;align-items:center;gap:6px;background:#2f5bd3;color:#fff;font-weight:700;font-size:13pt;
  padding:10px 16px;border-radius:24px;text-decoration:none;white-space:nowrap;align-self:flex-start;box-shadow:0 2px 0 #1f2a5c}
.qrrow{flex-wrap:wrap;gap:8px}
.nav{position:sticky;top:0;z-index:5;background:#1f2a5c;display:flex;gap:6px;padding:8px;justify-content:center;flex-wrap:wrap}
.nav a{color:#fff;text-decoration:none;font-weight:700;font-family:Poppins,sans-serif;padding:8px 14px;border-radius:18px;background:#4338ca;font-size:15px}
.readbtn{position:absolute;top:0.12in;left:50%;transform:translateX(-50%);background:#6d28d9;color:#fff;border:0;border-radius:18px;
  font:700 12pt Poppins,sans-serif;padding:6px 14px;cursor:pointer}
.chk{cursor:pointer}.chk.on{background:#6d28d9}
[id^=day-],#top{scroll-margin-top:64px}

input.fill{border:0;border-bottom:1.4px solid #9aa0bb;font:inherit;font-size:12.5pt;color:#1f2a5c;background:transparent;width:100%;padding:2px 4px;outline:none}
input.fill:focus,textarea.fill:focus{background:#f1ebfd}
input.blankin{border:0;border-bottom:1.4px solid #333;font:inherit;color:#1f2a5c;background:transparent;width:90px;min-width:60px;text-align:center;outline:none}
.vert input.blankin{width:100%;text-align:right;font-family:Inter;font-size:17pt}
td.edit{color:#1f2a5c;outline:none}
td.edit:focus{background:#f1ebfd}
.opt{cursor:pointer;user-select:none}.opt.sel{background:#6d28d9;color:#fff;border-color:#6d28d9!important}
.drawwrap{position:relative;display:inline-block}
.drawwrap canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:crosshair}
.answer-space{position:relative}
.answer-space canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.tools{position:absolute;right:4px;top:4px;display:flex;gap:4px;z-index:2}
.tools button{width:26px;height:26px;border-radius:50%;border:2px solid #fff;box-shadow:0 0 0 1px #999;cursor:pointer;padding:0}
.tools button.clr{width:auto;border-radius:12px;padding:0 8px;font:600 11px Poppins;background:#fff;color:#333}
.tools button.on{box-shadow:0 0 0 3px #1f2a5c}
.drawwrap .tools{opacity:.85;top:-6px;right:-6px}
.drawwrap .tools button.clr{padding:0 6px;height:22px}
.saved{position:fixed;bottom:10px;right:10px;background:#1f2a5c;color:#fff;font:600 12px Poppins;padding:6px 12px;border-radius:14px;opacity:0;transition:opacity .3s}


.vmodal{position:fixed;inset:0;background:rgba(10,12,30,.88);z-index:50;display:none;align-items:center;justify-content:center;flex-direction:column;gap:12px;padding:12px}
.vmodal.on{display:flex}
.vmodal .frame{width:min(96vw,960px);aspect-ratio:16/9;background:#000;border-radius:10px;overflow:hidden}
.vmodal iframe{width:100%;height:100%;border:0}
.vmodal .bar{display:flex;gap:10px}
.vmodal button,.vmodal a{font:700 16px Poppins,sans-serif;border:0;border-radius:22px;padding:10px 20px;cursor:pointer;text-decoration:none}
.vmodal button{background:#fff;color:#1f2a5c}.vmodal a{background:#4338ca;color:#fff}

.note{max-width:780px;margin:10px auto 0;font:13px Poppins,sans-serif;color:#444;text-align:center}
"""

JS = """
<script>
(function(){
  function fit(){var w=Math.min(window.innerWidth-12,816);document.querySelectorAll('.page').forEach(function(p){p.style.zoom=(w/816)})}
  window.addEventListener('resize',fit);fit();
  var key='chk-'+document.title;var saved={};try{saved=JSON.parse(localStorage.getItem(key)||'{}')}catch(e){}
  document.querySelectorAll('.chk').forEach(function(c,i){if(saved[i])c.classList.add('on');
    c.addEventListener('click',function(){c.classList.toggle('on');saved[i]=c.classList.contains('on');try{localStorage.setItem(key,JSON.stringify(saved))}catch(e){}})});
  var synth=window.speechSynthesis;
  document.querySelectorAll('.page').forEach(function(p){
    if(p.classList.contains('blank')||!synth)return;
    var b=document.createElement('button');b.className='readbtn';b.textContent='🔊 Read to me';p.appendChild(b);
    b.addEventListener('click',function(){
      if(synth.speaking){synth.cancel();b.textContent='🔊 Read to me';return}
      var body=p.querySelector('.body');var t=(p.querySelector('.subj .t')||{}).innerText||'';
      var u=new SpeechSynthesisUtterance(t+'. '+(body?body.innerText:'').replace(/[_☆✪]+/g,' '));u.rate=0.9;
      u.onend=function(){b.textContent='🔊 Read to me'};synth.speak(u);b.textContent='■ Stop';});
  });
})();
</script>
"""

JS2 = r"""
<script>
function schoolInit(){
  var C=window.SCHOOL||{}, KEY='ans-'+document.title, S={};
  var VIEW=/[?&]view=1/.test(location.search);
  if(VIEW){ S=C.remote||{}; }
  else { try{S=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){} }
  var badge=document.createElement('div');badge.className='saved';badge.textContent='Saved ✓';document.body.appendChild(badge);
  var t,st;
  function progress(){var P={};document.querySelectorAll('.page').forEach(function(p){
      var d=p.querySelector('.dayblk .d'),sj=p.querySelector('.subj .s'),tt=p.querySelector('.subj .t');if(!d||!sj||!/DAY/.test(d.textContent))return;
      var f=p.querySelectorAll('input.fill,input.blankin,td.edit'),n=0,tot=f.length;
      f.forEach(function(x){if((x.value||x.textContent||'').trim())n++});
      var cv=p.querySelectorAll('canvas');tot+=cv.length;cv.forEach(function(c){if(c.dataset.k&&S[c.dataset.k])n++});
      var grp=[];p.querySelectorAll('.opt').forEach(function(o){if(grp.indexOf(o.parentElement)<0)grp.push(o.parentElement)});tot+=grp.length;n+=p.querySelectorAll('.opt.sel').length;
      if(!tot)return;var k=d.textContent.replace('DAY ','D')+'|'+sj.textContent+'|'+(tt?tt.textContent:'');
      P[k]=n===0?0:(n/tot>=0.8?2:1)});return P}
  function sync(){if(VIEW||!C.api)return;var A={};for(var k in S){A[k]=(/^(dr|sv)/.test(k))?1:S[k]}
    var body=JSON.stringify({kid:C.kid,week:C.week,progress:progress(),answers:A});
    try{fetch(C.api,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain'},body:body})}catch(e){}}
  document.addEventListener('visibilitychange',function(){if(document.visibilityState==='hidden'){clearTimeout(st);sync()}});
  function save(){if(VIEW)return;try{localStorage.setItem(KEY,JSON.stringify(S));badge.style.opacity=1;clearTimeout(t);t=setTimeout(function(){badge.style.opacity=0},900)}catch(e){}
    clearTimeout(st);st=setTimeout(sync,5000)}
  // lines -> inputs
  document.querySelectorAll('.ln').forEach(function(el,i){
    var inp=document.createElement('input');inp.className='fill';inp.style.height=el.style.height||'26px';
    var k='ln'+i;inp.value=S[k]||'';inp.addEventListener('input',function(){S[k]=inp.value;save()});el.replaceWith(inp)});
  // blanks -> inputs
  document.querySelectorAll('.blank-ln').forEach(function(el,i){
    var inp=document.createElement('input');inp.className='blankin';var w=parseInt(el.style.minWidth)||70;inp.style.width=w+'px';
    var k='bl'+i;inp.value=S[k]||'';inp.addEventListener('input',function(){S[k]=inp.value;save()});el.replaceWith(inp)});
  // vertical problem answer rows
  document.querySelectorAll('.vert').forEach(function(v,i){var last=v.lastElementChild;if(!last)return;
    var inp=document.createElement('input');inp.className='blankin';inp.inputMode='numeric';var k='vt'+i;inp.value=S[k]||'';
    inp.addEventListener('input',function(){S[k]=inp.value;save()});last.innerHTML='';last.appendChild(inp)});
  // empty table cells
  document.querySelectorAll('table.t td').forEach(function(td,i){if(td.textContent.trim()!==''||td.querySelector('*'))return;
    td.contentEditable='true';td.classList.add('edit');var k='td'+i;if(S[k])td.textContent=S[k];
    td.addEventListener('input',function(){S[k]=td.textContent;save()})});
  // choice bubbles
  document.querySelectorAll('.opt').forEach(function(o,i){var k='op'+i;if(S[k])o.classList.add('sel');
    o.addEventListener('click',function(){var on=!o.classList.contains('sel');
      o.parentElement.querySelectorAll('.opt').forEach(function(x){x.classList.remove('sel');var j=[].indexOf.call(document.querySelectorAll('.opt'),x);delete S['op'+j]});
      if(on){o.classList.add('sel');S[k]=1}save()})});
  // drawing
  var COLORS=['#1f2a5c','#2f5bd3','#6d28d9','#d6336c','#2b8a3e','#e8590c'];
  function makeCanvas(host,k,small){
    var c=document.createElement('canvas');c.dataset.k=k;host.appendChild(c);
    var tools=document.createElement('div');tools.className='tools';host.appendChild(tools);
    var col=COLORS[0];
    (small?[]:COLORS).forEach(function(cc,n){var b=document.createElement('button');b.style.background=cc;if(!n)b.classList.add('on');
      b.onclick=function(e){e.stopPropagation();col=cc;tools.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on')};tools.appendChild(b)});
    var clr=document.createElement('button');clr.className='clr';clr.textContent=small?'⟲':'Clear';tools.appendChild(clr);
    function size(){var r=host.getBoundingClientRect();var w=host.offsetWidth,h=host.offsetHeight;if(!w||!h)return;
      if(c.width!==w*2){c.width=w*2;c.height=h*2;load()}}
    var ctx=c.getContext('2d');
    function load(){if(S[k]){var im=new Image();im.onload=function(){ctx.drawImage(im,0,0,c.width,c.height)};im.src=S[k]}}
    clr.onclick=function(e){e.stopPropagation();ctx.clearRect(0,0,c.width,c.height);delete S[k];save()};
    var drawing=false,last=null;
    function pt(e){var r=c.getBoundingClientRect();return[(e.clientX-r.left)*c.width/r.width,(e.clientY-r.top)*c.height/r.height]}
    c.addEventListener('pointerdown',function(e){size();drawing=true;last=pt(e);c.setPointerCapture(e.pointerId)});
    c.addEventListener('pointermove',function(e){if(!drawing)return;var p=pt(e);ctx.strokeStyle=col;ctx.lineWidth=7;ctx.lineCap='round';ctx.lineJoin='round';
      ctx.beginPath();ctx.moveTo(last[0],last[1]);ctx.lineTo(p[0],p[1]);ctx.stroke();last=p});
    function end(){if(!drawing)return;drawing=false;try{S[k]=c.toDataURL('image/png')}catch(e){}save()}
    c.addEventListener('pointerup',end);c.addEventListener('pointercancel',end);
    setTimeout(size,300);window.addEventListener('resize',function(){var d=S[k];c.width=0;size()});
  }
  document.querySelectorAll('.answer-space').forEach(function(a,i){makeCanvas(a,'dr'+i)});
  var n=0;
  document.querySelectorAll('.page .body svg').forEach(function(sv){
    if(sv.closest('.qr')||sv.classList.contains('qr'))return;
    var w=sv.getBoundingClientRect().width;if(w<100&&!sv.closest('.trow'))return;
    var wrap=document.createElement('span');wrap.className='drawwrap';sv.parentNode.insertBefore(wrap,sv);wrap.appendChild(sv);
    makeCanvas(wrap,'sv'+(n++),sv.getBoundingClientRect().height<120);
  });
}
(function(){var C=window.SCHOOL||{};var view=/[?&]view=1/.test(location.search);
  var KEY='ans-'+document.title,has=false;try{has=!!localStorage.getItem(KEY)}catch(e){}
  if(!C.api||(!view&&has)){schoolInit();return}
  var done=false;function go(){if(done)return;done=true;schoolInit()}
  fetch(C.api+'?action=get&kid='+encodeURIComponent(C.kid)+'&week='+encodeURIComponent(C.week)).then(function(r){return r.json()}).then(function(j){
    var a=j.answers||{},b={};for(var k in a){if(!/^(dr|sv)/.test(k))b[k]=a[k]}
    if(view){C.remote=b}else if(Object.keys(b).length){try{localStorage.setItem(KEY,JSON.stringify(b))}catch(e){}}
    go()}).catch(go);
  setTimeout(go,7000);
})();
</script>
"""

API = "https://script.google.com/macros/s/AKfycbzgvfEOWoBFQHBeHmbvklVpT-UCOSJUHCx3rcUvQVwzFDg9CfIY0UC6UlDvA9kr3ZeIaQ/exec"
WEEK = "2026-11-03"

MODAL = r"""
<div class="vmodal" id="vmodal"><div class="frame"><iframe id="vframe" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
<div class="bar"><button id="vclose">✕ Close video</button><a id="vyt" href="#" target="_blank" rel="noopener">Open in YouTube</a></div></div>
<script>
(function(){var m=document.getElementById('vmodal'),f=document.getElementById('vframe'),y=document.getElementById('vyt');
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a.vidbtn');if(!a||!a.dataset.vid)return;e.preventDefault();
  f.src='https://www.youtube-nocookie.com/embed/'+a.dataset.vid+'?autoplay=1&rel=0&modestbranding=1&playsinline=1';y.href=a.href;m.classList.add('on')});
 function close(){m.classList.remove('on');f.src='about:blank'}
 document.getElementById('vclose').addEventListener('click',close);m.addEventListener('click',function(e){if(e.target===m)close()});})();
</script>
"""

def web_html(kid, P):
    pages = [p for p in P.pages if 'class="page blank"' not in p]
    out, seen = [], set()
    for p in pages:
        m = re.search(r'<div class="d">DAY (\d)</div>', p)
        if m and m.group(1) not in seen:
            seen.add(m.group(1)); p = f'<div id="day-{m.group(1)}"></div>' + p
        out.append(p)
    nav = '<div class="nav"><a href="#top">My Week</a>' + "".join(f'<a href="#day-{n}">Day {n}</a>' for n in range(1, 6)) + '</div>'
    title = f"{kid} · School Week of Nov 3"
    return (f"<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>{esc(title)}</title><link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@400;500;600;700&display=swap'>"
            f"<style>{CSS}{WEBCSS}</style></head><body><div id='top'></div>{nav}"
            f"<div class='note'>Tap ▶ to watch a video. Tap 🔊 to hear a page read aloud. Tap an answer bubble to pick it. Tap a line to type your answer. Draw and trace right on the page with your finger. Your work saves on this tablet.</div>"
            f"{''.join(out)}<script>window.SCHOOL={{api:'{API}',kid:'{kid}',week:'{WEEK}'}};</script>{JS}{JS2}{MODAL}</body></html>")

if __name__ == "__main__":
  os.makedirs("/home/claude/web", exist_ok=True)
  for kid in ["Nevaeh", "Nylah", "Naomi", "Nariah", "Titus", "Nayeli"]:
    P = build.build_kid(kid, build.KIDS[kid])
    open(f"/home/claude/web/{kid}.html", "w").write(web_html(kid, P))
    print(kid, os.path.getsize(f"/home/claude/web/{kid}.html"))
