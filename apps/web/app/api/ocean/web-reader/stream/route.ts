import { NextRequest } from "next/server";

const OCEAN_CORE = process.env.OCEAN_API_URL || "http://ocean-core:8030";

/**
 * Web Reader Stream Proxy - SSE streaming for chat with webpage
 * POST /api/ocean/web-reader/stream
 */
export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { url, message } = body;

    if (!url || !message) {
      return new Response(
        JSON.stringify({ error: '"url" and "message" are required' }),
        { status: 400, headers: { "Content-Type": "application/json" } },
      );
    }

    // Proxy to Ocean Core streaming endpoint
    const upstream = await fetch(`${OCEAN_CORE}/api/v1/chat/browse/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, message }),
    });

    if (!upstream.ok || !upstream.body) {
      return new Response(
        JSON.stringify({ error: `Ocean Core error: ${upstream.status}` }),
        { status: 502, headers: { "Content-Type": "application/json" } },
      );
    }

    // Stream through the response
    return new Response(upstream.body, {
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      },
    });
  } catch (error) {
    console.error("[web-reader/stream] proxy error:", error);
    return new Response(
      JSON.stringify({ error: "Failed to connect to Ocean Core" }),
      { status: 502, headers: { "Content-Type": "application/json" } },
    );
  }
}
