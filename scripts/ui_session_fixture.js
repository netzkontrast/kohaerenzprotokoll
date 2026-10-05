// Offline behavior checks for the real Component; ui.py supplies DCLogic and data.
(async () => {
  const fail = [];
  const expect = (ok, why) => { if (!ok) fail.push(why); };
  const c = new Component();
  c.props = {}; c.state = { screen: 'now', sess: 'free' };
  const pe = () => c.renderVals().now.pe;
  let copied = 0, saved = 0;
  c.copy = () => { copied += 1; };
  c.download = () => { saved += 1; };
  expect(pe().blocked && pe().hasProblem, 'empty free session must explain why export is blocked');
  pe().copy(); pe().save();
  expect(!copied && !saved, 'empty free session must not copy or download');
  c.saveDraft('psed', 'free', { title: 'Session UI', next: '', files: '' });
  expect(pe().blocked && !pe().hasEntry, 'title alone is neither a task nor a NOW.md session');
  expect(c.entryOf({ title: 'Session UI', next: '' }, '') === '', 'no unreadable title-only NOW.md entry');
  c.saveDraft('pask', 'free', 'Die Session-UI prüfen und verbessern');
  expect(!pe().blocked && !pe().hasEntry && pe().entryHint, 'instruction permits a prompt; NOW.md still needs Next');
  expect(pe().text.includes('Die Session-UI prüfen und verbessern'), 'instruction is present in generated prompt');
  c.saveDraft('psed', 'free', { title: 'Session UI', next: 'Check the free editor', files: 'scripts/ui.js' });
  expect(!pe().blocked && pe().hasEntry && pe().entry.includes('**Next:**'), 'complete free session is exportable');
  expect(pe().text.includes('Session: session-ui'), 'generated prompt carries its own claim id');
  pe().copy(); pe().save();
  expect(copied === 1 && saved === 1, 'complete session exports once');
  c.saveDraft('psed', 'free', { title: '東京', next: 'Review', files: '' });
  expect(pe().blocked && !pe().hasEntry, 'title with no usable id is explained rather than exported');
  c.saveDraft('psed', 'free', { title: 'Session UI', next: 'Check the free editor', files: '' });
  c.saveDraft('poff', 'free', ['notes']);
  c.saveDraft('pedit', 'free', 'Manual task with its own wording');
  expect(pe().edited && !pe().hasEntry && pe().text === 'Manual task with its own wording', 'manual text wins explicitly');
  expect(pe().chips.every((x) => x.dis), 'block controls are disabled for manual text');
  pe().useFields();
  expect(!pe().edited && pe().edTitle === 'Session UI' && pe().ask.includes('verbessern'), 'return to fields preserves title and instruction');
  expect(c.drafts().poff.free.includes('notes'), 'return to fields preserves block choices');
  c.saveDraft('pedit', 'free', '');
  expect(pe().edited && pe().text === '' && pe().blocked, 'deleting manual text does not resurrect the generated prompt');
  c.state.sess = c.kp().sessions.sessions[0].id;
  expect(!pe().blocked, 'planned session remains exportable');
  pe().fork();
  expect(c.state.sess === 'free' && !pe().edited && pe().blocked && !pe().hasEntry, 'fork uses fields and requires its own claim id');
  pe().onEdTitle({ target: { value: 'Session UI follow-up' } });
  expect(!pe().blocked && pe().hasEntry, 'renamed fork gets a distinct exportable claim');

  // React batches setState. Storage must not retain maps from before a clear.
  const queued = new Component(); queued.props = {}; queued.state = {
    screen: 'now', sess: 'free', pedit: { free: 'old manual text' },
    pask: { free: 'old instruction' }, poff: { free: ['notes'] },
    psed: { free: { title: 'Old session', next: 'Old next' } },
  };
  let stored, patch;
  globalThis.window = { localStorage: { setItem: (key, value) => { stored = JSON.parse(value); } } };
  queued.routable = () => true;
  queued.setState = (p) => { patch = p; };
  queued.renderVals().now.pe.reset();
  expect(['pedit', 'pask', 'poff', 'psed'].every((k) => !stored[k].free && !patch[k].free), 'clear persists all maps together before React commits queued state');
  delete globalThis.window;

  // Test request lifecycle with an offline fetch, fake clock and fake timer.
  const nativeNow = Date.now, nativeSet = globalThis.setTimeout, nativeClear = globalThis.clearTimeout;
  let clock = 1800000000000, requests = 0, timeout, timerCleared = false;
  Date.now = () => clock;
  globalThis.setTimeout = (fn, ms) => { timeout = fn; expect(ms === 15000, 'board request has a 15 s timeout'); return 1; };
  globalThis.clearTimeout = () => { timerCleared = true; };
  globalThis.fetch = async () => { requests += 1; return { ok: true, json: async () => [] }; };
  const b = new Component(); b.props = {}; b.state = { screen: 'now' };
  await b.loadBoard();
  expect(requests === 2 && b.state.board.ok && !b.state.boardBusy && timerCleared, 'successful board refresh completes and clears timer');
  clock += 60000; await b.loadBoard();
  expect(requests === 2, 'minute tick does not spend two more requests');
  clock += 240000; await b.loadBoard();
  expect(requests === 4, 'board automatically refreshes after five minutes');
  b.state.screen = 'wiki'; clock += 300000; await b.loadBoard();
  expect(requests === 4, 'other screens do not poll the board');
  b.state.screen = 'now';
  let release;
  globalThis.fetch = () => { requests += 1; return new Promise((resolve) => { release = resolve; }); };
  const pending = b.loadBoard(true);
  await b.loadBoard(true);
  expect(requests === 5 && b.state.boardBusy, 'concurrent manual refresh does not start a second request');
  // Let both calls of this one refresh complete.
  globalThis.fetch = async () => { requests += 1; return { ok: true, json: async () => [] }; };
  release({ ok: true, json: async () => [] }); await pending;
  expect(requests === 6 && !b.state.boardBusy, 'one in-flight refresh finishes normally');
  globalThis.fetch = async () => ({ ok: false, status: 403 });
  await b.loadBoard(true);
  expect(!b.state.board.ok && b.state.board.rows.every((r) => r.state === 'unknown') && !b.state.boardBusy, 'failed refresh clears stale free states and busy flag');
  globalThis.fetch = (url, options) => new Promise((resolve, reject) => {
    options.signal.addEventListener('abort', () => reject(new Error('aborted')));
  });
  const stalled = b.loadBoard(true); timeout(); await stalled;
  expect(!b.state.boardBusy && b.state.board.error === 'request timed out', 'stalled request becomes an actionable unknown state');
  Date.now = nativeNow; globalThis.setTimeout = nativeSet; globalThis.clearTimeout = nativeClear;
  console.log(JSON.stringify(fail));
})().catch((err) => { console.error(err); process.exitCode = 1; });
