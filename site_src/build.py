"""Static site generator for xtechverse.com.  python3 build.py  ->  writes ../site/"""
import pathlib, html, hashlib, time
from data import PROJECTS, APPS, U
from services import SERVICES
import json

OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
V = hashlib.md5(((OUT/"assets/site.js").read_bytes()+(OUT/"assets/site.css").read_bytes())).hexdigest()[:8]
WA = "https://wa.me/201039253652"
BASE = "https://xtechverse.com/"
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
   aq_title="عقاري EG | X TechVerse", how="كيف يعمل التطبيق",
   f_h="ابدأ مشروعك معنا", f_name="الاسم", f_phone="رقم الموبايل أو واتساب", f_email="البريد الإلكتروني (اختياري)", f_type="نوع المشروع",
   f_types=["موقع شركة","متجر إلكتروني","تطبيق موبايل","نظام مخصص","صيانة أو تطوير"], f_budget="الميزانية التقريبية (اختياري)", f_choose="اختر",
   f_budgets=["أقل من 15,000 جنيه","15,000 - 40,000 جنيه","40,000 - 100,000 جنيه","أكثر من 100,000 جنيه","لم أحدد بعد"],
   f_details="تفاصيل المشروع", f_details_ph="اكتب فكرتك أو المشكلة التي تريد حلها", f_send="أرسل الطلب",
   f_need="من فضلك اكتب الاسم ورقم الموبايل.", f_sending="جارٍ الإرسال...", f_ok="وصلنا طلبك، وسنتواصل معك قريباً.",
   f_wa="طلب مشروع جديد من الموقع:", f_walink="فتحنا لك واتساب برسالة جاهزة، اضغط إرسال."),
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
   aq_title="Aqary EG | X TechVerse", how="How the app works",
   f_h="Start your project", f_name="Name", f_phone="Mobile or WhatsApp", f_email="Email (optional)", f_type="Project type",
   f_types=["Company website","Online store","Mobile app","Custom system","Maintenance"], f_budget="Approximate budget (optional)", f_choose="Choose",
   f_budgets=["Under 15,000 EGP","15,000 - 40,000 EGP","40,000 - 100,000 EGP","Over 100,000 EGP","Not decided yet"],
   f_details="Project details", f_details_ph="Describe your idea or the problem you want solved", f_send="Send request",
   f_need="Please enter your name and mobile number.", f_sending="Sending...", f_ok="We received your request and will contact you soon.",
   f_wa="New project request from the website:", f_walink="We opened WhatsApp with a ready message, press send."),
}

T["ar"].update(svcs_title="خدماتنا | تصميم مواقع ومتاجر وتطبيقات وأنظمة | X TechVerse", svcs_h1="خدماتنا",
  svcs_lead="نصمم ونبرمج المواقع والمتاجر والتطبيقات والأنظمة لشركات في مصر والسعودية، ونتابع معك بعد الإطلاق.",
  svc_more="تفاصيل الخدمة", incl_h="ماذا يشمل", who_h="لمن هذه الخدمة", rel_h="من أعمالنا في هذه الخدمة", svc_faq="أسئلة عن الخدمة",
  other_svcs="خدمات أخرى", cta_h="جاهز تبدأ؟", cta_p="أرسل لنا فكرتك ونرد عليك بخطة وتكلفة ومدة واضحة.", cta_btn="ابدأ مشروعك",
  ct_title="تواصل معنا | X TechVerse", ct_h1="تواصل معنا", ct_lead="اكتب لنا عن مشروعك من النموذج، أو تواصل معنا مباشرة على واتساب أو البريد الإلكتروني.",
  ct_direct="تواصل مباشر", ct_where="مكاننا", ct_where_v="القاهرة، مصر. نعمل مع عملاء في مصر والسعودية.", ct_after_h="ماذا يحدث بعد إرسال الطلب؟",
  ct_after=[("نقرأ طلبك","نراجع فكرتك ونوع المشروع الذي اخترته."),("نتواصل معك","نتصل بك أو نرسل لك على واتساب لنفهم التفاصيل."),("نرسل لك خطة","خطة واضحة بالمراحل والتكلفة والمدة.")],
  start_h="عندك مشروع؟ احكيلنا عنه", start_p="املأ النموذج في دقيقة، ونرد عليك بخطة وتكلفة واضحة.",
  start_pts=["نرد على كل طلب","خطة مكتوبة بالمراحل والتكلفة","بالعربية أو الإنجليزية"],
  f_pages="الصفحات", f_svcs="الخدمات", f_contact="التواصل", f_tag="استوديو برمجة من القاهرة يصمم ويبرمج المواقع والتطبيقات والأنظمة لشركات في مصر والسعودية.")
