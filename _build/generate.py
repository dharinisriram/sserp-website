# -*- coding: utf-8 -*-
"""SS ERP Solutions website — page generator.
Generates every page except index.html from shared layout templates,
so header/footer/nav stay consistent. Re-run after editing:
    python _build/generate.py
"""
import os

SITE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
EMAIL = "support@sserpsolutions.net"
WHATSAPP = "https://wa.me/910000000000"  # WhatsApp business number pending (PRD §10)

# ---------------------------------------------------------------- layout

HEAD = """<!DOCTYPE html>
<html lang="{LANG}"{DIR}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://www.sserpsolutions.net/{CANON}">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="https://www.sserpsolutions.net/{CANON}">
<meta property="og:site_name" content="SS ERP Solutions">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet"></noscript>
<script>document.documentElement.classList.add("js");(function(){try{var t=localStorage.getItem("sserp-theme");if(t==="light"||t==="dark"){document.documentElement.setAttribute("data-theme",t);}}catch(e){}})();</script>
<link rel="stylesheet" href="{ROOT}css/styles.css">
<link rel="icon" type="image/png" href="{ROOT}assets/logo-mark.png">
<link rel="manifest" href="{ROOT}site.webmanifest">
<meta name="theme-color" content="#0B1220">
<meta property="og:image" content="https://www.sserpsolutions.net/assets/og-image.png">
{EXTRA_HEAD}</head>
<body>
"""

# Official interlocking-S mark, reconstructed as vector art (_build/make_logo.py)
LOGO_SVG = """<img src="{ROOT}assets/logo.svg" alt="" width="42" height="42" style="display:block;">"""

LANG_MENU = """<div class="has-sub lang-menu">
        <a class="lang-switch" href="{ROOT}index.html">{LANG_LABEL} <span class="caret" aria-hidden="true">▼</span></a>
        <ul class="submenu">
          <li><a href="{ROOT}index.html">English</a></li>
          <li><a href="{ROOT}ja/index.html" lang="ja">日本語</a></li>
          <li><a href="{ROOT}ar/index.html" lang="ar">العربية</a></li>
          <li><a href="{ROOT}hi/index.html" lang="hi">हिन्दी</a></li>
        </ul>
      </div>"""

HEADER = """<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{ROOT}index.html" aria-label="SS ERP Solutions — home">
      """ + LOGO_SVG + """
      <span>
        <span class="brand-name">SS ERP Solutions</span><br>
        <span class="brand-tag">Implement | Optimize | Transform</span>
      </span>
    </a>
    <ul class="nav-links">
      <li class="has-sub">
        <a href="{ROOT}services/index.html">Services <span class="caret" aria-hidden="true">▼</span></a>
        <ul class="submenu submenu-wide">
          <li class="sub-all"><a href="{ROOT}services/index.html">ALL SERVICES →</a></li>
          <li><a href="{ROOT}services/erp-consulting.html">ERP Consulting</a></li>
          <li><a href="{ROOT}services/enterprise-application-implementation.html">Application Implementation</a></li>
          <li><a href="{ROOT}services/greenfield-brownfield.html">Greenfield &amp; Brownfield</a></li>
          <li><a href="{ROOT}services/rollouts-upgrades-migrations.html">Rollouts, Upgrades &amp; Migrations</a></li>
          <li><a href="{ROOT}services/digital-transformation.html">Digital Transformation</a></li>
          <li><a href="{ROOT}services/pmo.html">PMO</a></li>
          <li><a href="{ROOT}services/ams.html">Application Management (AMS)</a></li>
          <li><a href="{ROOT}services/production-support-enhancements.html">Production Support</a></li>
          <li><a href="{ROOT}services/analytics-reporting.html">Analytics &amp; Custom Dashboards</a></li>
          <li><a href="{ROOT}services/training-internships-knowledge-transfer.html">Training &amp; Internships</a></li>
          <li><a href="{ROOT}services/oracle-multi-erp.html">Oracle &amp; Multi-ERP</a></li>
          <li><a href="{ROOT}services/ai-integration.html">AI Integration</a></li>
        </ul>
      </li>
      <li class="has-sub">
        <a href="{ROOT}about/index.html">Company <span class="caret" aria-hidden="true">▼</span></a>
        <ul class="submenu">
          <li><a href="{ROOT}about/index.html">About Us</a></li>
          <li><a href="{ROOT}why-us/index.html">Why Choose Us</a></li>
          <li><a href="{ROOT}about/index.html#global">Global Presence</a></li>
          <li><a href="{ROOT}faq/index.html">FAQ</a></li>
        </ul>
      </li>
      <li><a href="{ROOT}growing-together/index.html">Growing Together</a></li>
      <li><a href="{ROOT}insights/index.html">Insights</a></li>
      <li><a href="{ROOT}careers/index.html">Careers</a></li>
      <li><a href="{ROOT}portal/index.html">Client Portal</a></li>
    </ul>
    <div class="nav-cta">
      <button class="theme-toggle" aria-label="Toggle dark or light theme">☀</button>
      """ + LANG_MENU.replace("{LANG_LABEL}", "EN") + """
      <a class="btn btn-gold" href="{ROOT}contact/index.html">Contact</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="{ROOT}index.html" aria-label="SS ERP Solutions — home">
          """ + LOGO_SVG + """
          <span><span class="brand-name">SS ERP Solutions</span><br><span class="brand-tag">Implement | Optimize | Transform</span></span>
        </a>
        <p>Enterprise technology consulting — rooted in India, serving clients worldwide.</p>
      </div>
      <div>
        <h3 class="foot-h">Company</h3>
        <ul>
          <li><a href="{ROOT}about/index.html">About Us</a></li>
          <li><a href="{ROOT}why-us/index.html">Why Choose Us</a></li>
          <li><a href="{ROOT}growing-together/index.html">Growing Together</a></li>
          <li><a href="{ROOT}faq/index.html">FAQ</a></li>
          <li><a href="{ROOT}careers/index.html">Careers</a></li>
          <li><a href="{ROOT}privacy.html">Privacy Notice</a></li>
          <li><a href="{ROOT}terms.html">Terms of Use</a></li>
        </ul>
      </div>
      <div>
        <h3 class="foot-h">Services</h3>
        <ul>
          <li><a href="{ROOT}services/erp-consulting.html">ERP Consulting</a></li>
          <li><a href="{ROOT}services/enterprise-application-implementation.html">Implementation</a></li>
          <li><a href="{ROOT}services/rollouts-upgrades-migrations.html">Rollouts &amp; Upgrades</a></li>
          <li><a href="{ROOT}services/ams.html">AMS &amp; Support</a></li>
          <li><a href="{ROOT}services/oracle-multi-erp.html">Oracle &amp; Multi-ERP</a></li>
          <li><a href="{ROOT}services/analytics-reporting.html">Analytics &amp; Dashboards</a></li>
          <li><a href="{ROOT}services/ai-integration.html">AI Integration</a></li>
        </ul>
      </div>
      <div>
        <h3 class="foot-h">Connect</h3>
        <ul>
          <li><a href="{ROOT}insights/index.html">Insights</a></li>
          <li><a href="{ROOT}contact/index.html">Contact</a></li>
          <li><a href="{ROOT}portal/index.html">Client Portal</a></li>
          <li><a href="https://www.linkedin.com/" rel="noopener" target="_blank">LinkedIn</a></li>
          <li><a href="{ROOT}ja/index.html" lang="ja">日本語</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 SS ERP Solutions. All rights reserved.</span>
      <span>Implement | Optimize | Transform</span>
    </div>
  </div>
</footer>
"""

FLOAT = """<button class="back-top" aria-label="Back to top">↑</button>
<div class="cookie-bar" role="region" aria-label="Privacy notice">
  <div class="container">
    <p>This site stores your theme preference in your browser and, at go-live, will use privacy-respecting analytics to measure visits. Form data goes only to our official mailbox. See the <a href="{ROOT}privacy.html">privacy notice</a>.</p>
    <button class="btn btn-gold" data-cookie-ok type="button">Got it</button>
  </div>
</div>
<div class="chat-panel" role="dialog" aria-label="How can we help?" data-root="{ROOT}">
  <h3>How can we help?</h3>
  <div class="chat-thread" data-chat-thread></div>
</div>
<div class="float-actions">
  <button class="float-btn chat" aria-label="Open live chat">
    <svg viewBox="0 0 24 24" fill="none" stroke="#0B1220" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
  </button>
  <a class="float-btn whatsapp" aria-label="Chat on WhatsApp" href=\"""" + WHATSAPP + """\" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24" fill="#fff"><path d="M17.5 14.4c-.3-.15-1.75-.86-2-.96-.27-.1-.47-.15-.66.15-.2.3-.77.96-.94 1.15-.17.2-.35.22-.64.08-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.04-.17-.3-.02-.46.13-.6.13-.14.3-.35.44-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.66-1.6-.9-2.18-.24-.58-.5-.5-.66-.5h-.56c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5 0 1.47 1.07 2.9 1.22 3.1.15.2 2.1 3.2 5.08 4.5.7.3 1.26.5 1.7.63.7.23 1.35.2 1.86.12.57-.08 1.75-.72 2-1.4.24-.7.24-1.3.17-1.42-.08-.13-.28-.2-.57-.35zM12.05 21.8h-.02a9.87 9.87 0 0 1-5.03-1.38l-.36-.2-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.9-9.88a9.82 9.82 0 0 1 7 2.9 9.82 9.82 0 0 1 2.9 7c0 5.45-4.45 9.88-9.9 9.88zm8.42-18.3A11.8 11.8 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.9c0 2.1.55 4.15 1.6 5.95L.06 24l6.3-1.65a11.9 11.9 0 0 0 5.68 1.45h.01c6.55 0 11.9-5.34 11.9-11.9 0-3.18-1.24-6.17-3.48-8.4z"/></svg>
  </a>
</div>
"""

SCRIPTS = """<script src="{ROOT}js/main.js"></script>
</body>
</html>
"""


def wrap(path, title, desc, canon, body, root="../", lang="en", floats=True, chrome=True, extra_head="", rtl=False):
    html = HEAD.replace("{TITLE}", title).replace("{DESC}", desc).replace("{CANON}", canon) \
               .replace("{LANG}", lang).replace("{EXTRA_HEAD}", extra_head) \
               .replace("{DIR}", ' dir="rtl"' if rtl else "")
    if chrome:
        html += HEADER
    html += '<main id="main">\n' + body + "\n</main>\n"
    if chrome:
        html += FOOTER
    if floats:
        html += FLOAT
    html += SCRIPTS
    html = html.replace("{ROOT}", root)
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


def li(items):
    return "\n".join("<li>%s</li>" % i for i in items)


# ---------------------------------------------------------------- services

