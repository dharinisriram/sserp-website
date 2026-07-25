# SS ERP Solutions — Corporate Website

Working prototype of www.sserpsolutions.net, built to **PRD v1.2** (People Axis Consultants, 25 Jul 2026)
with client amendments agreed in the build interview of 25 Jul 2026. Pure static HTML/CSS/JS —
no build step, no dependencies — designed to be rebuilt 1:1 on Webflow per the PRD's technical plan.

## Run it

```
cd website
python -m http.server 8080
# open http://localhost:8080
```

(Or just open `index.html` in a browser — everything works from file:// except web fonts need internet.)

## What's here

| Area | Path | Notes |
|---|---|---|
| Homepage (marketing landing) | `index.html` | Hero, counters, 6 featured services, marquees, teasers + testimonials; full content lives on dedicated pages (client restructure 26 Jul: dropdown menus, no single-page site) |
| Services overview + 12 detail pages | `services/` | Ten PRD service lines **+ Oracle & Multi-ERP + AI Integration** |
| Company pages | `about/`, `why-us/`, `faq/`, `growing-together/` | About (story, global map, vision/mission), commitments + testimonials, FAQ w/ JSON-LD, people development |
| Insights | `insights/` | 3 starter articles (drafts for client review) + pending case-study card |
| Careers | `careers/` | 3 sample roles (placeholders) + application form |
| Contact | `contact/` | Spam-protected form (honeypot), direct contacts, WhatsApp |
| Client portal | `portal/` | Login screen + **demo** dashboard — real scope set by the PRD §10 workshop (milestone M4) |
| Japanese version | `ja/` | Key-page content in Japanese with language switcher; machine-assisted draft, needs human review before publishing (PRD §9) |
| Campaign template | `campaign-template.html` | Reusable landing template, `noindex` |
| Privacy | `privacy.html` | Basic notice per PRD §11 |
| SEO | `sitemap.xml`, `robots.txt`, per-page meta/OG | Portal disallowed in robots |

Subpages are generated from `_build/generate.py` (shared header/footer). After editing it:
`python _build/generate.py`.

## Decisions from the client interview (25 Jul 2026)

- **Theme:** dark navy (PRD default) **and** light, user-toggleable (☀/🌙 in header, persisted in localStorage).
- **Founding year:** 2018 — published.
- **Official email:** `support@sserpsolutions.net` (not the PRD-suggested info@).
- **Key numbers:** placeholders retained pending real figures.
- **Careers:** sample roles + form. **Insights:** drafted starter articles. **Portal:** login + demo dashboard. **Testimonials:** placeholder strip added.
- **Offering expanded** beyond the PRD's ten lines: Oracle Fusion Cloud/NetSuite & multi-ERP, custom dashboards (Power BI/Tableau/custom), AI integration & intelligent automation.
- **Design reference:** vantagepointconsulting.com/erp-implementation — confident contrast headlines, methodology-first service pages, repeated CTAs, closing CTA section.
- **Logo:** official interlocking-S mark extracted from the PRD cover (`assets/logo-mark.png`, `assets/logo-full.png`).

## Still placeholder (PRD §10 — needed from SS ERP Solutions)

- Key-number figures (years, projects, clients) — marked in `index.html`
- Client testimonial quotes with written permission (placeholder cards flagged on-page)
- Case-study material for Insights
- Real open roles for Careers
- WhatsApp business number (`wa.me/910000000000` placeholder), phone, registered address
- LinkedIn company page URL
- Team/office photography (styled placeholder in Who We Are)
- Japanese content review by a human translator
- Portal requirements workshop → real portal build (Next.js on Webflow Cloud per PRD §9)

## Webflow rebuild notes

- Colours/typography tokens are in `css/styles.css` `:root` (navy `#0B1220`, gold `#C9A24B`, maroon `#8C1D24`; Archivo / Instrument Sans / IBM Plex Mono).
- Interactions to recreate with Webflow interactions/GSAP: particle hero, scroll counters, marquee, reveals, accordion.
- Forms here are demo-only (client-side validation + honeypot); on Webflow use native forms with spam protection and file upload.
- Insights/Careers become Webflow CMS collections; articles in `insights/` are the seed content.
- Japanese pages map to Webflow Localization (one locale) with localized SEO.
