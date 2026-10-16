// The project's own login on Vercel (decision 029 §4, the author's „Build your own Auth“ of 2026-10-16).
//
// Vercel's login sits in front of every path and also locks out MCP clients, so the author turns it off and this
// Routing Middleware takes its place, on every request before the site, the static pages or the function:
//
//   the website, llms.txt, agents/, static/  →  HTTP Basic, any user name, the password in SITE_PASSWORD
//   /mcp and /api/*                          →  Authorization: Bearer <RAG_MCP_TOKEN> (api/rag_server.py checks again)
//
// It fails closed: with a variable unset, its paths answer 503 and serve nothing. No dependency — the continue
// signal is the header `x-middleware-next` that `@vercel/functions`' next() sets. scripts/auth_selftest.js tests it.

const REALM = 'Kohaerenz Protokoll';

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
  const auth = request.headers.get('authorization') || '';
  if (path === '/mcp' || path.startsWith('/api/')) {
    const token = env.RAG_MCP_TOKEN;
    if (!token) return refuse(503, 'the MCP server has no RAG_MCP_TOKEN set: it stays closed');
    if (!same(auth, `Bearer ${token}`)) {
      return refuse(401, 'a bearer token is required', { 'www-authenticate': 'Bearer realm="kohaerenzprotokoll-mcp"' });
    }
    return proceed();
  }
  const password = env.SITE_PASSWORD;
  if (!password) return refuse(503, 'the site has no SITE_PASSWORD set: it stays closed');
  if (auth.startsWith('Basic ')) {
    let decoded = '';
    try {
      decoded = atob(auth.slice(6));
    } catch {
      decoded = '';
    }
    const given = decoded.slice(decoded.indexOf(':') + 1);
    if (decoded.includes(':') && same(given, password)) return proceed();
  }
  return refuse(401, 'login required', { 'www-authenticate': `Basic realm="${REALM}", charset="UTF-8"` });
}

export default function middleware(request) {
  return decide(request, process.env);
}
