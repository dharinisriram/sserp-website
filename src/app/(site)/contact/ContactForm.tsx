"use client";
import { useActionState } from "react";
import { submitInquiry, type InquiryState } from "./actions";
import { services } from "@/lib/content";

export function ContactForm() {
  const [state, action, pending] = useActionState<InquiryState, FormData>(submitInquiry, {});
  if (state.ok)
    return (
      <div className="card p-10 text-center">
        <p className="font-serif text-2xl">Thank you — we&apos;ve received your inquiry.</p>
        <p className="mt-3 text-muted">Our team will get back to you within one working day.</p>
      </div>
    );
  return (
    <form action={action} className="card space-y-5 p-7 sm:p-9">
      <div className="grid gap-5 sm:grid-cols-2">
        <div><label className="label" htmlFor="full_name">Full name</label><input className="input" id="full_name" name="full_name" required autoComplete="name" /></div>
        <div><label className="label" htmlFor="email">Work email</label><input className="input" id="email" name="email" type="email" required autoComplete="email" /></div>
      </div>
      <div><label className="label" htmlFor="company">Company</label><input className="input" id="company" name="company" autoComplete="organization" /></div>
      <div>
        <label className="label" htmlFor="topic">What do you need help with?</label>
        <select className="input" id="topic" name="topic" defaultValue="Not sure yet">
          <option>Not sure yet</option>
          {services.map((s) => <option key={s.slug}>{s.title}</option>)}
        </select>
      </div>
      <div>
        <label className="label" htmlFor="message">The situation, in a paragraph</label>
        <textarea className="input min-h-36" id="message" name="message" required placeholder="Your ERP landscape, what's not working, and what you'd like to achieve." />
      </div>
      <input type="text" name="website" tabIndex={-1} autoComplete="off" className="hidden" aria-hidden />
      {state.error && <p className="text-sm text-bad">{state.error}</p>}
      <button className="btn-primary" disabled={pending}>{pending ? "Sending…" : "Send inquiry →"}</button>
    </form>
  );
}
