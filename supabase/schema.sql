-- SS ERP Solutions — client portal schema
-- Run once in Supabase: SQL Editor → New query → paste → Run.

-- ───────────── Tables ─────────────
create table if not exists public.companies (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  full_name text,
  email text,
  company_id uuid references public.companies(id) on delete set null,
  role text not null default 'client' check (role in ('client','admin')),
  created_at timestamptz not null default now()
);

create table if not exists public.projects (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  name text not null,
  summary text,
  phase text not null default 'Assess' check (phase in ('Assess','Plan','Deliver','Improve')),
  status text not null default 'On track' check (status in ('On track','At risk','Blocked','On hold','Completed')),
  progress int not null default 0 check (progress between 0 and 100),
  start_date date,
  target_date date,
  created_at timestamptz not null default now()
);

create table if not exists public.project_updates (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references public.projects(id) on delete cascade,
  author_id uuid references public.profiles(id) on delete set null,
  body text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.tickets (
  id uuid primary key default gen_random_uuid(),
  ref serial,
  company_id uuid not null references public.companies(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  created_by uuid references public.profiles(id) on delete set null,
  title text not null,
  description text,
  priority text not null default 'Medium' check (priority in ('Low','Medium','High','Critical')),
  status text not null default 'Open' check (status in ('Open','In progress','Awaiting client','Resolved','Closed')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.ticket_comments (
  id uuid primary key default gen_random_uuid(),
  ticket_id uuid not null references public.tickets(id) on delete cascade,
  author_id uuid references public.profiles(id) on delete set null,
  body text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.documents (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  name text not null,
  storage_path text not null unique,
  size_bytes bigint,
  uploaded_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);

create table if not exists public.inquiries (
  id uuid primary key default gen_random_uuid(),
  full_name text not null,
  email text not null,
  company text,
  topic text,
  message text not null,
  handled boolean not null default false,
  created_at timestamptz not null default now()
);

-- ───────────── Helpers ─────────────
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;

create or replace function public.my_company() returns uuid
language sql stable security definer set search_path = public as $$
  select company_id from public.profiles where id = auth.uid();
$$;

-- Auto-create a profile for every new auth user.
-- Role and company are NEVER taken from user metadata (a sign-up could forge them);
-- the portal's admin screen sets them server-side after the invite.
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, full_name)
  values (new.id, new.email, new.raw_user_meta_data->>'full_name')
  on conflict (id) do nothing;
  return new;
end; $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- Clients cannot change their own role or company
create or replace function public.protect_profile() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  -- auth.uid() is null for the service role / SQL editor, which are trusted
  if auth.uid() is not null and not public.is_admin() and (new.role <> old.role or new.company_id is distinct from old.company_id) then
    raise exception 'Not allowed';
  end if;
  return new;
end; $$;
drop trigger if exists protect_profile on public.profiles;
create trigger protect_profile before update on public.profiles
  for each row execute function public.protect_profile();

create or replace function public.touch_ticket() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end; $$;
drop trigger if exists touch_ticket on public.tickets;
create trigger touch_ticket before update on public.tickets for each row execute function public.touch_ticket();

-- ───────────── Row Level Security ─────────────
alter table public.companies       enable row level security;
alter table public.profiles        enable row level security;
alter table public.projects        enable row level security;
alter table public.project_updates enable row level security;
alter table public.tickets         enable row level security;
alter table public.ticket_comments enable row level security;
alter table public.documents       enable row level security;
alter table public.inquiries       enable row level security;

-- companies
drop policy if exists "companies read" on public.companies;
create policy "companies read" on public.companies for select using (public.is_admin() or id = public.my_company());
drop policy if exists "companies admin" on public.companies;
create policy "companies admin" on public.companies for all using (public.is_admin()) with check (public.is_admin());

-- profiles
drop policy if exists "profiles read" on public.profiles;
create policy "profiles read" on public.profiles for select
  using (public.is_admin() or id = auth.uid() or company_id = public.my_company() or role = 'admin');
drop policy if exists "profiles self update" on public.profiles;
create policy "profiles self update" on public.profiles for update using (id = auth.uid() or public.is_admin());
drop policy if exists "profiles admin" on public.profiles;
create policy "profiles admin" on public.profiles for all using (public.is_admin()) with check (public.is_admin());

-- projects (clients read only)
drop policy if exists "projects read" on public.projects;
create policy "projects read" on public.projects for select using (public.is_admin() or company_id = public.my_company());
drop policy if exists "projects admin" on public.projects;
create policy "projects admin" on public.projects for all using (public.is_admin()) with check (public.is_admin());

-- project updates (clients read only)
drop policy if exists "updates read" on public.project_updates;
create policy "updates read" on public.project_updates for select using (
  public.is_admin() or exists (select 1 from public.projects p where p.id = project_id and p.company_id = public.my_company()));
drop policy if exists "updates admin" on public.project_updates;
create policy "updates admin" on public.project_updates for all using (public.is_admin()) with check (public.is_admin());

-- tickets: clients read + create for their company; admins everything
drop policy if exists "tickets read" on public.tickets;
create policy "tickets read" on public.tickets for select using (public.is_admin() or company_id = public.my_company());
drop policy if exists "tickets create" on public.tickets;
create policy "tickets create" on public.tickets for insert
  with check (company_id = public.my_company() and created_by = auth.uid());
drop policy if exists "tickets admin" on public.tickets;
create policy "tickets admin" on public.tickets for all using (public.is_admin()) with check (public.is_admin());

-- ticket comments
drop policy if exists "comments read" on public.ticket_comments;
create policy "comments read" on public.ticket_comments for select using (
  public.is_admin() or exists (select 1 from public.tickets t where t.id = ticket_id and t.company_id = public.my_company()));
drop policy if exists "comments create" on public.ticket_comments;
create policy "comments create" on public.ticket_comments for insert with check (
  author_id = auth.uid() and (public.is_admin() or exists (select 1 from public.tickets t where t.id = ticket_id and t.company_id = public.my_company())));

-- documents
drop policy if exists "docs read" on public.documents;
create policy "docs read" on public.documents for select using (public.is_admin() or company_id = public.my_company());
drop policy if exists "docs create" on public.documents;
create policy "docs create" on public.documents for insert with check (
  uploaded_by = auth.uid() and (public.is_admin() or company_id = public.my_company()));
drop policy if exists "docs admin" on public.documents;
create policy "docs admin" on public.documents for all using (public.is_admin()) with check (public.is_admin());

-- inquiries: anyone can submit, only admins read
drop policy if exists "inquiries submit" on public.inquiries;
create policy "inquiries submit" on public.inquiries for insert to anon, authenticated with check (true);
drop policy if exists "inquiries admin" on public.inquiries;
create policy "inquiries admin" on public.inquiries for all using (public.is_admin()) with check (public.is_admin());

-- ───────────── Storage (private bucket, one folder per company) ─────────────
insert into storage.buckets (id, name, public) values ('documents', 'documents', false)
  on conflict (id) do nothing;

drop policy if exists "docs storage read" on storage.objects;
create policy "docs storage read" on storage.objects for select using (
  bucket_id = 'documents' and (public.is_admin() or (storage.foldername(name))[1] = public.my_company()::text));
drop policy if exists "docs storage upload" on storage.objects;
create policy "docs storage upload" on storage.objects for insert with check (
  bucket_id = 'documents' and (public.is_admin() or (storage.foldername(name))[1] = public.my_company()::text));
drop policy if exists "docs storage admin delete" on storage.objects;
create policy "docs storage admin delete" on storage.objects for delete using (bucket_id = 'documents' and public.is_admin());
