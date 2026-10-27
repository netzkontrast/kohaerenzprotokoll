// The middleware's access rule, each case with the outcome it must produce (middleware.js, decisions 029 §5 and 032).
//   node scripts/auth_selftest.js
import { decide } from '../middleware.js';

const env = { RAG_MCP_TOKEN: 'tok' };
const basic = (user, pass) => 'Basic ' + btoa(`${user}:${pass}`);
const req = (path, auth) => new Request('https://example.test' + path, { headers: auth ? { authorization: auth } : {} });
const passes = (r) => r.headers.get('x-middleware-next') === '1';

const cases = [
  // the site is open (decision 032): no credentials, no variable needed
  ['the site opens without credentials', () => passes(decide(req('/'), env)) && passes(decide(req('/Main.dc.html'), env))],
  ['static pages, llms.txt and agent files open without credentials', () =>
    passes(decide(req('/static/index.html'), env)) && passes(decide(req('/llms.txt'), env)) && passes(decide(req('/agents/data.json'), env))],
  ['the site opens with no variable set at all', () => passes(decide(req('/'), {}))],
  ['a stray Basic header does not change the site', () => passes(decide(req('/', basic('x', 'y')), env))],
  // the MCP server keeps its token
  ['/mcp without a token is refused', () => decide(req('/mcp'), env).status === 401],
  ['/mcp with the token passes', () => passes(decide(req('/mcp', 'Bearer tok'), env))],
  ['/mcp with a wrong token is refused', () => decide(req('/mcp', 'Bearer toK'), env).status === 401],
  ['/mcp with a Basic login does not pass', () => decide(req('/mcp', basic('x', 'tok')), env).status === 401],
  ['/api/rag_server needs the token too', () => decide(req('/api/rag_server'), env).status === 401],
  ['any other /api/ path needs the token', () => decide(req('/api/anything'), env).status === 401],
  ['/mcp without RAG_MCP_TOKEN stays closed (503)', () => decide(req('/mcp', 'Bearer '), {}).status === 503],
  ['a path that only looks like /mcp is the site', () => passes(decide(req('/mcp-notes.html'), env))],
];

const failed = cases.filter(([, ok]) => { try { return !ok(); } catch (e) { return true; } }).map(([name]) => name);
console.log(`auth: ${failed.length ? 'FAILED — ' + failed.join('; ') : 'held — every case holds'} (${cases.length} cases)`);
process.exit(failed.length ? 1 : 0);
