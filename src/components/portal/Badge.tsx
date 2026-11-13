const tone: Record<string, string> = {
  "On track": "bg-ok/10 text-ok", Completed: "bg-ok/10 text-ok", Resolved: "bg-ok/10 text-ok", Closed: "bg-ink/10 text-muted",
  "At risk": "bg-warn/10 text-warn", "Awaiting client": "bg-warn/10 text-warn", "On hold": "bg-ink/10 text-muted", Medium: "bg-warn/10 text-warn",
  Blocked: "bg-bad/10 text-bad", Critical: "bg-bad/10 text-bad", High: "bg-accent/10 text-accent",
  Open: "bg-ink/10 text-ink", "In progress": "bg-ink text-paper", Low: "bg-ink/10 text-muted",
};

export function Badge({ children }: { children: string }) {
  return <span className={`inline-flex whitespace-nowrap rounded-full px-2.5 py-0.5 text-xs font-semibold ${tone[children] ?? "bg-ink/10"}`}>{children}</span>;
}

export function Progress({ value }: { value: number }) {
  return (
    <div className="h-2 w-full rounded-full bg-paper" role="progressbar" aria-valuenow={value} aria-valuemin={0} aria-valuemax={100}>
      <div className="h-2 rounded-full bg-accent" style={{ width: `${value}%` }} />
    </div>
  );
}

export function Empty({ children }: { children: React.ReactNode }) {
  return <div className="rounded-xl border border-dashed border-line px-6 py-10 text-center text-sm text-muted">{children}</div>;
}