T["en"].update(svcs_title="Services | Websites, stores, apps and systems | X TechVerse", svcs_h1="Our services",
  svcs_lead="We design and build websites, online stores, apps and systems for companies in Egypt and Saudi Arabia, and stay with you after launch.",
  svc_more="Service details", incl_h="What's included", who_h="Who it's for", rel_h="Our work in this service", svc_faq="Questions about this service",
  other_svcs="Other services", cta_h="Ready to start?", cta_p="Send us your idea and we reply with a clear plan, cost and timeline.", cta_btn="Start your project",
  ct_title="Contact | X TechVerse", ct_h1="Contact us", ct_lead="Tell us about your project using the form, or reach us directly on WhatsApp or email.",
  ct_direct="Direct contact", ct_where="Where we are", ct_where_v="Cairo, Egypt. We work with clients in Egypt and Saudi Arabia.", ct_after_h="What happens after you send a request?",
  ct_after=[("We read it","We review your idea and the project type you picked."),("We get in touch","We call or message you on WhatsApp to understand the details."),("We send a plan","A clear plan with stages, cost and timeline.")],
  start_h="Have a project? Tell us about it", start_p="Fill in the form in a minute and we reply with a clear plan and cost.",
  start_pts=["We answer every request","A written plan with stages and cost","In Arabic or English"],
  f_pages="Pages", f_svcs="Services", f_contact="Contact", f_tag="A software studio in Cairo designing and building websites, apps and systems for companies in Egypt and Saudi Arabia.")

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

def lead_form(L, api):
    t = T[L]
    types = "".join(f'<label><input type="radio" name="type" value="{v}"><span>{v}</span></label>' for v in t["f_types"])
    return (f'<form class="lead-form" id="leadForm" action="{api}" method="post" novalidate data-need="{t["f_need"]}" data-sending="{t["f_sending"]}" data-ok="{t["f_ok"]}" data-wa="{t["f_wa"]}" data-walink="{t["f_walink"]}">'
            f'<label>{t["f_name"]}<input name="name" autocomplete="name" required></label>'
            f'<label>{t["f_phone"]}<input name="phone" type="tel" autocomplete="tel" dir="ltr" required></label>'
            f'<label class="full">{t["f_email"]}<input name="email" type="email" autocomplete="email" dir="ltr"></label>'
            f'<div class="full"><span class="lbl">{t["f_type"]}</span><div class="types">{types}</div></div>'
            f'<label class="full">{t["f_budget"]}<select name="budget"><option value="">{t["f_choose"]}</option>{"".join(f"<option>{b}</option>" for b in t["f_budgets"])}</select></label>'
            f'<label class="full">{t["f_details"]}<textarea name="details" placeholder="{t["f_details_ph"]}"></textarea></label>'
            f'<input class="hp" name="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
            f'<button class="btn pri" type="submit">{t["f_send"]}</button><p class="msg" role="status"></p></form>')

