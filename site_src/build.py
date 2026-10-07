"""Static site generator for xtechverse.com.  python3 build.py  ->  writes ../site/"""
import pathlib, html, hashlib, time
from data import PROJECTS, APPS, U

OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
V = hashlib.md5(((OUT/"assets/site.js").read_bytes()+(OUT/"assets/site.css").read_bytes())).hexdigest()[:8]
WA = "https://wa.me/201039253652"
e = html.escape

T = {
 "ar": dict(dir="rtl", other="en", other_label="English", work="الأعمال", services="الخدمات", contact="تواصل", start="ابدأ مشروعك",
   home_title="X TechVerse | تصميم وبرمجة مواقع وتطبيقات", home_desc="X TechVerse استوديو برمجة من مصر، يصمم ويبرمج مواقع وتطبيقات وأنظمة لشركات في مصر والسعودية.",
   h1a="نصمم ونبرمج", h1b="مواقع وتطبيقات", h1c="لشركات في مصر والسعودية.",
   lead="استوديو برمجة يعمل على مشروعك من الفكرة حتى الإطلاق، ويستمر معك بعد التسليم.",
   wa_cta="تواصل معنا على واتساب", see_work="شاهد أعمالنا", pf1="موقع نفذناه", pf2="تطبيقات وأنظمة", pf3="دولتين",
   chip1="منشور على جوجل بلاي", chip2="مصر والسعودية", chip2s="18 موقع نفذناه",
   feat_h="مشاريع مختارة", feat_p="مواقع منشورة لعملاء حقيقيين. افتح أي مشروع لتشاهد تفاصيله والصفحة كاملة.", all_work="كل الأعمال",
   view="عرض المشروع", eg="مصر", sa="السعودية",
   aq_kind="تطبيق عقارات للأندرويد، منشور على جوجل بلاي", aq_go="تفاصيل التطبيق",
   fl1="كفر الشيخ", fl1s="عقاران في المنطقة", fl2="شقة 140م² للإيجار", fl2s="3 غرف وحمامان", fl3="تواصل عبر واتساب", fl3s="بضغطة من صفحة الوحدة",
   k1="الخطوة 1", k2="الخطوة 2", k3="الخطوة 3",
   st1h="العميل يبحث على الخريطة", st1p="فلاتر للشقق والفلل والشاليهات، بيع أو إيجار، وكل وحدة في مكانها على الخريطة.",
   st2h="يفتح صفحة الوحدة", st2p="الصور والسعر والمساحة وعدد الغرف والحمامات والمرافق.",
   st3h="ويتواصل مع المعلن بضغطة", st3p="اتصال أو واتساب أو محادثة داخل التطبيق.",
   svc_h="ماذا نقدم", svc_p="نفس الفريق يصمم ويبرمج ويتابع معك بعد الإطلاق.",
   svcs=[("site","مواقع الشركات","مواقع تعريفية بالعربية والإنجليزية، سريعة وسهلة التعديل.",["صفحات خدمات ومعرض أعمال","نماذج تواصل وطلب عروض أسعار","تهيئة لمحركات البحث"]),
         ("store","المتاجر الإلكترونية","متاجر بكتالوج وسلة وحسابات للعملاء.",["أقسام ومنتجات بلا حدود","سلة ومقارنة ومفضلة","عربي وإنجليزي"]),
         ("app","تطبيقات الموبايل","تطبيقات أندرويد وiOS من التصميم حتى النشر على المتاجر.",["تصميم الواجهات","ربط بالخرائط والإشعارات","النشر على جوجل بلاي"]),
         ("sys","أنظمة مخصصة وصيانة","لوحات تحكم وأنظمة إدارة، وصيانة للمواقع القائمة.",["أنظمة إدارة عيادات ومتاجر","تحديثات وحماية ونسخ احتياطي","تحسين سرعة المواقع"])],
   proc_h="كيف نعمل", proc_p="أربع مراحل واضحة، وتعرف في كل مرحلة ما الذي يحدث.",
   procs=[("نفهم مشروعك","اجتماع نتعرف فيه على نشاطك وجمهورك وما تحتاجه من الموقع أو التطبيق."),("نصمم","نرسم الصفحات والشاشات ونراجعها معك قبل أي برمجة."),
          ("نبرمج ونختبر","نبني المشروع ونختبره على الكمبيوتر والموبايل."),("نطلق ونتابع","ننشر المشروع ونبقى معك للتعديلات والصيانة.")],
   nums_h="بالأرقام", n1="موقع نفذناه لعملاء حقيقيين", n2="مواقع بلغتين عربي وإنجليزي", n3="تطبيقات وأنظمة", n4="دولتان: مصر والسعودية",
   inds_h="قطاعات عملنا معها",
   faq_h="أسئلة شائعة",
   faqs=[("هل تعملون مع عملاء خارج مصر؟","نعم. أكثر من نصف المواقع في معرض أعمالنا لشركات في السعودية، في الرياض وجدة والمدينة المنورة والظهران."),
         ("هل يمكن أن يكون الموقع بالعربية والإنجليزية؟","نعم، ونفذنا مواقع كثيرة باللغتين، مثل Cross Road وSistema Plastic Egypt وSoft Light."),
         ("كم يستغرق المشروع وكم يكلف؟","يختلف حسب حجم المشروع. أرسل لنا فكرتك وسنرد عليك بخطة وتكلفة ومدة واضحة.")],
   big="لنبدأ", ct_p="أخبرنا عن مشروعك في رسالة، ونرد عليك بخطة وتكلفة واضحة.", ct_wa="واتساب", ct_mail="البريد الإلكتروني", ct_fb="فيسبوك",
   foot_city="القاهرة، مصر",
   work_title="أعمالنا | X TechVerse", work_h1="أعمالنا", work_lead="مواقع وتطبيقات وأنظمة صممناها وبرمجناها لشركات في مصر والسعودية.",
   apps_h="تطبيقات وأنظمة", sites_h="المواقع", f_all="الكل", f_store="متاجر", tally="# مشروع",
   offline_note="بعض المواقع في هذه الصفحة غير متاحة حالياً على الإنترنت، فنعرضها بالصور فقط.",
   home="الرئيسية", visit="زيارة الموقع", offline="الموقع غير متاح حالياً",
   m_sector="المجال", m_city="المكان", m_type="نوع المشروع", m_langs="اللغات", m_partner="بالتعاون مع",
   tour_h="جولة في الصفحة الرئيسية", tour_p="مرّر الصفحة لتشاهد الصفحة الرئيسية للموقع كاملة كما يراها الزائر.",
   about_h="عن العميل", pages_h="صفحات الموقع", feats_h="أبرز ما في الموقع", shots_h="لقطات من الموقع", next="المشروع التالي",
   aq_title="عقاري EG | X TechVerse", how="كيف يعمل التطبيق"),
 "en": dict(dir="ltr", other="ar", other_label="العربية", work="Work", services="Services", contact="Contact", start="Start your project",
   home_title="X TechVerse | Websites and apps", home_desc="X TechVerse is a software studio from Egypt designing and building websites, apps and systems for companies in Egypt and Saudi Arabia.",
   h1a="We design and build", h1b="websites and apps", h1c="for companies in Egypt and Saudi Arabia.",
   lead="A software studio that takes your project from idea to launch, and stays with you after.",
   wa_cta="Message us on WhatsApp", see_work="See our work", pf1="websites delivered", pf2="apps and systems", pf3="countries",
   chip1="Live on Google Play", chip2="Egypt and Saudi Arabia", chip2s="18 websites delivered",
   feat_h="Selected projects", feat_p="Live websites for real clients. Open any project to see its details and the full page.", all_work="All work",
   view="View project", eg="Egypt", sa="Saudi Arabia",
   aq_kind="Real-estate app for Android, on Google Play", aq_go="App details",
   fl1="Kafr El Sheikh", fl1s="2 properties nearby", fl2="140 m² apartment for rent", fl2s="3 rooms, 2 bathrooms", fl3="Contact on WhatsApp", fl3s="One tap from the unit page",
   k1="Step 1", k2="Step 2", k3="Step 3",
   st1h="Customers search on the map", st1p="Filters for apartments, villas and chalets, for sale or rent, with every unit pinned in place.",
   st2h="They open the unit page", st2p="Photos, price, area, rooms, bathrooms and amenities.",
   st3h="And reach the agent in one tap", st3p="Call, WhatsApp or in-app chat.",
   svc_h="What we do", svc_p="The same team designs, builds and stays with you after launch.",
   svcs=[("site","Company websites","Arabic and English websites that are fast and easy to update.",["Service pages and portfolios","Contact and quote forms","Search engine setup"]),
         ("store","Online stores","Stores with catalogue, cart and customer accounts.",["Unlimited categories and products","Cart, compare and wishlist","Arabic and English"]),
         ("app","Mobile apps","Android and iOS apps, from design to store release.",["Interface design","Maps and notifications","Google Play release"]),
         ("sys","Custom systems and care","Dashboards and management systems, plus care for existing sites.",["Clinic and store management","Updates, security and backups","Speed optimisation"])],
   proc_h="How we work", proc_p="Four clear stages, so you always know what is happening.",
   procs=[("Understand","A meeting to learn about your business, your audience and what the site or app must do."),("Design","We draw the pages and screens and review them with you before any code."),
          ("Build and test","We build the project and test it on desktop and mobile."),("Launch and support","We publish it and stay with you for changes and maintenance.")],
   nums_h="In numbers", n1="websites delivered for real clients", n2="bilingual Arabic and English sites", n3="apps and systems", n4="countries: Egypt and Saudi Arabia",
   inds_h="Industries we have worked with",
   faq_h="Common questions",
   faqs=[("Do you work with clients outside Egypt?","Yes. More than half of the websites in our portfolio are for companies in Saudi Arabia, in Riyadh, Jeddah, Madinah and Dhahran."),
         ("Can the website be in Arabic and English?","Yes. Many of our sites run in both, such as Cross Road, Sistema Plastic Egypt and Soft Light."),
         ("How long does a project take and what does it cost?","It depends on the size of the project. Send us your idea and we reply with a clear plan, cost and timeline.")],
   big="Let's build it", ct_p="Tell us about your project in one message, and we reply with a clear plan and cost.", ct_wa="WhatsApp", ct_mail="Email", ct_fb="Facebook",
   foot_city="Cairo, Egypt",
   work_title="Work | X TechVerse", work_h1="Our work", work_lead="Websites, apps and systems we designed and built for companies in Egypt and Saudi Arabia.",
   apps_h="Apps and systems", sites_h="Websites", f_all="All", f_store="Stores", tally="# projects",
   offline_note="Some websites on this page are not online at the moment, so we show them as screenshots only.",
   home="Home", visit="Visit website", offline="Website currently offline",
   m_sector="Industry", m_city="Location", m_type="Project type", m_langs="Languages", m_partner="In partnership with",
   tour_h="A tour of the home page", tour_p="Scroll to see the site's whole home page as a visitor sees it.",
   about_h="About the client", pages_h="Site pages", feats_h="Highlights", shots_h="Screens from the site", next="Next project",
   aq_title="Aqary EG | X TechVerse", how="How the app works"),
}