SERVICES = [
 dict(slug="erp-consulting", num="01", name="ERP Consulting",
  tag="Independent advice on ERP strategy, selection and roadmaps — grounded in how your business actually runs.",
  intro=["An ERP decision outlives the people who make it. The platform you choose — and the processes you design around it — will shape how your organisation works for a decade. We help you make that decision with clear eyes: what you need, what it will really cost, and what it will take to land. Most of our clients are growing mid-size businesses making this call for the first time — so we explain everything, and assume nothing.",
         "We are practitioners first. The consultants who write your roadmap are the same people who have implemented, migrated and supported these systems — so the advice is grounded in delivery reality."],
  approach=["<strong>Process audit first.</strong> We map how your business actually operates today — order-to-cash, procure-to-pay, record-to-report — before any technology talk.",
            "<strong>Requirements before vendors.</strong> Selection criteria come from your processes and growth plans.",
            "<strong>Honest fit assessment.</strong> We tell you which gaps are configuration, which are customisation, and which should change your process instead.",
            "<strong>A roadmap you can execute.</strong> Phasing, team shape, budget ranges and risks — written so your board can act on it."],
  engagements=["ERP strategy and platform selection for a first ERP or a replacement", "S/4HANA readiness assessments and migration roadmaps", "Health checks of existing implementations that underperform", "Business-case development for transformation programmes"],
  outcomes=["A decision your leadership can defend, with the trade-offs on paper", "Realistic budget and timeline ranges before you commit", "Reduced implementation risk because the groundwork happened first"]),

 dict(slug="enterprise-application-implementation", num="02", name="Enterprise Application Implementation",
  tag="End-to-end implementation of SAP and enterprise applications — scoped honestly, staffed properly, delivered to plan.",
  intro=["A good implementation is mostly decided before the first configuration screen: honest scope, the right team, and a plan that respects how your people work. We run implementations with those three things in place from day one.",
         "Our teams cover the full SAP core — FICO, MM, SD, PP, QM, PM — with ABAP and BASIS capability in-house, so functional and technical decisions are made together, by one team."],
  approach=["<strong>Blueprint against reality.</strong> Design workshops run with the people who will use the system, not just the steering committee.",
            "<strong>Build in visible increments.</strong> Regular playbacks of working configuration, with progress visible every few weeks.",
            "<strong>Data taken seriously.</strong> Migration is planned from week one: mapping, cleansing, mock loads, reconciliation.",
            "<strong>Cutover as a rehearsed event.</strong> Documented runbooks, rehearsals and rollback plans before go-live weekend.",
            "<strong>Hypercare that stays.</strong> Structured post-go-live support that stays until the system is genuinely stable."],
  engagements=["Full-cycle SAP S/4HANA and SAP Business One implementations", "Module additions to a running landscape (e.g. Treasury, RAR, Group Reporting)", "Rescue of stalled or troubled implementations", "Integration of SAP with surrounding enterprise applications"],
  outcomes=["A system your teams actually use, adopted with training and change support", "Opening balances that reconcile on day one", "Documentation and knowledge transfer your team keeps"]),

 dict(slug="greenfield-brownfield", num="03", name="Greenfield & Brownfield Projects",
  tag="New builds and system conversions — including S/4HANA journeys that protect what works and fix what doesn't.",
  intro=["The greenfield-versus-brownfield question has no universal answer. A clean reimplementation buys you simplicity at the price of disruption; a system conversion preserves your history at the price of carrying old decisions forward. We help you choose on evidence, then deliver either path.",
         "For S/4HANA journeys specifically, we assess your custom code, data volumes, process debt and business appetite before recommending a route — and we will tell you if the honest answer is a hybrid, selective approach."],
  approach=["<strong>Assessment decides the route.</strong> Custom-code analysis, data profiling and process-debt review pick the path on evidence.",
            "<strong>Greenfield: design freedom used deliberately.</strong> Standard-first design, clean master data, only justified customisation.",
            "<strong>Brownfield: conversion without carry-over.</strong> We use the conversion to retire dead code and clean data along the way.",
            "<strong>Business continuity throughout.</strong> Month-end still closes, orders still ship, payroll still runs — through every phase."],
  engagements=["Greenfield S/4HANA implementations for growing enterprises", "Brownfield ECC-to-S/4HANA system conversions", "Selective data transition projects combining both approaches", "New-entity builds inside an existing corporate template"],
  outcomes=["A defensible route decision with the trade-offs documented", "A landscape ready for the 2030 ECC maintenance horizon", "Less custom code and cleaner data than you started with"]),

 dict(slug="rollouts-upgrades-migrations", num="04", name="Rollouts, Upgrades & Migrations",
  tag="Multi-country template rollouts, version upgrades and platform migrations — without disrupting the running business.",
  intro=["Rollouts and upgrades fail quietly: a template that ignores local statutory reality, an upgrade that breaks a bolt-on nobody documented, a migration weekend that runs long. We plan for exactly those failure modes.",
         "With delivery experience across India, Japan, the UAE and Singapore, we understand localisation as a first-class requirement — tax regimes, statutory reporting and language are part of the template design from day one."],
  approach=["<strong>Template with local intelligence.</strong> A global core plus a defined localisation layer per country — statutory, language, fiscal calendars.",
            "<strong>Impact analysis before upgrades.</strong> Custom code, interfaces and authorisations tested against the target version before anyone commits a date.",
            "<strong>Rehearsed migrations.</strong> Mock runs with timed cutover plans; the go-live weekend follows a script that has already worked twice.",
            "<strong>One team across countries.</strong> The same core team carries the template between rollouts, so lessons compound instead of repeating."],
  engagements=["Country rollouts of an existing corporate SAP template", "SAP version upgrades and enhancement-pack projects", "Database and platform migrations (including to HANA)", "Landscape consolidations after mergers and acquisitions"],
  outcomes=["Go-lives that hit their weekend and their budget", "Local statutory compliance built in from day one", "An upgrade path your team understands and can repeat"]),

 dict(slug="digital-transformation", num="05", name="Digital Transformation",
  tag="Process redesign, automation and integration that make transformation real — not just rebranded.",
  intro=["Real transformation starts with the process: what should this workflow look like if we designed it today — and only then, what technology gets us there?",
         "We keep transformation honest by tying every initiative to an operational measure: days to close, order cycle time, first-time-right rate. Every workstream starts by naming the measure it will move."],
  approach=["<strong>Redesign before automation.</strong> Core workflows are challenged and simplified before any tool is configured.",
            "<strong>Integrate, don't duplicate.</strong> One source of truth per data domain, with interfaces designed as products, not point fixes.",
            "<strong>Automate the repeatable.</strong> Workflow, RPA and smart forms where the volume justifies it — measured before and after.",
            "<strong>Adoption as a workstream.</strong> Training, champions and feedback loops planned with the same rigour as the build."],
  engagements=["Finance transformation: faster close, better controls, cleaner reporting", "Supply-chain digitisation across procurement and logistics", "Workflow and approval automation on the SAP core", "Legacy application rationalisation and integration"],
  outcomes=["Processes measurably faster and more reliable than before", "A smaller, cleaner application landscape", "Changes that stick, because the people who run them helped design them"]),

 dict(slug="pmo", num="06", name="PMO",
  tag="Programme and project management that keeps large initiatives honest: plans, risks, governance and decisions on the record.",
  intro=["Large programmes rarely fail from a single bad decision — they fail from a hundred small ones nobody wrote down. A disciplined PMO makes the state of the programme visible: what was decided, what it costs, what is at risk, and who owns the next move.",
         "We run PMO as a service — from full programme management of an implementation to an independent PMO layer over your own delivery teams or another vendor's."],
  approach=["<strong>A single plan that is real.</strong> One integrated plan with dependencies and capacity, that everyone works from.",
            "<strong>Risks with owners and dates.</strong> A living risk register reviewed weekly, with escalation that actually escalates.",
            "<strong>Decisions on the record.</strong> Every material decision logged with its context and alternatives — so the programme never re-litigates.",
            "<strong>Reporting people read.</strong> One page per week for the sponsor: status, spend, risks, asks."],
  engagements=["Full programme management of ERP implementations and rollouts", "Independent PMO oversight of a system-integrator-led programme", "Recovery management of programmes in trouble", "Portfolio governance across parallel initiatives"],
  outcomes=["A sponsor who always knows the true state of the programme", "Fewer surprises, earlier — risks surfaced while they are cheap", "An audit trail of decisions from kickoff to closure"]),

 dict(slug="ams", num="07", name="Application Management Services",
  tag="Ongoing management of your enterprise application landscape under defined service levels — so your team can focus on the business.",
  intro=["After go-live, an ERP system needs steady, competent care: incidents resolved, changes controlled, month-ends supported, patches applied. Our AMS provides that care under defined service levels — with the continuity that makes support genuinely good.",
         "We deliberately keep the same consultants on your account. The person who fixes your issue in month twelve knows the decisions made in month one — for systems we implemented, and for systems we inherited."],
  approach=["<strong>Structured takeover.</strong> A documented transition: landscape inventory, open-issue triage, knowledge capture — whether from your team or another vendor.",
            "<strong>Defined service levels.</strong> Priority-based response and resolution targets, reported monthly, with an honest conversation when we miss one.",
            "<strong>Prevention over firefighting.</strong> Recurring-incident analysis and quarterly health checks reduce ticket volume over time.",
            "<strong>Month-end presence.</strong> Support cover aligned to your close calendar and your time zones."],
  engagements=["Full AMS for SAP landscapes (functional + ABAP + BASIS)", "Second- and third-level support behind your internal service desk", "AMS takeover from an incumbent vendor", "Support for multi-country landscapes across time zones"],
  outcomes=["Falling incident volume, quarter on quarter", "A support partner who knows your system's history", "Predictable support cost your CFO can plan around"]),

 dict(slug="production-support-enhancements", num="08", name="Production Support & Enhancements",
  tag="Steady-state support, issue resolution and continuous small enhancements that keep the system in step with the business.",
  intro=["Businesses change every quarter; systems that don't follow become the reason for workarounds, shadow spreadsheets and eventually a costly reimplementation. Continuous small enhancements are the cheapest insurance against that drift.",
         "We combine production support with a managed enhancement pipeline: small, well-scoped improvements delivered in regular cycles, prioritised jointly with your process owners."],
  approach=["<strong>Stabilise first.</strong> Recurring incidents are fixed at root cause before enhancement work begins.",
            "<strong>A visible pipeline.</strong> Enhancement requests estimated, prioritised and scheduled in a backlog your team can see.",
            "<strong>Small batches, tested properly.</strong> Regular release cycles with regression testing, released in small, safe batches.",
            "<strong>Documentation as part of done.</strong> Every change lands with its documentation and, where needed, user communication."],
  engagements=["Production support for SAP functional modules and custom developments", "Continuous-improvement retainers with a monthly enhancement budget", "Statutory and year-end change support (tax rates, legal reporting)", "Performance tuning and batch-schedule optimisation"],
  outcomes=["A system that keeps pace with the business, quarter by quarter", "Fewer workarounds and shadow tools in the business", "Change delivered safely, on a rhythm your users can trust"]),

 dict(slug="analytics-reporting", num="09", name="Analytics, Reporting & Custom Dashboards",
  tag="SAP Analytics Cloud, Power BI, Tableau and custom-built dashboards — numbers leadership can rely on, wherever they live.",
  intro=["Most enterprises don't lack data; they lack numbers everyone agrees on. We build reporting across the modern analytics stack — SAP Analytics Cloud, Power BI, Tableau and, where the need is specific enough, fully custom web dashboards — with the discipline that makes a number trustworthy: defined once, calculated in one place, reconciled to the books.",
         "From board packs to operational control towers, we design for the reader: what decision does this report serve, and what is the least it needs to show? When an off-the-shelf tool can't express that, we build the dashboard ourselves — tailored views over your ERP data with exactly the drill-downs your teams ask for."],
  approach=["<strong>One definition per measure.</strong> A governed set of KPIs with owners and calculation logic — before any dashboard is drawn.",
            "<strong>Reconciled to the core.</strong> Every management number traceable to the underlying ERP documents — SAP, Oracle or otherwise.",
            "<strong>Self-service with guardrails.</strong> Curated models your analysts can explore without breaking the definitions.",
            "<strong>Right tool per audience.</strong> SAC or Power BI for leadership, embedded analytics for operations, custom-built dashboards where the requirement outgrows the tools."],
  engagements=["SAP Analytics Cloud implementations for planning and reporting", "Power BI and Tableau dashboard suites over ERP and operational data", "Custom web dashboards for requirements packaged tools can't express", "Group Reporting, consolidation and migration of legacy BO/BW reporting"],
  outcomes=["Month-end packs produced in hours, not days", "One version of the truth leadership actually trusts", "Dashboards shaped around your decisions and the way your teams work"]),

 dict(slug="training-internships-knowledge-transfer", num="10", name="Training, Internships & Knowledge Transfer",
  tag="Structured SAP training, internship programmes and project-embedded knowledge transfer — Growing Together.",
  intro=["The consulting industry runs on talent, and talent is built deliberately. Growing Together is our people-development practice: SAP training for professionals and graduates, structured internships with real project exposure, and formal knowledge transfer inside every client engagement.",
         "Our trainers are delivering consultants. What we teach on Saturday is what we configured on Thursday."],
  approach=["<strong>Practitioner-led curriculum.</strong> Functional and technical SAP tracks built from real project artefacts and scenarios.",
            "<strong>Learning by doing.</strong> Sandbox systems, case-based exercises and supervised work on realistic deliverables.",
            "<strong>Mentoring built in.</strong> Every trainee gets a senior consultant mentor for career and specialisation guidance.",
            "<strong>Certification with a plan.</strong> Honest advice on which SAP certifications matter for your goals — and efficient preparation for them."],
  engagements=["Corporate SAP training for client teams around go-lives", "Open training programmes for professionals moving into SAP", "Graduate internship cohorts with project placement", "End-of-project knowledge-transfer programmes for client IT teams"],
  outcomes=["Teams that can run and improve their own systems", "Graduates with genuine, hands-on project experience", "A talent pipeline for clients — and for our own bench"]),

 dict(slug="oracle-multi-erp", num="11", name="Oracle & Multi-ERP Solutions",
  tag="Oracle Fusion Cloud, NetSuite and other leading ERP platforms — the same delivery discipline, applied beyond SAP.",
  intro=["The right ERP depends on your size, complexity and growth plans — not on what a consultancy happens to sell. Our roots are in SAP, and our delivery discipline travels: we implement and support Oracle Fusion Cloud ERP, Oracle NetSuite and other leading platforms where they are the honest fit.",
         "This matters most in mixed estates: a group running SAP at the centre with NetSuite subsidiaries, or an acquisition arriving with Oracle already in place. We work across those boundaries — integration, consolidated reporting and one support arrangement — instead of pretending the estate is uniform."],
  approach=["<strong>Vendor-agnostic selection.</strong> Platform recommendations follow your requirements and budget, documented with the trade-offs, independent of any resale incentive.",
            "<strong>The same implementation discipline.</strong> Honest scope, blueprint against reality, rehearsed cutover and real hypercare — regardless of the logo on the login screen.",
            "<strong>Mixed-estate integration.</strong> Interfaces, master-data alignment and consolidated reporting across SAP, Oracle and other systems living side by side.",
            "<strong>One support arrangement.</strong> AMS that covers the estate you actually run, not just one vendor's slice of it."],
  engagements=["Oracle Fusion Cloud ERP implementations and rollouts", "Oracle NetSuite for subsidiaries, ventures and mid-market groups", "ERP selection between SAP, Oracle, Microsoft Dynamics 365 and Odoo", "Post-acquisition integration of mixed SAP/Oracle landscapes"],
  outcomes=["A platform chosen on evidence, with the reasoning on paper", "Subsidiaries live on fit-for-size systems without breaking group reporting", "One partner accountable across a multi-ERP estate"]),

 dict(slug="ai-integration", num="12", name="AI Integration & Intelligent Automation",
  tag="Practical AI inside your enterprise systems — assistants, document automation and forecasting that respect your data and your controls.",
  intro=["AI in the enterprise fails in two predictable ways: pilots that never touch real workflows, and deployments that ignore the controls finance and audit depend on. We do neither. We integrate AI where it demonstrably saves hours or improves decisions — grounded in your ERP data, inside your security boundary, with a human accountable for anything that posts, pays or promises.",
         "Our position is deliberately conservative: AI drafts, summarises, extracts and predicts; your systems and your people decide. That is what makes AI adoption survivable in an audited enterprise — and it is why our AI work starts from the ERP outward."],
  approach=["<strong>Use-cases triaged by value and risk.</strong> We rank candidates by hours saved and control impact — the first deployment should be boring, useful and safe.",
            "<strong>Grounded on your data.</strong> Assistants answer from your documents and ERP records, with access control intact.",
            "<strong>Human-in-the-loop where it counts.</strong> Anything touching postings, payments or external commitments keeps an approval step by design.",
            "<strong>Measured results.</strong> Baseline before, measure after — cycle time, hours returned, error rates. If it doesn't move, we say so."],
  engagements=["AI assistants over ERP, reporting and policy documents for finance and operations teams", "Intelligent document processing: invoices, purchase orders, delivery notes and contracts", "Machine-learning forecasting for cash, demand and inventory", "Workflow automation combining RPA, APIs and LLMs across the back office"],
  outcomes=["Hours returned to teams every week, measured against a baseline", "Faster document cycle times with fewer keying errors", "AI your auditors can live with — controls intact, decisions traceable"]),
]


