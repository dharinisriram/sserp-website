import Link from "next/link";
import { Badge, Empty } from "@/components/portal/Badge";
import { SubmitButton } from "@/components/portal/SubmitButton";
import { fmtDate, getPortalContext } from "@/lib/portal";
import { createTicket } from "../../actions";

type Row = { id: string; ref: number; title: string; status: string; priority: string; updated_at: string; companies: { name: string } | null; projects: { name: string } | null };

export default async function Tickets({ searchParams }: { searchParams: Promise<{ new?: string; project?: string; view?: string }> }) {
  const sp = await searchParams;
  const { supabase, isAdmin } = await getPortalContext();
  const closed = sp.view === "closed";

  let q = supabase.from("tickets").select("id,ref,title,status,priority,updated_at,companies(name),projects(name)").order("updated_at", { ascending: false });
  q = closed ? q.in("status", ["Resolved", "Closed"]) : q.not("status", "in", "(Resolved,Closed)");
  const [{ data: tickets }, { data: projects }, { data: companies }] = await Promise.all([
    q.returns<Row[]>(),
    supabase.from("projects").select("id,name").neq("status", "Completed").order("name"),
    isAdmin ? supabase.from("companies").select("id,name").order("name") : Promise.resolve({ data: [] as { id: string; name: string }[] }),
  ]);

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <h1 className="font-serif text-4xl">Support tickets</h1>
        <div className="flex gap-2 text-sm">
          <Link href="/portal/tickets" className={`rounded-full px-4 py-2 ${!closed ? "bg-white font-semibold" : "text-muted"}`}>Open</Link>
          <Link href="/portal/tickets?view=closed" className={`rounded-full px-4 py-2 ${closed ? "bg-white font-semibold" : "text-muted"}`}>Resolved</Link>
        </div>
      </div>

      <details className="card p-6" open={sp.new === "1"}>
        <summary className="cursor-pointer font-semibold">+ Raise a new ticket</summary>
        <form action={createTicket} className="mt-5 grid gap-4 sm:grid-cols-2">
          {isAdmin && (
            <div className="sm:col-span-2"><label className="label">Client</label>
              <select name="company_id" required className="input">{companies?.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</select></div>
          )}
          <div className="sm:col-span-2"><label className="label" htmlFor="title">Subject</label><input id="title" name="title" required maxLength={200} className="input" placeholder="e.g. MIRO posting error for vendor invoices" /></div>
          <div><label className="label">Priority</label>
            <select name="priority" defaultValue="Medium" className="input">{["Low", "Medium", "High", "Critical"].map((x) => <option key={x}>{x}</option>)}</select></div>
          <div><label className="label">Related project</label>
            <select name="project_id" defaultValue={sp.project ?? ""} className="input"><option value="">None</option>{projects?.map((p) => <option key={p.id} value={p.id}>{p.name}</option>)}</select></div>
          <div className="sm:col-span-2"><label className="label">Details</label><textarea name="description" className="input min-h-32" placeholder="What happened, where (transaction / module), steps to reproduce, business impact." /></div>
          <div><SubmitButton>Submit ticket</SubmitButton></div>
        </form>
      </details>

      {tickets?.length ? (
        <div className="card overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="border-b border-line text-xs uppercase tracking-wider text-muted">
              <tr><th className="px-5 py-3">#</th><th className="px-5 py-3">Subject</th>{isAdmin && <th className="px-5 py-3">Client</th>}<th className="px-5 py-3">Priority</th><th className="px-5 py-3">Status</th><th className="px-5 py-3">Updated</th></tr>
            </thead>
            <tbody className="divide-y divide-line">
              {tickets.map((t) => (
                <tr key={t.id} className="hover:bg-paper">
                  <td className="px-5 py-3 text-muted">{t.ref}</td>
                  <td className="px-5 py-3"><Link href={`/portal/tickets/${t.id}`} className="font-medium hover:text-accent">{t.title}</Link>{t.projects && <p className="text-xs text-muted">{t.projects.name}</p>}</td>
                  {isAdmin && <td className="px-5 py-3">{t.companies?.name}</td>}
                  <td className="px-5 py-3"><Badge>{t.priority}</Badge></td>
                  <td className="px-5 py-3"><Badge>{t.status}</Badge></td>
                  <td className="whitespace-nowrap px-5 py-3 text-muted">{fmtDate(t.updated_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : <Empty>{closed ? "No resolved tickets yet." : "No open tickets."}</Empty>}
    </div>
  );
}
