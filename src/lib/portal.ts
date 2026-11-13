import "server-only";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export type Profile = { id: string; full_name: string | null; email: string | null; company_id: string | null; role: "client" | "admin" };

export async function getPortalContext() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/portal/login");
  const { data: profile } = await supabase.from("profiles").select("*").eq("id", user.id).single<Profile>();
  if (!profile) redirect("/portal/login?error=profile");
  let companyName: string | null = null;
  if (profile.company_id) {
    const { data } = await supabase.from("companies").select("name").eq("id", profile.company_id).single();
    companyName = data?.name ?? null;
  }
  return { supabase, user, profile, companyName, isAdmin: profile.role === "admin" };
}

export async function requireAdmin() {
  const ctx = await getPortalContext();
  if (!ctx.isAdmin) redirect("/portal");
  return ctx;
}

export const fmtDate = (d?: string | null) =>
  d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "—";

export const fmtSize = (b?: number | null) =>
  !b ? "—" : b < 1024 * 1024 ? `${Math.max(1, Math.round(b / 1024))} KB` : `${(b / 1024 / 1024).toFixed(1)} MB`;
