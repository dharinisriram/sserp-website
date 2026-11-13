# SS ERP Solutions — website + client portal

Next.js 15 (App Router) · Tailwind v4 · Supabase (auth, Postgres, storage) · deploys to Vercel.

- **Public site:** `/`, `/about`, `/services`, `/insights`, `/contact`. Contact form submissions are saved to Supabase and appear in Admin → Inquiries.
- **Client portal:** `/portal`. Access is by invitation only. Every table and file is protected by Row Level Security, so a client only ever sees their own company's data.
  - Clients can see their projects (phase, status, progress, updates), raise and reply to support tickets, and upload or download documents.
  - Admins (the SS ERP team) see all clients. They can invite users, create projects, post updates, change ticket status, and read inquiries.

## 1. Supabase setup (one time)

1. Create a project at supabase.com (choose the Mumbai region).
2. Open **SQL Editor → New query**, paste `supabase/schema.sql` and click **Run**. This creates the tables, the security policies and the private `documents` storage bucket.
3. Go to **Authentication → Sign In / Providers → Email**. Turn **off** "Allow new users to sign up", because the portal is invite-only.
4. Go to **Authentication → URL Configuration**. Set the Site URL to `https://sserpsolutions.net` and add `https://sserpsolutions.net/**` under Redirect URLs. While testing, add your `*.vercel.app` URL too.
5. Go to **Authentication → Email Templates** and replace the link in two templates:
   - **Invite user:**
     ```html
     <h2>You're invited to the SS ERP Solutions client portal</h2>
     <p><a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=invite&next=/portal/set-password">Accept invitation</a></p>
     ```
   - **Reset password:**
     ```html
     <h2>Reset your portal password</h2>
     <p><a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=recovery&next=/portal/set-password">Set a new password</a></p>
     ```
6. Optional but recommended: under **Authentication → SMTP**, send email from support@sserpsolutions.net. Supabase's built-in sender is heavily rate-limited.

## 2. Deploy on Vercel

1. Push this folder to a GitHub repo, then in Vercel choose **Add New → Project** and import it.
2. Add these environment variables (values are in Supabase → Project Settings → API):

   | Name | Value |
   |---|---|
   | `NEXT_PUBLIC_SUPABASE_URL` | Project URL |
   | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | anon / publishable key |
   | `SUPABASE_SERVICE_ROLE_KEY` | service_role / secret key (keep this secret) |
   | `NEXT_PUBLIC_SITE_URL` | `https://sserpsolutions.net` |

3. Deploy. Then go to **Settings → Domains**, add `sserpsolutions.net` and `www.sserpsolutions.net`, and update DNS at the registrar as Vercel instructs. Once the new site works, remove the domain from Framer.

## 3. Create the first admin

1. In Supabase, go to **Authentication → Users → Add user → Send invitation** and enter Shalini's email.
2. After she has set her password, run this in the SQL Editor:
   ```sql
   update public.profiles set role = 'admin' where email = 'her@email.com';
   ```
3. From then on she manages everything from **/portal/admin**: add a company, invite its users, then create projects.

## Local development

```bash
cp .env.example .env.local   # fill in values
npm install
npm run dev                  # http://localhost:3000
```

## Content still to come from Shalini

The team, testimonials, client logos, headline stats and Insights articles were all template placeholders, so they have been removed. Add them back once real content exists:

- **Services, stages, case studies:** `src/lib/content.ts`
- **About page:** `src/app/(site)/about/page.tsx`
- **Insights:** `src/app/(site)/insights/page.tsx`
