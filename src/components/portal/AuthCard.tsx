import Link from "next/link";
import { Logo } from "@/components/Logo";

export function AuthCard({ title, subtitle, children }: { title: string; subtitle?: string; children: React.ReactNode }) {
  return (
    <div className="grid min-h-screen lg:grid-cols-2">
      <div className="relative hidden overflow-hidden bg-ink p-12 text-paper lg:flex lg:flex-col lg:justify-between">
        <Logo light />
        <div className="absolute -bottom-32 -right-32 h-96 w-96 rounded-full border-[60px] border-accent/25" aria-hidden />
        <div className="relative max-w-md">
          <p className="eyebrow">Client portal</p>
          <p className="mt-4 font-serif text-3xl leading-snug">Your projects, support tickets and documents — in one secure place.</p>
        </div>
        <p className="relative text-xs text-paper/50">Access is by invitation only. Each client sees only their own company&apos;s information.</p>
      </div>
      <div className="flex flex-col justify-center px-6 py-16 sm:px-16">
        <div className="mx-auto w-full max-w-sm">
          <div className="lg:hidden"><Logo /></div>
          <h1 className="mt-8 font-serif text-3xl lg:mt-0">{title}</h1>
          {subtitle && <p className="mt-2 text-sm text-muted">{subtitle}</p>}
          <div className="mt-8">{children}</div>
          <Link href="/" className="mt-10 block text-sm text-muted hover:text-ink">← Back to sserpsolutions.net</Link>
        </div>
      </div>
    </div>
  );
}
