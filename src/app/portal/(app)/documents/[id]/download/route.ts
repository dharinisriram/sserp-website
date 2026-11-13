import { NextResponse, type NextRequest } from "next/server";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const supabase = await createClient();
  // RLS ensures a client can only see their own company's documents
  const { data: doc } = await supabase.from("documents").select("name,storage_path").eq("id", id).single();
  if (!doc) return new NextResponse("Not found", { status: 404 });
  const { data, error } = await supabase.storage.from("documents").createSignedUrl(doc.storage_path, 60, { download: doc.name });
  if (error || !data) return new NextResponse("Unable to open file", { status: 500 });
  return NextResponse.redirect(data.signedUrl);
}
