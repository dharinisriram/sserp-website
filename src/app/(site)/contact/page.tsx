import type { Metadata } from "next";
import { ContactForm } from "./ContactForm";
import { site } from "@/lib/content";

export const metadata: Metadata = { title: "Contact" };

export default function Contact() {
  return (
    <section className="container-x py-20 lg:py-28">
      <p className="eyebrow">Contact</p>
      <h1 className="h-display mt-5 max-w-3xl">Tell us what your business needs to solve</h1>
      <p className="mt-6 max-w-2xl text-lg text-muted">
        Tell us about your ERP challenge or requirement. Our team will review it and get back to you with the right next step.
      </p>
      <div className="mt-14 grid gap-10 lg:grid-cols-[1.5fr_1fr]">
        <ContactForm />
        <aside className="space-y-6">
          <div className="card p-7">
            <h2 className="font-serif text-xl">Speak to us directly</h2>
            <a href={`mailto:${site.email}`} className="mt-3 block font-semibold text-accent hover:text-ink">{site.email}</a>
            <p className="mt-2 text-sm text-muted">We respond within one working day.</p>
          </div>
          <div className="card p-7">
            <h2 className="font-serif text-xl">How quickly can you start?</h2>
            <p className="mt-2 text-sm leading-relaxed text-muted">
              We typically begin within two to three weeks, depending on scope, requirements and consultant availability.
            </p>
          </div>
        </aside>
      </div>
    </section>
  );
}
