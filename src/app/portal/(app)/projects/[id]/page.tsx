import Link from "next/link";
import { notFound } from "next/navigation";
import { Badge, Empty, Progress } from "@/components/portal/Badge";
import { SubmitButton } from "@/components/portal/SubmitButton";
import { fmtDate, getPortalContext } from "@/lib/portal";
import { postProjectUpdate, updateProject } from "../../../actions";

type Update = { id: string; body: string; created_at: string; profiles: { full_name: string | null } | null };

const PHASES = ["Assess", "Plan", "Deliver", "Improve"];
const STATUSES = ["On track", "At risk", "Blocked", "On hold", "Completed"];

export default async function ProjectPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const { supabase, isAdmin } = await getPortalContext();
  const { data: p } = await supabase.from("projects").select("*, companies(name)").eq("id", id).single();
  if (!p) notFound();

  const [{ data: updates }, { data: tickets }, { data: docs }] = await Promise.all([
    supabase.from("project_updates").select("id,body,created_at,profiles(full_name)").eq("project_id", id).order("created_at", { ascending: false }).returns<Update[]>(),
    supabase.from("tickets").select("id,ref,title,status").eq("project_id", id).order("updated_at", { ascending: false }),
    supabase.from("documents").select("id,name,created_at").eq("project_id", id).order("created_at", { ascending: false }),
  ]);
  const phaseIdx = PHASES.indexOf(p.phase);

  return (
    <div className="space-y-8">
      <Link href="/portal" className="text-sm text-muted hover:text-ink">← Overview</Link>
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          {isAdmin && <p className="eyebrow">{p.companies?.name}</p>}
          <h1 className="mt-1 font-serif text-4xl">{p.name}</h1>
          {p.summary && <p className="mt-3 max-w-2xl text-muted">{p.summary}</p>}
        </div>
        <Badge>{p.status}</Badge>
      </div>

      <div className="card p-6">
        <ol className="grid grid-cols-4 gap-2">
          {PHASES.map((ph, i) => (
            <li key={ph}>
              <div className={`h-1.5 rounded-full ${i <= phaseIdx ? "bg-accent" : "bg-line"}`} />
              <p className={`mt-2 text-xs sm:text-sm ${i === phaseIdx ? "font-semibold" : "text-muted"}`}>{String(i + 1).padStart(2, "0")} {ph}</p>
            </li>
          ))}
        </ol>
        <div className="mt-6 grid gap-4 text-sm sm:grid-cols-3">
          <div><p className="text-muted">Start</p><p className="font-medium">{fmtDate(p.start_date)}</p></div>
          <div><p className="text-muted">Target</p><p className="font-medium">{fmtDate(p.target_date)}</p></div>
          <div><p className="text-muted">Progress</p><div className="mt-1.5 flex items-center gap-3"><Progress value={p.progress} /><b>{p.progress}%</b></div></div>
        </div>
      </div>

      {isAdmin && (
        <details className="card p-6">
          <summary className="cursor-pointer font-semibold">Update project status</summary>
          <form action={updateProject} className="mt-5 grid gap-4 sm:grid-cols-5 sm:items-end">
            <input type="hidden" name="id" value={p.id} />
            <div><label className="label">Phase</label><select name="phase" defaultValue={p.phase} className="input">{PHASES.map((x) => <option key={x}>{x}</option>)}</select></div>
            <div><label className="label">Status</label><select name="status" defaultValue={p.status} className="input">{STATUSES.map((x) => <option key={x}>{x}</option>)}</select></div>
            <div><label className="label">Progress %</label><input name="progress" type="number" min={0} max={100} defaultValue={p.progress} className="input" /></div>
            <div><label className="label">Target date</label><input name="target_date" type="date" defaultValue={p.target_date ?? ""} className="input" /></div>
            <SubmitButton>Save</SubmitButton>
          </form>
        </details>
      )}

      <div className="grid gap-8 lg:grid-cols-[1.4fr_1fr]">
        <section>
          <h2 className="mb-4 font-serif text-2xl">Updates</h2>
          {isAdmin && (
            <form action={postProjectUpdate} className="card mb-4 space-y-3 p-5">
              <input type="hidden" name="project_id" value={p.id} />
              <textarea name="body" required className="input min-h-24" placeholder="Post an update the client will see…" />
              <SubmitButton>Post update</SubmitButton>
            </form>
          )}
          {updates?.length ? (
            <ol className="space-y-4">
              {updates.map((u) => (
                <li key={u.id} className="card p-5">
                  <p className="text-xs text-muted">{fmtDate(u.created_at)}{u.profiles?.full_name ? ` · ${u.profiles.full_name}` : ""}</p>
                  <p className="mt-2 whitespace-pre-line text-sm leading-relaxed">{u.body}</p>
                </li>
              ))}
            </ol>
          ) : <Empty>No updates posted yet.</Empty>}
        </section>
        <aside className="space-y-8">
          <section>
            <div className="mb-3 flex justify-between"><h2 className="font-serif text-xl">Tickets</h2>
              <Link href={`/portal/tickets?new=1&project=${p.id}`} className="text-sm font-semibold text-accent">+ Raise</Link></div>
            {tickets?.length ? (
              <ul className="card divide-y divide-line">
                {tickets.map((t) => (
                  <li key={t.id}><Link href={`/portal/tickets/${t.id}`} className="flex justify-between gap-2 px-4 py-3 text-sm hover:bg-paper"><span className="truncate">#{t.ref} {t.title}</span><Badge>{t.status}</Badge></Link></li>
                ))}
              </ul>
            ) : <Empty>No tickets for this project.</Empty>}
          </section>
          <section>
            <h2 className="mb-3 font-serif text-xl">Documents</h2>
            {docs?.length ? (
              <ul className="card divide-y divide-line">
                {docs.map((d) => (
                  <li key={d.id}><a href={`/portal/documents/${d.id}/download`} className="block truncate px-4 py-3 text-sm hover:bg-paper">{d.name}</a></li>
                ))}
              </ul>
            ) : <Empty>No documents for this project.</Empty>}
          </section>
        </aside>
      </div>
    </div>
  );
}