ICON = dict(
 wa='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.2.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
 arrow='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 ext='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
 site='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8"/></svg>',
 store='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2l2.4 11h11L21 7H6.2"/><circle cx="9" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/></svg>',
 app='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>',
 sys='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
 pin='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 home='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
 check='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
 globe='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
)

def host(u): return u.replace("https://", "").rstrip("/") if u else ""

def win(p, L, cls="", lazy=True):
    return (f'<div class="win {cls}"><div class="bar"><i></i><i></i><i></i><u>{e(host(p["url"]) or p["name"]["en"])}</u></div>'
            f'<div class="vp"><img src="{U + p["img"]}" alt="{e(p["name"][L])}"{' loading="lazy"' if lazy else ''}></div></div>')

def page(L, depth, title, desc, body, path, current=""):
    t = T[L]; r = "../" * depth
    alt = ("../" * depth + "en/" + path) if L == "ar" else ("../" * (depth + 1) + path)
    root = r  # site root for this language
    assets = ("../" * (depth + (1 if L == "en" else 0))) + "assets/"
    vendor = ("../" * (depth + (1 if L == "en" else 0))) + "vendor/"
    ar = lambda s: s
    nav = (f'<header class="top"><div class="wrap"><a class="brand" href="{root}index.html"><img src="{assets}logo.png" alt="">X TechVerse</a>'
           f'<nav class="menu" aria-label="Main"><a href="{root}work/index.html"{" aria-current=page" if current=="work" else ""}>{t["work"]}</a>'
           f'<a href="{root}index.html#services">{t["services"]}</a><a href="#contact">{t["contact"]}</a>'
           f'<a class="lang" href="{alt}" hreflang="{t["other"]}">{t["other_label"]}</a>'
           f'<a class="btn pri" href="#contact">{t["start"]}</a></nav></div></header>')
    contact = (f'<section class="contact" id="contact"><div class="big" aria-hidden="true"><div class="t" id="big">{("<span>"+e(t["big"])+"</span>")*8}</div></div>'
               f'<div class="wrap"><p>{t["ct_p"]}</p><div class="rows">'
               f'<a href="{WA}" target="_blank" rel="noopener"><small>{t["ct_wa"]}</small><span>+20 10 3925 3652</span></a>'
               f'<a href="mailto:info@xtechverse.com"><small>{t["ct_mail"]}</small><span>info@xtechverse.com</span></a>'
               f'<a href="https://www.facebook.com/xtechverse1" target="_blank" rel="noopener"><small>{t["ct_fb"]}</small><span>xtechverse1</span></a>'
               f'</div></div></section><footer class="foot"><div class="wrap"><span>© 2026 X TechVerse</span><span>{t["foot_city"]}</span></div></footer>')
    return f"""<!doctype html>
<html lang="{L}" dir="{t['dir']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="alternate" hreflang="{t['other']}" href="{alt}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}site.css?v={V}">
<link rel="icon" href="{assets}logo.png">
</head>
<body>
{body.replace('{ASSETS}', assets)}
{nav}
{contact}
<script src="{vendor}gsap.min.js"></script><script src="{vendor}ScrollTrigger.min.js"></script><script src="{assets}site.js?v={V}"></script>
</body></html>"""

