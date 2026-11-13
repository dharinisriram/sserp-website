import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = { title: "Insights" };

export default function Insights() {
  return (
    <section className="container-x py-20 lg:py-28">
      <p className="eyebrow">Insights</p>
      <h1 className="h-display mt-5 max-w-3xl">Notes from the ERP floor</h1>
      <p className="mt-6 max-w-2xl text-lg text-muted">
        Perspectives on SAP, Oracle and multi-ERP programmes — what works, what doesn&apos;t, and why.
      </p>
      <div className="card mt-14 p-10 text-center">
        <p className="font-serif text-2xl">First articles coming soon.</p>
        <p className="mt-3 text-muted">
          In the meantime, if there&apos;s a question on your mind,{" "}
          <Link href="/contact" className="font-semibold text-accent underline underline-offset-4">ask us directly</Link>.
        </p>
      </div>
    </section>
  );
}
