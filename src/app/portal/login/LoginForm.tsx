"use client";
import Link from "next/link";
import { useActionState } from "react";
import { signIn, type AuthState } from "../auth-actions";

export function LoginForm({ next }: { next?: string }) {
  const [state, action, pending] = useActionState<AuthState, FormData>(signIn, {});
  return (
    <form action={action} className="space-y-5">
      <input type="hidden" name="next" value={next || "/portal"} />
      <div><label className="label" htmlFor="email">Email</label><input className="input" id="email" name="email" type="email" required autoComplete="email" /></div>
      <div>
        <div className="flex justify-between"><label className="label" htmlFor="password">Password</label>
          <Link href="/portal/forgot" className="text-xs text-muted hover:text-ink">Forgot password?</Link></div>
        <input className="input" id="password" name="password" type="password" required autoComplete="current-password" />
      </div>
      {state.error && <p className="text-sm text-bad">{state.error}</p>}
      <button className="btn-primary w-full justify-center" disabled={pending}>{pending ? "Signing in…" : "Sign in"}</button>
    </form>
  );
}
