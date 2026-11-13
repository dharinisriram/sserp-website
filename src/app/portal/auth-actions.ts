"use server";
import { redirect } from "next/navigation";
import { headers } from "next/headers";
import { createClient } from "@/lib/supabase/server";

export type AuthState = { error?: string; message?: string };

export async function signIn(_p: AuthState, form: FormData): Promise<AuthState> {
  const supabase = await createClient();
  const { error } = await supabase.auth.signInWithPassword({
    email: String(form.get("email") || "").trim(),
    password: String(form.get("password") || ""),
  });
  if (error) return { error: "Incorrect email or password." };
  const next = String(form.get("next") || "/portal");
  redirect(next.startsWith("/portal") ? next : "/portal");
}

export async function sendReset(_p: AuthState, form: FormData): Promise<AuthState> {
  const supabase = await createClient();
  const origin = process.env.NEXT_PUBLIC_SITE_URL || (await headers()).get("origin") || "";
  await supabase.auth.resetPasswordForEmail(String(form.get("email") || "").trim(), {
    redirectTo: `${origin}/auth/confirm?next=/portal/set-password`,
  });
  return { message: "If that email has a portal account, a reset link is on its way." };
}

export async function setPassword(_p: AuthState, form: FormData): Promise<AuthState> {
  const password = String(form.get("password") || "");
  if (password.length < 10) return { error: "Use at least 10 characters." };
  if (password !== String(form.get("confirm") || "")) return { error: "Passwords don't match." };
  const supabase = await createClient();
  const { error } = await supabase.auth.updateUser({ password });
  if (error) return { error: error.message };
  const name = String(form.get("full_name") || "").trim();
  if (name) {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) await supabase.from("profiles").update({ full_name: name }).eq("id", user.id);
  }
  redirect("/portal");
}

export async function signOut() {
  const supabase = await createClient();
  await supabase.auth.signOut();
  redirect("/portal/login");
}