def service_related(current):
    others = [s for s in SERVICES if s["slug"] != current][:4]
    return "\n".join('<li><a href="%s.html">%s</a></li>' % (s["slug"], s["name"]) for s in others)


def build_services():
    for s in SERVICES:
        body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / <a href="{ROOT}index.html#services">Services</a> / """ + s["name"] + """</p>
    <span class="eyebrow">Service """ + s["num"] + """ of 12</span>
    <h1>""" + s["name"] + """</h1>
    <p class="lead">""" + s["tag"] + """</p>
  </div>
</section>
<section class="section">
  <div class="container detail-grid">
    <article class="prose">
      """ + "\n      ".join("<p>%s</p>" % p for p in s["intro"]) + """
      <h2>Our approach</h2>
      <ul>""" + li(s["approach"]) + """</ul>
      <h2>Typical engagements</h2>
      <ul>""" + li(s["engagements"]) + """</ul>
      <h2>What you can expect</h2>
      <ul>""" + li(s["outcomes"]) + """</ul>
    </article>
    <aside class="side-card">
      <h3>Discuss this with us</h3>
      <p>Tell us what you're planning. We'll give you an honest view of what it takes — and whether we're the right team for it.</p>
      <a class="btn btn-gold" href="{ROOT}contact/index.html">Start a conversation</a>
      <ul class="side-links">
        <li><strong style="font-family:var(--font-mono);font-size:0.72rem;letter-spacing:0.14em;color:var(--muted);">RELATED SERVICES</strong></li>
        """ + service_related(s["slug"]) + """
      </ul>
    </aside>
  </div>
</section>
"""
        wrap("services/%s.html" % s["slug"],
             s["name"] + " — SS ERP Solutions",
             s["tag"],
             "services/%s.html" % s["slug"],
             body)


# ---------------------------------------------------------------- insights

# Case studies are anonymised project narratives — client sign-off required before go-live.
ARTICLES = [
 dict(slug="case-study-s4hana-nine-months", kind="Case study", thumb="t2",
  title="ECC to S/4HANA in nine months — without missing a single close",
  teaser="A mid-size manufacturing group needed off ECC before its hardware refresh. The programme landed on time because the hard decisions were made in the first four weeks.",
  date="July 2026", read="4 min read",
  body=["<strong>The challenge.</strong> A manufacturing group running SAP ECC across three plants faced a hardware refresh that made staying put as expensive as moving. Leadership wanted S/4HANA — but month-end close could not slip, statutory filings could not slip, and the internal IT team was four people.",
   "<strong>The approach.</strong> We spent the first four weeks on assessment rather than configuration: custom-code analysis showed just under half the group's custom objects had not executed in a year, and data profiling found the real cleansing burden sat in vendor and material masters, not transactions. That evidence made the route decision straightforward — a brownfield conversion with aggressive retirement of dead code, and master-data cleansing run as a parallel workstream from week one.",
   "<strong>The delivery.</strong> Two mock conversions were rehearsed and timed before anyone committed to a cutover weekend. Month-end procedures were walked through on the converted sandbox with the finance team a full cycle before go-live. The cutover ran to a scripted runbook that had already worked twice.",
   "<strong>The outcome.</strong> The group went live on S/4HANA inside nine months. Every close during the programme ran on schedule, the first close on the new system completed without escalation, and the custom-code estate shrank by nearly half. The same team provides AMS support today.",
   "<em>Client identity anonymised; published with client approval.</em>"]),
 dict(slug="case-study-gulf-rollout", kind="Case study", thumb="t3",
  title="Four countries, one template: a Gulf rollout that kept every statutory deadline",
  teaser="An enterprise group expanding across the Gulf needed one corporate template and four different statutory realities. Localisation was designed in, never bolted on.",
  date="July 2026", read="4 min read",
  body=["<strong>The challenge.</strong> A UAE-headquartered enterprise group was rolling its corporate SAP template into four country subsidiaries. Each country brought its own tax regime, statutory reporting and language requirements — and the group's previous rollout attempt, run template-first and localisation-later, had stalled in country two.",
   "<strong>The approach.</strong> We rebuilt the rollout model around a defined localisation layer: the global core stayed untouched, and each country's statutory, fiscal-calendar and language requirements were specified as first-class design objects before configuration began. One core team carried the template between countries, so every lesson from country one arrived in country two as standard practice.",
   "<strong>The delivery.</strong> Countries went live in sequence, each on a template that already contained its statutory reality. A PMO cadence of weekly one-page sponsor reporting and a jointly-owned risk register kept the four workstreams honest across time zones.",
   "<strong>The outcome.</strong> All four subsidiaries went live on the corporate template with every statutory deadline met across the programme. Group reporting consolidated from day one in each country, and the rollout playbook is now the group's standard for future markets.",
   "<em>Client identity anonymised; published with client approval.</em>"]),
 dict(slug="custom-dashboards-beyond-bi", kind="Article", thumb="t1",
  title="Custom dashboards: what to build when Power BI runs out of road",
  teaser="Packaged BI tools cover most reporting needs brilliantly. The judgement call is recognising the moment your requirement has outgrown them — and what to do next.",
  date="July 2026", read="5 min read",
  body=["Power BI, Tableau and SAP Analytics Cloud cover the overwhelming majority of enterprise reporting needs, and covering them with a packaged tool is almost always the right call: faster to build, cheaper to run, easier to hand over. The interesting question is the residual minority — the requirements that keep fighting the tool.",
   "You recognise them by the workarounds. A dashboard that needs three exports and a spreadsheet macro before the Monday meeting. A drill-down the tool cannot express, so analysts keep a parallel workbook. An operational view that needs write-back — approve this, hold that — which BI tools were never designed to do.",
   "That third case is the clearest signal. The moment a 'report' needs to trigger action — an approval, a hold, a reorder — you are no longer building a report; you are building a thin operational application over your ERP data. Forcing it into a BI tool produces the workaround culture; building it as a small custom dashboard produces software people actually use.",
   "The economics are better than most IT leaders expect. A focused custom dashboard — one audience, one decision, live ERP data, exactly the drill-downs asked for — is weeks of work, not months, when the data foundations already exist. The expensive version is the one built without governed KPI definitions underneath; then every number becomes a negotiation.",
   "Our rule of thumb: packaged BI first, always — then custom, surgically, where the requirement involves action, unusual interaction, or an audience the packaged tools price out. The mistake is not choosing one or the other; it is failing to notice when the requirement crossed the line."]),
 dict(slug="practical-ai-finance-operations", kind="Article", thumb="t3",
  title="AI in finance operations: start boring, win big",
  teaser="The AI deployments that survive audit season are the unglamorous ones. A field guide to choosing your first use-case — and the controls that keep it in production.",
  date="July 2026", read="5 min read",
  body=["Two years into the enterprise AI wave, a pattern is visible: the deployments still running are rarely the impressive ones. The chatbot that promised to answer anything is gone; the document extractor that reads supplier invoices into the ERP, every night, is quietly saving four hours a day.",
   "The survivors share three properties. First, they are grounded: they answer from the organisation's own documents and records, with access control intact, rather than from a model's general knowledge. Second, they keep a human in the loop wherever money moves or commitments are made — AI drafts and extracts; people approve. Third, they were measured against a baseline from day one, so their value is a number, not a feeling.",
   "That discipline points to where to start: document-heavy, judgement-light workflows. Invoice and purchase-order capture. First-draft reconciliation matching. Summarising a month's exceptions for review. Answering 'what is our policy on X' from the policy library. None of these makes a keynote; all of them return hours every week, and none of them frightens an auditor.",
   "The controls conversation is where most programmes stall, and it needs to happen first, not after the pilot. Where does the data go? Which model sees it, and is it retained? Who approved the output before it posted? An AI integration designed around those questions passes review; one retrofitted to them usually does not.",
   "Start boring. Measure honestly. Expand from evidence. The organisations doing this are building a compounding advantage — one unglamorous workflow at a time."]),
 dict(slug="ecc-to-s4hana-roadmap", kind="Article", thumb="t1",
  title="ECC to S/4HANA: plan the move before the deadline plans it for you",
  teaser="SAP ECC mainstream maintenance ends in 2027, with extended options to 2030. The enterprises that move well are the ones that start with an assessment, not a contract.",
  date="July 2026", read="6 min read",
  body=["Every SAP ECC customer knows the dates by now: mainstream maintenance ends in 2027, and even the extended-maintenance option runs out in 2030. What fewer organisations have internalised is what the calendar does to programme quality. Migrations planned in 2026 are assessments, choices and phased programmes. Migrations planned in 2029 are whatever can be contracted in time.",
   "The first decision is not greenfield versus brownfield — it is understanding what you actually run today. A serious readiness assessment covers four things: how much of your custom code is still executed at all; how far your processes have drifted from SAP standard; the state of your master data; and which interfaces and bolt-ons your business quietly depends on.",
   "In our assessments it is common to find that 40–60% of custom code has not been executed in the last year. That single finding changes the migration conversation: you are not carrying your whole history forward, only the part that is alive.",
   "From there, the route decision becomes evidence-based. Heavy process drift and poor master data push towards greenfield — a clean reimplementation. A disciplined landscape with valued customisations favours brownfield conversion. Many real answers are selective: a new core, with surgical carry-over of what has proven value.",
   "Whichever route, the calendar argument is the same: assessment now costs weeks and buys you options. Assessment later costs the options. If your organisation runs ECC and has no written S/4HANA position yet, the assessment — not the migration — is the urgent step."]),
 dict(slug="greenfield-vs-brownfield", kind="Article", thumb="t2",
  title="Greenfield or brownfield? An honest decision framework",
  teaser="Vendors tend to recommend whichever route they sell best. The right answer comes from your custom code, your data quality and your appetite for change — not from a preference.",
  date="July 2026", read="5 min read",
  body=["Ask three system integrators about greenfield versus brownfield and you may get three confident, incompatible answers. The uncomfortable truth is that both routes work, both routes fail, and the deciding factors sit in your landscape — not in anyone's methodology deck.",
   "Greenfield — a fresh implementation — buys you a clean process design, clean master data and freedom from a decade of accumulated decisions. Its price is disruption: the business re-learns its system, historic data lives in an archive rather than in transactions, and the change-management effort is real.",
   "Brownfield — a system conversion — preserves your history, your customisations and much of your users' muscle memory. Its price is that you carry your past forward: process debt, dormant code and old configuration decisions arrive in the new system unless you deliberately clean as you convert.",
   "Our framework asks four questions. One: how much of your customisation still earns its keep? Two: would your process owners redesign their workflows today if given the chance — and do they have the energy to? Three: can your business absorb a re-implementation's disruption, or is continuity the binding constraint? Four: what does your data deserve — a fresh start or a faithful carry?",
   "Score those honestly and the route usually names itself. And when the answers conflict, selective transition — new core, chosen history — is a legitimate middle path, not a compromise. What matters is that the decision is made on your evidence, once, with the trade-offs written down."]),
 dict(slug="ams-handover-checklist", kind="Article", thumb="t3",
  title="Taking over SAP support without drama: the AMS handover checklist",
  teaser="Switching AMS vendors — or moving support in-house — fails at handover more often than at steady state. Here is the checklist we run before we accept a single ticket.",
  date="July 2026", read="5 min read",
  body=["Most AMS relationships are judged on response times, but most AMS failures are decided earlier — in a rushed handover where knowledge walked out with the incumbent. Before we accept responsibility for a landscape, we insist on a structured transition, and we recommend the same checklist even when we are not the vendor.",
   "First, the landscape inventory: every system, client, interface, batch job and third-party bolt-on, with owners named. Undocumented interfaces are where month-one incidents live.",
   "Second, open-item triage: every open incident, problem and change request reviewed jointly, with the incumbent, before cutover. Anything unclear gets a written status. The alternative is inheriting a backlog you cannot interpret.",
   "Third, knowledge capture with the calendar in mind: month-end, quarter-end and year-end procedures are rehearsed on paper with the outgoing team while they are still reachable. The first close under new support should follow a script someone has already walked through.",
   "Fourth, access and authorisation hygiene: support users, emergency access procedures and audit requirements agreed before day one — not discovered during the first priority-one incident.",
   "A disciplined handover takes four to eight weeks. It is the cheapest insurance an IT leader can buy: the cost of doing it properly is a rounding error against the cost of a failed month-end in month two."]),
]


def build_insights():
    cards = []
    for a in ARTICLES:
        body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Insights</p>
    <span class="eyebrow">Insights</span>
    <h1>Articles, news &amp; case studies</h1>
    <p class="lead">Practical writing on ERP decisions, SAP delivery and enterprise technology — from consultants who do the work. Published by the SS ERP Solutions team through the site's CMS.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid">""" + "".join(cards) + """
    </div>
  </div>
</section>
"""
    wrap("insights/index.html", "Insights — SS ERP Solutions",
         "Articles, company news and case studies on ERP, SAP delivery and enterprise technology from SS ERP Solutions.",
         "insights/", body)

    for a in ARTICLES:
        abody = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / <a href="index.html">Insights</a> / """ + a["kind"] + """</p>
    <span class="eyebrow">""" + a["kind"] + " · " + a["date"] + " · " + a["read"] + """</span>
    <h1>""" + a["title"] + """</h1>
  </div>
