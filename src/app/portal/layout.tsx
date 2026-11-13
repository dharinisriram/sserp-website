import type { Metadata } from "next";

export const metadata: Metadata = { title: { default: "Client portal", template: "%s | Client portal" }, robots: { index: false, follow: false } };
export const dynamic = "force-dynamic";

export default function PortalRoot({ children }: { children: React.ReactNode }) {
  return children;
}
