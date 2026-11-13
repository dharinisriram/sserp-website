"use server";
import { createClient } from "@/lib/supabase/server";

export type InquiryState = { ok?: boolean; error?: string };

export async function submitInquiry(_prev: InquiryState, form: FormData): Promise<InquiryState> {
  // Honeypot: bots fill hidden fields
  if (form.get("website")) return { ok: true };

  const full_name = String(form.get("full_name") || "").trim();
  const email = String(form.get("email") || "").trim();
  const company = String(form.get("company") || "").trim();
  const topic = String(form.get("topic") || "").trim();
  const message = String(form.get("message") || "").trim();

  if (!full_name || !email || !message) return { error: "Please fill in your name, work email and the situation." };
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return { error: "Please enter a valid email address." };
  if (message.length > 5000) return { error: "Please keep the description under 5,000 characters." };

  const supabase = await createClient();
  const { error } = await supabase.from("inquiries").insert({ full_name, email, company, topic, message });
  if (error) return { error: "Something went wrong. Please email us directly at support@sserpsolutions.net." };
  return { ok: true };
}