</section>
<section class="section">
  <div class="container detail-grid">
    <article class="prose">
      """ + "\n      ".join("<p>%s</p>" % p for p in a["body"]) + """
    </article>
    <aside class="side-card">
      <h3>Talk to the authors</h3>
      <p>These articles are written by our delivery consultants. If the topic is live for your organisation, we're happy to discuss it.</p>
      <a class="btn btn-gold" href="{ROOT}contact/index.html">Start a conversation</a>
      <ul class="side-links">
        <li><strong style="font-family:var(--font-mono);font-size:0.72rem;letter-spacing:0.14em;color:var(--muted);">MORE INSIGHTS</strong></li>
        """ + "\n".join('<li><a href="%s.html">%s</a></li>' % (o["slug"], o["title"]) for o in ARTICLES if o["slug"] != a["slug"]) + """
      </ul>
    </aside>
  </div>
</section>
"""
        wrap("insights/%s.html" % a["slug"], a["title"] + " — SS ERP Solutions Insights",
             a["teaser"], "insights/%s.html" % a["slug"], abody)


# ---------------------------------------------------------------- careers

def build_careers():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Careers</p>
    <span class="eyebrow">Careers</span>
    <h1>Do the best work of your career — properly</h1>
    <p class="lead">We hire consultants who care how the work is done: honest scoping, real expertise, long client relationships. If that sounds like you, we'd like to meet you.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <h2>Open roles</h2>
      <p>We hire for depth and character in equal measure. Current openings below — strong profiles are welcome at any time.</p><!-- roles to be confirmed by SS ERP Solutions before go-live -->
    </div>
    <div class="role-card reveal">
      <div>
        <h3>Senior SAP FICO Consultant</h3>
        <p style="color:var(--muted);font-size:0.95rem;">Lead finance workstreams on S/4HANA implementations and support engagements. Strong FI/CO configuration depth; Group Reporting or Central Finance exposure a plus.</p>
        <div class="role-tags"><span class="role-tag">Chennai · Hybrid</span><span class="role-tag">6–10 years</span><span class="role-tag">Full time</span></div>
      </div>
      <a class="btn btn-outline" href="#apply">Apply</a>
    </div>
    <div class="role-card reveal">
      <div>
        <h3>SAP ABAP Developer</h3>
        <p style="color:var(--muted);font-size:0.95rem;">Build and maintain custom developments across our client landscapes — reports, interfaces, enhancements, Fiori. Clean-code habits and S/4HANA experience valued.</p>
        <div class="role-tags"><span class="role-tag">Chennai</span><span class="role-tag">3–6 years</span><span class="role-tag">Full time</span></div>
      </div>
      <a class="btn btn-outline" href="#apply">Apply</a>
    </div>
    <div class="role-card reveal">
      <div>
        <h3>SAP SD/MM Consultant</h3>
        <p style="color:var(--muted);font-size:0.95rem;">Deliver logistics workstreams on implementations and rollouts across the Gulf region. Client-facing, hands-on configuration; Arabic or Japanese language skills a plus.</p>
        <div class="role-tags"><span class="role-tag">Dubai, UAE</span><span class="role-tag">4–8 years</span><span class="role-tag">Full time</span></div>
      </div>
      <a class="btn btn-outline" href="#apply">Apply</a>
    </div>
  </div>
</section>
<section class="section section-alt" id="apply">
  <div class="container" style="max-width:820px;">
    <div class="section-head reveal">
      <h2>Apply — or register your interest</h2>
      <p>Every strong profile is welcome — send yours even without a matching role. Applications are delivered to our official mailbox and every serious one gets a reply.</p>
    </div>
    <form class="form-card reveal" data-demo-form novalidate>
      <div class="form-grid">
        <div class="form-field"><label for="ap-name">Full name <span class="req">*</span></label><input id="ap-name" name="name" type="text" required autocomplete="name"></div>
        <div class="form-field"><label for="ap-email">Email <span class="req">*</span></label><input id="ap-email" name="email" type="email" required autocomplete="email"></div>
        <div class="form-field"><label for="ap-phone">Phone</label><input id="ap-phone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="form-field"><label for="ap-role">Role</label>
          <select id="ap-role" name="role">
            <option>Senior SAP FICO Consultant</option>
            <option>SAP ABAP Developer</option>
            <option>SAP SD/MM Consultant</option>
            <option>General application / internship</option>
          </select>
        </div>
        <div class="form-field full"><label for="ap-cv">CV / resume (PDF)</label><input id="ap-cv" name="cv" type="file" accept=".pdf,.doc,.docx"></div>
        <div class="form-field full"><label for="ap-msg">Tell us about yourself <span class="req">*</span></label><textarea id="ap-msg" name="message" required></textarea></div>
      </div>
      <div class="honeypot" aria-hidden="true"><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
      <div style="margin-top:26px;display:flex;align-items:center;gap:18px;flex-wrap:wrap;">
        <button class="btn btn-gold" type="submit">Submit application</button>
        <span class="form-note">Your application is delivered to """ + EMAIL + """ and treated confidentially.</span>
      </div>
      <div class="form-success" role="status">Thank you — your application has been received. We reply to every serious application.</div>
    </form>
  </div>
</section>
"""
    wrap("careers/index.html", "Careers — SS ERP Solutions",
         "Open SAP consulting roles at SS ERP Solutions across India and the UAE, plus a general application form for consultants and interns.",
         "careers/", body)


# ---------------------------------------------------------------- contact

def build_contact():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Contact</p>
    <span class="eyebrow">Contact</span>
    <h1>Tell us what you're planning</h1>
    <p class="lead">An implementation, a migration, a support handover, a training programme — or just a question. We'll come back with an honest view, usually within one business day.</p>
  </div>
</section>
<section class="section">
  <div class="container detail-grid">
    <form class="form-card" data-demo-form novalidate>
      <div class="form-grid">
        <div class="form-field"><label for="ct-name">Full name <span class="req">*</span></label><input id="ct-name" name="name" type="text" required autocomplete="name"></div>
        <div class="form-field"><label for="ct-company">Company <span class="req">*</span></label><input id="ct-company" name="company" type="text" required autocomplete="organization"></div>
        <div class="form-field"><label for="ct-email">Work email <span class="req">*</span></label><input id="ct-email" name="email" type="email" required autocomplete="email"></div>
        <div class="form-field"><label for="ct-phone">Phone</label><input id="ct-phone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="form-field"><label for="ct-country">Country</label>
          <select id="ct-country" name="country"><option>India</option><option>Japan</option><option>UAE</option><option>Singapore</option><option>Other</option></select>
        </div>
        <div class="form-field"><label for="ct-topic">What is this about?</label>
          <select id="ct-topic" name="topic">
            <option>ERP consulting / selection</option><option>New implementation</option><option>S/4HANA migration</option>
            <option>Rollout / upgrade</option><option>AMS / production support</option><option>Contract / subcontract delivery</option><option>Analytics &amp; reporting</option>
            <option>Training / internships</option><option>Something else</option>
          </select>
        </div>
        <div class="form-field full"><label for="ct-msg">Your message <span class="req">*</span></label><textarea id="ct-msg" name="message" required placeholder="A few lines about your landscape, timeline and what you need."></textarea></div>
      </div>
      <div class="honeypot" aria-hidden="true"><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
      <div style="margin-top:26px;display:flex;align-items:center;gap:18px;flex-wrap:wrap;">
        <button class="btn btn-gold" type="submit">Send message</button>
        <span class="form-note">Spam-protected. Delivered to our official mailbox; never sold or shared.</span>
      </div>
      <div class="form-success" role="status">Thank you — your message has been received. We usually reply within one business day.</div>
    </form>
    <aside class="side-card">
      <h3>Reach us directly</h3>
      <p style="margin-bottom:8px;"><strong>Email</strong><br><a href="mailto:""" + EMAIL + """\">""" + EMAIL + """</a></p>
      <p style="margin-bottom:8px;"><strong>WhatsApp</strong><br><a href=\"""" + WHATSAPP + """\" rel="noopener" target="_blank">Chat with us on WhatsApp</a></p>
      <p><strong>Where we work</strong><br>India · Japan · UAE · Singapore — serving clients worldwide.</p>
    </aside>
  </div>
</section>
"""
    wrap("contact/index.html", "Contact — SS ERP Solutions",
         "Contact SS ERP Solutions about SAP implementations, migrations, support, analytics and training. Form, email and WhatsApp.",
         "contact/", body)


# ---------------------------------------------------------------- portal

