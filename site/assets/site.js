(function boot(){if(!(window.gsap&&window.ScrollTrigger))return setTimeout(boot,40);
gsap.registerPlugin(ScrollTrigger);
/* some embedded browsers pause requestAnimationFrame; fall back to timers so the page never freezes */
(function(){let ok=false;requestAnimationFrame(()=>ok=true);setTimeout(()=>{if(ok)return;const raf=cb=>setTimeout(()=>cb(performance.now()),16);window.requestAnimationFrame=raf;gsap.ticker.sleep();gsap.ticker.wake()},400)})();
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const desk=matchMedia('(min-width: 901px)').matches;

/* header */
const bg=$('.burger');if(bg){bg.addEventListener('click',()=>{const o=document.documentElement.classList.toggle('navopen');bg.setAttribute('aria-expanded',o)});document.addEventListener('keydown',ev=>{if(ev.key==='Escape'){document.documentElement.classList.remove('navopen');bg.setAttribute('aria-expanded','false')}})}
const hdr=$('header.top');const onS=()=>hdr&&hdr.classList.toggle('solid',scrollY>30);addEventListener('scroll',onS,{passive:true});onS();

/* in-page anchors */
$$('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const t=$(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:reduce?'auto':'smooth'})}}));

/* card hover: the page scrolls inside the frame */
function hoverScroll(root=document){$$('.card',root).forEach(c=>{const s=$('.shot',c),im=$('img',s);if(!im)return;
 c.addEventListener('mouseenter',()=>{const d=im.offsetHeight-s.offsetHeight;if(d<=0)return;gsap.to(im,{y:-d,duration:Math.max(2.5,d/300),ease:'power1.inOut',overwrite:true})});
 c.addEventListener('mouseleave',()=>gsap.to(im,{y:0,duration:1.1,ease:'power3.out',overwrite:true}))})}
hoverScroll();

/* counters */
function counters(){$$('[data-count]').forEach(b=>{const n=+b.dataset.count,o={v:0};
 ScrollTrigger.create({trigger:b,start:'top 90%',once:true,onEnter:()=>gsap.to(o,{v:n,duration:1.8,ease:'power2.out',onUpdate:()=>b.textContent=Math.round(o.v)})})})}

/* generic reveals */
function reveals(){const io=new IntersectionObserver(es=>es.forEach(en=>{if(!en.isIntersecting)return;io.unobserve(en.target);gsap.to(en.target,{y:0,opacity:1,duration:.9,ease:'power3.out',delay:(+en.target.dataset.i||0)*.08})}),{rootMargin:'0px 0px -8% 0px'});
 $$('[data-rv]').forEach(el=>{const ts=el.dataset.rv==='kids'?[...el.children]:[el];ts.forEach((t,i)=>{if(t.getBoundingClientRect().top<innerHeight*.92)return;t.dataset.i=i;gsap.set(t,{y:40,opacity:0});io.observe(t)})});}
/* hero composition */
function hero(){const comp=$('#comp');if(!comp)return;const layers=$$('.layer',comp);
 gsap.from(layers,{y:160,opacity:0,rotate:i=>[-6,4,8,-4,4][i]||0,duration:1.3,stagger:.1,ease:'expo.out'});
 const qs=layers.map(l=>({x:gsap.quickTo(l,'x',{duration:1,ease:'power3'}),y:gsap.quickTo(l,'y',{duration:1,ease:'power3'}),d:+l.dataset.d}));
 if(!reduce)addEventListener('mousemove',e=>{const nx=e.clientX/innerWidth-.5,ny=e.clientY/innerHeight-.5;qs.forEach(q=>{q.x(-nx*q.d);q.y(-ny*q.d)})});
 $$('.win',comp).forEach((w,k)=>{const im=$('img',w),vp=$('.vp',w);const go=()=>{const d=im.offsetHeight-vp.offsetHeight;if(d>0&&!reduce)gsap.to(im,{y:-d*.55,duration:20+k*6,ease:'sine.inOut',repeat:-1,yoyo:true,delay:1+k})};im.complete?go():im.onload=go});
 layers.forEach(l=>gsap.to(l,{yPercent:-(+l.dataset.d)*.9,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}}));
 gsap.to('.hero .wrap>div:first-child',{y:-80,opacity:.2,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}})}

/* marquees */
function marquees(){if(reduce)return;if($('#mq'))gsap.to('#mq',{xPercent:-50,duration:60,ease:'none',repeat:-1});
 if($('#big')){const bg=gsap.to('#big',{xPercent:-50,duration:30,ease:'none',repeat:-1});
  ScrollTrigger.create({trigger:'.foot',start:'top bottom',end:'bottom top',onUpdate:s=>{gsap.to(bg,{timeScale:1+Math.min(4,Math.abs(s.getVelocity()/400)),duration:.2,overwrite:true});gsap.to(bg,{timeScale:1,duration:1,delay:.2})}})}}

/* app story */
function story(){if(!$('#story'))return;const steps=$$('.step'),bars=$$('.story .bars b'),fl=$$('.stage .float');
 if(!desk)return;
 const tl=gsap.timeline({scrollTrigger:{trigger:'#story',start:'top top',end:'+=2400',pin:true,scrub:.6}});
 tl.from('.stage .phone',{scale:.82,rotate:-8,y:80,duration:1,ease:'power2.out'},0)
   .to(bars[0],{scaleX:1,duration:1},0).fromTo(fl[0],{opacity:0,x:-30},{opacity:1,x:0,duration:.6},.3)
   .to(steps[0],{opacity:0,y:-20,duration:.4},1.2).fromTo(steps[1],{opacity:0,y:30},{opacity:1,y:0,duration:.5},1.4)
   .to('#s2',{opacity:1,duration:.5},1.3).to('.stage .phone',{rotate:3,duration:.8},1.3).to(fl[0],{opacity:0,duration:.4},1.3)
   .to(bars[1],{scaleX:1,duration:1},1.3).fromTo(fl[1],{opacity:0,x:30},{opacity:1,x:0,duration:.6},1.6)
   .to(steps[1],{opacity:0,y:-20,duration:.4},2.5).fromTo(steps[2],{opacity:0,y:30},{opacity:1,y:0,duration:.5},2.7)
   .to('.stage .phone',{rotate:-2,scale:1.04,duration:.8},2.6).to(fl[1],{opacity:0,duration:.4},2.6)
   .to(bars[2],{scaleX:1,duration:1},2.6).fromTo(fl[2],{opacity:0,y:30},{opacity:1,y:0,duration:.6},2.9).to({},{duration:.4})}

/* process */
function process(){const p=$('.proc');if(!p)return;const items=$$('.proc>div');
 gsap.to('.proc .line',{scaleX:1,ease:'none',scrollTrigger:{trigger:p,start:'top 75%',end:'bottom 55%',scrub:true,onUpdate:s=>items.forEach((it,i)=>it.classList.toggle('on',s.progress>=i/items.length+.02))}})}

/* work filters */
function filters(){const tabs=$('[data-filter]');if(!tabs)return;const cards=$$('.gridw .card'),tally=$('#tally');
 const run=f=>{let n=0;cards.forEach(c=>{const v=f==='all'||c.dataset.c===f||c.dataset.k===f;c.hidden=!v;if(v)n++});tally.textContent=tally.dataset.tpl.replace('#',n);ScrollTrigger.refresh();
  gsap.fromTo(cards.filter(c=>!c.hidden),{opacity:0,y:24},{opacity:1,y:0,duration:.5,stagger:.04,ease:'power2.out'})};
 $$('button',tabs).forEach(b=>b.onclick=()=>{$$('button',tabs).forEach(x=>x.setAttribute('aria-pressed',x===b));run(b.dataset.f)});run('all')}

/* project page */
function project(){const ps=$('.pj-scroll');if(ps&&desk){const im=$('.vp img',ps),vp=$('.vp',ps);
  gsap.to(im,{y:()=>-(im.offsetHeight-vp.offsetHeight),ease:'none',scrollTrigger:{trigger:ps,start:'top top',end:'bottom bottom',scrub:.5,invalidateOnRefresh:true}});
  gsap.to('.pj-scroll .meter i',{scaleX:1,ease:'none',scrollTrigger:{trigger:ps,start:'top top',end:'bottom bottom',scrub:true}});
  im.addEventListener('load',()=>ScrollTrigger.refresh(),{once:true})}
 const h=$('.pj-hero .win');if(h){gsap.from(h,{y:120,opacity:0,rotateX:12,duration:1.3,ease:'expo.out',delay:.2,transformPerspective:1400});
  const im=$('img',h),vp=$('.vp',h);const go=()=>{const d=im.offsetHeight-vp.offsetHeight;if(d>0&&!reduce)gsap.to(im,{y:-Math.min(d,1400),duration:14,ease:'sine.inOut',repeat:-1,yoyo:true,delay:1.2})};im.complete?go():im.onload=go}
 $$('.crops .c').forEach((c,i)=>gsap.fromTo(c,{y:80+i*30},{y:-30-i*10,ease:'none',scrollTrigger:{trigger:'.crops',start:'top bottom',end:'bottom top',scrub:true}}));
 if($('.phead h1'))gsap.from('.phead>*',{y:40,opacity:0,duration:1,stagger:.08,ease:'power3.out',delay:.15})}

function start(){hero();marquees();story();process();filters();project();counters();reveals();
 if($('.hero h1'))gsap.from('.hero h1>span,.hero .lead,.hero .acts,.proof',{y:40,opacity:0,duration:1,stagger:.09,ease:'power4.out'});
 setTimeout(()=>ScrollTrigger.refresh(),600)}

/* lead form: posts to api/lead.php on the real server; falls back to WhatsApp where PHP is not available */
function track(n,v){try{if(window.gtag)gtag('event',n==='lead'?'generate_lead':'contact_whatsapp',{project_type:v||''});if(window.fbq)fbq('track',n==='lead'?'Lead':'Contact')}catch(e){}}
document.addEventListener('click',ev=>{const a=ev.target.closest&&ev.target.closest('a[href*="wa.me"]');if(a)track('wa')});
function leadForm(){const f=$('#leadForm');if(!f)return;const msg=$('.msg',f);
 f.addEventListener('submit',async e=>{e.preventDefault();if(f.hp.value)return;
  const d=Object.fromEntries(new FormData(f));if(!d.name||!d.phone){msg.className='msg err';msg.textContent=f.dataset.need;return}
  const btn=$('button',f);btn.disabled=true;msg.className='msg';msg.textContent=f.dataset.sending;
  d.page=location.pathname;d.lang=document.documentElement.lang;
  try{const r=await fetch(f.action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});const j=await r.json();if(!j.ok)throw 0;
   msg.className='msg ok';msg.textContent=f.dataset.ok;f.reset();track('lead',d.type)}
  catch(err){const t=`${f.dataset.wa}\n${d.name}\n${d.phone}${d.email?'\n'+d.email:''}\n${d.type||''}\n${d.details||''}`;
   msg.className='msg ok';msg.textContent=f.dataset.walink;track('lead',d.type);window.open('https://wa.me/201039253652?text='+encodeURIComponent(t),'_blank','noopener')}
  btn.disabled=false})}



