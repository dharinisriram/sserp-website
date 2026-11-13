import type { Metadata } from "next";
import { AuthCard } from "@/components/portal/AuthCard";
import { LoginForm } from "./LoginForm";

export const metadata: Metadata = { title: "Client login", robots: { index: false } };

export default async function Login({ searchParams }: { searchParams: Promise<{ next?: string; error?: string }> }) {
  const { next, error } = await searchParams;
  return (
    <AuthCard title="Client login" subtitle="Sign in with the email you were invited with.">
      {error === "link" && <p className="mb-5 rounded-lg bg-bad/10 p-3 text-sm text-bad">That link has expired or was already used. Ask us for a new one, or reset your password.</p>}
      <LoginForm next={next} />
    </AuthCard>
  );
}