def build_portal():
    login = """
<div class="portal-wrap">
  <div>
    <div class="portal-card">
      <a class="brand" href="{ROOT}index.html">""" + LOGO_SVG + """</a>
      <h1>Client Portal</h1>
      <p>Secure workspace for engaged clients: shared documents, project status and your SS ERP Solutions contacts.</p>
      <form data-demo-form data-portal-login novalidate>
        <div class="form-grid" style="grid-template-columns:1fr;">
          <div class="form-field"><label for="po-email">Work email</label><input id="po-email" type="email" required autocomplete="username"></div>
          <div class="form-field"><label for="po-pass">Password</label><input id="po-pass" type="password" required autocomplete="current-password"></div>
        </div>
        <div style="margin-top:22px;">
          <button class="btn btn-gold" type="submit" style="width:100%;justify-content:center;">Sign in</button>
        </div>
        <div class="form-success" role="status">Portal access is provisioned per engagement. If you need credentials, contact your SS ERP Solutions programme manager.</div>
      </form>
      <p style="margin-top:22px;font-size:0.82rem;">Access is provisioned by SS ERP Solutions for engaged clients.<br>Need access? <a href="{ROOT}contact/index.html">Contact us</a>.</p>
      <p style="margin-top:14px;text-align:center;"><a class="btn btn-outline" href="dashboard.html" style="width:100%;justify-content:center;">View demo dashboard →</a></p>
    </div>
  </div>
</div>
"""
    wrap("portal/index.html", "Client Portal — SS ERP Solutions",
         "Secure client portal for SS ERP Solutions engagement documents and project status.",
         "portal/", login, floats=False, chrome=False)

    dash = """
<section style="padding-top:var(--header-h);">
  <div class="container">
    <div style="margin-top:28px;border:1px dashed var(--maroon-light);border-radius:10px;padding:12px 18px;font-family:var(--font-mono);font-size:0.78rem;color:var(--maroon-light);letter-spacing:0.08em;">
      SAMPLE WORKSPACE — shown with demonstration data.
    </div>
    <div class="dash-layout" style="padding-top:28px;">
      <aside class="dash-side">
        <nav>
          <a class="active" href="#">Overview</a>
          <a href="#documents">Documents</a>
          <a href="#status">Project status</a>
          <a href="#contacts">Your contacts</a>
        </nav>
      </aside>
      <div class="dash-main">
        <div>
          <span class="eyebrow">Acme Manufacturing Ltd — S/4HANA Implementation</span>
          <h1 style="font-size:1.7rem;"><span data-user-greet></span>Programme overview</h1>
        </div>
        <div class="dash-cards">
          <div class="dash-card"><div class="k">Current phase</div><div class="v">Realisation</div><span class="badge ok">On track</span></div>
          <div class="dash-card"><div class="k">Next milestone</div><div class="v">Integration test start</div><span class="badge info">12 Aug 2026</span></div>
          <div class="dash-card"><div class="k">Open actions on client</div><div class="v">3</div><span class="badge warn">2 due this week</span></div>
        </div>
        <div class="panel" id="status">
          <div class="panel-head"><h3>Workstream status</h3><span class="badge ok">Updated weekly</span></div>
          <table class="data-table">
            <thead><tr><th>Workstream</th><th>Lead</th><th>Status</th><th>Note</th></tr></thead>
            <tbody>
              <tr><td>Finance (FICO)</td><td>SSES</td><td><span class="badge ok">On track</span></td><td>CO-PA design signed off</td></tr>
              <tr><td>Logistics (MM/SD)</td><td>SSES</td><td><span class="badge warn">Watch</span></td><td>Pricing decision pending client input</td></tr>
              <tr><td>Data migration</td><td>Joint</td><td><span class="badge ok">On track</span></td><td>Mock load 2 reconciled</td></tr>
              <tr><td>Integrations</td><td>Client IT</td><td><span class="badge info">Starting</span></td><td>Bank interface spec in review</td></tr>
            </tbody>
          </table>
        </div>
        <div class="panel" id="documents">
          <div class="panel-head"><h3>Shared documents</h3></div>
          <table class="data-table">
            <thead><tr><th>Document</th><th>Type</th><th>Updated</th></tr></thead>
            <tbody>
              <tr><td>Weekly status report — W30</td><td>PDF</td><td>24 Jul 2026</td></tr>
              <tr><td>Integration test plan v0.9</td><td>DOCX</td><td>22 Jul 2026</td></tr>
              <tr><td>Data migration reconciliation — Mock 2</td><td>XLSX</td><td>18 Jul 2026</td></tr>
              <tr><td>Steering committee pack — July</td><td>PDF</td><td>15 Jul 2026</td></tr>
            </tbody>
          </table>
        </div>
        <div class="panel" id="contacts">
          <div class="panel-head"><h3>Your SS ERP Solutions contacts</h3></div>
          <table class="data-table">
            <thead><tr><th>Name</th><th>Role</th><th>Email</th></tr></thead>
            <tbody>
              <tr><td>Programme Manager</td><td>Delivery lead &amp; escalation</td><td class="mono">pm@sserpsolutions.net</td></tr>
              <tr><td>Finance Lead</td><td>FICO workstream</td><td class="mono">fico@sserpsolutions.net</td></tr>
              <tr><td>Support Desk</td><td>Issues &amp; requests</td><td class="mono">""" + EMAIL + """</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    wrap("portal/dashboard.html", "Client Portal — Demo Dashboard — SS ERP Solutions",
         "Demonstration of the SS ERP Solutions client portal: shared documents, project status and contacts.",
         "portal/dashboard.html", dash, floats=False)


# ---------------------------------------------------------------- japanese

def build_japanese():
    global HEADER
    body = """
<section class="hero" id="top" style="min-height:82vh;">
  <canvas id="particle-canvas" aria-hidden="true"></canvas>
  <div class="container hero-inner">
    <span class="eyebrow">エンタープライズ・テクノロジー・コンサルティング</span>
    <h1 style="font-size:clamp(2rem,4.6vw,3.4rem);">エンタープライズ・テクノロジーで、ビジネス<span class="gold">変革</span>を実現する。</h1>
    <p class="hero-sub">SS ERP Solutionsは、深いSAPの専門知識、OracleをはじめとするマルチERP対応力、カスタムダッシュボードと実用的なAIを、信頼と紹介によって築かれた確かなデリバリー基準でお届けします。現場が本当に使えるエンタープライズ・ソリューションを計画・構築・運用します。</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="#contact">お問い合わせ</a>
      <a class="btn btn-outline" href="#services">サービスを見る</a>
    </div>
  </div>
</section>

<section class="section section-alt" id="who">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">私たちについて</span>
      <h2>信頼の上に築かれ、紹介によって成長してきました</h2>
      <p>SS ERP Solutionsは2018年の創業以来、広告ではなく、お客様の信頼と紹介によって成長してきました。インドを拠点に、日本、UAE、シンガポールのお客様を支援し、現在グローバルに展開を進めています。日本のお客様には日本語でサービスを提供しています。</p>
    </div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">サービス</span>
      <h2>12のサービスライン、ひとつのデリバリー基準</h2>
    </div>
    <div class="services-grid">
      <a class="service-card reveal" href="../services/erp-consulting.html"><span class="service-num">01</span><h3>ERPコンサルティング</h3><p>ERP戦略・製品選定・ロードマップに関する独立した助言。</p></a>
      <a class="service-card reveal" href="../services/enterprise-application-implementation.html"><span class="service-num">02</span><h3>エンタープライズ・アプリケーション導入</h3><p>SAPおよび企業アプリケーションのエンドツーエンド導入。</p></a>
      <a class="service-card reveal" href="../services/greenfield-brownfield.html"><span class="service-num">03</span><h3>グリーンフィールド／ブラウンフィールド</h3><p>新規構築とシステムコンバージョン、S/4HANAへの移行。</p></a>
      <a class="service-card reveal" href="../services/rollouts-upgrades-migrations.html"><span class="service-num">04</span><h3>ロールアウト・アップグレード・移行</h3><p>多国籍テンプレート展開、バージョンアップ、プラットフォーム移行。</p></a>
      <a class="service-card reveal" href="../services/digital-transformation.html"><span class="service-num">05</span><h3>デジタルトランスフォーメーション</h3><p>業務プロセスの再設計、自動化、システム統合。</p></a>
      <a class="service-card reveal" href="../services/pmo.html"><span class="service-num">06</span><h3>PMO</h3><p>大規模プログラムを支えるプロジェクトマネジメント。</p></a>
      <a class="service-card reveal" href="../services/ams.html"><span class="service-num">07</span><h3>アプリケーション・マネジメント・サービス</h3><p>SLAに基づくアプリケーション環境の継続的な管理・運用。</p></a>
      <a class="service-card reveal" href="../services/production-support-enhancements.html"><span class="service-num">08</span><h3>本番サポート＆機能拡張</h3><p>安定運用サポートと継続的な小規模改善。</p></a>
      <a class="service-card reveal" href="../services/analytics-reporting.html"><span class="service-num">09</span><h3>アナリティクス＆カスタムダッシュボード</h3><p>SAP Analytics Cloud、Power BI、Tableau、カスタム開発ダッシュボード。</p></a>
      <a class="service-card reveal" href="../services/training-internships-knowledge-transfer.html"><span class="service-num">10</span><h3>トレーニング・インターンシップ・ナレッジ移転</h3><p>実務者によるSAP教育と人材育成（Growing Together）。</p></a>
      <a class="service-card reveal" href="../services/oracle-multi-erp.html"><span class="service-num">11</span><h3>Oracle＆マルチERPソリューション</h3><p>Oracle Fusion Cloud、NetSuiteをはじめとする主要ERPプラットフォーム。</p></a>
      <a class="service-card reveal" href="../services/ai-integration.html"><span class="service-num">12</span><h3>AI統合＆インテリジェント自動化</h3><p>業務システムに組み込む実用的なAI——アシスタント、文書自動処理、予測分析。</p></a>
    </div>
    <p class="form-note" style="margin-top:18px;">サービス詳細ページは現在英語版のみです。日本語版は順次公開予定です。</p>
  </div>
</section>

<section class="section section-alt" id="why">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">選ばれる理由</span>
      <h2>エンタープライズ・プログラムを任せられる、最高のチームであるために</h2>
    </div>
    <div class="commit-list reveal">
      <div class="commit"><div class="commit-num">01</div><div><h3>確実に提供できる仕事だけをお引き受けします</h3><p>契約の前に、能力と体制を正直に見極めたうえでお引き受けします。</p></div></div>
      <div class="commit"><div class="commit-num">02</div><div><h3>最適なチームを編成します</h3><p>案件ごとに、適切なモジュール経験・業界知識・経験年数を持つコンサルタントを配置します。</p></div></div>
      <div class="commit"><div class="commit-num">03</div><div><h3>長期的な関係を大切にします</h3><p>ゴーライブ後の関係を最優先に考えます。多くのお客様と複数プロジェクトを重ねています。</p></div></div>
      <div class="commit"><div class="commit-num">04</div><div><h3>実用的で高品質なソリューションを構築します</h3><p>目的に適った設計を第一に、実際に運用する方々のために作ります。</p></div></div>
      <div class="commit"><div class="commit-num">05</div><div><h3>学び続けます</h3><p>継続的な資格取得、社内勉強会、率直なプロジェクト振り返りで基準を保ちます。</p></div></div>
    </div>
  </div>
</section>

<section class="section" id="global">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">グローバル展開</span>
      <h2>インドから、世界へ。</h2>
    </div>
    <div class="country-chips reveal">
      <span class="country-chip">インド — デリバリー＆コンサルティング拠点</span>
      <span class="country-chip">日本 — 日本語によるお客様対応</span>
      <span class="country-chip">UAE — 湾岸地域のお客様</span>
      <span class="country-chip">シンガポール — APAC案件</span>
      <span class="country-chip">グローバル展開 — リモート・ファーストで世界中のお客様に対応</span>
    </div>
  </div>
</section>

<section class="contact-cta" id="contact">
  <div class="container reveal">
    <span class="eyebrow" style="justify-content:center;display:inline-flex;">お問い合わせ</span>
    <h2>次のERPの意思決定を、確かなものに。</h2>
    <p>導入、移行、運用サポート、トレーニング——ご計画をお聞かせください。日本語で対応いたします。</p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn-gold" href="../contact/index.html">お問い合わせフォームへ</a>
      <a class="btn btn-outline" href="mailto:""" + EMAIL + """\">""" + EMAIL + """</a>
    </div>
  </div>
</section>
"""
    # JA page has its own explicit header (Japanese labels, switcher back to EN)
    ja_header = """<a class="skip-link" href="#main">メインコンテンツへ</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{ROOT}ja/index.html" aria-label="SS ERP Solutions — ホーム">
      """ + LOGO_SVG + """
      <span>
        <span class="brand-name">SS ERP Solutions</span><br>
        <span class="brand-tag">Implement | Optimize | Transform</span>
      </span>
    </a>
    <ul class="nav-links">
      <li><a href="#services">サービス</a></li>
      <li><a href="#why">選ばれる理由</a></li>
      <li><a href="#global">グローバル展開</a></li>
      <li><a href="{ROOT}insights/index.html">インサイト</a></li>
      <li><a href="{ROOT}careers/index.html">採用情報</a></li>
      <li><a href="{ROOT}portal/index.html">クライアントポータル</a></li>
    </ul>
    <div class="nav-cta">
      <button class="theme-toggle" aria-label="テーマ切り替え">☀</button>
      """ + LANG_MENU.replace("{LANG_LABEL}", "日本語") + """
      <a class="btn btn-gold" href="{ROOT}contact/index.html">お問い合わせ</a>
      <button class="nav-toggle" aria-label="メニュー" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
"""
    saved = HEADER
    HEADER = ja_header
    extra = '<link rel="alternate" hreflang="en" href="https://www.sserpsolutions.net/">\n<link rel="alternate" hreflang="ja" href="https://www.sserpsolutions.net/ja/">\n'
    wrap("ja/index.html", "SS ERP Solutions — エンタープライズ・テクノロジー・コンサルティング | 導入。最適化。変革。",
         "SS ERP Solutionsは、SAP導入・移行・運用サポート・デジタルトランスフォーメーションをインド、日本、UAE、シンガポールで提供するコンサルティング会社です。",
         "ja/", body, lang="ja", extra_head=extra)
    HEADER = saved


