import Link from "next/link";

export function Logo({ light = false, href = "/" }: { light?: boolean; href?: string }) {
  return (
    <Link href={href} className="flex items-center gap-2.5" aria-label="SS ERP Solutions home">
      <span className="grid h-9 w-9 place-items-center rounded-lg bg-accent font-serif text-sm font-semibold text-white">SS</span>
      <span className={`font-serif text-lg leading-none ${light ? "text-paper" : "text-ink"}`}>
        SS ERP <span className="text-accent">Solutions</span>
      </span>
    </Link>
  );
}
