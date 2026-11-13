import { Logo } from "@/components/Logo";
import { PortalNav } from "@/components/portal/PortalNav";
import { getPortalContext } from "@/lib/portal";
import { signOut } from "../auth-actions";

export default async function PortalShell({ children }: { children: React.ReactNode }) {
  const { profile, companyName, isAdmin } = await getPortalContext();
  return (
    <div className="min-h-screen">
      <header className="border-b border-line bg-paper">
        <div className="container-x flex h-16 items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <Logo href="/portal" />
            <span className="hidden rounded-full border border-line px-3 py-1 text-xs text-muted sm:inline">
              {isAdmin ? "SS ERP team" : companyName ?? "Client portal"}
            </span>
          </div>
          <div className="flex items-center gap-4">
            <span className="hidden text-sm text-muted sm:inline">{profile.full_name || profile.email}</span>
            <form action={signOut}><button className="text-sm font-medium hover:text-accent">Sign out</button></form>
          </div>
        </div>
        <div className="container-x pb-3"><PortalNav isAdmin={isAdmin} /></div>
      </header>
      <main className="container-x py-10">
        {!isAdmin && !profile.company_id ? (
          <div className="card p-10 text-center">
            <p className="font-serif text-2xl">Your account is being set up.</p>
            <p className="mt-2 text-muted">We haven&apos;t linked it to your company yet. Please contact support@sserpsolutions.net.</p>
          </div>
        ) : children}
      </main>
    </div>
  );
}