# ---------------------------------------------------------------- arabic & hindi (machine-assisted drafts — human review before publishing)

def locale_header(root, home_href, labels, lang_label):
    return """<a class="skip-link" href="#main">""" + labels["skip"] + """</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href=\"""" + home_href + """\">
      """ + LOGO_SVG + """
      <span>
        <span class="brand-name">SS ERP Solutions</span><br>
        <span class="brand-tag">Implement | Optimize | Transform</span>
      </span>
    </a>
    <ul class="nav-links">
      <li><a href="#services">""" + labels["services"] + """</a></li>
      <li><a href="#why">""" + labels["why"] + """</a></li>
      <li><a href="#global">""" + labels["global"] + """</a></li>
      <li><a href="{ROOT}portal/index.html">""" + labels["portal"] + """</a></li>
    </ul>
    <div class="nav-cta">
      <button class="theme-toggle" aria-label="Theme">☀</button>
      """ + LANG_MENU.replace("{LANG_LABEL}", lang_label) + """
      <a class="btn btn-gold" href="{ROOT}contact/index.html">""" + labels["contact"] + """</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
"""


def build_locale(code, lang_label, rtl, labels, t):
    """Condensed localized homepage: hero, 12 services, why-us, global, contact CTA."""
    global HEADER
    cards = "\n".join(
        '      <a class="service-card reveal" href="../services/%s.html"><span class="service-num">%s</span><h3>%s</h3><p>%s</p></a>'
        % (s["slug"], s["num"], name, blurb)
        for s, (name, blurb) in zip(SERVICES, t["services"]))
    commits = "\n".join(
        '      <div class="commit"><div class="commit-num">0%d</div><div><h3>%s</h3><p>%s</p></div></div>'
        % (i + 1, h, p) for i, (h, p) in enumerate(t["commits"]))
    chips = "\n".join('      <span class="country-chip">%s</span>' % c for c in t["chips"])
    body = """
<section class="hero" id="top" style="min-height:70vh;">
  <canvas id="particle-canvas" aria-hidden="true"></canvas>
  <div class="container hero-inner">
    <span class="eyebrow">""" + t["eyebrow"] + """</span>
    <h1 style="font-size:clamp(1.9rem,4.4vw,3.2rem);">""" + t["h1"] + """</h1>
    <p class="hero-sub">""" + t["sub"] + """</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="../contact/index.html">""" + labels["contact"] + """</a>
      <a class="btn btn-outline" href="#services">""" + labels["services"] + """</a>
    </div>
  </div>
</section>
<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">""" + labels["services"] + """</span><h2>""" + t["services_h2"] + """</h2></div>
    <div class="services-grid">
""" + cards + """
    </div>
    <p class="form-note" style="margin-top:18px;">""" + t["services_note"] + """</p>
  </div>
</section>
<section class="section section-alt" id="why">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">""" + labels["why"] + """</span><h2>""" + t["why_h2"] + """</h2></div>
    <div class="commit-list reveal">
""" + commits + """
    </div>
  </div>
</section>
<section class="section" id="global">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">""" + labels["global"] + """</span><h2>""" + t["global_h2"] + """</h2></div>
    <div class="country-chips reveal">
""" + chips + """
    </div>
  </div>
</section>
<section class="contact-cta" id="contact">
  <div class="container reveal">
    <h2>""" + t["cta_h2"] + """</h2>
    <p>""" + t["cta_p"] + """</p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn-gold" href="../contact/index.html">""" + labels["contact"] + """</a>
      <a class="btn btn-outline" href="mailto:""" + EMAIL + """\">""" + EMAIL + """</a>
    </div>
  </div>
</section>
"""
    saved = HEADER
    HEADER = locale_header("../", "index.html", labels, lang_label)
    extra = ('<link rel="alternate" hreflang="en" href="https://www.sserpsolutions.net/">\n'
             '<link rel="alternate" hreflang="ja" href="https://www.sserpsolutions.net/ja/">\n'
             '<link rel="alternate" hreflang="ar" href="https://www.sserpsolutions.net/ar/">\n'
             '<link rel="alternate" hreflang="hi" href="https://www.sserpsolutions.net/hi/">\n')
    wrap("%s/index.html" % code, t["title"], t["desc"], "%s/" % code, body,
         lang=code, rtl=rtl, extra_head=extra)
    HEADER = saved


AR = dict(
 title="SS ERP Solutions — استشارات تقنية المؤسسات | التنفيذ. التحسين. التحوّل.",
 desc="SS ERP Solutions شركة استشارات تقنية للمؤسسات: تنفيذ أنظمة SAP وOracle، والدعم المُدار، ولوحات المعلومات المخصصة، ودمج الذكاء الاصطناعي — في الهند واليابان والإمارات وسنغافورة وحول العالم.",
 eyebrow="استشارات تقنية المؤسسات",
 h1='نُمكّن <span class="gold">تحوّل</span> الأعمال من خلال تقنية المؤسسات.',
 sub="نخطّط ونبني وندير حلول المؤسسات التي تستخدمها فرقكم فعلاً — خبرة عميقة في SAP، وقدرة على Oracle ومنصات ERP المتعددة، ولوحات معلومات مخصصة وذكاء اصطناعي عملي، بمعايير تسليم بُنيت على ثقة العملاء وتوصياتهم.",
 services_h2="اثنا عشر خط خدمة، ومعيار تسليم واحد",
 services_note="صفحات تفاصيل الخدمات متاحة حالياً باللغة الإنجليزية.",
 services=[
  ("استشارات ERP", "مشورة مستقلة في استراتيجية ERP واختيار الأنظمة وخرائط الطريق."),
  ("تنفيذ تطبيقات المؤسسات", "تنفيذ شامل لأنظمة SAP وتطبيقات المؤسسات."),
  ("مشاريع Greenfield وBrownfield", "بناء جديد أو تحويل الأنظمة القائمة إلى S/4HANA."),
  ("النشر والترقيات والترحيل", "نشر القوالب متعددة الدول والترقيات وترحيل المنصات."),
  ("التحوّل الرقمي", "إعادة تصميم العمليات والأتمتة والتكامل."),
  ("مكتب إدارة المشاريع PMO", "إدارة برامج تحافظ على وضوح الخطط والمخاطر والقرارات."),
  ("خدمات إدارة التطبيقات AMS", "إدارة مستمرة لتطبيقاتكم وفق مستويات خدمة محددة."),
  ("الدعم التشغيلي والتحسينات", "دعم مستقر وتحسينات صغيرة مستمرة."),
  ("التحليلات ولوحات المعلومات المخصصة", "SAP Analytics Cloud وPower BI وTableau ولوحات مبنية خصيصاً."),
  ("التدريب والتدريب العملي ونقل المعرفة", "تدريب SAP عملي وبرامج تدريب داخلي وإرشاد."),
  ("Oracle وحلول ERP المتعددة", "Oracle Fusion Cloud وNetSuite وغيرها من المنصات الرائدة."),
  ("دمج الذكاء الاصطناعي والأتمتة الذكية", "مساعدون ذكيون ومعالجة مستندات وتنبؤات تحترم بياناتكم وضوابطكم."),
 ],
 why_h2="أفضل فريق يمكن أن تُسنِد إليه برنامج مؤسستك",
 commits=[
  ("نلتزم فقط بما نثق بقدرتنا على تنفيذه", "نتحقق من القدرة والجاهزية بصدق قبل توقيع العقد."),
  ("نبني الفرق المناسبة", "استشاريون يُختارون بدقة حسب المشكلة: الوحدات والخبرة القطاعية والأقدمية المناسبة."),
  ("نُقدّر العلاقات طويلة الأمد", "معظم عملائنا عملوا معنا في مشاريع متعددة."),
  ("نبني حلولاً عملية عالية الجودة", "نصمّم للأشخاص الذين يشغّلون النظام كل يوم."),
  ("لا نتوقف عن التعلّم", "شهادات مستمرة وجلسات معرفة داخلية ومراجعات صادقة بعد كل مشروع."),
 ],
 global_h2="جذورنا في الهند، ونخدم العالم",
 chips=["الهند — مركز التسليم والاستشارات", "اليابان — خدمة العملاء باليابانية", "الإمارات — عملاء الخليج", "سنغافورة — مشاريع آسيا والمحيط الهادئ", "التوسع العالمي — تسليم عن بُعد حول العالم"],
 cta_h2="قراركم القادم بشأن ERP أهم من أن يُترك للصدفة.",
 cta_p="أخبرونا بما تخططون له — تنفيذ أو ترحيل أو دعم أو تدريب — وسنقدّم لكم رؤية خبيرة وواضحة.",
)

HI = dict(
 title="SS ERP Solutions — एंटरप्राइज़ टेक्नोलॉजी कंसल्टिंग | इम्प्लीमेंट. ऑप्टिमाइज़. ट्रांसफ़ॉर्म.",
 desc="SS ERP Solutions — SAP और Oracle ERP कार्यान्वयन, प्रबंधित सपोर्ट, कस्टम डैशबोर्ड और AI इंटीग्रेशन — भारत, जापान, UAE, सिंगापुर और दुनिया भर में।",
 eyebrow="एंटरप्राइज़ टेक्नोलॉजी कंसल्टिंग",
 h1='एंटरप्राइज़ टेक्नोलॉजी के ज़रिए कारोबारी <span class="gold">बदलाव</span> को साकार करते हैं।',
 sub="हम ऐसे एंटरप्राइज़ समाधान बनाते और चलाते हैं जिन्हें आपकी टीमें वाक़ई इस्तेमाल करती हैं — गहरी SAP विशेषज्ञता, Oracle व मल्टी-ERP क्षमता, कस्टम डैशबोर्ड और व्यावहारिक AI — ग्राहकों के भरोसे और रेफ़रल से बने डिलीवरी मानकों के साथ।",
 services_h2="बारह सेवा-क्षेत्र, एक ही डिलीवरी मानक",
 services_note="सेवा विवरण पृष्ठ फ़िलहाल अंग्रेज़ी में उपलब्ध हैं।",
 services=[
  ("ERP कंसल्टिंग", "ERP रणनीति, चयन और रोडमैप पर स्वतंत्र सलाह।"),
  ("एंटरप्राइज़ एप्लिकेशन कार्यान्वयन", "SAP और एंटरप्राइज़ एप्लिकेशनों का एंड-टू-एंड कार्यान्वयन।"),
  ("ग्रीनफ़ील्ड और ब्राउनफ़ील्ड", "नया निर्माण या मौजूदा सिस्टम का S/4HANA में रूपांतरण।"),
  ("रोलआउट, अपग्रेड और माइग्रेशन", "बहु-देशीय टेम्पलेट रोलआउट, अपग्रेड और प्लेटफ़ॉर्म माइग्रेशन।"),
  ("डिजिटल ट्रांसफ़ॉर्मेशन", "प्रक्रिया पुनर्रचना, ऑटोमेशन और इंटीग्रेशन।"),
  ("PMO", "योजना, जोखिम और निर्णयों को स्पष्ट रखने वाला प्रोग्राम प्रबंधन।"),
  ("एप्लिकेशन मैनेजमेंट (AMS)", "निर्धारित सेवा-स्तरों के साथ निरंतर एप्लिकेशन प्रबंधन।"),
  ("प्रोडक्शन सपोर्ट और संवर्धन", "स्थिर सपोर्ट और लगातार छोटे सुधार।"),
  ("एनालिटिक्स और कस्टम डैशबोर्ड", "SAP Analytics Cloud, Power BI, Tableau और कस्टम डैशबोर्ड।"),
  ("प्रशिक्षण, इंटर्नशिप और ज्ञान-हस्तांतरण", "व्यवसायी-नेतृत्व वाला SAP प्रशिक्षण और मेंटरिंग।"),
  ("Oracle और मल्टी-ERP समाधान", "Oracle Fusion Cloud, NetSuite और अन्य प्रमुख प्लेटफ़ॉर्म।"),
  ("AI इंटीग्रेशन और इंटेलिजेंट ऑटोमेशन", "आपके डेटा और नियंत्रणों का सम्मान करने वाला व्यावहारिक AI।"),
 ],
 why_h2="आपके एंटरप्राइज़ प्रोग्राम के लिए सर्वश्रेष्ठ टीम",
 commits=[
  ("हम वही वादा करते हैं जो पूरा कर सकें", "अनुबंध से पहले क्षमता और उपलब्धता की ईमानदार जाँच।"),
  ("हम सही टीमें बनाते हैं", "समस्या के अनुरूप मॉड्यूल, उद्योग-अनुभव और वरिष्ठता वाले सलाहकार।"),
  ("हम दीर्घकालिक रिश्तों को महत्व देते हैं", "हमारे अधिकांश ग्राहक कई परियोजनाओं में हमारे साथ रहे हैं।"),
  ("हम व्यावहारिक, उच्च-गुणवत्ता समाधान बनाते हैं", "उनके लिए डिज़ाइन, जो सिस्टम रोज़ चलाते हैं।"),
  ("हम सीखना कभी नहीं छोड़ते", "निरंतर प्रमाणन, आंतरिक ज्ञान-सत्र और ईमानदार समीक्षाएँ।"),
 ],
 global_h2="जड़ें भारत में, सेवा पूरी दुनिया में",
 chips=["भारत — डिलीवरी और कंसल्टिंग हब", "जापान — जापानी भाषा में सेवा", "UAE — खाड़ी क्षेत्र के ग्राहक", "सिंगापुर — APAC परियोजनाएँ", "वैश्विक विस्तार — दुनिया भर में रिमोट-फ़र्स्ट डिलीवरी"],
 cta_h2="आपका अगला ERP निर्णय संयोग पर छोड़ने लायक नहीं है।",
 cta_p="हमें बताइए आप क्या योजना बना रहे हैं — कार्यान्वयन, माइग्रेशन, सपोर्ट या प्रशिक्षण — हम स्पष्ट, विशेषज्ञ राय देंगे।",
)


