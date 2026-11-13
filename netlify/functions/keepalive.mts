// Runs daily on Netlify (free). Makes one tiny Supabase request so the free
// project never hits the 7-day inactivity pause.
export default async () => {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!url || !key) return new Response("Supabase env vars missing", { status: 500 });
  const res = await fetch(`${url}/rest/v1/companies?select=id&limit=1`, {
    headers: { apikey: key, Authorization: `Bearer ${key}` },
  });
  return new Response(`Supabase ping: ${res.status}`);
};

export const config = { schedule: "@daily" };