def place(p, L): return T[L][p["country"]]

def card(p, L, rel, cls=""):
    href = f'{rel}work/{p["slug"]}/index.html'
    return (f'<a class="card {cls}" href="{href}" data-c="{p["country"]}" data-k="{p["kind"]}"><div class="shot"><img src="{U + p["img"]}" alt="{e(p["name"][L])}" loading="lazy">'
            f'<span class="open">{T[L]["view"]}</span></div><div class="info"><div><h3>{e(p["name"][L])}</h3><div class="sector">{e(p["sector"][L])}</div></div>'
            f'<span class="place">{e(p["city"][L])}</span></div></a>')

# ---------------------------------------------------------------- home
def home(L):
    t = T[L]; rel = ""
    live = [p for p in PROJECTS if p["live"]]
    feat = [p for p in PROJECTS if p.get("featured")]
    bilingual = sum(1 for p in PROJECTS if p.get("langs") and ("و" in p["langs"]["ar"]))
    inds = sorted({p["sector"][L] for p in PROJECTS if p["sector"][L] not in ("موقع شركة", "Company website")})
    cross, ahram = PROJECTS[1], PROJECTS[0]
    comp = (f'<div class="layer c-back" data-d="14">{win(cross, L, lazy=False)}</div><div class="layer c-mid" data-d="26">{win(ahram, L, lazy=False)}</div>'
            f'<div class="layer c-phone" data-d="44"><div class="phone"><div class="scr"><img src="{{ASSETS}}aqary_map.png" alt=""></div></div></div>'
            f'<div class="layer c-chip1 chip" data-d="60"><span class="ic">{ICON["check"]}</span><span>{t["chip1"]}<small>{APPS[0]["name"][L]}</small></span></div>'
            f'<div class="layer c-chip2 chip" data-d="52"><span class="ic">{ICON["globe"]}</span><span>{t["chip2"]}<small>{t["chip2s"]}</small></span></div>')
    svcs = "".join(f'<div><span class="ic">{ICON[k]}</span><h3>{h}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for k, h, d, li in t["svcs"])
    procs = "".join(f'<div><span class="dot">{i+1}</span><h3>{h}</h3><p>{d}</p></div>' for i, (h, d) in enumerate(t["procs"]))
    faqs = "".join(f'<details><summary>{q}<i>+</i></summary><p>{a}</p></details>' for q, a in t["faqs"])
    others = "".join(f'<div class="other"><h4>{a["name"][L]}</h4><span class="st">{a["status"][L]}</span><p>{a["summary"][L]}</p></div>' for a in APPS[1:])
    names = "".join(f"<span>{e(p['name']['en'])}</span>" for p in PROJECTS) * 2
    body = f"""<div id="loader" data-logo="{{ASSETS}}logo.png" aria-hidden="true"><canvas id="lc" width="520" height="520"></canvas><div class="count" id="lcount">0</div></div>
<main id="top">
<section class="hero"><div class="wrap"><div>
 <h1><span>{t['h1a']}</span> <span class="grad">{t['h1b']}</span> <span>{t['h1c']}</span></h1>
 <p class="lead">{t['lead']}</p>
 <div class="acts"><a class="btn pri" href="{WA}" target="_blank" rel="noopener">{ICON['wa']}<span>{t['wa_cta']}</span></a><a class="btn alt" href="work/index.html">{t['see_work']}</a></div>
 <div class="proof"><div><b class="grad" data-count="{len(PROJECTS)}">0</b><span>{t['pf1']}</span></div><div><b class="grad" data-count="{len(APPS)}">0</b><span>{t['pf2']}</span></div><div><b class="grad" data-count="2">0</b><span>{t['pf3']}</span></div></div>
</div><div class="comp" id="comp" aria-hidden="true">{comp}</div></div></section>
<div class="mq" aria-hidden="true"><div class="t" id="mq">{names}</div></div>

<section class="wrap sec" id="featured">
 <div class="sh" data-rv="kids"><h2>{t['feat_h']}</h2><p>{t['feat_p']}</p></div>
 <div class="bento">{''.join(card(p, L, rel) for p in feat)}</div>
 <div class="more-row"><a class="btn alt" href="work/index.html">{t['all_work']} ({len(PROJECTS) + len(APPS)})</a></div>
</section>

<section class="apps" id="apps">
 <div class="wrap story" id="story">
  <div><div class="name grad">{APPS[0]['name'][L]}</div><div class="kind">{t['aq_kind']}</div><div class="bars"><i><b></b></i><i><b></b></i><i><b></b></i></div>
   <a class="arrowlink go" href="work/aqary-eg/index.html">{t['aq_go']}{ICON['arrow']}</a></div>
  <div class="stage"><div class="phone"><div class="scr"><img id="s1" src="{{ASSETS}}aqary_map.png" alt=""><img id="s2" src="{{ASSETS}}aqary_detail.png" alt="" style="opacity:0"></div></div>
   <div class="float f1 chip"><span class="ic">{ICON['pin']}</span><span>{t['fl1']}<small>{t['fl1s']}</small></span></div>
   <div class="float f2 chip"><span class="ic">{ICON['home']}</span><span>{t['fl2']}<small>{t['fl2s']}</small></span></div>
   <div class="float f3 chip"><span class="ic">{ICON['wa']}</span><span>{t['fl3']}<small>{t['fl3s']}</small></span></div></div>
  <div class="steps">
   <div class="step"><small>{t['k1']}</small><h3>{t['st1h']}</h3><p>{t['st1p']}</p></div>
   <div class="step"><small>{t['k2']}</small><h3>{t['st2h']}</h3><p>{t['st2p']}</p></div>
   <div class="step"><small>{t['k3']}</small><h3>{t['st3h']}</h3><p>{t['st3p']}</p></div></div>
 </div>
 <div class="wrap others" data-rv="kids">{others}</div>
</section>

<section class="wrap sec" id="services"><div class="sh" data-rv="kids"><h2>{t['svc_h']}</h2><p>{t['svc_p']}</p></div><div class="svc" data-rv="kids">{svcs}</div></section>

<section class="band"><div class="wrap sec">
 <div class="sh" data-rv="kids"><h2>{t['proc_h']}</h2><p>{t['proc_p']}</p></div>
 <div class="proc"><span class="line"></span>{procs}</div>
</div></section>

<section class="wrap sec">
 <div class="sh" data-rv="kids"><h2>{t['nums_h']}</h2></div>
 <div class="nums"><div><b class="grad" data-count="{len(PROJECTS)}">0</b><span>{t['n1']}</span></div><div><b class="grad" data-count="{bilingual}">0</b><span>{t['n2']}</span></div>
  <div><b class="grad" data-count="{len(APPS)}">0</b><span>{t['n3']}</span></div><div><b class="grad" data-count="2">0</b><span>{t['n4']}</span></div></div>
 <h3 class="inds-h">{t['inds_h']}</h3><div class="inds" data-rv="kids">{''.join(f'<span>{e(i)}</span>' for i in inds)}</div>
</section>

<section class="band"><div class="wrap sec"><div class="sh" data-rv="kids"><h2>{t['faq_h']}</h2></div><div class="faq">{faqs}</div></div></section>
</main>"""
    return page(L, 0, t["home_title"], t["home_desc"], body, "index.html")

# ---------------------------------------------------------------- work
def work(L):
    t = T[L]; rel = "../"
    apps = "".join(
        (f'<a class="appc" href="aqary-eg/index.html">' if a["slug"] == "aqary-eg" else '<div class="appc">')
        + f'<div class="top"><h3>{a["name"][L]}</h3><span class="st">{a["status"][L]}</span></div><div class="sec2">{a["sector"][L]}</div><p>{a["summary"][L]}</p>'
        + ("</a>" if a["slug"] == "aqary-eg" else "</div>") for a in APPS)
    ordered = [p for p in PROJECTS if p["live"]] + [p for p in PROJECTS if not p["live"]]
    cards = "".join(card(p, L, rel) for p in ordered)
    body = f"""<main>
<section class="wrap phead"><div class="crumb"><a href="../index.html">{t['home']}</a><span>/</span><span>{t['work']}</span></div><h1>{t['work_h1']}</h1><p class="lead">{t['work_lead']}</p></section>
<section class="wrap"><div class="sh"><h2>{t['apps_h']}</h2></div><div class="approw" data-rv="kids">{apps}</div></section>
<section class="wrap" style="padding-bottom:clamp(90px,11vw,160px)">
 <div class="sh" style="margin-bottom:24px"><h2>{t['sites_h']}</h2></div>
 <div class="tools"><div class="tabs" data-filter role="group"><button aria-pressed="true" data-f="all">{t['f_all']}</button><button aria-pressed="false" data-f="eg">{t['eg']}</button><button aria-pressed="false" data-f="sa">{t['sa']}</button><button aria-pressed="false" data-f="store">{t['f_store']}</button></div>
 <div class="tally" id="tally" data-tpl="{t['tally']}"></div></div>
 <div class="gridw">{cards}</div>
 <p class="note">{t['offline_note']}</p>
</section></main>"""
    return page(L, 1, t["work_title"], t["work_lead"], body, "work/index.html", current="work")

# ---------------------------------------------------------------- project
def project(L, i):
    t = T[L]; p = PROJECTS[i]; nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    rel = "../../"
    meta = [(t["m_sector"], p["sector"][L]), (t["m_city"], p["city"][L]), (t["m_type"], p["type"][L])]
    if p.get("langs"): meta.append((t["m_langs"], p["langs"][L]))
    if p.get("partner"): meta.append((t["m_partner"], p["partner"]))
    dl = "".join(f"<dt>{a}</dt><dd>{e(b)}</dd>" for a, b in meta)
    acts = (f'<a class="btn pri" href="{p["url"]}" target="_blank" rel="noopener">{t["visit"]}{ICON["ext"]}</a>' if p["live"] and p["url"]
            else f'<span class="offline">{t["offline"]}</span>')
    acts += f'<a class="btn alt" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}<span>{t["start"]}</span></a>'
    body_parts = []
    if p.get("about"):
        cols = ""
        if p.get("pages"): cols += f'<div><h3>{t["pages_h"]}</h3><div class="pages">{"".join(f"<span>{e(x)}</span>" for x in p["pages"][L])}</div></div>'
        if p.get("features"): cols += f'<div><h3>{t["feats_h"]}</h3><ul class="feats">{"".join(f"<li><i>✓</i><span>{e(x)}</span></li>" for x in p["features"][L])}</ul></div>'
        body_parts.append(f'<section class="wrap sec" style="padding-bottom:0"><div class="pj-body"><h2>{t["about_h"]}</h2><div><p class="txt">{e(p["about"][L])}</p><div class="pj-cols" data-rv="kids">{cols}</div></div></div></section>')
    img = U + p["img"]
    crops = "".join(f'<div class="c"><img src="{img}" alt="" loading="lazy" style="object-position:50% {pos}%"></div>' for pos in (18, 45, 75))
    body = f"""<main>
<section class="wrap phead">
 <div class="pj-head"><div><div class="crumb"><a href="{rel}index.html">{t['home']}</a><span>/</span><a href="../index.html">{t['work']}</a><span>/</span><span>{e(p['name'][L])}</span></div>
  <h1>{e(p['name'][L])}</h1><p class="lead">{e(p['summary'][L])}</p><div class="pj-acts">{acts}</div></div>
  <dl class="pj-meta">{dl}</dl></div>
 <div class="pj-hero">{win(p, L, lazy=False)}</div>
</section>
{''.join(body_parts)}
<section class="wrap sec"><div class="pj-scroll"><div class="pin"><div><h2>{t['tour_h']}</h2><p>{t['tour_p']}</p><div class="meter"><i></i></div></div>{win(p, L)}</div></div></section>
<section class="wrap" style="padding-bottom:clamp(110px,12vw,170px)"><div class="sh"><h2>{t['shots_h']}</h2></div><div class="crops">{crops}</div></section>
<section class="wrap"><a class="next" href="../{nxt['slug']}/index.html"><div><small>{t['next']}</small><h2>{e(nxt['name'][L])}</h2></div><div class="thumb"><img src="{U + nxt['img']}" alt="" loading="lazy"></div></a></section>
</main>"""
    return page(L, 2, f'{p["name"][L]} | X TechVerse', p["summary"][L], body, f'work/{p["slug"]}/index.html', current="work")

def aqary(L):
    t = T[L]; a = APPS[0]; rel = "../../"
    meta = "".join(f"<dt>{x}</dt><dd>{y}</dd>" for x, y in [(t["m_sector"], a["sector"][L]), (t["m_type"], "Android"), (t["m_city"], T[L]["eg"])])
    steps = "".join(f'<div><span class="dot">{k+1}</span><h3>{t[h]}</h3><p>{t[d]}</p></div>' for k, (h, d) in enumerate([("st1h", "st1p"), ("st2h", "st2p"), ("st3h", "st3p")]))
    body = f"""<main>
<section class="wrap phead"><div class="pj-head"><div><div class="crumb"><a href="{rel}index.html">{t['home']}</a><span>/</span><a href="../index.html">{t['work']}</a><span>/</span><span>{a['name'][L]}</span></div>
 <h1 class="grad">{a['name'][L]}</h1><p class="lead">{a['summary'][L]}</p>
 <div class="pj-acts"><a class="btn pri" href="{a['url']}" target="_blank" rel="noopener">Google Play{ICON['ext']}</a><a class="btn alt" href="{WA}" target="_blank" rel="noopener">{ICON['wa']}<span>{t['start']}</span></a></div></div>
 <dl class="pj-meta">{meta}</dl></div></section>
<section class="wrap"><div class="crops" style="grid-template-columns:repeat(2,minmax(0,320px));justify-content:center">
 <div class="c" style="aspect-ratio:244/498;border-radius:34px;border:9px solid #14161f"><img src="{{ASSETS}}aqary_map.png" alt=""></div>
 <div class="c" style="aspect-ratio:244/498;border-radius:34px;border:9px solid #14161f"><img src="{{ASSETS}}aqary_detail.png" alt=""></div></div></section>
<section class="band" style="margin-top:clamp(110px,12vw,170px)"><div class="wrap sec"><div class="sh"><h2>{t['how']}</h2></div><div class="proc"><span class="line"></span>{steps}</div></div></section>
</main>"""
    return page(L, 2, t["aq_title"], a["summary"][L], body, "work/aqary-eg/index.html", current="work")

def write(path, txt):
    f = OUT / path; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(txt, encoding="utf-8")

for L in ("ar", "en"):
    pre = "" if L == "ar" else "en/"
    write(pre + "index.html", home(L))
    write(pre + "work/index.html", work(L))
    for i, p in enumerate(PROJECTS):
        write(pre + f'work/{p["slug"]}/index.html', project(L, i))
    write(pre + "work/aqary-eg/index.html", aqary(L))
print("built", len(PROJECTS) * 2 + 6, "pages")