def build_arabic():
    build_locale("ar", "العربية", True,
                 dict(skip="تجاوز إلى المحتوى", services="الخدمات", why="لماذا نحن",
                      **{"global": "حضورنا العالمي"}, portal="بوابة العملاء", contact="اتصل بنا"),
                 AR)


def build_hindi():
    build_locale("hi", "हिन्दी", False,
                 dict(skip="मुख्य सामग्री पर जाएँ", services="सेवाएँ", why="हमें क्यों चुनें", **{"global": "वैश्विक उपस्थिति"}, portal="क्लाइंट पोर्टल", contact="संपर्क करें"),
                 HI)


# ---------------------------------------------------------------- campaign template

def build_campaign():
    body = """
<section class="landing-hero">
  <canvas id="particle-canvas" aria-hidden="true" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
  <div class="container landing-grid" style="position:relative;">
    <div>
      <span class="eyebrow">Campaign landing template</span>
      <h1 style="font-size:clamp(2rem,4.5vw,3.4rem);">[Campaign headline: the one promise this campaign makes]</h1>
      <p class="hero-sub" style="margin:20px 0 28px;">[One short paragraph expanding the promise — who it is for and why now. Swap this copy per campaign; the layout, brand system and form stay.]</p>
      <ul style="list-style:none;display:grid;gap:12px;margin-bottom:8px;color:var(--ink-soft);">
        <li>◆ [Proof point one — concrete and defensible]</li>
        <li>◆ [Proof point two]</li>
        <li>◆ [Proof point three]</li>
      </ul>
    </div>
    <form class="form-card" data-demo-form novalidate>
      <h3 style="margin-bottom:6px;">[Offer: e.g. Book a 30-minute assessment call]</h3>
      <p class="form-note" style="margin-bottom:20px;">[One line of reassurance — no obligation, honest advice.]</p>
      <div class="form-grid" style="grid-template-columns:1fr;">
        <div class="form-field"><label for="lp-name">Full name <span class="req">*</span></label><input id="lp-name" type="text" required></div>
        <div class="form-field"><label for="lp-email">Work email <span class="req">*</span></label><input id="lp-email" type="email" required></div>
        <div class="form-field"><label for="lp-company">Company</label><input id="lp-company" type="text"></div>
      </div>
      <div class="honeypot" aria-hidden="true"><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
      <div style="margin-top:22px;"><button class="btn btn-gold" type="submit" style="width:100%;justify-content:center;">[Campaign CTA]</button></div>
      <div class="form-success" role="status">Thank you — we will be in touch shortly.</div>
    </form>
  </div>
</section>
<section class="marquee-band" aria-label="SAP technology expertise">
  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <span class="marquee-item">SAP S/4HANA</span><span class="marquee-item">SAP ECC</span><span class="marquee-item">SAP Business One</span><span class="marquee-item">FICO</span><span class="marquee-item">SAC</span><span class="marquee-item">MM</span><span class="marquee-item">SD</span><span class="marquee-item">ABAP</span><span class="marquee-item">BASIS</span>
    </div>
    <div class="marquee-track">
      <span class="marquee-item">SAP S/4HANA</span><span class="marquee-item">SAP ECC</span><span class="marquee-item">SAP Business One</span><span class="marquee-item">FICO</span><span class="marquee-item">SAC</span><span class="marquee-item">MM</span><span class="marquee-item">SD</span><span class="marquee-item">ABAP</span><span class="marquee-item">BASIS</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:820px;">
    <div class="section-head">
      <h2>[Section: why this matters / what you get]</h2>
      <p>[Two or three short paragraphs of campaign-specific substance. Confident, specific copy: lead with the strongest true claim this campaign can make — every figure and reference must be real and defensible.]</p>
    </div>
    <div style="display:flex;gap:16px;flex-wrap:wrap;">
      <a class="btn btn-gold" href="#top">[Repeat campaign CTA]</a>
      <a class="btn btn-outline" href="index.html">Visit the main site</a>
    </div>
  </div>
</section>
"""
    wrap("campaign-template.html", "[Campaign title] — SS ERP Solutions",
         "Reusable campaign landing-page template for SS ERP Solutions paid and email campaigns.",
         "campaign-template.html", body, root="", chrome=False, floats=True,
         extra_head='<meta name="robots" content="noindex">\n')


# ---------------------------------------------------------------- privacy

def build_privacy():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Privacy Notice</p>
    <h1>Privacy notice</h1>
    <p class="lead">A plain-language summary of what this website collects and how it is used.</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <h2>What we collect</h2>
    <p>When you submit the contact form, a careers application or the client-portal login, we receive the information you type — typically your name, email address, phone number, company and message, and for applications your CV. The site also uses a web-analytics tool to measure visits and enquiry sources in aggregate.</p>
    <h2>How we use it</h2>
    <p>Form submissions are delivered to the official SS ERP Solutions mailbox and used solely to respond to your enquiry or application. We do not sell or share your personal information with third parties for their own purposes.</p>
    <h2>Retention and contact</h2>
    <p>We keep correspondence for as long as needed to handle your enquiry and reasonable business records thereafter. To ask what we hold about you or to request deletion, write to <a href="mailto:""" + EMAIL + """\">""" + EMAIL + """</a>.</p>
    <h2>Cookies and chat</h2>
    <p>The site stores your dark/light theme preference in your browser. The embedded live-chat widget and WhatsApp click-to-chat are provided by third parties and apply their own privacy terms when you choose to use them.</p>
    <p class="form-note">This notice will be finalised with SS ERP Solutions before go-live.</p>
  </div>
</section>
"""
    wrap("privacy.html", "Privacy Notice — SS ERP Solutions",
         "Privacy notice for the SS ERP Solutions website: what we collect through forms and analytics, and how it is used.",
         "privacy.html", body, root="", floats=False)


# ---------------------------------------------------------------- split-out pages (menu restructure, client 2026-07-26)

def build_services_index():
    cards = "\n".join("""
      <a class="service-card reveal" href="%s.html">
        <span class="service-num">%s</span>
        <h3>%s</h3>
        <p>%s</p>
      </a>""" % (s["slug"], s["num"], s["name"], s["tag"]) for s in SERVICES)
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Services</p>
    <span class="eyebrow">What We Do</span>
    <h1>Twelve service lines. One standard of delivery.</h1>
    <p class="lead">From first blueprint to long-term support, every engagement follows the same discipline: understand the process before touching the technology.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="services-grid">""" + cards + """
    </div>
  </div>
</section>
<section class="section section-alt" id="engagement-models">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How We Engage</span>
      <h2>Three ways to work with us</h2>
    </div>
    <div class="grow-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Direct engagements</h3>
        <p>Project-based delivery and AMS retainers contracted directly with your business — from assessment to go-live and beyond.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Contract &amp; subcontract delivery</h3>
        <p>Consulting firms and system integrators subcontract SAP workstreams or complete deliveries to us — under your methodology or ours, white-label where required, confidentiality respected.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Consultant contracting</h3>
        <p>Our SAP consultants join your programme on contract — individually or as a ready-made pod — with the bench strength to scale up when your timeline demands it.</p>
      </div>
    </div>
  </div>
</section>
"""
    wrap("services/index.html", "Services — SS ERP Solutions",
         "Twelve service lines: SAP and Oracle ERP consulting, implementation, rollouts, AMS, analytics and custom dashboards, AI integration, and training.",
         "services/", body)


def build_about():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Company / About Us</p>
    <span class="eyebrow">Who We Are</span>
    <h1>Built on trust. Grown by referral.</h1>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="lead">SS ERP Solutions was founded in 2018 on a simple conviction: enterprise technology work should be done properly, or not at all.</p>
      <p style="margin-top:16px;">We have grown entirely through trust: every engagement we hold today traces back to a client who trusted us with something difficult — and then told someone else. It is a patient way to build a company, and the right one. SAP is where our practice was born and where it runs deepest — the majority of our consultants, projects and training hours live in the SAP ecosystem.</p>
      <p style="margin-top:16px;">Most of our clients are growing mid-size businesses: companies stepping up to enterprise-grade systems without enterprise-size IT departments. We built our delivery model for exactly that — senior attention, honest scope and systems your team can actually run.</p>
      <p>From our roots in India we support organisations across Japan, the UAE and Singapore — and we are expanding globally, with a delivery model built to serve clients anywhere: implementing and optimising enterprise systems, running transformation programmes, and keeping mission-critical applications healthy long after go-live.</p>
      <p>We hold ourselves to high professional standards, and we commit only to work we are confident we can deliver.</p>
    </div>
    <figure class="figure-card reveal">
      <div class="ph" style="flex-direction:column;gap:18px;"><img src="{ROOT}assets/logo-mark.png" alt="SS ERP Solutions" width="110" height="107" style="opacity:0.9;"><span style="letter-spacing:0.22em;">IMPLEMENT | OPTIMIZE | TRANSFORM</span></div>
      <figcaption>One team, one delivery standard — from Chennai to Tokyo, Dubai and Singapore.</figcaption>
    </figure>
  </div>
</section>
<section class="section section-alt" id="global">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Global Presence</span>
      <h2>Rooted in India. Delivering worldwide.</h2>
      <p>Active today across India, Japan, the UAE and Singapore — and built to serve clients anywhere, with distributed teams, follow-the-sun support and remote-first delivery.</p>
    </div>
    <div class="globe-wrap reveal">
      <img src="{ROOT}assets/worldmap.svg" alt="Map showing SS ERP Solutions presence in India, Japan, UAE and Singapore" style="width:100%;height:auto;">
      <div class="country-chips">
        <span class="country-chip">India — delivery &amp; consulting hub</span>
        <span class="country-chip">Japan — 日本語 client services</span>
        <span class="country-chip">UAE — Gulf enterprise clients</span>
        <span class="country-chip">Singapore — APAC engagements</span>
        <span class="country-chip">Expanding globally — remote-first delivery worldwide</span>
      </div>
    </div>
  </div>
</section>
<section class="section" id="vision-mission">
  <div class="container">
    <div class="vm-grid">
      <div class="vm-card vision reveal">
        <h3><span>◆</span> Our Vision</h3>
        <p>To be the consulting partner enterprises trust with their most important technology decisions — known for keeping every promise we make.</p>
      </div>
      <div class="vm-card mission reveal">
        <h3><span>◆</span> Our Mission</h3>
        <p>To deliver practical, high-quality enterprise solutions through the right teams and honest advice — and to grow the people we work with, on our clients' side and our own, with every engagement.</p>
      </div>
    </div>
  </div>
</section>
"""
    wrap("about/index.html", "About Us — SS ERP Solutions",
         "SS ERP Solutions: founded 2018, grown by client trust and referral, rooted in India and serving clients across Japan, the UAE, Singapore and worldwide.",
         "about/", body)


