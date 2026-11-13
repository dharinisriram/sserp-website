"use client";
import { useActionState } from "react";
import { AuthCard } from "@/components/portal/AuthCard";
import { sendReset, type AuthState } from "../auth-actions";

export default function Forgot() {
  const [state, action, pending] = useActionState<AuthState, FormData>(sendReset, {});
  return (
    <AuthCard title="Reset your password" subtitle="We'll email you a link to set a new one.">
      {state.message ? (
        <p className="rounded-lg bg-ok/10 p-4 text-sm text-ok">{state.message}</p>
      ) : (
        <form action={action} className="space-y-5">
          <div><label className="label" htmlFor="email">Email</label><input className="input" id="email" name="email" type="email" required /></div>
          <button className="btn-primary w-full justify-center" disabled={pending}>{pending ? "Sending…" : "Send reset link"}</button>
        </form>
      )}
    </AuthCard>
  );
}
