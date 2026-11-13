import type { Metadata } from "next";
import "@fontsource-variable/inter";
import "@fontsource-variable/source-serif-4";
import "./globals.css";


export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || "https://sserpsolutions.net"),
  title: { default: "SS ERP Solutions | Enterprise Technology Consulting", template: "%s | SS ERP Solutions" },
  description:
    "Practical ERP expertise for smarter systems, stronger operations, and sustainable growth. SAP, Oracle and multi-ERP consulting, rooted in India, serving clients worldwide.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