def org_schema(L):
    return {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "X TechVerse", "url": BASE,
            "logo": BASE + "assets/logo.png", "email": "info@xtechverse.com", "telephone": "+201039253652",
            "address": {"@type": "PostalAddress", "addressLocality": "Cairo", "addressCountry": "EG"},
            "areaServed": ["EG", "SA"], "sameAs": ["https://www.facebook.com/xtechverse1"],
            "description": T[L]["f_tag"], "knowsLanguage": ["ar", "en"]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def page(L, depth, title, desc, body, path, current="", schema=()):
    t = T[L]; r = "../" * depth
    alt = ("../" * depth + "en/" + path) if L == "ar" else ("../" * (depth + 1) + path)
    root = r
    up = "../" * (depth + (1 if L == "en" else 0))
    assets, vendor = up + "assets/", up + "vendor/"
    canon = BASE + ("" if L == "ar" else "en/") + path.replace("index.html", "")
    canon_alt = BASE + ("en/" if L == "ar" else "") + path.replace("index.html", "")
    ar_url, en_url = (canon, canon_alt) if L == "ar" else (canon_alt, canon)
    sw = (f'<span class="on">AR</span><a href="{alt}" hreflang="en" lang="en">EN</a>' if L == "ar"
          else f'<a href="{alt}" hreflang="ar" lang="ar">AR</a><span class="on">EN</span>')
    cur = lambda k: ' aria-current="page"' if current == k else ""
    nav = (f'<header class="top"><div class="wrap"><a class="brand" href="{root}index.html"><img src="{assets}logo.png" alt="">X TechVerse</a>'
           f'<nav class="menu" aria-label="Main"><a href="{root}index.html"{cur("home")}>{t["home"]}</a>'
           f'<a href="{root}work/index.html"{cur("work")}>{t["work"]}</a>'
           f'<a href="{root}services/index.html"{cur("services")}>{t["services"]}</a>'
           f'<a href="{root}contact/index.html"{cur("contact")}>{t["contact"]}</a>'
           f'<a class="btn pri" href="{root}contact/index.html">{t["start"]}</a>'
           f'<div class="langsw" role="group" aria-label="Language">{ICON["globe"]}{sw}</div></nav></div></header>')
    svc_links = "".join(f'<a href="{root}services/{s["slug"]}/index.html">{s[L]["name"]}</a>' for s in SERVICES)
    footer = (f'<footer class="foot" id="contact"><div class="big" aria-hidden="true"><div class="t" id="big">{("<span>"+e(t["big"])+"</span>")*8}</div></div>'
              f'<div class="wrap fcols"><div class="fbrand"><a class="brand" href="{root}index.html"><img src="{assets}logo.png" alt="">X TechVerse</a><p>{t["f_tag"]}</p>'
              f'<a class="btn pri" href="{root}contact/index.html">{t["start"]}</a></div>'
              f'<nav><h4>{t["f_pages"]}</h4><a href="{root}index.html">{t["home"]}</a><a href="{root}work/index.html">{t["work"]}</a><a href="{root}services/index.html">{t["services"]}</a><a href="{root}contact/index.html">{t["contact"]}</a></nav>'
              f'<nav><h4>{t["f_svcs"]}</h4>{svc_links}</nav>'
              f'<nav><h4>{t["f_contact"]}</h4><a href="{WA}" target="_blank" rel="noopener" dir="ltr">+20 10 3925 3652</a><a href="mailto:info@xtechverse.com">info@xtechverse.com</a>'
              f'<a href="https://www.facebook.com/xtechverse1" target="_blank" rel="noopener">Facebook</a><span>{t["foot_city"]}</span></nav></div>'
              f'<div class="wrap fbot"><span>© 2026 X TechVerse</span><span dir="ltr">xtechverse.com</span></div></footer>')
    loader = f'<div id="loader" data-logo="{assets}logo.png" aria-hidden="true"><canvas id="lc" width="520" height="520"></canvas><div class="count" id="lcount">0</div></div>'
    schemas = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (org_schema(L),) + tuple(schema))
    return f"""<!doctype html>
<html lang="{L}" dir="{t['dir']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="ar" href="{ar_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="x-default" href="{ar_url}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}assets/logo.png"><meta property="og:locale" content="{'ar_EG' if L=='ar' else 'en_US'}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}site.css?v={V}">
<link rel="icon" href="{assets}logo.png">
{schemas}
</head>
<body>
{loader}
{body.replace('{ASSETS}', assets).replace('{API}', up + 'api/lead.php')}
{nav}
{footer}
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
    svcs = "".join(f'<a href="services/{sv["slug"]}/index.html"><span class="ic">{ICON[k]}</span><h3>{h}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul><span class="arrowlink">{t["svc_more"]}{ICON["arrow"]}</span></a>' for sv, (k, h, d, li) in zip(SERVICES, t["svcs"]))
    procs = "".join(f'<div><span class="dot">{i+1}</span><h3>{h}</h3><p>{d}</p></div>' for i, (h, d) in enumerate(t["procs"]))
    faqs = "".join(f'<details><summary>{q}<i>+</i></summary><p>{a}</p></details>' for q, a in t["faqs"])
    others = "".join(f'<div class="other"><h4>{a["name"][L]}</h4><span class="st">{a["status"][L]}</span><p>{a["summary"][L]}</p></div>' for a in APPS[1:])
    names = "".join(f"<span>{e(p['name']['en'])}</span>" for p in PROJECTS) * 2
    body = f"""<main id="top">
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

<section class="start" id="start"><div class="wrap"><div class="start-box">
 <div class="start-txt"><h2>{t['start_h']}</h2><p>{t['start_p']}</p><ul>{''.join(f'<li>{ICON["check"]}<span>{x}</span></li>' for x in t['start_pts'])}</ul>
  <a class="wa-direct" href="{WA}" target="_blank" rel="noopener">{ICON['wa']}<span dir="ltr">+20 10 3925 3652</span></a></div>
 {lead_form(L, '{API}')}
</div></div></section>

