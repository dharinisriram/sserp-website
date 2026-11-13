"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { headers } from "next/headers";
import { getPortalContext, requireAdmin } from "@/lib/portal";
import { createAdminClient } from "@/lib/supabase/admin";

const s = (f: FormData, k: string) => String(f.get(k) ?? "").trim();

/* ───────── Tickets ───────── */
export async function createTicket(form: FormData) {
  const { supabase, user, profile, isAdmin } = await getPortalContext();
  const company_id = isAdmin ? s(form, "company_id") : profile.company_id;
  const title = s(form, "title");
  if (!company_id || !title) return;
  const { data, error } = await supabase
    .from("tickets")
    .insert({
      company_id, title, created_by: user.id,
      description: s(form, "description") || null,
      priority: s(form, "priority") || "Medium",
      project_id: s(form, "project_id") || null,
    })
    .select("id")
    .single();
  if (error) throw new Error(error.message);
  redirect(`/portal/tickets/${data.id}`);
}

export async function addComment(form: FormData) {
  const { supabase, user, isAdmin } = await getPortalContext();
  const ticket_id = s(form, "ticket_id");
  const body = s(form, "body");
  if (!ticket_id || !body) return;
  await supabase.from("ticket_comments").insert({ ticket_id, body, author_id: user.id });
  // A client reply moves "Awaiting client" back to "Open"
  if (!isAdmin) {
    const admin = createAdminClient();
    await admin.from("tickets").update({ status: "Open" }).eq("id", ticket_id).eq("status", "Awaiting client");
  }
  revalidatePath(`/portal/tickets/${ticket_id}`);
}

export async function updateTicket(form: FormData) {
  const { supabase } = await requireAdmin();
  const id = s(form, "id");
  await supabase.from("tickets").update({ status: s(form, "status"), priority: s(form, "priority") }).eq("id", id);
  revalidatePath(`/portal/tickets/${id}`);
  revalidatePath("/portal/tickets");
}

/* ───────── Documents ───────── */
export async function recordDocument(input: { company_id: string; project_id?: string | null; name: string; storage_path: string; size_bytes: number }) {
  const { supabase, user, profile, isAdmin } = await getPortalContext();
  const company_id = isAdmin ? input.company_id : profile.company_id;
  if (!company_id || !input.storage_path.startsWith(`${company_id}/`)) throw new Error("Invalid upload path");
  const { error } = await supabase.from("documents").insert({ ...input, company_id, uploaded_by: user.id, project_id: input.project_id || null });
  if (error) throw new Error(error.message);
  revalidatePath("/portal/documents");
}

export async function deleteDocument(form: FormData) {
  const { supabase } = await requireAdmin();
  const id = s(form, "id");
  const { data } = await supabase.from("documents").select("storage_path").eq("id", id).single();
  if (data) await supabase.storage.from("documents").remove([data.storage_path]);
  await supabase.from("documents").delete().eq("id", id);
  revalidatePath("/portal/documents");
}

/* ───────── Admin: clients ───────── */
export async function createCompany(form: FormData) {
  const { supabase } = await requireAdmin();
  const name = s(form, "name");
  if (name) await supabase.from("companies").insert({ name });
  revalidatePath("/portal/admin");
}

export async function inviteUser(form: FormData): Promise<void> {
  await requireAdmin();
  const email = s(form, "email").toLowerCase();
  const company_id = s(form, "company_id") || null;
  const role = s(form, "role") === "admin" ? "admin" : "client";
  if (!email) return;
  const admin = createAdminClient();
  const origin = process.env.NEXT_PUBLIC_SITE_URL || (await headers()).get("origin") || "";
  const { data, error } = await admin.auth.admin.inviteUserByEmail(email, {
    data: { full_name: s(form, "full_name") || null },
    redirectTo: `${origin}/auth/confirm?next=/portal/set-password`,
  });
  if (error) redirect(`/portal/admin?tab=clients&msg=${encodeURIComponent(error.message)}`);
  await admin.from("profiles").upsert({ id: data.user.id, email, full_name: s(form, "full_name") || null, company_id, role });
  revalidatePath("/portal/admin");
  redirect(`/portal/admin?tab=clients&msg=${encodeURIComponent(`Invitation sent to ${email}`)}`);
}

export async function updateMember(form: FormData) {
  await requireAdmin();
  const admin = createAdminClient();
  await admin.from("profiles").update({ company_id: s(form, "company_id") || null, role: s(form, "role") === "admin" ? "admin" : "client" }).eq("id", s(form, "id"));
  revalidatePath("/portal/admin");
}

export async function removeMember(form: FormData) {
  const { user } = await requireAdmin();
  const id = s(form, "id");
  if (id === user.id) return;
  await createAdminClient().auth.admin.deleteUser(id);
  revalidatePath("/portal/admin");
}

/* ───────── Admin: projects ───────── */
export async function createProject(form: FormData) {
  const { supabase } = await requireAdmin();
  const { data, error } = await supabase
    .from("projects")
    .insert({
      company_id: s(form, "company_id"), name: s(form, "name"), summary: s(form, "summary") || null,
      start_date: s(form, "start_date") || null, target_date: s(form, "target_date") || null,
    })
    .select("id")
    .single();
  if (error) throw new Error(error.message);
  redirect(`/portal/projects/${data.id}`);
}

export async function updateProject(form: FormData) {
  const { supabase } = await requireAdmin();
  const id = s(form, "id");
  await supabase.from("projects").update({
    phase: s(form, "phase"), status: s(form, "status"),
    progress: Math.min(100, Math.max(0, Number(s(form, "progress")) || 0)),
    target_date: s(form, "target_date") || null,
  }).eq("id", id);
  revalidatePath(`/portal/projects/${id}`);
}

export async function postProjectUpdate(form: FormData) {
  const { supabase, user } = await requireAdmin();
  const project_id = s(form, "project_id");
  const body = s(form, "body");
  if (body) await supabase.from("project_updates").insert({ project_id, body, author_id: user.id });
  revalidatePath(`/portal/projects/${project_id}`);
}

/* ───────── Admin: inquiries ───────── */
export async function toggleInquiry(form: FormData) {
  const { supabase } = await requireAdmin();
  await supabase.from("inquiries").update({ handled: s(form, "handled") === "true" }).eq("id", s(form, "id"));
  revalidatePath("/portal/admin");
}