/* the animated X: on every page load and on every page change */
const lo=$('#loader'),c=$('#lc'),x=c.getContext('2d'),S=520;let parts=null,anim=null;
const draw=(e,mode)=>{x.clearRect(0,0,S,S);for(const p of parts){let px,py,a;
 if(mode==='in'){px=p.x+(p.tx-p.x)*e;py=p.y+(p.ty-p.y)*e;a=.25+e*.75}else{px=p.tx+(p.ox-p.tx)*e;py=p.ty+(p.oy-p.ty)*e;a=1-e}
 x.fillStyle=`hsla(${232+p.h*36},78%,${56-(mode==='in'?e:1)*6}%,${a})`;x.fillRect(px,py,4.2,4.2)}};
const run=(dur,mode,count)=>new Promise(res=>{if(!parts){res();return}const st=performance.now();cancelAnimationFrame(anim);
 (function f(now){const k=Math.min(1,((now||performance.now())-st)/dur),e=mode==='in'?1-Math.pow(1-k,4):k*k;draw(e,mode);if(count)$('#lcount').textContent=Math.round(e*100);
  if(k<1)anim=requestAnimationFrame(f);else res()})(st)});
const ready=new Promise(res=>{const im=new Image();im.crossOrigin='anonymous';im.src=lo.dataset.logo;
 im.onload=()=>{try{const o=document.createElement('canvas');o.width=o.height=130;const ox=o.getContext('2d');ox.drawImage(im,0,0,130,130);const d=ox.getImageData(0,0,130,130).data;const tg=[];
  for(let y=0;y<130;y+=2)for(let xx=0;xx<130;xx+=2){const k=(y*130+xx)*4;if(d[k]+d[k+1]+d[k+2]>640)tg.push([xx*4,y*4])}
  parts=tg.map(t=>({tx:t[0],ty:t[1],x:Math.random()*S,y:Math.random()*S,ox:t[0]+(Math.random()-.5)*700,oy:t[1]+(Math.random()-.5)*700,h:Math.random()}))}catch(e){}res()};im.onerror=()=>res();setTimeout(res,1500)});
