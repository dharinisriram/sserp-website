"use client";
import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { recordDocument } from "@/app/portal/actions";

type Opt = { id: string; name: string };

export function Uploader({ companyId, companies, projects }: { companyId: string | null; companies: Opt[]; projects: Opt[] }) {
  const router = useRouter();
  const fileRef = useRef<HTMLInputElement>(null);
  const [company, setCompany] = useState(companyId ?? companies[0]?.id ?? "");
  const [project, setProject] = useState("");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  async function upload() {
    const files = Array.from(fileRef.current?.files ?? []);
    if (!files.length || !company) return;
    setBusy(true); setErr(null);
    const supabase = createClient();
    try {
      for (const f of files) {
        if (f.size > 50 * 1024 * 1024) throw new Error(`${f.name} is larger than 50 MB.`);
        const safe = f.name.replace(/[^\w.\-]+/g, "_");
        const path = `${company}/${crypto.randomUUID()}-${safe}`;
        const { error } = await supabase.storage.from("documents").upload(path, f, { contentType: f.type || undefined });
        if (error) throw new Error(error.message);
        await recordDocument({ company_id: company, project_id: project || null, name: f.name, storage_path: path, size_bytes: f.size });
      }
      if (fileRef.current) fileRef.current.value = "";
      router.refresh();
    } catch (e) {
      setErr(e instanceof Error ? e.message : "Upload failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card grid gap-4 p-6 sm:grid-cols-[1fr_1fr_1.4fr_auto] sm:items-end">
      {!companyId && (
        <div><label className="label">Client</label>
          <select className="input" value={company} onChange={(e) => setCompany(e.target.value)}>{companies.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</select></div>
      )}
      <div><label className="label">Project</label>
        <select className="input" value={project} onChange={(e) => setProject(e.target.value)}><option value="">General</option>{projects.map((p) => <option key={p.id} value={p.id}>{p.name}</option>)}</select></div>
      <div className={companyId ? "sm:col-span-2" : ""}><label className="label">Files</label><input ref={fileRef} type="file" multiple className="input file:mr-3 file:rounded-full file:border-0 file:bg-ink file:px-3 file:py-1 file:text-xs file:text-paper" /></div>
      <button onClick={upload} disabled={busy} className="btn-primary justify-center">{busy ? "Uploading…" : "Upload"}</button>
      {err && <p className="text-sm text-bad sm:col-span-4">{err}</p>}
    </div>
  );
}