<section class="wrap sec"><div class="sh" data-rv="kids"><h2>{t['faq_h']}</h2></div><div class="faq">{faqs}</div></section>
</main>"""
    return page(L, 0, t["home_title"], t["home_desc"], body, "index.html", current="home", schema=(faq_schema(t["faqs"]),))

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
            else "")
    acts += f'<a class="btn {"alt" if acts else "pri"}" href="{rel}contact/index.html">{t["start"]}</a>'
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


# ---------------------------------------------------------------- services
def cta_band(L, rel):
    t = T[L]
    return (f'<section class="wrap" style="padding-bottom:clamp(90px,11vw,150px)"><div class="cta-band"><div><h2>{t["cta_h"]}</h2><p>{t["cta_p"]}</p></div>'
            f'<div class="acts"><a class="btn pri" href="{rel}contact/index.html">{t["cta_btn"]}</a><a class="btn alt" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}<span>{t["ct_wa"]}</span></a></div></div></section>')

def services_index(L):
    t = T[L]; rel = "../"
    cards = "".join(f'<a class="svc-big" href="{s["slug"]}/index.html"><span class="ic">{ICON[s["icon"]]}</span><h2>{s[L]["name"]}</h2><p>{s[L]["lead"]}</p>'
                    f'<ul>{"".join(f"<li>{h}</li>" for h, _ in s[L]["incl"][:4])}</ul><span class="arrowlink">{t["svc_more"]}{ICON["arrow"]}</span></a>' for s in SERVICES)
    procs = "".join(f'<div><span class="dot">{i+1}</span><h3>{h}</h3><p>{d}</p></div>' for i, (h, d) in enumerate(t["procs"]))
    body = f"""<main>
<section class="wrap phead"><div class="crumb"><a href="../index.html">{t['home']}</a><span>/</span><span>{t['services']}</span></div><h1>{t['svcs_h1']}</h1><p class="lead">{t['svcs_lead']}</p></section>
<section class="wrap"><div class="svc-grid" data-rv="kids">{cards}</div></section>
<section class="band" style="margin-top:clamp(90px,11vw,150px)"><div class="wrap sec"><div class="sh"><h2>{t['proc_h']}</h2><p>{t['proc_p']}</p></div><div class="proc"><span class="line"></span>{procs}</div></div></section>
<div style="height:clamp(90px,11vw,150px)"></div>{cta_band(L, rel)}
</main>"""
    sch = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": s[L]["name"], "url": BASE + ("" if L == "ar" else "en/") + f'services/{s["slug"]}/'} for i, s in enumerate(SERVICES)]}
    return page(L, 1, t["svcs_title"], t["svcs_lead"], body, "services/index.html", current="services", schema=(sch,))

def service_page(L, s):
    t = T[L]; d = s[L]; rel = "../../"
    incl = "".join(f'<div><span class="ck">{ICON["check"]}</span><h3>{h}</h3><p>{x}</p></div>' for h, x in d["incl"])
    rel_cards = "".join(card(next(p for p in PROJECTS if p["slug"] == sl), L, rel) for sl in s["related"])
    if s.get("apps"):
        rel_cards += "".join((f'<a class="appc" href="{rel}work/aqary-eg/index.html">' if a["slug"] == "aqary-eg" else '<div class="appc">')
            + f'<div class="top"><h3>{a["name"][L]}</h3><span class="st">{a["status"][L]}</span></div><div class="sec2">{a["sector"][L]}</div><p>{a["summary"][L]}</p>'
            + ("</a>" if a["slug"] == "aqary-eg" else "</div>") for a in APPS)
    faqs = "".join(f'<details><summary>{q}<i>+</i></summary><p>{a}</p></details>' for q, a in d["faqs"])
    others = "".join(f'<a href="../{o["slug"]}/index.html"><span class="ic">{ICON[o["icon"]]}</span><span>{o[L]["name"]}</span>{ICON["arrow"]}</a>' for o in SERVICES if o is not s)
    body = f"""<main>
<section class="wrap phead sv-head"><div class="crumb"><a href="{rel}index.html">{t['home']}</a><span>/</span><a href="../index.html">{t['services']}</a><span>/</span><span>{d['name']}</span></div>
 <div class="sv-top"><div><span class="sv-ic">{ICON[s['icon']]}</span><h1>{d['h1']}</h1><p class="lead">{d['lead']}</p>
 <div class="pj-acts"><a class="btn pri" href="{rel}contact/index.html">{t['cta_btn']}</a><a class="btn alt" href="{WA}" target="_blank" rel="noopener">{ICON['wa']}<span>{t['ct_wa']}</span></a></div></div>
 <p class="sv-intro">{d['intro']}</p></div></section>
