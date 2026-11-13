import Link from "next/link";
import { CtaBand } from "@/components/CtaBand";
import { caseStudies, services, stages } from "@/lib/content";

export default function Home() {
  return (
    <>
      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="container-x grid items-center gap-12 py-20 lg:grid-cols-[1.25fr_1fr] lg:py-28">
          <div>
            <p className="eyebrow">Enterprise technology consulting</p>
            <h1 className="h-display mt-5">Enterprise Technology Consulting for Better Business</h1>
            <p className="mt-6 max-w-xl text-lg text-muted">
              Practical ERP expertise for smarter systems, stronger operations, and sustainable growth.
            </p>
            <div className="mt-9 flex flex-wrap gap-3">
              <Link href="/contact" className="btn-primary">Start a conversation →</Link>
              <Link href="/services" className="btn-ghost">Explore services</Link>
            </div>
          </div>
          <HeroGraphic />
        </div>
      </section>

      {/* What we do */}
      <section className="border-y border-line bg-white">
        <div className="container-x py-20">
          <div className="flex flex-wrap items-end justify-between gap-6">
            <div>
              <p className="eyebrow">What we do</p>
              <h2 className="h-section mt-3 max-w-xl">Twelve ways we help your business perform better</h2>
            </div>
            <Link href="/services" className="text-sm font-semibold text-accent hover:text-ink">All services →</Link>
          </div>
          <div className="mt-12 grid gap-px overflow-hidden rounded-2xl border border-line bg-line sm:grid-cols-2 lg:grid-cols-3">
            {services.map((s, i) => (
              <Link key={s.slug} href={`/services#${s.slug}`} className="group bg-white p-7 transition hover:bg-paper">
                <span className="text-xs font-semibold text-muted">{String(i + 1).padStart(2, "0")}</span>
                <h3 className="mt-3 font-serif text-xl group-hover:text-accent">{s.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted">{s.summary}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Why */}
      <section className="container-x py-20">
        <p className="eyebrow">Why firms choose us</p>
        <h2 className="h-section mt-3 max-w-2xl">Consultants who understand the business, not just the system</h2>
        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {[
            { t: "Experienced ERP consultants", d: "Hands-on expertise across SAP, Oracle and mixed enterprise landscapes." },
            { t: "A business-first approach", d: "Every recommendation starts from how your operations actually run." },
            { t: "Support beyond go-live", d: "We stay with you through stabilisation, enhancements and ongoing improvement." },
          ].map((x) => (
            <div key={x.t} className="card p-7">
              <div className="h-1 w-10 rounded bg-accent" />
              <h3 className="mt-5 font-serif text-xl">{x.t}</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted">{x.d}</p>
            </div>
          ))}
        </div>
      </section>

      {/* How we work */}
      <section className="bg-ink text-paper">
        <div className="container-x py-20">
          <p className="eyebrow">How we work</p>
          <h2 className="h-section mt-3 max-w-2xl">Four stages, built around your business</h2>
          <ol className="mt-12 grid gap-8 md:grid-cols-4">
            {stages.map((s) => (
              <li key={s.n} className="border-t border-paper/20 pt-6">
                <span className="font-serif text-3xl text-accent-2">{s.n}</span>
                <h3 className="mt-3 text-lg font-semibold">{s.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-paper/70">{s.text}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* Selected work */}
      <section className="container-x py-20">
        <p className="eyebrow">Selected work</p>
        <h2 className="h-section mt-3">Outcomes, not just go-lives</h2>
        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {caseStudies.map((c) => (
            <article key={c.title} className="card flex flex-col p-7">
              <span className="font-serif text-4xl text-accent">{c.stat}</span>
              <h3 className="mt-6 text-lg font-semibold">{c.title}</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted">{c.text}</p>
            </article>
          ))}
        </div>
      </section>

      <CtaBand title="Let's transform your ERP with confidence" text="Tell us about your landscape and what you're trying to solve. We'll come back within one working day." />
    </>
  );
}

function HeroGraphic() {
  const rows = ["Finance", "Procurement", "Manufacturing", "Sales", "Analytics"];
  return (
    <div className="relative hidden lg:block" aria-hidden>
      <div className="card relative p-6 shadow-[0_30px_60px_-30px_rgba(15,28,46,0.35)]">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold uppercase tracking-widest text-muted">Landscape health</span>
          <span className="rounded-full bg-ok/10 px-2.5 py-1 text-xs font-semibold text-ok">Stable</span>
        </div>
        <div className="mt-6 space-y-4">
          {rows.map((r, i) => (
            <div key={r}>
              <div className="flex justify-between text-sm"><span>{r}</span><span className="text-muted">{[96, 88, 92, 84, 78][i]}%</span></div>
              <div className="mt-1.5 h-2 rounded-full bg-paper">
                <div className="h-2 rounded-full bg-ink" style={{ width: `${[96, 88, 92, 84, 78][i]}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="card absolute -bottom-14 -left-10 flex items-center gap-3 px-5 py-4 shadow-lg">
        <span className="grid h-10 w-10 place-items-center rounded-full bg-accent text-white">✓</span>
        <div><div className="text-sm font-semibold">Period close</div><div className="text-xs text-muted">On schedule</div></div>
      </div>
    </div>
  );
}
