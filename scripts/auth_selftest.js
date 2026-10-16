// The middleware's login, each case with the outcome it must produce (middleware.js, decision 029 §4).
//   node scripts/auth_selftest.js
import { decide } from '../middleware.js';

const env = { SITE_PASSWORD: 'pw', RAG_MCP_TOKEN: 'tok' };
const basic = (user, pass) => 'Basic ' + btoa(`${user}:${pass}`);
const req = (path, auth) => new Request('https://example.test' + path, { headers: auth ? { authorization: auth } : {} });
const passes = (r) => r.headers.get('x-middleware-next') === '1';

const cases = [
  ['site without credentials asks for a login', () => decide(req('/'), env).status === 401
    && decide(req('/'), env).headers.get('www-authenticate').startsWith('Basic')],
  ['site with the password passes, any user', () => passes(decide(req('/Main.dc.html', basic('x', 'pw')), env))],
  ['site with a wrong password is refused', () => decide(req('/', basic('x', 'pW')), env).status === 401],
  ['a password containing a colon is compared whole', () =>
    passes(decide(req('/', basic('u', 'a:b')), { ...env, SITE_PASSWORD: 'a:b' }))],
  ['site without SITE_PASSWORD stays closed (503), even with credentials', () =>
    decide(req('/', basic('x', 'pw')), { RAG_MCP_TOKEN: 'tok' }).status === 503],
  ['/mcp without a token is refused', () => decide(req('/mcp'), env).status === 401],
  ['/mcp with the token passes', () => passes(decide(req('/mcp', 'Bearer tok'), env))],
  ['/mcp with the site password does not pass', () => decide(req('/mcp', basic('x', 'pw')), env).status === 401],
  ['/api/rag_server needs the token too', () => decide(req('/api/rag_server'), env).status === 401],
  ['/mcp without RAG_MCP_TOKEN stays closed (503)', () => decide(req('/mcp', 'Bearer '), { SITE_PASSWORD: 'pw' }).status === 503],
  ['static pages and agent files are behind the login', () =>
    decide(req('/static/index.html'), env).status === 401 && decide(req('/agents/data.json'), env).status === 401],
  ['garbage in the Basic header is refused, not thrown', () => decide(req('/', 'Basic %%%'), env).status === 401],
];

const failed = cases.filter(([, ok]) => { try { return !ok(); } catch (e) { return true; } }).map(([name]) => name);
console.log(`auth: ${failed.length ? 'FAILED — ' + failed.join('; ') : 'held — every case holds'} (${cases.length} cases)`);
process.exit(failed.length ? 1 : 0);
