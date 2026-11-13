import Link from "next/link";

export function CtaBand({ title, text, cta = "Book a consultation" }: { title: string; text?: string; cta?: string }) {
  return (
    <section className="container-x py-20">
      <div className="relative overflow-hidden rounded-3xl bg-ink px-8 py-14 text-paper sm:px-14">
        <div className="absolute -right-24 -top-24 h-72 w-72 rounded-full border-[40px] border-accent/30" aria-hidden />
        <h2 className="h-section relative max-w-2xl">{title}</h2>
        {text && <p className="relative mt-4 max-w-xl text-paper/70">{text}</p>}
        <Link href="/contact" className="btn-primary relative mt-8">{cta} →</Link>
      </div>
    </section>
  );
}
