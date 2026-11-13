"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function PortalNav({ isAdmin }: { isAdmin: boolean }) {
  const path = usePathname();
  const items = [
    { href: "/portal", label: "Overview" },
    { href: "/portal/tickets", label: "Support tickets" },
    { href: "/portal/documents", label: "Documents" },
    ...(isAdmin ? [{ href: "/portal/admin", label: "Admin" }] : []),
  ];
  return (
    <nav className="flex gap-1 overflow-x-auto">
      {items.map((i) => {
        const active = i.href === "/portal" ? path === "/portal" || path.startsWith("/portal/projects") : path.startsWith(i.href);
        return (
          <Link key={i.href} href={i.href}
            className={`whitespace-nowrap rounded-full px-4 py-2 text-sm transition ${active ? "bg-ink text-paper" : "text-muted hover:bg-white hover:text-ink"}`}>
            {i.label}
          </Link>
        );
      })}
    </nav>
  );
}
