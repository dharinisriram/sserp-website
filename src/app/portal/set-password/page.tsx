"use client";
import { useActionState } from "react";
import { AuthCard } from "@/components/portal/AuthCard";
import { setPassword, type AuthState } from "../auth-actions";

export default function SetPassword() {
  const [state, action, pending] = useActionState<AuthState, FormData>(setPassword, {});
  return (
    <AuthCard title="Set your password" subtitle="Choose a password for your portal account.">
      <form action={action} className="space-y-5">
        <div><label className="label" htmlFor="full_name">Your name <span className="font-normal text-muted">(optional)</span></label><input className="input" id="full_name" name="full_name" autoComplete="name" /></div>
        <div><label className="label" htmlFor="password">New password</label><input className="input" id="password" name="password" type="password" minLength={10} required autoComplete="new-password" /></div>
        <div><label className="label" htmlFor="confirm">Confirm password</label><input className="input" id="confirm" name="confirm" type="password" required autoComplete="new-password" /></div>
        {state.error && <p className="text-sm text-bad">{state.error}</p>}
        <button className="btn-primary w-full justify-center" disabled={pending}>{pending ? "Saving…" : "Save and continue"}</button>
      </form>
    </AuthCard>
  );
}
