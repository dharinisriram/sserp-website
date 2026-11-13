import Link from "next/link";
import { Badge, Empty, Progress } from "@/components/portal/Badge";
import { fmtDate, getPortalContext } from "@/lib/portal";

type Project = { id: string; name: string; summary: string | null; phase: string; status: string; progress: number; target_date: string | null; companies: { name: string } | null };
type Ticket = { id: string; ref: number; title: string; status: string; priority: string; updated_at: string; companies: { name: string } | null };
type Doc = { id: string; name: string; created_at: string };

export default async function Overview() {
  const { supabase, profile, companyName, isAdmin } = await getPortalContext();

  const [{ data: projects }, { data: tickets }, { data: docs }, inq] = await Promise.all([
    supabase.from("projects").select("id,name,summary,phase,status,progress,target_date,companies(name)").neq("status", "Completed").order("created_at", { ascending: false }).returns<Project[]>(),
    supabase.from("tickets").select("id,ref,title,status,priority,updated_at,companies(name)").not("status", "in", "(Resolved,Closed)").order("updated_at", { ascending: false }).limit(6).returns<Ticket[]>(),
    supabase.from("documents").select("id,name,created_at").order("created_at", { ascending: false }).limit(5).returns<Doc[]>(),
    isAdmin ? supabase.from("inquiries").select("id", { count: "exact", head: true }).eq("handled", false) : Promise.resolve({ count: 0 }),
  ]);

  const first = (profile.full_name || "").split(" ")[0];

  return (
    <div className="space-y-10">
      <div>
        <p className="eyebrow">{isAdmin ? "All clients" : companyName}</p>
        <h1 className="mt-2 font-serif text-4xl">Welcome{first ? `, ${first}` : ""}</h1>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Stat label="Active projects" value={projects?.length ?? 0} />
        <Stat label="Open tickets" value={tickets?.length ?? 0} href="/portal/tickets" />
        {isAdmin ? <Stat label="New inquiries" value={inq.count ?? 0} href="/portal/admin?tab=inquiries" /> : <Stat label="Documents" value={docs?.length ?? 0} href="/portal/documents" />}
      </div>

      <section>
        <h2 className="mb-4 font-serif text-2xl">Projects</h2>
        {projects?.length ? (
          <div className="grid gap-4 md:grid-cols-2">
            {projects.map((p) => (
              <Link key={p.id} href={`/portal/projects/${p.id}`} className="card block p-6 transition hover:border-ink">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    {isAdmin && <p className="text-xs font-semibold text-muted">{p.companies?.name}</p>}
                    <h3 className="font-serif text-xl">{p.name}</h3>
                  </div>
                  <Badge>{p.status}</Badge>
                </div>
                {p.summary && <p className="mt-2 line-clamp-2 text-sm text-muted">{p.summary}</p>}
                <div className="mt-5 flex items-center justify-between text-xs text-muted">
                  <span>Phase: <b className="text-ink">{p.phase}</b></span><span>Target {fmtDate(p.target_date)}</span>
                </div>
                <div className="mt-2 flex items-center gap-3"><Progress value={p.progress} /><span className="text-xs font-semibold">{p.progress}%</span></div>
              </Link>
            ))}
          </div>
        ) : <Empty>No active projects yet.</Empty>}
      </section>

      <div className="grid gap-8 lg:grid-cols-[1.4fr_1fr]">
        <section>
          <div className="mb-4 flex items-center justify-between">
            <h2 className="font-serif text-2xl">Open tickets</h2>
            <Link href="/portal/tickets?new=1" className="text-sm font-semibold text-accent hover:text-ink">+ Raise a ticket</Link>
          </div>
          {tickets?.length ? (
            <ul className="card divide-y divide-line">
              {tickets.map((t) => (
                <li key={t.id}>
                  <Link href={`/portal/tickets/${t.id}`} className="flex items-center justify-between gap-3 px-5 py-4 hover:bg-paper">
                    <div className="min-w-0">
                      <p className="truncate text-sm font-medium"><span className="text-muted">#{t.ref}</span> {t.title}</p>
                      <p className="text-xs text-muted">{isAdmin && t.companies?.name ? `${t.companies.name} · ` : ""}Updated {fmtDate(t.updated_at)}</p>
                    </div>
                    <Badge>{t.status}</Badge>
                  </Link>
                </li>
              ))}
            </ul>
          ) : <Empty>No open tickets.</Empty>}
        </section>
        <section>
          <div className="mb-4 flex items-center justify-between">
            <h2 className="font-serif text-2xl">Recent documents</h2>
            <Link href="/portal/documents" className="text-sm font-semibold text-accent hover:text-ink">All →</Link>
          </div>
          {docs?.length ? (
            <ul className="card divide-y divide-line">
              {docs.map((d) => (
                <li key={d.id}>
                  <a href={`/portal/documents/${d.id}/download`} className="flex justify-between gap-3 px-5 py-4 text-sm hover:bg-paper">
                    <span className="truncate">{d.name}</span><span className="shrink-0 text-xs text-muted">{fmtDate(d.created_at)}</span>
                  </a>
                </li>
              ))}
            </ul>
          ) : <Empty>No documents shared yet.</Empty>}
        </section>
      </div>
    </div>
  );
}

function Stat({ label, value, href }: { label: string; value: number; href?: string }) {
  const inner = (<><p className="text-sm text-muted">{label}</p><p className="mt-1 font-serif text-4xl">{value}</p></>);
  return href ? <Link href={href} className="card p-6 hover:border-ink">{inner}</Link> : <div className="card p-6">{inner}</div>;
}
