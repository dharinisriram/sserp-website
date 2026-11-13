import type { Metadata } from "next";
import Link from "next/link";
import { CtaBand } from "@/components/CtaBand";
import { engagementModels, services, stages } from "@/lib/content";

export const metadata: Metadata = { title: "Services" };

export default function Services() {
  return (
    <>
      <section className="container-x py-20 lg:py-28">
        <p className="eyebrow">Services</p>
        <h1 className="h-display mt-5 max-w-3xl">Twelve services, one way of working</h1>
        <p className="mt-6 max-w-2xl text-lg text-muted">
          We help businesses build, improve and run the systems their operations depend on.
        </p>
      </section>

      <section className="border-y border-line bg-white">
        <div className="container-x grid gap-x-12 py-16 md:grid-cols-2">
          {services.map((s, i) => (
            <div key={s.slug} id={s.slug} className="scroll-mt-24 border-b border-line py-8 last:border-0 md:[&:nth-last-child(2)]:border-0">
              <div className="flex gap-5">
                <span className="w-8 shrink-0 pt-1 text-sm font-semibold text-accent">{String(i + 1).padStart(2, "0")}</span>
                <div>
                  <h2 className="font-serif text-2xl">{s.title}</h2>
                  <p className="mt-2 leading-relaxed text-muted">{s.summary}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="container-x py-20">
        <p className="eyebrow">How we work</p>
        <h2 className="h-section mt-3 max-w-2xl">Four stages, built around your business</h2>
        <p className="mt-4 max-w-xl text-muted">Every engagement follows a clear, practical path from assessment to ongoing improvement.</p>
        <ol className="mt-12 grid gap-6 md:grid-cols-4">
          {stages.map((s) => (
            <li key={s.n} className="card p-6">
              <span className="font-serif text-3xl text-accent">{s.n}</span>
              <h3 className="mt-3 font-semibold">{s.title}</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted">{s.text}</p>
            </li>
          ))}
        </ol>
      </section>

      <section className="bg-ink text-paper">
        <div className="container-x py-20">
          <p className="eyebrow">Working together</p>
          <h2 className="h-section mt-3">Three ways to start</h2>
          <p className="mt-4 max-w-xl text-paper/70">Choose the level of support that fits — from a focused assessment to a long-term partnership.</p>
          <div className="mt-12 grid gap-6 md:grid-cols-3">
            {engagementModels.map((m) => (
              <div key={m.title} className="rounded-2xl border border-paper/15 p-7">
                <span className="text-xs font-semibold uppercase tracking-widest text-accent-2">{m.duration}</span>
                <h3 className="mt-3 font-serif text-2xl">{m.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-paper/70">{m.text}</p>
              </div>
            ))}
          </div>
          <p className="mt-10 text-paper/70">
            Not sure which one you need?{" "}
            <Link href="/contact" className="font-semibold text-paper underline underline-offset-4">Describe your situation</Link>{" "}
            and we&apos;ll tell you which practice fits — or whether you need us at all.
          </p>
        </div>
      </section>

      <CtaBand title="Let's transform your ERP with confidence" cta="Discuss an engagement" />
    </>
  );
}
