import Link from "next/link";
import { Badge, Empty } from "@/components/portal/Badge";
import { SubmitButton } from "@/components/portal/SubmitButton";
import { fmtDate, requireAdmin, type Profile } from "@/lib/portal";
import { createCompany, createProject, inviteUser, removeMember, toggleInquiry, updateMember } from "../../actions";

type Inquiry = { id: string; full_name: string; email: string; company: string | null; topic: string | null; message: string; handled: boolean; created_at: string };
type Company = { id: string; name: string };
type ProjectRow = { id: string; name: string; status: string; phase: string; progress: number; companies: { name: string } | null };

const TABS = [
  { id: "inquiries", label: "Inquiries" },
  { id: "clients", label: "Clients & users" },
  { id: "projects", label: "Projects" },
];

export default async function Admin({ searchParams }: { searchParams: Promise<{ tab?: string; msg?: string }> }) {
  const { tab = "inquiries", msg } = await searchParams;
  const { supabase, user } = await requireAdmin();

  return (
    <div className="space-y-8">
      <div>
        <p className="eyebrow">SS ERP team only</p>
        <h1 className="mt-2 font-serif text-4xl">Admin</h1>
      </div>
      <div className="flex gap-2 border-b border-line">
        {TABS.map((t) => (
          <Link key={t.id} href={`/portal/admin?tab=${t.id}`}
            className={`-mb-px border-b-2 px-4 py-2.5 text-sm ${tab === t.id ? "border-accent font-semibold" : "border-transparent text-muted hover:text-ink"}`}>{t.label}</Link>
        ))}
      </div>
      {msg && <p className="rounded-lg bg-ink/5 px-4 py-3 text-sm">{msg}</p>}

      {tab === "inquiries" && <Inquiries supabase={supabase} />}
      {tab === "clients" && <Clients supabase={supabase} selfId={user.id} />}
      {tab === "projects" && <Projects supabase={supabase} />}
    </div>
  );
}

type SB = Awaited<ReturnType<typeof requireAdmin>>["supabase"];

async function Inquiries({ supabase }: { supabase: SB }) {
  const { data } = await supabase.from("inquiries").select("*").order("handled").order("created_at", { ascending: false }).limit(100).returns<Inquiry[]>();
  if (!data?.length) return <Empty>No inquiries from the contact form yet.</Empty>;
  return (
    <ul className="space-y-4">
      {data.map((q) => (
        <li key={q.id} className={`card p-6 ${q.handled ? "opacity-60" : ""}`}>
          <div className="flex flex-wrap items-start justify-between gap-3">
            <div>
              <p className="font-semibold">{q.full_name}{q.company && <span className="font-normal text-muted"> · {q.company}</span>}</p>
              <a href={`mailto:${q.email}`} className="text-sm text-accent hover:underline">{q.email}</a>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-xs text-muted">{fmtDate(q.created_at)}</span>
              {q.topic && <span className="rounded-full bg-paper px-2.5 py-0.5 text-xs">{q.topic}</span>}
            </div>
          </div>
          <p className="mt-3 whitespace-pre-line text-sm leading-relaxed">{q.message}</p>
          <form action={toggleInquiry} className="mt-4">
            <input type="hidden" name="id" value={q.id} /><input type="hidden" name="handled" value={String(!q.handled)} />
            <button className="text-xs font-semibold text-muted hover:text-ink">{q.handled ? "Mark as new" : "Mark as handled ✓"}</button>
          </form>
        </li>
      ))}
    </ul>
  );
}