<section class="wrap sec" style="padding-top:clamp(40px,5vw,70px)"><div class="sh"><h2>{t['incl_h']}</h2><p><b>{t['who_h']}:</b> {d['who']}</p></div><div class="incl" data-rv="kids">{incl}</div></section>
<section class="band"><div class="wrap sec"><div class="sh"><h2>{t['rel_h']}</h2></div><div class="gridw rel">{rel_cards}</div></div></section>
<section class="wrap sec"><div class="sv-split"><div><div class="sh"><h2>{t['svc_faq']}</h2></div><div class="faq">{faqs}</div></div>
 <aside class="sv-others"><h3>{t['other_svcs']}</h3>{others}</aside></div></section>
{cta_band(L, rel)}
</main>"""
    sch = {"@context": "https://schema.org", "@type": "Service", "name": d["name"], "description": d["desc"], "serviceType": d["name"],
           "provider": {"@type": "ProfessionalService", "name": "X TechVerse", "url": BASE}, "areaServed": [{"@type": "Country", "name": "Egypt"}, {"@type": "Country", "name": "Saudi Arabia"}],
           "url": BASE + ("" if L == "ar" else "en/") + f'services/{s["slug"]}/'}
    return page(L, 2, d["title"], d["desc"], body, f'services/{s["slug"]}/index.html', current="services", schema=(sch, faq_schema(d["faqs"])))

def contact_page(L):
    t = T[L]; rel = "../"
    steps = "".join(f'<li><b>{i+1}</b><div><h3>{h}</h3><p>{x}</p></div></li>' for i, (h, x) in enumerate(t["ct_after"]))
    body = f"""<main>
<section class="wrap phead"><div class="crumb"><a href="../index.html">{t['home']}</a><span>/</span><span>{t['contact']}</span></div><h1>{t['ct_h1']}</h1><p class="lead">{t['ct_lead']}</p></section>
<section class="wrap" style="padding-bottom:clamp(90px,11vw,150px)"><div class="ct-grid">
 <div class="ct-side">
  <h2>{t['ct_direct']}</h2>
  <a class="ct-card" href="{WA}" target="_blank" rel="noopener"><span class="ic">{ICON['wa']}</span><span><small>{t['ct_wa']}</small><b dir="ltr">+20 10 3925 3652</b></span></a>
  <a class="ct-card" href="mailto:info@xtechverse.com"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span><span><small>{t['ct_mail']}</small><b>info@xtechverse.com</b></span></a>
  <a class="ct-card" href="https://www.facebook.com/xtechverse1" target="_blank" rel="noopener"><span class="ic">{ICON['globe']}</span><span><small>{t['ct_fb']}</small><b>xtechverse1</b></span></a>
  <div class="ct-card"><span class="ic">{ICON['pin']}</span><span><small>{t['ct_where']}</small><b>{t['ct_where_v']}</b></span></div>
  <h2 style="margin-top:36px">{t['ct_after_h']}</h2><ol class="ct-steps">{steps}</ol>
 </div>
 <div class="ct-form"><h2>{t['f_h']}</h2>{lead_form(L, '{API}')}</div>
</div></section>
</main>"""
    sch = {"@context": "https://schema.org", "@type": "ContactPage", "name": t["ct_h1"], "url": BASE + ("" if L == "ar" else "en/") + "contact/"}
    return page(L, 1, t["ct_title"], t["ct_lead"], body, "contact/index.html", current="contact", schema=(sch,))

def write(path, txt):
    f = OUT / path; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(txt, encoding="utf-8")

for L in ("ar", "en"):
    pre = "" if L == "ar" else "en/"
    write(pre + "index.html", home(L))
    write(pre + "work/index.html", work(L))
    for i, p in enumerate(PROJECTS):
        write(pre + f'work/{p["slug"]}/index.html', project(L, i))
    write(pre + "work/aqary-eg/index.html", aqary(L))
    write(pre + "services/index.html", services_index(L))
    for sv in SERVICES:
        write(pre + f'services/{sv["slug"]}/index.html', service_page(L, sv))
    write(pre + "contact/index.html", contact_page(L))
urls = []
for pre in ("", "en/"):
    urls += [pre, pre + "work/", pre + "services/", pre + "contact/", pre + "work/aqary-eg/"]
    urls += [pre + f'work/{p["slug"]}/' for p in PROJECTS] + [pre + f'services/{sv["slug"]}/' for sv in SERVICES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {BASE}sitemap.xml\n")
print("built", len(urls), "pages")