let seen=false;try{seen=sessionStorage.getItem('xtv-seen')==='1';sessionStorage.setItem('xtv-seen','1')}catch(e){}
$('#lcount').style.visibility=seen?'hidden':'visible';
let started=false;const go=()=>{if(started)return;started=true;start();leadForm()};
const reveal=async()=>{await ready;if(reduce){lo.remove();go();return}
 await run(seen?650:1900,'in',!seen);await new Promise(r=>setTimeout(r,seen?80:250));
 lo.classList.add('out');run(600,'out');gsap.to(lo,{opacity:0,duration:.55,delay:.15,ease:'power2.out',onComplete:()=>{lo.style.display='none'}});setTimeout(go,200)};
setTimeout(()=>{if(!started){lo.style.display='none';go()}},5000);
reveal();
addEventListener('pageshow',e=>{if(e.persisted){lo.style.display='none';lo.style.opacity=0;document.documentElement.classList.remove('leaving')}});
document.addEventListener('click',async e=>{const a=e.target.closest('a');if(!a||reduce)return;const h=a.getAttribute('href');
 if(!h||h.startsWith('#')||a.target==='_blank'||/^(https?:|mailto:|tel:)/.test(h)&&new URL(a.href).host!==location.host||e.metaKey||e.ctrlKey||e.shiftKey)return;
 e.preventDefault();document.documentElement.classList.add('leaving');lo.style.display='grid';lo.classList.remove('out');$('#lcount').style.visibility='hidden';
 gsap.fromTo(lo,{opacity:0},{opacity:1,duration:.25});await run(600,'in');location.href=a.href});
})();