async function Clients({ supabase, selfId }: { supabase: SB; selfId: string }) {
  const [{ data: companies }, { data: people }] = await Promise.all([
    supabase.from("companies").select("id,name").order("name").returns<Company[]>(),
    supabase.from("profiles").select("*").order("created_at", { ascending: false }).returns<Profile[]>(),
  ]);
  const cname = (id: string | null) => companies?.find((c) => c.id === id)?.name ?? "—";

  return (
    <div className="space-y-10">
      <div className="grid gap-6 lg:grid-cols-2">
        <form action={createCompany} className="card space-y-4 p-6">
          <h2 className="font-serif text-xl">Add a client company</h2>
          <input name="name" required className="input" placeholder="Company name" />
          <SubmitButton>Add company</SubmitButton>
        </form>
        <form action={inviteUser} className="card space-y-4 p-6">
          <h2 className="font-serif text-xl">Invite a user</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            <input name="full_name" className="input" placeholder="Full name" />
            <input name="email" type="email" required className="input" placeholder="Email" />
            <select name="company_id" className="input"><option value="">— Company —</option>{companies?.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</select>
            <select name="role" className="input" defaultValue="client"><option value="client">Client</option><option value="admin">SS ERP team (admin)</option></select>
          </div>
          <SubmitButton>Send invitation</SubmitButton>
        </form>
      </div>

      <section>
        <h2 className="mb-4 font-serif text-2xl">Users</h2>
        <div className="card overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="border-b border-line text-xs uppercase tracking-wider text-muted">
              <tr><th className="px-5 py-3">User</th><th className="px-5 py-3">Company / role</th><th className="px-5 py-3">Since</th><th /></tr>
            </thead>
            <tbody className="divide-y divide-line">
              {people?.map((p) => (
                <tr key={p.id}>
                  <td className="px-5 py-3"><p className="font-medium">{p.full_name || "—"}</p><p className="text-xs text-muted">{p.email}</p></td>
                  <td className="px-5 py-3">
                    {p.id === selfId ? <span className="text-muted">{cname(p.company_id)} · {p.role} (you)</span> : (
                      <form action={updateMember} className="flex flex-wrap gap-2">
                        <input type="hidden" name="id" value={p.id} />
                        <select name="company_id" defaultValue={p.company_id ?? ""} className="input w-auto py-1.5"><option value="">—</option>{companies?.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</select>
                        <select name="role" defaultValue={p.role} className="input w-auto py-1.5"><option value="client">Client</option><option value="admin">Admin</option></select>
                        <SubmitButton className="text-xs font-semibold text-accent">Save</SubmitButton>
                      </form>
                    )}
                  </td>
                  <td className="whitespace-nowrap px-5 py-3 text-muted">{fmtDate((p as Profile & { created_at: string }).created_at)}</td>
                  <td className="px-5 py-3 text-right">
                    {p.id !== selfId && (
                      <form action={removeMember}><input type="hidden" name="id" value={p.id} /><button className="text-xs text-bad hover:underline">Remove access</button></form>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

async function Projects({ supabase }: { supabase: SB }) {
  const [{ data: companies }, { data: projects }] = await Promise.all([
    supabase.from("companies").select("id,name").order("name").returns<Company[]>(),
    supabase.from("projects").select("id,name,status,phase,progress,companies(name)").order("created_at", { ascending: false }).returns<ProjectRow[]>(),
  ]);
  return (
    <div className="space-y-10">
      {companies?.length ? (
        <form action={createProject} className="card grid gap-4 p-6 sm:grid-cols-2">
          <h2 className="font-serif text-xl sm:col-span-2">New project</h2>
          <select name="company_id" required className="input">{companies.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</select>
          <input name="name" required className="input" placeholder="Project name, e.g. S/4HANA Conversion" />
          <textarea name="summary" className="input min-h-20 sm:col-span-2" placeholder="One-paragraph summary the client will see" />
          <div><label className="label">Start</label><input name="start_date" type="date" className="input" /></div>
          <div><label className="label">Target</label><input name="target_date" type="date" className="input" /></div>
          <div><SubmitButton>Create project</SubmitButton></div>
        </form>
      ) : <Empty>Add a client company first (Clients &amp; users tab).</Empty>}
      <ul className="card divide-y divide-line">
        {projects?.map((p) => (
          <li key={p.id}>
            <Link href={`/portal/projects/${p.id}`} className="flex items-center justify-between gap-3 px-5 py-4 hover:bg-paper">
              <div><p className="font-medium">{p.name}</p><p className="text-xs text-muted">{p.companies?.name} · {p.phase} · {p.progress}%</p></div>
              <Badge>{p.status}</Badge>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