def build_whyus():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Company / Why Choose Us</p>
    <span class="eyebrow">Why Choose Us</span>
    <h1>The best team you can put on an enterprise programme</h1>
    <p class="lead">That is the standard we hold ourselves to — and these five commitments are how we prove it, on every engagement.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="commit-list reveal">
      <div class="commit">
        <div class="commit-num">01</div>
        <div>
          <h3>We deliver only what we are confident we can deliver</h3>
          <p>We check capability and capacity honestly before the contract is signed. Scope we accept is scope we complete.</p>
        </div>
      </div>
      <div class="commit">
        <div class="commit-num">02</div>
        <div>
          <h3>We build the right teams</h3>
          <p>Every engagement is staffed with consultants matched to the problem — the right modules, the right industry exposure, the right seniority — assembled for your problem from the first workshop.</p>
        </div>
      </div>
      <div class="commit">
        <div class="commit-num">03</div>
        <div>
          <h3>We value long-term relationships</h3>
          <p>Most of our clients have worked with us across multiple projects. We optimise for the relationship that continues long after go-live.</p>
        </div>
      </div>
      <div class="commit">
        <div class="commit-num">04</div>
        <div>
          <h3>We build practical, high-quality solutions</h3>
          <p>Fit-for-purpose beats over-engineered. We design for the people who will run the system on a Tuesday afternoon.</p>
        </div>
      </div>
      <div class="commit">
        <div class="commit-num">05</div>
        <div>
          <h3>We never stop learning</h3>
          <p>The SAP landscape moves; so do we. Continuous certification, internal knowledge sessions and honest post-project reviews keep our standards current.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">What Clients Say</span>
      <h2>In our clients' words</h2>
    </div>
    <div class="testi-grid">
      <div class="testi-card reveal">
        <div class="testi-stars" aria-hidden="true">★★★★★</div>
        <p class="testi-quote">"They told us in week two that our original scope was wrong — and they were right. That honesty saved the programme."</p>
        <div class="testi-who">
          <div class="name">Chief Financial Officer</div>
          <div class="role">Manufacturing group, India · S/4HANA implementation</div>
        </div>
      </div>
      <div class="testi-card reveal">
        <div class="testi-stars" aria-hidden="true">★★★★★</div>
        <p class="testi-quote">"Three years after go-live, the same team still supports us. That continuity is why we keep coming back."</p>
        <div class="testi-who">
          <div class="name">Head of IT</div>
          <div class="role">Trading company, Japan · AMS partnership</div>
        </div>
      </div>
      <div class="testi-card reveal">
        <div class="testi-stars" aria-hidden="true">★★★★★</div>
        <p class="testi-quote">"Our rollout covered four countries and met every statutory deadline. The PMO discipline was exceptional."</p>
        <div class="testi-who">
          <div class="name">Programme Director</div>
          <div class="role">Enterprise group, UAE · Multi-country rollout</div>
        </div>
      </div>
    </div>
    <div style="margin-top:40px;" class="reveal">
      <a class="btn btn-gold" href="{ROOT}contact/index.html">Start a conversation</a>
    </div>
  </div>
</section>
"""
    wrap("why-us/index.html", "Why Choose Us — SS ERP Solutions",
         "Five commitments kept on every engagement: honest scope, the right teams, long-term relationships, practical solutions and continuous learning.",
         "why-us/", body)


def build_growing():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Growing Together</p>
    <span class="eyebrow">Growing Together</span>
    <h1>We grow people alongside systems</h1>
    <p class="lead">The consulting industry runs on talent. We invest in it deliberately — for our clients' teams, for young professionals entering the field, and for our own people.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grow-grid">
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>SAP Training Programmes</h3>
        <p>Structured, practitioner-led training in SAP functional and technical modules — taught by consultants who deliver client projects every week.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Internships</h3>
        <p>Real project exposure for graduates and early-career professionals, with mentoring that treats interns as future colleagues.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Mentoring</h3>
        <p>One-to-one guidance from senior consultants on career paths, specialisation choices and the habits that make great consultants.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Certification Guidance</h3>
        <p>Practical advice on which SAP certifications matter for your goals, and how to prepare for them efficiently.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Practical Project Exposure</h3>
        <p>Learning by doing — supervised work on live project artefacts, sandboxes and realistic case scenarios.</p>
      </div>
      <div class="grow-card reveal">
        <span class="ico" aria-hidden="true">◆</span>
        <h3>Knowledge Transfer</h3>
        <p>Every engagement ends with your team stronger: documented, demonstrated and handed over properly.</p>
      </div>
    </div>
    <div style="margin-top:40px;display:flex;gap:16px;flex-wrap:wrap;" class="reveal">
      <a class="btn btn-maroon" href="{ROOT}services/training-internships-knowledge-transfer.html">Training &amp; internship programmes</a>
      <a class="btn btn-outline" href="{ROOT}careers/index.html">Join the team</a>
    </div>
  </div>
</section>
"""
    wrap("growing-together/index.html", "Growing Together — SS ERP Solutions",
         "SAP training, internships, mentoring, certification guidance and knowledge transfer — the people-development side of SS ERP Solutions.",
         "growing-together/", body)


FAQS = [
 ("What services does SS ERP Solutions provide?",
  "We provide twelve service lines across the enterprise technology lifecycle: ERP consulting, enterprise application implementation, greenfield and brownfield projects, rollouts, upgrades and migrations, digital transformation, PMO, application management services (AMS), production support and enhancements, analytics, reporting and custom dashboards, SAP training, internships and knowledge transfer, Oracle and multi-ERP solutions, and AI integration and intelligent automation."),
 ("Which ERP platforms and modules do you work with?",
  "Our deepest expertise is SAP: S/4HANA, ECC and Business One, with functional depth in FICO, Group Reporting, Central Finance, Treasury, RAR, MM, SD, PP, QM and PM, analytics on SAP Analytics Cloud (SAC), and technical capability in ABAP and BASIS. We also implement and support Oracle Fusion Cloud ERP, Oracle NetSuite and other leading platforms such as Microsoft Dynamics 365 where they are the better fit, and build custom dashboards and AI integrations across all of them."),
 ("Which countries do you operate in?",
  "We are headquartered in India with active engagements across Japan, the UAE and Singapore, and we are expanding globally — our remote-first delivery model serves clients worldwide. Our Japan client base is served in Japanese, and this website is available in a Japanese-language version."),
 ("Do you handle S/4HANA migrations from SAP ECC?",
  "Yes. We deliver both greenfield S/4HANA implementations and brownfield system conversions from ECC, including assessment, roadmap, data migration, custom-code remediation and post-go-live support. The right path depends on your landscape — we assess before we recommend."),
 ("Can you support our SAP system after go-live?",
  "Yes. Our application management services (AMS) and production support offerings provide ongoing incident resolution, monitoring, small enhancements and periodic health checks under defined service levels — for systems we implemented and for systems we didn't."),
 ("Do you offer SAP training and internships?",
  "Yes — this is our Growing Together programme. We run practitioner-led SAP training, structured internships with real project exposure, mentoring, and certification guidance for graduates and working professionals."),
 ("Do you take contract and subcontract work from other consulting firms?",
  "Yes. Alongside direct client engagements, consulting firms and system integrators regularly subcontract SAP workstreams or complete deliveries to us, and we place consultants on contract into client and partner programmes. White-label arrangements and confidentiality are respected as a matter of course."),
 ("How do your engagements usually start?",
  "With a conversation. We start by understanding your processes, landscape and goals — typically a short discovery discussion followed by a written proposal with honest scope, team and timeline. We commit only to work we are confident we can deliver."),
 ("How can we contact SS ERP Solutions?",
  "Use the contact form on this site, email us at " + EMAIL + ", or reach us instantly through the WhatsApp chat button. We respond to every serious enquiry."),
]


def build_faq():
    import json as _json
    items = "\n".join("""
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">%s<span class="chev">▼</span></button>
        <div class="faq-a"><div class="faq-a-inner">%s</div></div>
      </div>""" % (q, a) for q, a in FAQS)
    ld = _json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]
    }, ensure_ascii=False)
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Company / FAQ</p>
    <span class="eyebrow">FAQ</span>
    <h1>Questions we're asked most</h1>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="faq-list reveal">""" + items + """
    </div>
    <div style="margin-top:36px;" class="reveal">
      <a class="btn btn-gold" href="{ROOT}contact/index.html">Ask us something else</a>
    </div>
  </div>
</section>
<script type="application/ld+json">""" + ld + """</script>
"""
    wrap("faq/index.html", "FAQ — SS ERP Solutions",
         "Frequently asked questions about SS ERP Solutions: services, SAP and Oracle platform coverage, countries, S/4HANA migrations, support and training.",
         "faq/", body)


# ---------------------------------------------------------------- 404 & terms

def build_404():
    body = """
<section class="page-hero" style="min-height:60vh;display:flex;align-items:center;">
  <div class="container" style="text-align:center;">
    <p class="mono" style="font-size:4rem;color:var(--gold);">404</p>
    <h1>This page doesn't exist</h1>
    <p class="lead" style="margin:18px auto 30px;max-width:520px;">The address may have changed or been mistyped. Everything we offer is one click from the homepage.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn-gold" href="{ROOT}index.html">Go to homepage</a>
      <a class="btn btn-outline" href="{ROOT}contact/index.html">Contact us</a>
    </div>
  </div>
</section>
"""
    wrap("404.html", "Page not found — SS ERP Solutions",
         "The page you were looking for does not exist on sserpsolutions.net.",
         "404.html", body, root="", floats=False,
         extra_head='<meta name="robots" content="noindex">\n')


def build_terms():
    body = """
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="{ROOT}index.html">Home</a> / Terms of Use</p>
    <h1>Terms of use</h1>
    <p class="lead">The short version of using this website fairly.</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <h2>Use of this site</h2>
    <p>This website presents SS ERP Solutions' services and publications. You may browse, link to and quote it with attribution. You may not scrape it wholesale, misrepresent its content, or attempt to disrupt or gain unauthorised access to any part of it, including the client portal.</p>
    <h2>Content and no advice</h2>
    <p>Articles and case studies are general commentary based on our project experience. They are not advice for your specific situation — engagements begin with a conversation, not a blog post. Figures, testimonials and case material are published only once approved by the clients involved.</p>
    <h2>Intellectual property</h2>
    <p>The SS ERP Solutions name, interlocking-S mark and site content belong to SS ERP Solutions. SAP, Oracle, NetSuite, Microsoft and other product names are trademarks of their respective owners and are used here only to describe our capability with those products.</p>
    <h2>Liability</h2>
    <p>The site is provided as-is. We keep it accurate and available with reasonable care, but we accept no liability for decisions made on the basis of website content alone, or for interruptions outside our control.</p>
    <p class="form-note">These terms will be finalised with SS ERP Solutions before go-live. Questions: <a href="mailto:""" + EMAIL + """\">""" + EMAIL + """</a>.</p>
  </div>
</section>
"""
    wrap("terms.html", "Terms of Use — SS ERP Solutions",
         "Terms of use for the SS ERP Solutions website.",
         "terms.html", body, root="", floats=False)


# ---------------------------------------------------------------- assets & seo

def build_assets():
    fav = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="18" fill="#0B1220"/><polygon points="50,10 84,30 84,70 50,90 16,70 16,30" fill="none" stroke="#C9A24B" stroke-width="5"/><text x="53" y="68" text-anchor="middle" font-family="Arial, sans-serif" font-size="44" font-weight="800" fill="#8C1D24">S</text><text x="47" y="64" text-anchor="middle" font-family="Arial, sans-serif" font-size="44" font-weight="800" fill="#C9A24B">S</text></svg>"""
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    with open(os.path.join(SITE, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(fav)
    print("wrote assets/favicon.svg")

    base = "https://www.sserpsolutions.net/"
    urls = ["", "ja/", "ar/", "hi/", "services/", "about/", "why-us/", "growing-together/", "faq/",
            "insights/", "careers/", "contact/", "privacy.html", "terms.html"]
    urls += ["services/%s.html" % s["slug"] for s in SERVICES]
    urls += ["insights/%s.html" % a["slug"] for a in ARTICLES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append("  <url><loc>%s%s</loc></url>" % (base, u))
    sm.append("</urlset>")
    with open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    print("wrote sitemap.xml")

    with open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /portal/\nSitemap: %ssitemap.xml\n" % base)
    print("wrote robots.txt")

    manifest = """{
  "name": "SS ERP Solutions",
  "short_name": "SS ERP",
  "description": "Enterprise technology consulting - SAP, Oracle and multi-ERP delivery, dashboards and AI integration.",
  "start_url": "/",
  "display": "browser",
  "background_color": "#0B1220",
  "theme_color": "#0B1220",
  "icons": [{"src": "assets/logo-mark.png", "sizes": "112x109", "type": "image/png"}]
}
"""
    with open(os.path.join(SITE, "site.webmanifest"), "w", encoding="utf-8") as f:
        f.write(manifest)
    print("wrote site.webmanifest")

    well_known = os.path.join(SITE, ".well-known")
    os.makedirs(well_known, exist_ok=True)
    with open(os.path.join(well_known, "security.txt"), "w", encoding="utf-8") as f:
        f.write("Contact: mailto:%s\nExpires: 2027-07-25T00:00:00.000Z\nPreferred-Languages: en, ja\nCanonical: https://www.sserpsolutions.net/.well-known/security.txt\n" % EMAIL)
    print("wrote .well-known/security.txt")

    # og-image.png is rendered from the vector lockup by _build/logopng flow — not regenerated here


if __name__ == "__main__":
    build_services_index()
    build_about()
    build_whyus()
    build_growing()
    build_faq()
    build_services()
    build_insights()
    build_careers()
    build_contact()
    build_portal()
    build_japanese()
    build_arabic()
    build_hindi()
    build_campaign()
    build_privacy()
    build_404()
    build_terms()
    build_assets()
    print("done.")
