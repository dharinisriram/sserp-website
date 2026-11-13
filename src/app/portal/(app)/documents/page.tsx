import { Empty } from "@/components/portal/Badge";
import { Uploader } from "@/components/portal/Uploader";
import { fmtDate, fmtSize, getPortalContext } from "@/lib/portal";
import { deleteDocument } from "../../actions";

type Doc = { id: string; name: string; size_bytes: number | null; created_at: string; companies: { name: string } | null; projects: { name: string } | null; profiles: { full_name: string | null; email: string | null } | null };

export default async function Documents() {
  const { supabase, profile, isAdmin } = await getPortalContext();
  const [{ data: docs }, { data: projects }, { data: companies }] = await Promise.all([
    supabase.from("documents").select("id,name,size_bytes,created_at,companies(name),projects(name),profiles(full_name,email)").order("created_at", { ascending: false }).returns<Doc[]>(),
    supabase.from("projects").select("id,name").order("name"),
    isAdmin ? supabase.from("companies").select("id,name").order("name") : Promise.resolve({ data: [] as { id: string; name: string }[] }),
  ]);

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-serif text-4xl">Documents</h1>
        <p className="mt-2 text-muted">Stored privately. Only your company and the SS ERP team can open these files.</p>
      </div>
      <Uploader companyId={isAdmin ? null : profile.company_id} companies={companies ?? []} projects={projects ?? []} />
      {docs?.length ? (
        <div className="card overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="border-b border-line text-xs uppercase tracking-wider text-muted">
              <tr><th className="px-5 py-3">Name</th>{isAdmin && <th className="px-5 py-3">Client</th>}<th className="px-5 py-3">Project</th><th className="px-5 py-3">Uploaded by</th><th className="px-5 py-3">Size</th><th className="px-5 py-3">Date</th>{isAdmin && <th />}</tr>
            </thead>
            <tbody className="divide-y divide-line">
              {docs.map((d) => (
                <tr key={d.id} className="hover:bg-paper">
                  <td className="px-5 py-3"><a href={`/portal/documents/${d.id}/download`} className="font-medium hover:text-accent">{d.name}</a></td>
                  {isAdmin && <td className="px-5 py-3">{d.companies?.name}</td>}
                  <td className="px-5 py-3 text-muted">{d.projects?.name ?? "General"}</td>
                  <td className="px-5 py-3 text-muted">{d.profiles?.full_name || d.profiles?.email || "—"}</td>
                  <td className="px-5 py-3 text-muted">{fmtSize(d.size_bytes)}</td>
                  <td className="whitespace-nowrap px-5 py-3 text-muted">{fmtDate(d.created_at)}</td>
                  {isAdmin && (
                    <td className="px-5 py-3 text-right">
                      <form action={deleteDocument}><input type="hidden" name="id" value={d.id} /><button className="text-xs text-bad hover:underline">Delete</button></form>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : <Empty>No documents yet.</Empty>}
    </div>
  );
}
