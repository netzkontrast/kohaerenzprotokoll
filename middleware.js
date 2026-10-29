// The project's own access rule on Vercel (decision 029 §5, changed by decision 032).
//
// Vercel's login is off; this Routing Middleware runs on every request before the site, the static pages or the
// function:
//
//   the website, llms.txt, agents/, static/  →  open: the author removed the site login on 2026-10-27 (decision 032)
//   /mcp and /api/*                          →  Authorization: Bearer <RAG_MCP_TOKEN> (api/rag_server.py checks again)
//
// The token path fails closed: with RAG_MCP_TOKEN unset it answers 503 and serves nothing. No dependency — the
// continue signal is the header `x-middleware-next` that `@vercel/functions`' next() sets. scripts/auth_selftest.js
// tests it.

export const config = { matcher: '/:path*' };

function same(a, b) {
  // constant-time over the longer length, so a wrong guess's length leaks nothing
  const x = new TextEncoder().encode(a);
  const y = new TextEncoder().encode(b);
  let diff = x.length ^ y.length;
  for (let i = 0; i < Math.max(x.length, y.length); i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}

function proceed() {
  return new Response(null, { headers: { 'x-middleware-next': '1' } });
}

function refuse(status, text, headers = {}) {
  return new Response(text + '\n', {
    status,
    headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store', ...headers },
  });
}

export function decide(request, env) {
  const path = new URL(request.url).pathname;
  if (path === '/mcp' || path.startsWith('/api/')) {
    const token = env.RAG_MCP_TOKEN;
    if (!token) return refuse(503, 'the MCP server has no RAG_MCP_TOKEN set: it stays closed');
    if (!same(request.headers.get('authorization') || '', `Bearer ${token}`)) {
      return refuse(401, 'a bearer token is required', { 'www-authenticate': 'Bearer realm="kohaerenzprotokoll-mcp"' });
    }
    return proceed();
  }
  return proceed();
}

export default function middleware(request) {
  return decide(request, process.env);
}
