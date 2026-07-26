# Deploying to www.sserpsolutions.net

The site in `website/` is fully static — it can go live on the real domain today with any
of the routes below. **In every route, the GoDaddy MX records must stay untouched** so
Google Workspace email keeps working (PRD §9 requirement).

## Route A — Webflow (the PRD's target platform)
The PRD plans Webflow as the production platform (CMS, forms, Localization, Webflow Cloud
portal). This build is the approved prototype to rebuild there.
1. Buy the premium template + Webflow Premium site plan (client sign-off per PRD §10).
2. Rebuild pages in Webflow using this prototype as the visual/content spec.
3. In Webflow → Site settings → Publishing, add `www.sserpsolutions.net` (+ apex redirect).
4. At GoDaddy DNS: `CNAME www → proxy-ssl.webflow.com`, apex `A` records per Webflow's
   instructions. **Do not touch MX or TXT (SPF/DKIM) records.**

## Route B — Static host now, Webflow later (fastest to live)
Puts this exact build on the domain in under an hour; can be swapped to Webflow at any time
by changing the same DNS records.

**Cloudflare Pages (recommended):** create project → connect this repo (or drag-drop the
`website/` folder) → build command: none, output dir: `website` → add custom domain
`www.sserpsolutions.net` → follow its DNS instructions at GoDaddy (CNAME `www`).

**Netlify:** `netlify deploy --prod --dir=website` (config in `netlify.toml`), then add the
custom domain and set GoDaddy `CNAME www → <site>.netlify.app`.

**GitHub Pages (prepared — branches ready):** `main` holds the project, `gh-pages` holds
the website at its root with the CNAME file already in place. Once the GitHub repo exists:
1. `git remote add origin <repo-url>` then `git push -u origin main gh-pages`
2. On GitHub: Settings → Pages → Source: *Deploy from a branch* → Branch: `gh-pages` / `/ (root)` → Save
3. Same page: Custom domain = `www.sserpsolutions.net` → Save (then tick *Enforce HTTPS* once the cert issues)
4. GoDaddy DNS (leave MX/TXT untouched):
   - CNAME `www` → `YOUR-USERNAME.github.io`
   - Apex `@` A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
5. Wait for DNS (minutes to a few hours) — the site is then live at https://www.sserpsolutions.net

**Old note — GitHub Pages:** push this repo to GitHub → Settings → Pages → deploy from branch,
folder `/website` (the `website/CNAME` file already names the domain) → GoDaddy
`CNAME www → <user>.github.io`.

## GoDaddy DNS — the only records to change
| Type | Name | Value | Note |
|---|---|---|---|
| CNAME | `www` | per chosen host | the live site |
| A / ALIAS | `@` | per chosen host | apex → redirect to www |
| — | MX, TXT (SPF/DKIM/DMARC) | **leave exactly as-is** | Google Workspace email |

`sserpsolutions.international` → domain forwarding (301) to `https://www.sserpsolutions.net`.

## After go-live (PRD milestone M7)
1. Verify https://www.sserpsolutions.net loads with a valid certificate.
2. Send + receive a test email on the domain — confirms MX untouched.
3. Google Search Console: add property, submit `sitemap.xml`.
4. Add the chosen analytics tool and the live-chat widget snippet.
5. Replace remaining placeholders (figures, testimonials, WhatsApp number, roles, photos).
