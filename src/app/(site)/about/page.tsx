import type { Metadata } from "next";
import { CtaBand } from "@/components/CtaBand";

export const metadata: Metadata = { title: "About" };

const principles = [
  { t: "Fewer clients, more attention", d: "We cap the number of live engagements so every client gets senior attention." },
  { t: "Evidence before opinion", d: "Every recommendation traces back to something measured, observed or tested in your system." },
  { t: "Your team in the room", d: "We work alongside your people, so there are no surprises at handover." },
];

export default function About() {
  return (
    <>
      <section className="container-x py-20 lg:py-28">
        <p className="eyebrow">About us</p>
        <h1 className="h-display mt-5 max-w-3xl">A small firm, deliberately</h1>
        <p className="mt-6 max-w-2xl text-lg text-muted">
          We take on a limited number of engagements, so the people you meet first are the people who do the work.
        </p>
      </section>

      <section className="border-y border-line bg-white">
        <div className="container-x grid gap-12 py-20 md:grid-cols-[1fr_1.4fr]">
          <div>
            <p className="eyebrow">Our story</p>
            <h2 className="h-section mt-3">ERP expertise, built from India for clients worldwide</h2>
          </div>
          <div className="space-y-5 text-muted">
            <p>
              SS ERP Solutions was founded in 2018 to give businesses direct access to experienced ERP consultants —
              people who understand both the system and the operations it runs.
            </p>
            <p>
              From our corporate office in Chromepet, Chennai, we advise and support clients across SAP, Oracle and
              mixed ERP landscapes: from health checks and implementations to rollouts, upgrades and ongoing
              application management.
            </p>
          </div>
        </div>
      </section>

      <section className="container-x py-20">
        <p className="eyebrow">How we operate</p>
        <h2 className="h-section mt-3 max-w-2xl">Principles we do not bend</h2>
        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {principles.map((p, i) => (
            <div key={p.t} className="card p-7">
              <span className="font-serif text-3xl text-accent">0{i + 1}</span>
              <h3 className="mt-4 font-serif text-xl">{p.t}</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted">{p.d}</p>
            </div>
          ))}
        </div>
      </section>

      <CtaBand title="Tell us what you are trying to decide" text="Describe the problem in a paragraph. We'll tell you honestly whether we're the right fit." cta="Discuss an engagement" />
    </>
  );
}
