import Link from "next/link";
import { notFound } from "next/navigation";
import { Badge } from "@/components/portal/Badge";
import { SubmitButton } from "@/components/portal/SubmitButton";
import { fmtDate, getPortalContext } from "@/lib/portal";
import { addComment, updateTicket } from "../../../actions";

type Comment = { id: string; body: string; created_at: string; author_id: string; profiles: { full_name: string | null; email: string | null; role: string } | null };

export default async function Ticket({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const { supabase, user, isAdmin } = await getPortalContext();
  const { data: t } = await supabase.from("tickets").select("*, companies(name), projects(id,name), profiles!tickets_created_by_fkey(full_name,email)").eq("id", id).single();
  if (!t) notFound();
  const { data: comments } = await supabase.from("ticket_comments").select("id,body,created_at,author_id,profiles(full_name,email,role)").eq("ticket_id", id).order("created_at").returns<Comment[]>();

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <Link href="/portal/tickets" className="text-sm text-muted hover:text-ink">← All tickets</Link>
      <div>
        <p className="text-sm text-muted">#{t.ref}{isAdmin ? ` · ${t.companies?.name}` : ""}{t.projects ? <> · <Link className="underline" href={`/portal/projects/${t.projects.id}`}>{t.projects.name}</Link></> : null}</p>
        <h1 className="mt-1 font-serif text-3xl">{t.title}</h1>
        <div className="mt-3 flex flex-wrap gap-2"><Badge>{t.status}</Badge><Badge>{t.priority}</Badge></div>
      </div>

      {isAdmin && (
        <form action={updateTicket} className="card flex flex-wrap items-end gap-4 p-5">
          <input type="hidden" name="id" value={t.id} />
          <div><label className="label">Status</label><select name="status" defaultValue={t.status} className="input">{["Open", "In progress", "Awaiting client", "Resolved", "Closed"].map((x) => <option key={x}>{x}</option>)}</select></div>
          <div><label className="label">Priority</label><select name="priority" defaultValue={t.priority} className="input">{["Low", "Medium", "High", "Critical"].map((x) => <option key={x}>{x}</option>)}</select></div>
          <SubmitButton>Update</SubmitButton>
        </form>
      )}

      <ol className="space-y-4">
        <li className="card p-5">
          <p className="text-xs text-muted">{t.profiles?.full_name || t.profiles?.email || "Client"} · {fmtDate(t.created_at)}</p>
          <p className="mt-2 whitespace-pre-line text-sm leading-relaxed">{t.description || <span className="text-muted">No details provided.</span>}</p>
        </li>
        {comments?.map((c) => {
          const team = c.profiles?.role === "admin";
          return (
            <li key={c.id} className={`rounded-2xl border p-5 ${team ? "border-ink/20 bg-ink/[0.03]" : "border-line bg-white"} ${c.author_id === user.id ? "ml-8" : "mr-8"}`}>
              <p className="text-xs text-muted">{c.profiles?.full_name || c.profiles?.email}{team && <span className="ml-1 font-semibold text-accent">· SS ERP</span>} · {fmtDate(c.created_at)}</p>
              <p className="mt-2 whitespace-pre-line text-sm leading-relaxed">{c.body}</p>
            </li>
          );
        })}
      </ol>

      {t.status !== "Closed" && (
        <form action={addComment} className="card space-y-3 p-5">
          <input type="hidden" name="ticket_id" value={t.id} />
          <label className="label" htmlFor="body">Add a reply</label>
          <textarea id="body" name="body" required className="input min-h-28" />
          <SubmitButton>Send reply</SubmitButton>
        </form>
      )}
    </div>
  );
}
