"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { Logo } from "./Logo";

const nav = [
  { href: "/", label: "Home" },
  { href: "/about", label: "About" },
  { href: "/services", label: "Services" },
  { href: "/insights", label: "Insights" },
  { href: "/contact", label: "Contact" },
];

export function SiteHeader() {
  const path = usePathname();
  const [open, setOpen] = useState(false);
  return (
    <header className="sticky top-0 z-40 border-b border-line/70 bg-paper/90 backdrop-blur">
      <div className="container-x flex h-16 items-center justify-between">
        <Logo />
        <nav className="hidden items-center gap-7 md:flex">
          {nav.map((n) => (
            <Link key={n.href} href={n.href}
              className={`text-sm transition hover:text-accent ${path === n.href ? "font-semibold text-ink" : "text-muted"}`}>
              {n.label}
            </Link>
          ))}
        </nav>
        <div className="hidden items-center gap-3 md:flex">
          <Link href="/portal/login" className="text-sm font-medium text-ink hover:text-accent">Client login</Link>
          <Link href="/contact" className="btn-primary">Discuss an engagement</Link>
        </div>
        <button className="md:hidden" onClick={() => setOpen(!open)} aria-label="Menu" aria-expanded={open}>
          <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2"><path d={open ? "M6 6l12 12M18 6L6 18" : "M4 7h16M4 12h16M4 17h16"} /></svg>
        </button>
      </div>
      {open && (
        <div className="border-t border-line bg-paper md:hidden">
          <div className="container-x flex flex-col gap-1 py-3">
            {nav.map((n) => (
              <Link key={n.href} href={n.href} onClick={() => setOpen(false)} className="py-2 text-sm">{n.label}</Link>
            ))}
            <Link href="/portal/login" onClick={() => setOpen(false)} className="py-2 text-sm font-semibold">Client login</Link>
            <Link href="/contact" onClick={() => setOpen(false)} className="btn-primary mt-2 w-fit">Discuss an engagement</Link>
          </div>
        </div>
      )}
    </header>
  );
}
