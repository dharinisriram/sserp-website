import Link from "next/link";
import { Logo } from "./Logo";
import { footerServices, services, site } from "@/lib/content";

export function SiteFooter() {
  return (
    <footer className="bg-ink text-paper/80">
      <div className="container-x grid gap-10 py-14 md:grid-cols-4">
        <div className="md:col-span-1">
          <Logo light />
          <p className="mt-4 text-sm leading-relaxed">{site.tagline}</p>
        </div>
        <div>
          <h3 className="mb-3 text-sm font-semibold text-paper">Company</h3>
          <ul className="space-y-2 text-sm">
            {["About", "Services", "Insights", "Contact"].map((l) => (
              <li key={l}><Link className="hover:text-paper" href={`/${l.toLowerCase()}`}>{l}</Link></li>
            ))}
            <li><Link className="hover:text-paper" href="/portal/login">Client login</Link></li>
          </ul>
        </div>
        <div>
          <h3 className="mb-3 text-sm font-semibold text-paper">Expertise</h3>
          <ul className="space-y-2 text-sm">
            {footerServices.map((s) => {
              const svc = services.find((x) => x.slug === s)!;
              return <li key={s}><Link className="hover:text-paper" href={`/services#${s}`}>{svc.title}</Link></li>;
            })}
          </ul>
        </div>
        <div>
          <h3 className="mb-3 text-sm font-semibold text-paper">Get in touch</h3>
          <a className="text-sm hover:text-paper" href={`mailto:${site.email}`}>{site.email}</a>
        </div>
      </div>
      <div className="border-t border-paper/10">
        <div className="container-x py-5 text-xs text-paper/50">© {new Date().getFullYear()} {site.name}. All rights reserved.</div>
      </div>
    </footer>
  );
}
