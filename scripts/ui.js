class Component extends DCLogic {
  kp() {
    const C = this.constructor;
    if (C.__kp) return C.__kp;
    const D = __DATA__;
    const f = (x) => String(x || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ß/g, 'ss');
    D.fold = f;
    D.val = (k) => (D.state[k] ? D.state[k][0] : 0);
    D.pages.forEach((p) => { p.fx = f([p.t, p.s].concat(p.sf).join(' | ')); });
    D.pageOrder = D.pages.map((p, i) => i).sort((a, b) => D.pages[a].t.localeCompare(D.pages[b].t, 'de', { sensitivity: 'base' }));
    D.defaultPage = Math.max(0, D.pages.findIndex((p) => p.s === 'aegis'));
    D.conflicts.forEach((c) => { c.fx = f([c.id, c.title, c.subj, c.kind].join(' | ')); });
    D.questions.forEach((q) => { q.fx = f([q.id, q.title, q.q].join(' | ')); });
    D.decisions.forEach((d) => { d.fx = f(d.id + ' ' + d.title); });
    D.principles.forEach((p) => { p.fx = f(p.id + ' ' + p.t + ' ' + p.grp); });
    const cp = D.corpus;
    D.rows = cp.rows.map((r, i) => ({
      i: i, title: r[0], slug: r[1], catIdx: r[2], cat: cp.cats[r[2]], tier: cp.tiers[r[3]], fmt: cp.fmts[r[4]],
      date: r[5], landed: !!r[6], read: r[7], sec: cp.sections[r[8]], fx: f(r[0] + ' | ' + r[1]),
    }));
    D.rowBySlug = {};
    D.rows.forEach((r) => { D.rowBySlug[r.slug] = r.i; });
    D.rowsByDate = D.rows.slice().sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : a.title.localeCompare(b.title, 'de')));
    D.catStats = cp.cats.map((c, i) => ({ i: i, name: c, total: 0, landed: 0, read: 0, desc: D.catdesc[c] || '' }));
    const months = {};
    D.rows.forEach((r) => {
      const st = D.catStats[r.catIdx];
      st.total += 1;
      if (r.landed) st.landed += 1;
      if (r.read >= 0) st.read += 1;
      const m = (r.date || '').slice(0, 7);
      if (!m) return;
      months[m] = months[m] || { total: 0, landed: 0, read: 0 };
      months[m].total += 1;
      if (r.landed) months[m].landed += 1;
      if (r.read >= 0) months[m].read += 1;
    });
    D.catOrder = D.catStats.slice().sort((a, b) => b.total - a.total);
    const keys = Object.keys(months).sort();
    D.months = [];
    if (keys.length) {
      let y = +keys[0].slice(0, 4), m = +keys[0].slice(5, 7);
      const last = keys[keys.length - 1];
      for (let guard = 0; guard < 60; guard += 1) {
        const key = y + '-' + (m < 10 ? '0' + m : '' + m);
        const v = months[key] || { total: 0, landed: 0, read: 0 };
        D.months.push({ key: key, y: y, m: m, total: v.total, landed: v.landed, read: v.read });
        if (key === last) break;
        m += 1;
        if (m > 12) { m = 1; y += 1; }
      }
    }
    D.nodeOf = { term: {}, doc: {}, conflict: {}, question: {} };
    D.graph.nodes.forEach((n, i) => { D.nodeOf[n.k][n.ref] = i; });
    D.adj = D.graph.nodes.map(() => []);
    D.graph.edges.forEach((e, i) => { D.adj[e[0]].push(i); D.adj[e[1]].push(i); });
    D.typeCount = D.graph.types.map(() => 0);
    D.graph.edges.forEach((e) => { D.typeCount[e[2]] += 1; });
    D.checkBy = {};
    D.checks.forEach((c) => { D.checkBy[c[0]] = c; });
    D.redMeans = {};
    if (D.invariants && D.invariants[2]) {
      D.invariants[2].forEach((row) => {
        const cmd = (row[0] || []).map((r) => (typeof r === 'string' ? r : r[1])).join('');
        D.redMeans[cmd.replace(/^python3\s+/, '').trim()] = row[1];
      });
    }
    C.__kp = D;
    return D;
  }

  st() { return this.state || {}; }

  go(screen, extra) {
    const patch = { screen: screen, q: '' };
    if (extra) Object.keys(extra).forEach((k) => { patch[k] = extra[k]; });
    this.setState(patch);
  }

  // The state as a URL, on the website only: `#/wiki/aegis`, `#/conflicts/C2`, `#/process/decisions/022`.
  // Stable ids, never list positions, so a link survives the next rebuild. A frame inside the canvas
  // (window.top !== window) neither reads nor writes the address, and a hash not starting `#/` is a
  // section anchor in the reader, left to the browser.
  routable() { try { return typeof window !== 'undefined' && window.top === window; } catch (e) { return false; } }

  route() {
    const D = this.kp();
    const s = this.st();
    const screen = s.screen || this.props.screen || 'now';
    const e = encodeURIComponent;
    let tail = '';
    if (screen === 'now' && s.sess) tail = 'session/' + e(s.sess);
    else if (screen === 'wiki' && s.page != null) tail = e(D.pages[s.page].s);
    else if (screen === 'conflicts' && s.conf != null) tail = D.conflicts[s.conf].id;
    else if (screen === 'questions' && s.ques != null) tail = s.ques === -1 ? 'agenda' : D.questions[s.ques].id;
    else if (screen === 'corpus' && s.crow != null && s.crow >= 0) tail = e(D.rows[s.crow].slug);
    else if (screen === 'graph' && s.gsel != null && s.gsel >= 0) {
      const n = D.graph.nodes[s.gsel];
      const id = n.k === 'term' ? D.pages[n.ref].s : n.k === 'doc' ? D.docs[n.ref].slug
        : n.k === 'conflict' ? D.conflicts[n.ref].id : D.questions[n.ref].id;
      tail = n.k + '/' + e(id);
    } else if (screen === 'manuscript') {
      tail = s.mtab || 'overview';
      if (s.msel) tail += '/' + e(s.msel);
    } else if (screen === 'process') {
      const ptab = s.ptab || 'loop';
      tail = ptab;
      if (ptab === 'decisions' && s.pdec != null) tail += '/' + e(D.decisions[s.pdec].id);
      if (ptab === 'principles' && s.pprin != null) tail += '/' + e(D.principles[s.pprin].id);
      if (ptab === 'compare' && s.pcmp != null) tail += '/' + e(D.compare[s.pcmp].k);
    }
    return '#/' + screen + (tail ? '/' + tail : '');
  }

  unroute(hash) {
    if (!hash || hash.indexOf('#/') !== 0) return null;
    const D = this.kp();
    const parts = hash.slice(2).split('/').map((x) => { try { return decodeURIComponent(x); } catch (err) { return x; } });
    const screen = parts[0];
    const at = (list, key, v) => list.findIndex((x) => x[key] === v);
    const st = { screen: screen, q: '' };
    if (screen === 'now' && parts[1] === 'session' && parts[2]) { if (parts[2] === 'free' || at(D.sessions.sessions, 'id', parts[2]) >= 0) st.sess = parts[2]; }
    else if (screen === 'wiki' && parts[1]) { const i = at(D.pages, 's', parts[1]); if (i >= 0) st.page = i; }
    else if (screen === 'conflicts' && parts[1]) { const i = at(D.conflicts, 'id', parts[1]); if (i >= 0) st.conf = i; }
    else if (screen === 'questions' && parts[1]) {
      const i = parts[1] === 'agenda' ? -1 : at(D.questions, 'id', parts[1]);
      if (i >= -1 && !(i === -1 && parts[1] !== 'agenda')) st.ques = i;
    } else if (screen === 'corpus' && parts[1]) { const i = D.rowBySlug[parts[1]]; if (i != null) st.crow = i; }
    else if (screen === 'graph' && parts[2]) {
      const k = parts[1];
      const ref = k === 'term' ? at(D.pages, 's', parts[2]) : k === 'doc' ? at(D.docs, 'slug', parts[2])
        : k === 'conflict' ? at(D.conflicts, 'id', parts[2]) : k === 'question' ? at(D.questions, 'id', parts[2]) : -1;
      const n = ref >= 0 && D.nodeOf[k] ? D.nodeOf[k][ref] : undefined;
      if (n != null) st.gsel = n;
    } else if (screen === 'manuscript' && parts[1]) {
      if (this.novelTabs().some((t) => t[0] === parts[1])) {
        st.mtab = parts[1];
        if (parts[2] && this.novelEntries(parts[1]).some((x) => x.key === parts[2])) st.msel = parts[2];
      }
    } else if (screen === 'process' && parts[1]) {
      st.ptab = parts[1];
      const list = { decisions: [D.decisions, 'id', 'pdec'], principles: [D.principles, 'id', 'pprin'], compare: [D.compare, 'k', 'pcmp'] }[parts[1]];
      if (list && parts[2]) { const i = at(list[0], list[1], parts[2]); if (i >= 0) st[list[2]] = i; }
    }
    return ['now', 'wiki', 'conflicts', 'questions', 'manuscript', 'graph', 'corpus', 'process'].indexOf(screen) >= 0 ? st : null;
  }

  componentDidMount() {
    if (!this.routable()) return;
    this.loadBoard();
    this._boardTimer = window.setInterval(() => { if (!document.hidden) this.loadBoard(); }, 60000);
    try {
      const saved = JSON.parse(window.localStorage.getItem('kp-prompt-drafts') || 'null');
      if (saved && typeof saved === 'object') this.setState({ pask: saved.pask || {}, pedit: saved.pedit || {}, poff: saved.poff || {}, psed: saved.psed || {} });
    } catch (err) { /* no storage: start empty */ }
    this._onHash = () => {
      const st = this.unroute(window.location.hash);
      if (st && window.location.hash !== this.route()) { this._fromUrl = true; this.setState(st); }
    };
    window.addEventListener('hashchange', this._onHash);
    this._onHash();
  }

  componentWillUnmount() {
    if (this._onHash) window.removeEventListener('hashchange', this._onHash);
    if (this._boardTimer) window.clearInterval(this._boardTimer);
  }

  fmt(n) { return typeof n === 'number' ? n.toLocaleString('en-US') : String(n); }

  // A prompt to the clipboard. A canvas frame may refuse the clipboard; then the button says so
  // instead of claiming a copy, and the prompt stays in the editor, selectable.
  copy(id, text) {
    const done = (ok) => this.setState({ copied: ok ? id : 'fail:' + id });
    try {
      if (typeof navigator !== 'undefined' && navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => done(true), () => done(false));
        return;
      }
    } catch (err) { /* fall through */ }
    done(false);
  }

  // ---- the session board: NOW.md's plan against GitHub (the same rule as scripts/sessions.py `board()`;
  // ui.py's check_board runs both on one case). Pure: the live state and the clock come in as arguments.
  boardOf(live, nowMs) {
    const P = this.kp().sessions;
    const re = new RegExp(P.board.claim, 'g');
    const hours = P.board.hours;
    const branches = {};
    (live.activity || []).forEach((a) => {
      if (a.type !== 'push' || a.ref.indexOf('refs/heads/') !== 0 || a.ref === 'refs/heads/main') return;
      if (nowMs - Date.parse(a.at) > hours * 3600000) return;
      const name = a.ref.slice('refs/heads/'.length);
      const b = branches[name] || (branches[name] = { pushes: 0, last: a.at, sha: a.sha });
      b.pushes += 1;
      if (a.at > b.last) { b.last = a.at; b.sha = a.sha; }
    });
    const claims = (live.pulls || []).map((p) => {
      const ids = []; const text = p.title + '\n' + p.body; let m;
      re.lastIndex = 0;
      while ((m = re.exec(text)) !== null) ids.push(m[1].toLowerCase());
      const b = branches[p.branch];
      return { pr: p.number, title: p.title, url: p.url, branch: p.branch, ids: ids, last: b ? b.last : p.updated, active: !!b };
    });
    const planned = {};
    P.sessions.forEach((x) => { planned[x.id] = true; });
    const rows = P.sessions.map((x) => {
      const by = claims.filter((c) => c.ids.indexOf(x.id) >= 0);
      return { id: x.id, state: !live.ok ? 'unknown' : by.length ? 'claimed' : 'free', by: by };
    });
    const claimedBranches = {};
    claims.forEach((c) => { if (c.ids.some((i) => planned[i])) claimedBranches[c.branch] = true; });
    const other = Object.keys(branches).filter((n) => !claimedBranches[n])
      .sort((a, b) => (branches[a].last < branches[b].last ? 1 : branches[a].last > branches[b].last ? -1 : 0))
      .map((n) => {
        const pr = claims.find((c) => c.branch === n);
        return { branch: n, last: branches[n].last, pr: pr ? pr.pr : null, title: pr ? pr.title : '', ids: pr ? pr.ids : [] };
      });
    return { ok: !!live.ok, error: live.error || '', rows: rows, other: other, claims: claims };
  }

  async loadBoard() {
    const P = this.kp().sessions.board;
    this.setState({ boardBusy: true });
    let live;
    try {
      const get = async (path) => {
        const r = await fetch(P.api + path, { headers: { Accept: 'application/vnd.github+json' } });
        if (!r.ok) throw new Error('GitHub answered ' + r.status);
        return r.json();
      };
      const pulls = await get('/pulls?state=open&per_page=100');
      const act = await get('/activity?per_page=100&time_period=day');
      live = { ok: true, error: '', at: new Date().toISOString().slice(0, 19) + 'Z',
        pulls: pulls.map((p) => ({ number: p.number, title: p.title, body: p.body || '', branch: p.head.ref, url: p.html_url, updated: p.updated_at })),
        activity: act.map((a) => ({ ref: a.ref, type: a.activity_type, at: a.timestamp, sha: a.after })) };
    } catch (err) {
      live = { ok: false, error: String(err && err.message || err).slice(0, 160), at: new Date().toISOString().slice(0, 19) + 'Z', pulls: [], activity: [] };
    }
    this.setState({ board: this.boardOf(live, Date.now()), boardAt: live.at, boardBusy: false });
  }

  claimLine(id) {
    const bd = this.st().board;
    if (!bd) return this.routable() ? 'checking claims…' : '';
    const r = bd.rows.find((x) => x.id === id);
    if (!bd.ok || !r) return 'claim unknown';
    if (r.state === 'free') return 'no claim';
    const c = r.by[0];
    return 'claimed · #' + c.pr + ' ' + c.branch + (c.active ? ' · pushed ' + this.ago(c.last) : ' · quiet');
  }

  claimTone(id) {
    const bd = this.st().board;
    const r = bd && bd.ok ? bd.rows.find((x) => x.id === id) : null;
    if (!r) return ['#EFEBE1', '#645F53'];
    return r.state === 'claimed' ? ['#F6E4DC', '#9A2D1A'] : ['#E4EDDF', '#2F5D2A'];
  }

  ago(iso) {
    const m = Math.max(0, Math.round((Date.now() - Date.parse(iso)) / 60000));
    return m < 90 ? m + ' min ago' : Math.round(m / 60) + ' h ago';
  }

  // ---- the start-prompt editor on the Now screen
  // A prompt is its session's blocks (scripts/sessions.py), those switched off left out, the author's own
  // instruction after the read-first block. Text edited by hand wins until Reset. Drafts are kept in this
  // browser only (website; a canvas frame keeps them for the visit) — never in the repository.
  promptSource(id) {
    const P = this.kp().sessions;
    return id === 'free' ? P.free : P.sessions.find((x) => x.id === id) || P.free;
  }

  // The session editor's id and NOW.md entry: the same rules as scripts/sessions.py (`slug`, `derive`), which
  // ui.py's check_editor runs both ways. The id is never typed: it is the slug of the title, because that is
  // the id NOW.md's entry will be given, and a claim under another id would claim nothing.
  slugOf(title) {
    const words = String(title || '').toLowerCase().normalize('NFKD').replace(/[^\x00-\x7f]/g, '').match(/[a-z0-9]+/g) || [];
    let out = '';
    for (let i = 0; i < words.length; i += 1) {
      if (out && out.length + 1 + words[i].length > 48) break;
      out = out ? out + '-' + words[i] : words[i];
    }
    return out;
  }

  entryOf(ed, ask) {
    const files = String(ed.files || '').split(/[\s,]+/).filter(Boolean);
    const clean = (t) => String(t || '').replace(/\s+/g, ' ').trim();
    const title = clean(ed.title).replace(/[.:]+$/, '');
    if (!title) return '';
    return '- **' + title + '.** ' + (clean(ask) ? clean(ask).replace(/\*\*/g, '') + ' ' : '')
      + (files.length ? 'Files: ' + files.map((f) => '`' + f + '`').join(', ') + '. ' : '')
      + (clean(ed.next) ? '**Next:** ' + clean(ed.next).replace(/\*\*/g, '') : '');
  }

  compose(x, ask, off, ed) {
    const out = [];
    const free = x.id === 'free' && ed && ed.title && ed.title.trim();
    const repo = this.kp().sessions.board.repo;
    x.blocks.forEach((b) => {
      if (off.indexOf(b[0]) >= 0) return;
      let text = b[2];
      if (free && b[0] === 'head') text = 'Session for ' + repo + ': ' + ed.title.trim();
      if (free && b[0] === 'rules') text = text.replace('Session: free', 'Session: ' + this.slugOf(ed.title));
      out.push(text);
      if (b[0] === 'read') {
        if (ask.trim()) out.push('The author\'s instruction for this session:\n' + ask.trim());
        if (free) {
          out.push('The task: ' + ed.title.trim());
          if ((ed.next || '').trim()) out.push('Start with: ' + ed.next.trim());
          const files = String(ed.files || '').split(/[\s,]+/).filter(Boolean);
          if (files.length) out.push('Open first: ' + files.join(', '));
        }
      }
    });
    return out.join('\n\n');
  }

  drafts() { const st = this.st(); return { pask: st.pask || {}, pedit: st.pedit || {}, poff: st.poff || {}, psed: st.psed || {} }; }

  saveDraft(kind, id, value) {
    const d = this.drafts();
    const next = Object.assign({}, d[kind]);
    if (value == null || value === '' || (Array.isArray(value) && !value.length) || (kind === 'psed' && !value.title && !value.next && !value.files)) delete next[id];
    else next[id] = value;
    const patch = { copied: null };
    patch[kind] = next;
    this.setState(patch);
    if (!this.routable()) return;
    try {
      const all = Object.assign({}, d, patch);
      window.localStorage.setItem('kp-prompt-drafts', JSON.stringify({ pask: all.pask, pedit: all.pedit, poff: all.poff, psed: all.psed }));
    } catch (err) { /* storage refused: the draft lives for this visit */ }
  }

  download(name, text) {
    try {
      const a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([text], { type: 'text/markdown;charset=utf-8' }));
      a.download = name;
      document.body.appendChild(a);
      a.click();
      setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 0);
    } catch (err) { /* nothing to save to */ }
  }

  txt(rs) {
    return (rs || []).map((r) => (typeof r === 'string' ? r : r[0] === 'r' ? '' : r[1])).join('').replace(/\s+/g, ' ').trim();
  }

  runs(rs, flat) {
    const D = this.kp();
    const out = [];
    (rs || []).forEach((r) => {
      if (typeof r === 'string') { out.push({ isT: true, x: r }); return; }
      const t = r[0];
      if (t === 'l') {
        const idx = r[2];
        if (flat) out.push({ isT: true, x: r[1] });
        else out.push({ isL: true, x: r[1], go: () => this.go('wiki', { page: idx }) });
      } else if (t === 'r') {
        const labs = [];
        const tips = [];
        (r[1] || []).forEach((ref) => {
          const d = ref[0];
          const lines = String(ref[1] || '');
          const doc = typeof d === 'number' && d >= 0 ? D.docs[d] : null;
          const sig = doc ? doc.sig : (typeof d === 'string' ? d.slice(0, 18) + '…' : '');
          const short = lines.length > 16 ? lines.split(',')[0] + ' …' : lines;
          labs.push(sig ? sig + ' ' + short : short);
          tips.push((doc ? doc.sig + ' · ' + doc.title : String(d)) + ' — ' + lines);
        });
        out.push({ isR: true, x: labs.join(' · '), title: tips.join('\n') });
      } else if (t === 'b') out.push({ isB: true, x: r[1] });
      else if (t === 'g') out.push({ isG: true, x: r[1] });
      else if (t === 'i') out.push({ isI: true, x: r[1] });
      else if (t === 'c') out.push({ isC: true, x: r[1] });
      else out.push({ isT: true, x: String(r[1] || '') });
    });
    return out;
  }

  blocks(bs) {
    const out = [];
    (bs || []).forEach((b) => {
      const k = b[0];
      if (k === 'p' || k === 'q' || k === 'h') out.push({ isP: k === 'p', isQ: k === 'q', isH: k === 'h', runs: this.runs(b[1]) });
      else if (k === 'ul' || k === 'ol') out.push({ isUL: k === 'ul', isOL: k === 'ol', items: (b[1] || []).map((it) => ({ runs: this.runs(it) })) });
      else if (k === 'tb') {
        const al = b[3] || '';
        const cols = b[4] || 'repeat(' + Math.max(1, (b[1] || []).length) + ', minmax(0, 1fr))';
        const cell = (c, j) => ({ runs: this.runs(c), ta: al.charAt(j) === 'r' ? 'right' : 'left' });
        out.push({ isTB: true, head: { cols: cols, cells: (b[1] || []).map(cell) }, rows: (b[2] || []).map((row) => ({ cols: cols, cells: row.map(cell) })) });
      } else if (k === 'pre') out.push({ isPre: true, x: b[1] });
    });
    return out;
  }

  secs(lede, secs, prefix) {
    const D = this.kp();
    const out = [];
    if (lede && lede.length) out.push({ hasHead: false, head: [], blocks: this.blocks(lede), hasSig: false, sig: '', slug: '', sigTitle: '', sigBg: '', sigFg: '', anchor: prefix + '-lede', pt: 0, label: '' });
    (secs || []).forEach((sc, i) => {
      const d = sc[1];
      const doc = typeof d === 'number' && d >= 0 ? D.docs[d] : null;
      const canon = !!(doc && doc.canon);
      out.push({
        hasHead: true, head: this.runs(sc[0]), blocks: this.blocks(sc[3]),
        hasSig: !!doc, sig: doc ? doc.sig : '', slug: doc ? doc.slug : '',
        sigTitle: doc ? doc.title + ' · ' + doc.date : '',
        sigBg: canon ? '#2B4C8C' : '#E4E9F2', sigFg: canon ? '#FBFAF6' : '#2B4C8C',
        anchor: prefix + '-' + i, pt: 6, label: this.txt(sc[0]), dt: sc[2] || '',
      });
    });
    return out;
  }

  chip(x, kind) {
    const k = {
      ink: ['#1C1B18', '#FBFAF6', '#1C1B18'],
      rubric: ['#F6E4DC', '#9A2D1A', '#E8C2B4'],
      blue: ['#E4E9F2', '#2B4C8C', '#C3CEE3'],
      plain: ['transparent', '#4A463E', '#C9C0AC'],
    }[kind || 'plain'];
    return { x: x, bg: k[0], fg: k[1], bd: k[2] };
  }

  // The novel's workspace (decision 024): its tabs, and each tab's entries with a stable key, so the
  // list, the reader and the address all read the same thing. Only canon and working drafts: canon is
  // what Manuscript/kanon.md lists; a wiki page is a link out, never content.
  novelTabs() {
    return [['overview', 'Overview'], ['chapters', 'Chapters'], ['cast', 'Cast'], ['world', 'World'], ['plot', 'Plot'], ['decisions', 'Decisions'], ['findings', 'Findings']];
  }

  novelDecided(w) {
    const N = this.kp().novel;
    return w.status === 'beantwortet' || N.kanon.some((k) => k.id === w.id);
  }

  novelEntries(tab) {
    const D = this.kp();
    const N = D.novel;
    const out = [];
    const fin = (j) => ({ key: N.findings[j].f, kind: 'finding', ref: j });
    if (tab === 'chapters') {
      N.chapters.forEach((c) => {
        out.push({ group: 'Kap ' + c.n });
        if (c.readme >= 0) out.push({ key: D.manuscript[c.readme].f, kind: 'draft', ref: c.readme });
        c.drafts.forEach((i) => out.push({ key: D.manuscript[i].f, kind: 'draft', ref: i }));
        if (c.findings.length) {
          out.push({ group: 'Findings on Kap ' + c.n });
          c.findings.forEach((j) => out.push(fin(j)));
        }
      });
    } else if (tab === 'cast' || tab === 'world') {
      const kind = tab === 'cast' ? 'figuren' : 'welt';
      const cards = N.cards.map((c, i) => ({ c: c, i: i })).filter((o) => o.c.kind === kind);
      [['Canon', (c) => c.kanon.length > 0], ['In the sources — nothing decided', (c) => !c.kanon.length && c.wiki >= 0],
        ['Invented in a draft', (c) => !c.kanon.length && c.wiki < 0]].forEach((g) => {
        const these = cards.filter((o) => g[1](o.c));
        if (these.length) {
          out.push({ group: g[0] });
          these.forEach((o) => out.push({ key: o.c.s, kind: 'card', ref: o.i }));
        }
      });
    } else if (tab === 'plot') {
      D.manuscript.forEach((m, i) => { if (m.part === 'plot') out.push({ key: m.f, kind: 'draft', ref: i }); });
    } else if (tab === 'decisions') {
      if (N.ledger) { out.push({ group: 'Canon' }); out.push({ key: 'kanon', kind: 'ledger', ref: 0 }); }
      const all = N.weichen.map((w, i) => ({ w: w, i: i }));
      const open = all.filter((o) => !this.novelDecided(o.w));
      const done = all.filter((o) => this.novelDecided(o.w));
      if (open.length) { out.push({ group: 'Weichen — open' }); open.forEach((o) => out.push({ key: o.w.id, kind: 'weiche', ref: o.i })); }
      if (done.length) { out.push({ group: 'Weichen — decided' }); done.forEach((o) => out.push({ key: o.w.id, kind: 'weiche', ref: o.i })); }
    } else if (tab === 'findings') {
      const idx = N.findings.map((x, j) => j);
      const own = idx.filter((j) => !N.findings[j].legacy);
      const leg = idx.filter((j) => N.findings[j].legacy);
      if (own.length) { out.push({ group: 'On the drafts and the material' }); own.forEach((j) => out.push(fin(j))); }
      if (leg.length) { out.push({ group: 'On the parked Legacy draft' }); leg.forEach((j) => out.push(fin(j))); }
    }
    return out;
  }

  pageChip(i) {
    const p = this.kp().pages[i];
    return { t: p.t, go: () => this.go('wiki', { page: i }) };
  }

  renderVals() {
    const D = this.kp();
    const s = this.st();
    const V = D.val;
    const fmt = (n) => this.fmt(n);
    const SCREENS = ['now', 'wiki', 'conflicts', 'questions', 'manuscript', 'graph', 'corpus', 'process'];
    let screen = s.screen || this.props.screen || 'now';
    if (SCREENS.indexOf(screen) < 0) screen = 'now';
    const uid = 'kp-' + (this.props.screen || 'main');
    const ptab = s.ptab || 'loop';
    const mtab = s.mtab || 'overview';
    const is = {
      now: screen === 'now', wiki: screen === 'wiki', conflicts: screen === 'conflicts', questions: screen === 'questions',
      graph: screen === 'graph', corpus: screen === 'corpus', process: screen === 'process', manuscript: screen === 'manuscript',
    };
    is.procList = (is.process && (ptab === 'compare' || ptab === 'decisions' || ptab === 'principles' || ptab === 'now' || ptab === 'goal'))
      || (is.manuscript && mtab !== 'overview');
    is.readerLayout = is.wiki || is.conflicts || is.questions || is.process || is.manuscript;
    is.left = is.wiki || is.conflicts || is.questions || is.procList;
    is.rail = is.wiki || is.conflicts || is.questions;
    is.loop = is.process && ptab === 'loop';
    is.checks = is.process && ptab === 'checks';

    const openC = D.conflicts.filter((c) => !c.decided).length;
    const navItem = (key, n) => {
      const on = screen === key;
      return {
        go: () => this.go(key), cur: on ? 'page' : undefined, n: n,
        bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', fw: on ? 600 : 400, ic: on ? '#B0341E' : '#4A463E',
      };
    };
    const nav = {
      now: navItem('now', ''),
      wiki: navItem('wiki', String(D.pages.length)),
      conflicts: navItem('conflicts', openC + ' open'),
      questions: navItem('questions', String(D.questions.length)),
      manuscript: navItem('manuscript', String(D.novel.kanon.length) + ' canon'),
      graph: navItem('graph', String(D.graph.nodes.length)),
      corpus: navItem('corpus', String(D.rows.length)),
      process: navItem('process', ''),
    };

    const held = D.selftests.filter((x) => x[0] === 'held').length;
    const failed = D.selftests.filter((x) => x[0] === 'FAILED').length;
    const chk = (label, val, ok) => ({ label: label, val: val, dot: ok === true ? '#2B4C8C' : ok === false ? '#B0341E' : '#9A9384', fg: ok === false ? '#B0341E' : '#4A463E' });
    const prose = D.checkBy['scripts/state.py --prose'];
    const proseN = prose ? parseInt(prose[2], 10) : NaN;
    const railChecks = [
      chk('Pipeline order', V('order.holds') ? 'holds' : 'broken', !!V('order.holds')),
      chk('Prose numbers', isNaN(proseN) ? '—' : proseN + ' stale', isNaN(proseN) ? null : proseN === 0),
      chk('Judgements', V('judgements.disagree') + ' disagree', V('judgements.disagree') === 0),
      chk('Quotations', V('quotes.unresolved') + ' unresolved', V('quotes.unresolved') === 0),
      chk('Self-tests', held + '/' + D.selftests.length + ' held', failed === 0),
    ];
    const goChecks = () => this.go('process', { ptab: 'checks' });

    const tops = {
      now: ['Now', 'What is open, what waits on the author, and what the repository measures today'],
      wiki: ['Wiki', D.pages.length + ' candidate pages · every reading attributed and unmerged · where sources disagree, a page says so and stops'],
      conflicts: ['Conflicts', D.conflicts.length + ' append-only records of two sources that cannot both hold · a record decides nothing; the author does'],
      questions: ['Questions', 'What several pages ask and no source read so far answers · and everything noted for the author'],
      manuscript: ['Manuscript', 'The novel’s workspace · only canon and working drafts · canon is what Manuscript/kanon.md lists; research lives in the Wiki'],
      graph: ['Knowledge graph', D.graph.nodes.length + ' nodes · ' + fmt(D.graph.edges.length) + ' typed edges · each carries the file line that states it; none is inferred'],
      corpus: ['Corpus', D.rows.length + ' Drive documents in the manifest · ' + V('sources.landed') + ' landed as Markdown · ' + D.docs.length + ' read'],
      process: ['Process', 'The loop that extends the wiki, the checks that keep it honest, and the rules behind both'],
    };
    const top = { title: tops[screen][0], sub: tops[screen][1] };

    // ------------------------------------------------------------ global search
    const q = s.q || '';
    const sr = { show: false, groups: [], none: false };
    const fq = D.fold(q.trim());
    if (fq.length >= 2) {
      const rank = (fx, name) => { const n = D.fold(name); return n === fq ? 0 : n.indexOf(fq) === 0 ? 1 : fx.indexOf(fq) === 0 ? 2 : 3; };
      const pick = (list, fxOf, nameOf) => list.map((x, i) => ({ x: x, i: i })).filter((o) => fxOf(o.x).indexOf(fq) >= 0).sort((a, b) => rank(fxOf(a.x), nameOf(a.x)) - rank(fxOf(b.x), nameOf(b.x)));
      const groups = [];
      const pg = pick(D.pages, (p) => p.fx, (p) => p.t);
      if (pg.length) groups.push({ label: 'Wiki pages', n: pg.length, items: pg.slice(0, 7).map((o) => ({ k: 'page', kc: '#4A463E', t: o.x.t, s: o.x.s + ' · ' + o.x.rd + ' readings', go: () => this.go('wiki', { page: o.i }) })) });
      const cf = pick(D.conflicts, (c) => c.fx, (c) => c.id);
      if (cf.length) groups.push({ label: 'Conflicts', n: cf.length, items: cf.slice(0, 5).map((o) => ({ k: o.x.id, kc: '#B0341E', t: o.x.title.replace(/^C\d+\s*—\s*/, ''), s: o.x.subj + ' · ' + (o.x.decided ? 'decided' : 'open'), go: () => this.go('conflicts', { conf: o.i }) })) });
      const qs = pick(D.questions, (x) => x.fx, (x) => x.id);
      if (qs.length) groups.push({ label: 'Questions', n: qs.length, items: qs.slice(0, 5).map((o) => ({ k: o.x.id, kc: '#B0341E', t: o.x.q, s: o.x.title, go: () => this.go('questions', { ques: o.i }) })) });
      const rs = pick(D.rows, (r) => r.fx, (r) => r.title);
      if (rs.length) groups.push({ label: 'Sources', n: rs.length, items: rs.slice(0, 6).map((o) => ({ k: o.x.read >= 0 ? D.docs[o.x.read].sig : (o.x.landed ? 'landed' : 'drive'), kc: '#2B4C8C', t: o.x.title, s: o.x.cat + ' · ' + o.x.date, go: () => this.go('corpus', { crow: o.i }) })) });
      const ds = pick(D.decisions, (d) => d.fx, (d) => d.title);
      if (ds.length) groups.push({ label: 'Decisions', n: ds.length, items: ds.slice(0, 4).map((o) => ({ k: o.x.id, kc: '#4A463E', t: o.x.title, s: o.x.date + ' · ' + o.x.status, go: () => this.go('process', { ptab: 'decisions', pdec: o.i }) })) });
      const ps = pick(D.principles, (p) => p.fx, (p) => p.t);
      if (ps.length) groups.push({ label: 'Principles', n: ps.length, items: ps.slice(0, 4).map((o) => ({ k: o.x.id, kc: '#4A463E', t: o.x.t, s: o.x.grp, go: () => this.go('process', { ptab: 'principles', pprin: o.i }) })) });
      sr.show = true;
      sr.groups = groups;
      sr.none = groups.length === 0;
    }
    const onQ = (e) => this.setState({ q: e.target.value });
    const onQKey = (e) => { if (e.key === 'Escape') this.setState({ q: '' }); };

    // ------------------------------------------------------------ now
    const now = { board: { live: false, other: [], hasOther: false, caution: false, showStamp: false, busy: false, stamp: '', hours: 24, refresh: null }, tiles: [], agenda: [], asks: [], log: [], sessions: [], sessSub: '', web: false, free: {}, pe: { chips: [] }, tabs: [], tabPrompt: true, tabLog: false, l1: '', l2: '', l3: '', logSub: '', selftests: '', stDot: '#2B4C8C' };
    if (is.now) {
      const total = V('sources.total');
      const landed = V('sources.landed');
      const pages = V('wiki.pages');
      const orphans = V('wiki.orphans');
      const decided = D.conflicts.length - openC;
      const qc = V('quotes.checked');
      const qu = V('quotes.unchecked');
      const qun = V('quotes.unresolved');
      const pct = (a, b) => Math.max(2, Math.min(100, Math.round((100 * a) / Math.max(1, b))));
      now.l1 = D.docs.length + ' of ' + fmt(landed) + ' landed documents read. ';
      now.l2 = pages + ' candidate pages, none promoted. ';
      now.l3 = openC + ' conflicts wait on the author.';
      now.tiles = [
        { label: 'Sources', big: fmt(landed), unit: 'of ' + fmt(total) + ' landed', pct: pct(landed, total), color: '#2B4C8C', sub: (total - landed) + ' still on Drive · ' + D.corpus.folded + ' copies folded away', go: () => this.go('corpus') },
        { label: 'Read', big: String(D.docs.length), unit: 'documents', pct: pct(D.docs.length, landed), color: '#1C1B18', sub: 'census, note and reconciliation each · ' + V('sources.canon_era_landed') + ' of ' + V('sources.canon_era') + ' canon-era rows landed', go: () => this.go('corpus', { cfilter: 'read' }) },
        { label: 'Wiki', big: String(pages), unit: 'candidate pages', pct: pct(pages - orphans, pages), color: '#1C1B18', sub: V('wiki.relations') + ' links · ' + orphans + ' pages nothing links to', go: () => this.go('wiki') },
        { label: 'Conflicts', big: String(D.conflicts.length), unit: 'records', pct: pct(decided, D.conflicts.length), color: '#B0341E', sub: openC + ' open · ' + decided + ' decided by the author', go: () => this.go('conflicts') },
        { label: 'Quotations', big: fmt(qc), unit: 'checked', pct: pct(qc, qc + qu), color: '#2B4C8C', sub: qun + ' do not resolve · ' + qu + ' carry no checkable citation', go: goChecks },
        { label: 'Retrieval', big: V('graphrag.recall_ppr') + '%', unit: 'recall@8', pct: pct(V('graphrag.recall_ppr'), 100), color: '#2B4C8C', sub: V('graphrag.recall_seeds') + '% from the seeds alone · ' + V('graphrag.cases') + ' labelled cases', go: () => this.go('graph') },
      ];
      const ag = [];
      D.conflicts.forEach((c, i) => {
        const question = c.np ? c.np.q : [c.title.replace(/^C\d+\s*—\s*/, '')];
        ag.push({
          id: c.id, idc: c.decided ? '#1C1B18' : '#B0341E', q: this.runs(question, true), meta: c.subj + ' · ' + c.kind,
          st: c.decided ? 'Decided' : 'Open', stBg: c.decided ? '#1C1B18' : '#F6E4DC', stFg: c.decided ? '#FBFAF6' : '#9A2D1A',
          order: c.decided ? 1 : 0, go: () => this.go('conflicts', { conf: i }),
        });
      });
      now.agenda = ag.filter((a) => a.order === 0).concat(ag.filter((a) => a.order === 1));
      now.asks = D.agenda.process.map((u) => ({ runs: this.runs(u) }));
      const mt = Math.max.apply(null, D.docs.map((d) => d.terms).concat([1]));
      const mr = Math.max.apply(null, D.docs.map((d) => d.readings).concat([1]));
      const mc = Math.max.apply(null, D.docs.map((d) => d.conflicts).concat([1]));
      now.log = D.docs.map((d, i) => ({
        sig: d.sig, title: d.title, date: d.date, cat: d.cat, sigBg: d.canon ? '#2B4C8C' : '#E4E9F2', sigFg: d.canon ? '#FBFAF6' : '#2B4C8C',
        t: d.terms ? String(d.terms) : '—', r: d.readings ? String(d.readings) : '—', c: d.conflicts ? String(d.conflicts) : '—',
        tw: Math.round((100 * d.terms) / mt), rw: Math.round((100 * d.readings) / mr), cw: Math.round((100 * d.conflicts) / mc),
        go: () => this.go('corpus', { crow: D.rowBySlug[d.slug] }),
      }));
      const canonN = D.docs.filter((d) => d.canon).length;
      now.logSub = (D.docs.length - canonN) + ' before the canon era · ' + canonN + ' from it';
      const plan = D.sessions;
      const firstReady = plan.sessions.find((x) => x.status === 'ready');
      const selId = s.sess || (firstReady ? firstReady.id : 'free');
      now.sessions = plan.sessions.map((x) => {
        const on = selId === x.id;
        const ready = x.status === 'ready';
        return {
          dom: uid + '-sess-' + x.id, n: String(x.n), t: x.title, st: x.status, stBg: ready ? '#E4E9F2' : '#F6E4DC', stFg: ready ? '#2B4C8C' : '#9A2D1A',
          claim: this.claimLine(x.id), claimBg: this.claimTone(x.id)[0], claimFg: this.claimTone(x.id)[1],
          next: this.runs(x.nruns), bd: on ? '#2B4C8C' : '#E6E0D2', bg: on ? '#FFFFFF' : 'transparent', cur: on ? 'true' : 'false',
          pick: () => this.setState({ sess: x.id, ntab: 'prompt', copied: null }),
        };
      });
      now.free = { bd: selId === 'free' ? '#2B4C8C' : '#E6E0D2', label: '＋ New session — title, next step, files, claim, NOW.md entry', cur: selId === 'free' ? 'true' : 'false', pick: () => this.setState({ sess: 'free', ntab: 'prompt', copied: null }) };
      const bd = s.board;
      now.board = {
        live: !!bd, ok: !!bd && bd.ok, busy: !!s.boardBusy, refresh: () => this.loadBoard(),
        stamp: !bd ? 'reading GitHub…' : bd.ok ? 'GitHub read ' + this.ago(s.boardAt) : 'GitHub not reached — ' + bd.error,
        showStamp: this.routable(),
        other: !bd || !bd.ok ? [] : bd.other.map((o) => ({
          branch: o.branch, when: this.ago(o.last),
          pr: o.pr ? '#' + o.pr + ' ' + o.title + (o.ids.length ? ' · Session: ' + o.ids.join(', ') : '') : 'no pull request — no claim',
          tone: o.pr ? '#4A463E' : '#9A2D1A',
        })),
        hasOther: !!bd && bd.ok && bd.other.length > 0,
        caution: !!bd && bd.ok && bd.other.some((o) => !o.pr) && bd.rows.some((r) => r.state === 'free'),
        hours: plan.board.hours,
      };
      const readyN = plan.sessions.filter((x) => x.status === 'ready').length;
      now.sessSub = readyN + ' ready · ' + (plan.sessions.length - readyN) + ' wait on the author · ' + plan.notes.length + ' notes bind all';
      now.tabPrompt = (s.ntab || 'prompt') === 'prompt';
      now.tabLog = !now.tabPrompt;
      now.tabs = [['prompt', 'Start prompt'], ['log', 'Reading log']].map((t) => {
        const on = (s.ntab || 'prompt') === t[0];
        return { label: t[1], on: on ? 'true' : 'false', bd: on ? '#1C1B18' : 'transparent', fg: on ? '#1C1B18' : '#645F53', go: () => this.setState({ ntab: t[0] }) };
      });
      const src = this.promptSource(selId);
      const d = this.drafts();
      const ask = d.pask[selId] || '';
      const off = d.poff[selId] || [];
      const edited = d.pedit[selId];
      const ed = Object.assign({ title: '', next: '', files: '' }, d.psed.free || {});
      const isFree = selId === 'free';
      const composed = this.compose(src, ask, off, ed);
      const text = edited != null ? edited : composed;
      const copied = s.copied === 'pe:' + selId;
      const failedCopy = s.copied === 'fail:pe:' + selId;
      const fixed = ['head', 'read'];
      now.pe = {
        kicker: selId === 'free' ? 'Session editor · a session of your own, with the rules every session keeps'
          : 'Session ' + src.n + ' · ' + src.status + ' · from NOW.md § Half-done',
        title: selId === 'free' ? (ed.title.trim() || 'A session you name yourself') : src.title,
        isFree: isFree, canFork: !isFree,
        edTitle: ed.title, edNext: ed.next, edFiles: ed.files, edId: this.slugOf(ed.title) || '—',
        onEdTitle: (e) => this.saveDraft('psed', 'free', Object.assign({}, ed, { title: e.target.value })),
        onEdNext: (e) => this.saveDraft('psed', 'free', Object.assign({}, ed, { next: e.target.value })),
        onEdFiles: (e) => this.saveDraft('psed', 'free', Object.assign({}, ed, { files: e.target.value })),
        fork: () => { this.saveDraft('psed', 'free', { title: src.title, next: src.next, files: (src.files || []).join(', ') }); this.setState({ sess: 'free', copied: null }); },
        hasEntry: isFree && !!ed.title.trim(),
        claimLine: 'Session: ' + this.slugOf(ed.title),
        entry: this.entryOf(ed, ask),
        copyClaim: () => this.copy('pc:' + selId, '## Claim\n\nSession: ' + this.slugOf(ed.title)),
        copyClaimLabel: s.copied === 'pc:' + selId ? 'Copied ✓' : 'Copy claim',
        copyEntry: () => this.copy('pn:' + selId, this.entryOf(ed, ask)),
        copyEntryLabel: s.copied === 'pn:' + selId ? 'Copied ✓' : 'Copy NOW.md entry',
        askId: uid + '-pe-ask', textId: uid + '-pe-text', ask: ask, text: text,
        askHint: selId === 'free' ? 'What should the session do? In your words — it goes right after “read NOW.md first”.'
          : 'Anything to add or narrow — „nur das erste Dokument“, a deadline, a question first. Goes before the task.',
        onAsk: (e) => this.saveDraft('pask', selId, e.target.value),
        onText: (e) => this.saveDraft('pedit', selId, e.target.value),
        chips: src.blocks.filter((b) => fixed.indexOf(b[0]) < 0).map((b) => {
          const isOn = off.indexOf(b[0]) < 0;
          return {
            label: b[1], on: isOn ? 'true' : 'false', bg: isOn ? '#2B4C8C' : 'transparent', fg: isOn ? '#FBFAF6' : '#645F53', bd: isOn ? '#2B4C8C' : '#C9C0AC',
            dis: edited != null, tip: edited != null ? 'Edited by hand — Reset to use the blocks again' : (isOn ? 'Leave this block out' : 'Put this block in'),
            go: () => this.saveDraft('poff', selId, isOn ? off.concat([b[0]]) : off.filter((k) => k !== b[0])),
          };
        }),
        info: text.length.toLocaleString('en-US') + ' characters · ' + text.split(/\s+/).filter(Boolean).length + ' words' + (edited != null ? ' · edited by hand' : ''),
        dirty: edited != null || !!ask || off.length > 0 || (isFree && !!(ed.title || ed.next || ed.files)), edited: edited != null,
        reset: () => { this.saveDraft('pedit', selId, null); this.saveDraft('pask', selId, null); this.saveDraft('poff', selId, null); if (isFree) this.saveDraft('psed', 'free', null); },
        copy: () => this.copy('pe:' + selId, text),
        copyLabel: copied ? 'Copied ✓' : failedCopy ? 'Copy blocked here — select the text' : 'Copy prompt',
        save: () => this.download('start-prompt-' + selId + '.md', text),
      };
      now.web = this.routable();
      now.selftests = held + ' held · ' + failed + ' failed · ' + (D.selftests.length - held - failed) + ' not run in this container';
      now.stDot = failed ? '#B0341E' : '#2B4C8C';
    }

    // ------------------------------------------------------------ reader + lists
    let rd = { kicker: '', title: '', tsz: 40, hasSub: false, sub: '', chips: [], secs: [], maxW: 700, key: screen };
    const w = { q: '', onQ: null, filters: [], docs: [], list: [], empty: false, count: '' };
    const wr = { toc: [], tocN: 0, out: [], outN: 0, outNone: true, inn: [], inN: 0, inNone: true, cx: [], hasCx: false, qx: [], hasQx: false, reads: [], sf: [], hasSf: false, evN: 0, evV: 0, evU: 0, evX: 0, ev0: 0, ev1: 0, ev2: 0, graph: null };
    const cl = { list: [], head: '', sub: '' };
    const cr = { hasNp: false, q: [], pos: [], decided: false, status: '', pages: [], pagesN: 0, qs: [], hasQs: false, path: '', first: '', src: '' };
    const nv = { tabs: [], isOverview: false, tiles: [] };
    const ql = { list: [], agenda: { bg: 'transparent', bd: 'transparent', go: null, cur: undefined } };
    const qr = { isQ: false, isAgenda: false, raised: [], raisedN: 0, docs: [], docsN: 0, conf: [], hasConf: false, path: '', decided: [], counts: '', intro: [] };
    const pl = { head: '', sub: '', items: [] };
    const proc = { tabs: [] };
    const loop = { steps: [], phases: [] };
    const chkv = { rows: [] };

    if (is.wiki) {
      const wq = s.wq || '';
      const wf = s.wf || 'all';
      const wd = s.wd == null ? -1 : s.wd;
      const wfq = D.fold(wq.trim());
      const sel = s.page == null ? D.defaultPage : s.page;
      const idx = D.pageOrder.filter((i) => {
        const p = D.pages[i];
        if (wf === 'contested' && !p.cx.length) return false;
        if (wf === 'orphans' && p.in.length) return false;
        if (wf === 'questions' && !p.qx.length) return false;
        if (wd >= 0 && p.ing.indexOf(wd) < 0) return false;
        if (wfq && p.fx.indexOf(wfq) < 0) return false;
        return true;
      });
      w.list = idx.map((i) => {
        const p = D.pages[i];
        const on = i === sel;
        return {
          t: p.t, meta: p.s + ' · ' + p.rd + (p.rd === 1 ? ' reading' : ' readings') + (p.in.length ? '' : ' · orphan'),
          hasC: p.cx.length > 0, cids: p.cx.map((c) => D.conflicts[c].id).join(' '),
          bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', cur: on ? 'true' : undefined,
          go: () => this.setState({ page: i }),
        };
      });
      w.empty = w.list.length === 0;
      w.count = idx.length === D.pages.length ? D.pages.length + ' pages' : idx.length + ' of ' + D.pages.length + ' pages';
      const cnt = (fn) => D.pages.filter(fn).length;
      const fl = (key, label, n) => ({
        label: label, n: n, on: wf === key, go: () => this.setState({ wf: key }),
        bg: wf === key ? '#1C1B18' : '#FBFAF6', fg: wf === key ? '#FBFAF6' : '#1C1B18', bd: wf === key ? '#1C1B18' : '#C9C0AC',
      });
      w.filters = [
        fl('all', 'All', D.pages.length),
        fl('contested', 'Contested', cnt((p) => p.cx.length > 0)),
        fl('orphans', 'Orphans', cnt((p) => p.in.length === 0)),
        fl('questions', 'In a question', cnt((p) => p.qx.length > 0)),
      ];
      w.docs = D.docs.map((d, i) => ({
        sig: d.sig, title: d.sig + ' · ' + d.title + ' · ' + d.date, on: wd === i,
        bg: wd === i ? '#2B4C8C' : d.canon ? '#E4E9F2' : '#FBFAF6', fg: wd === i ? '#FBFAF6' : '#2B4C8C',
        go: () => this.setState({ wd: wd === i ? -1 : i }),
      }));
      w.q = wq;
      w.onQ = (e) => this.setState({ wq: e.target.value });

      const p = D.pages[sel];
      const chips = [this.chip(p.st || 'candidate', 'ink'), this.chip(p.src + ' sources'), this.chip(p.rd + (p.rd === 1 ? ' reading' : ' readings'))];
      if (p.cx.length) chips.push(this.chip('contested · ' + p.cx.map((c) => D.conflicts[c].id).join(', '), 'rubric'));
      if (p.g) chips.push(this.chip('gathered ' + p.g));
      rd = {
        kicker: 'Candidate page · Wiki/candidates/' + p.s + '.md', title: p.t, tsz: p.t.length > 30 ? 34 : 46,
        hasSub: false, sub: '', chips: chips, secs: this.secs(p.lede, p.sec, uid + '-p' + sel), maxW: 700, key: 'wiki:' + sel,
      };
      wr.toc = rd.secs.filter((x) => x.hasHead).map((x) => {
        let label = x.label;
        if (x.hasSig) {
          const rest = label.replace(/^Readings?\s*—\s*/, '').replace(/^\d{4}-\d{2}-\d{2}\s*—?\s*/, '');
          label = (x.dt || 'Reading') + (rest && rest !== label ? ' · ' + rest : '');
        }
        return { href: '#' + x.anchor, label: label, hasSig: x.hasSig, sig: x.sig, sigBg: x.sigBg, sigFg: x.sigFg };
      });
      wr.tocN = wr.toc.length;
      wr.out = p.out.map((i) => this.pageChip(i));
      wr.outN = wr.out.length;
      wr.outNone = wr.outN === 0;
      wr.inn = p.in.map((i) => this.pageChip(i));
      wr.inN = wr.inn.length;
      wr.inNone = wr.inN === 0;
      wr.cx = p.cx.map((ci) => ({ id: D.conflicts[ci].id, t: D.conflicts[ci].title.replace(/^C\d+\s*—\s*/, ''), go: () => this.go('conflicts', { conf: ci }) }));
      wr.hasCx = wr.cx.length > 0;
      wr.qx = p.qx.map((qi) => ({ id: D.questions[qi].id, t: D.questions[qi].q, go: () => this.go('questions', { ques: qi }) }));
      wr.hasQx = wr.qx.length > 0;
      wr.reads = p.ing.map((di) => {
        const d = D.docs[di];
        return { sig: d.sig, t: d.title, s: d.date + ' · ' + d.cat, sigBg: d.canon ? '#2B4C8C' : '#E4E9F2', sigFg: d.canon ? '#FBFAF6' : '#2B4C8C', go: () => this.go('corpus', { crow: D.rowBySlug[d.slug] }) };
      });
      wr.sf = p.sf.map((x) => ({ x: x }));
      wr.hasSf = wr.sf.length > 0;
      const ev = p.ev;
      const evN = ev[0] + ev[1] + ev[2];
      wr.evN = evN;
      wr.ev0 = ev[0];
      wr.ev1 = ev[1];
      wr.ev2 = ev[2];
      wr.evV = evN ? (100 * ev[0]) / evN : 0;
      wr.evU = evN ? (100 * ev[1]) / evN : 0;
      wr.evX = evN ? (100 * ev[2]) / evN : 0;
      wr.graph = () => this.go('graph', { gsel: D.nodeOf.term[sel] });
    }

    if (is.conflicts) {
      const sel = s.conf == null ? 0 : s.conf;
      const decided = D.conflicts.length - openC;
      cl.head = D.conflicts.length + ' records';
      cl.sub = openC + ' open · ' + decided + ' decided · append-only; each is an item for discussion with the author (decision 006)';
      cl.list = D.conflicts.map((c, i) => {
        const on = i === sel;
        return {
          id: c.id, main: c.np ? this.txt(c.np.q) : c.title.replace(/^C\d+\s*—\s*/, ''), sub: c.subj,
          st: c.decided ? 'Decided' : 'Open', stBg: c.decided ? '#1C1B18' : '#F6E4DC', stFg: c.decided ? '#FBFAF6' : '#9A2D1A',
          idc: c.decided ? '#1C1B18' : '#B0341E', bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent',
          cur: on ? 'true' : undefined, go: () => this.setState({ conf: i }),
        };
      });
      const c = D.conflicts[sel];
      rd = {
        kicker: 'Conflict record · append-only · Wiki/conflicts/' + c.f + '.md', title: c.title.replace(/`/g, ''), tsz: c.title.length > 60 ? 28 : 34,
        hasSub: !!c.kind, sub: c.kind,
        chips: [c.decided ? this.chip('Decided', 'ink') : this.chip('Open', 'rubric'), this.chip('first seen ' + c.first), this.chip(c.src + ' sources'), this.chip(c.pages.length + ' pages')],
        secs: this.secs(c.lede, c.sec, uid + '-c' + sel), maxW: 700, key: 'conf:' + sel,
      };
      cr.hasNp = !!c.np;
      cr.q = c.np ? this.runs(c.np.q) : [];
      cr.pos = c.np ? this.runs(c.np.pos) : [];
      cr.decided = c.decided;
      cr.status = c.status;
      cr.pages = c.pages.map((i) => this.pageChip(i));
      cr.pagesN = cr.pages.length;
      cr.qs = D.questions.map((x, i) => ({ x: x, i: i })).filter((o) => o.x.conf.indexOf(sel) >= 0).map((o) => ({ id: o.x.id, t: o.x.q, go: () => this.go('questions', { ques: o.i }) }));
      cr.hasQs = cr.qs.length > 0;
      cr.path = 'Wiki/conflicts/' + c.f + '.md';
      cr.first = c.first;
      cr.src = c.src;
    }

    if (is.manuscript) {
      const N = D.novel;
      const item = (k, t, sub, on, go, kc) => ({ isBtn: true, isGroup: false, isLink: false, k: k, t: t, s: sub || '', hasS: !!sub, kc: kc || '#645F53', bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', go: go });
      const group = (t) => ({ isBtn: false, isGroup: true, isLink: false, t: t });
      const cards = (kind) => N.cards.filter((c) => c.kind === kind).length;
      const plots = D.manuscript.filter((m) => m.part === 'plot');
      const chDrafts = N.chapters.reduce((n, c) => n + c.drafts.length, 0);
      const openW = N.weichen.filter((w) => !this.novelDecided(w));
      const own = N.findings.filter((x) => !x.legacy);
      const counts = { overview: '', chapters: N.chapters.length, cast: cards('figuren'), world: cards('welt'), plot: plots.length, decisions: openW.length + ' open', findings: N.findings.length };
      nv.tabs = this.novelTabs().map((t) => ({
        label: t[1] + (counts[t[0]] !== '' ? ' · ' + counts[t[0]] : ''), on: mtab === t[0], bd: mtab === t[0] ? '#B0341E' : 'transparent',
        fw: mtab === t[0] ? 600 : 400, fg: mtab === t[0] ? '#1C1B18' : '#4A463E', go: () => this.setState({ mtab: t[0], msel: null }),
      }));
      const draftId = (m) => {
        if (m.readme) return '—';
        const b = m.f.split('/').pop();
        const pm = b.match(/^plot-entwurf-0*(\d+)/);
        if (pm) return 'P' + pm[1];
        const em = b.match(/^entwurf-([a-z])-/);
        return em ? em[1].toUpperCase() : '·';
      };
      const isApproved = (m) => N.approved.indexOf(m.f.replace(/^Manuscript\//, '')) >= 0;
      const short = (t) => t.replace(/^Kap \d+ — (Entwurf [A-Z]: )?/, '').replace(/^Plot-Entwurf \d+: /, '').replace(/`/g, '');
      const occOf = (c) => c.occ.reduce((n, o) => n + o[1], 0);
      const nOf = (n, one, many) => n + ' ' + (n === 1 ? one : many);
      if (mtab === 'overview') {
        nv.isOverview = true;
        const tile = (label, big, cap, path, color, go) => ({ label: label, big: String(big), cap: cap, path: path, color: color, go: go });
        nv.tiles = [
          tile('canon', N.kanon.length, 'decisions of yours · ' + N.kanon.map((k) => k.id).join(', '), 'Manuscript/kanon.md', '#1C1B18', () => this.setState({ mtab: 'decisions', msel: 'kanon' })),
          tile('approved', N.approved.length, 'chapters approved, of ' + N.chapters.length + ' begun', 'kanon.md · Freigegebene Kapitel', '#B0341E', () => this.setState({ mtab: 'chapters', msel: null })),
          tile('drafts', chDrafts, 'chapter drafts · working, none canon', 'Manuscript/kap-NN/', '#4A463E', () => this.setState({ mtab: 'chapters', msel: null })),
          tile('plot', plots.length, 'plot drafts · proposals, not a treatment', 'Manuscript/plot/', '#4A463E', () => this.setState({ mtab: 'plot', msel: null })),
          tile('cards', cards('figuren') + cards('welt'), cards('figuren') + ' cast · ' + cards('welt') + ' world', 'Manuscript/figuren/ · welt/', '#4A463E', () => this.setState({ mtab: 'cast', msel: null })),
          tile('weichen', openW.length, 'open decisions · ' + (openW.length ? openW[0].id + ' first' : 'none'), 'Plan/weichen/', '#B0341E', () => this.setState({ mtab: 'decisions', msel: openW.length ? openW[0].id : null })),
          tile('findings', own.length, 'readings of the drafts by the writing skills', 'Plan/runs/writing/', '#2B4C8C', () => this.setState({ mtab: 'findings', msel: null })),
        ];
        const readme = D.manuscript.find((m) => m.f === 'Manuscript/README.md');
        const ledgerTable = ['tb', [['id'], ['date'], ['what holds']], N.kanon.map((k) => [[['b', k.id]], [k.date], k.what]), 'lll', 'minmax(0, 0.35fr) minmax(0, 0.7fr) minmax(0, 3.2fr)'];
        rd = {
          kicker: 'Manuscript/ · the novel’s workspace', title: 'The novel', tsz: 44, hasSub: true,
          sub: 'Only canon and working drafts. Canon is what you decided or approved, listed once in Manuscript/kanon.md; everything else waits on your yes.',
          chips: [this.chip(N.kanon.length + ' canon entries', 'ink'), this.chip(N.approved.length + ' chapters approved', N.approved.length ? 'blue' : 'rubric'), this.chip(openW.length + ' Weichen open', 'rubric')],
          secs: this.secs(null, [[['Canon, as it stands'], -1, '', [ledgerTable, ['p', [N.approved.length ? N.approved.length + ' chapters approved.' : 'No chapter is approved yet.']]]]], uid + '-nvk')
            .concat(readme ? this.secs(readme.lede, readme.sec, uid + '-nvr') : []),
          maxW: 980, key: 'nv:overview',
        };
      } else {
        const entries = this.novelEntries(mtab);
        const firsts = entries.filter((x) => !x.group);
        const selKey = s.msel && firsts.some((x) => x.key === s.msel) ? s.msel : (firsts.length ? firsts[0].key : null);
        const sel = (k) => () => this.setState({ msel: k });
        pl.head = { chapters: nOf(N.chapters.length, 'chapter', 'chapters') + ' begun', cast: cards('figuren') + ' cards — the cast', world: cards('welt') + ' cards — the world', plot: plots.length + ' plot drafts', decisions: N.kanon.length + ' canon · ' + openW.length + ' Weichen open', findings: N.findings.length + ' findings' }[mtab];
        pl.sub = {
          chapters: 'Each chapter folder with its drafts and the findings that read them. A draft is canon only when Manuscript/kanon.md lists it.',
          cast: 'One card per figure: what you decided, what the drafts make of it, what is open. The wiki holds the research.',
          world: 'One card per place, rule or mechanism, built like the cast cards.',
          plot: 'Whole-novel plot drafts. Proposals, never a treatment, until you approve one.',
          decisions: 'The canon ledger, and the decision sheets in Plan/weichen/ — each open until you answer it.',
          findings: 'What the writing skills said about the drafts and the material. Readings, never canon; they live in Plan/runs/writing/.',
        }[mtab];
        pl.items = entries.map((x) => {
          if (x.group) return group(x.group);
          const on = x.key === selKey;
          if (x.kind === 'draft') {
            const m = D.manuscript[x.ref];
            return item(draftId(m), short(m.t), m.readme ? 'the folder’s overview' : this.fmt(m.w) + ' words · ' + (isApproved(m) ? 'canon' : 'working draft'), on, sel(x.key), isApproved(m) ? '#2B4C8C' : '#B0341E');
          }
          if (x.kind === 'finding') {
            const f = N.findings[x.ref];
            return item(f.date.slice(5), f.t.replace(/^[a-z-]+ — /, '').replace(/`/g, ''), f.skill + ' · ' + f.target, on, sel(x.key), f.legacy ? '#9A9384' : '#2B4C8C');
          }
          if (x.kind === 'card') {
            const c = N.cards[x.ref];
            const n = occOf(c);
            return item(c.kanon.length ? c.kanon.join(' ') : '—', c.t, n ? nOf(n, 'mention', 'mentions') + ' in ' + nOf(c.occ.length, 'draft', 'drafts') : 'in no draft yet', on, sel(x.key), c.kanon.length ? '#1C1B18' : '#B0341E');
          }
          if (x.kind === 'ledger') return item('§', 'The canon ledger', N.kanon.length + ' decisions · ' + N.approved.length + ' chapters approved', on, sel(x.key), '#1C1B18');
          const w = N.weichen[x.ref];
          return item(w.id, w.t.replace(/`/g, ''), (w.rec ? 'recommended ' + w.rec + ' · ' : '') + (this.novelDecided(w) ? 'decided' : 'open'), on, sel(x.key), '#B0341E');
        });
        const cur = entries.find((x) => !x.group && x.key === selKey);
        if (cur && cur.kind === 'draft') {
          const m = D.manuscript[cur.ref];
          rd = {
            kicker: 'Manuscript · ' + m.f, title: m.t.replace(/`/g, ''), tsz: m.t.length > 56 ? 30 : 36, hasSub: false, sub: '',
            chips: [m.readme ? this.chip('overview') : isApproved(m) ? this.chip('canon', 'ink') : this.chip('working draft', 'rubric'), this.chip(this.fmt(m.w) + ' words')],
            secs: this.secs(m.lede, m.sec, uid + '-m' + cur.ref), maxW: 700, key: 'ms:' + cur.key,
          };
        } else if (cur && cur.kind === 'finding') {
          const f = N.findings[cur.ref];
          rd = {
            kicker: 'Finding · ' + f.f, title: f.t.replace(/`/g, ''), tsz: f.t.length > 60 ? 28 : 34, hasSub: true,
            sub: f.legacy ? 'A reading of the parked Legacy draft — kept as a measurement, never a voice reference.' : 'A reading of the drafts or the material by a writing skill. It proposes; you decide.',
            chips: [this.chip(f.skill, 'blue'), this.chip(f.target), this.chip(f.date || 'undated'), this.chip('not canon', 'rubric')],
            secs: this.secs(f.lede, f.sec, uid + '-f' + cur.ref), maxW: 760, key: 'mf:' + cur.key,
          };
        } else if (cur && cur.kind === 'card') {
          const c = N.cards[cur.ref];
          const occTable = ['tb', [['draft'], ['mentions']], c.occ.map((o) => [[D.manuscript[o[0]].t.replace(/`/g, '')], [String(o[1])]]), 'lr', 'minmax(0, 3fr) minmax(0, 0.6fr)'];
          const extra = [[['In the drafts'], -1, '', [['p', ['How often ' + c.match.map((x) => '„' + x + '“').join(', ') + ' occurs in each draft — counted, not read.']], c.occ.length ? occTable : ['p', ['In no draft yet.']]]]];
          if (c.wiki >= 0) extra.push([['Research'], -1, '', [['p', ['The wiki collects what the sources say. None of it holds here until you decide it: ', ['l', D.pages[c.wiki].t + ' in the wiki', c.wiki], '.']]]]);
          rd = {
            kicker: (c.kind === 'figuren' ? 'Cast' : 'World') + ' · ' + c.f, title: c.t, tsz: 40, hasSub: false, sub: '',
            chips: (c.kanon.length ? c.kanon.map((k) => this.chip('canon · ' + k, 'ink')) : [this.chip('nothing decided', 'rubric')]).concat([this.chip(c.wiki >= 0 ? 'in the sources' : 'invented in a draft')]),
            secs: this.secs(c.lede, c.sec.concat(extra), uid + '-c' + cur.ref), maxW: 720, key: 'mc:' + cur.key,
          };
        } else if (cur && cur.kind === 'ledger') {
          rd = {
            kicker: 'Canon · ' + N.ledger.f, title: N.ledger.t || 'Kanon', tsz: 40, hasSub: true,
            sub: 'The one place canon is stated. A card, chapter or Weiche counts as canon only by naming an id from it.',
            chips: [this.chip(N.kanon.length + ' decisions', 'ink'), this.chip(N.approved.length + ' chapters approved', N.approved.length ? 'blue' : 'rubric')],
            secs: this.secs(N.ledger.lede, N.ledger.sec, uid + '-k'), maxW: 760, key: 'mk',
          };
        } else if (cur && cur.kind === 'weiche') {
          const w = N.weichen[cur.ref];
          rd = {
            kicker: 'Weiche ' + w.id + ' · ' + w.f, title: w.t.replace(/`/g, ''), tsz: w.t.length > 60 ? 28 : 34, hasSub: false, sub: '',
            chips: [this.novelDecided(w) ? this.chip('decided', 'ink') : this.chip('open', 'rubric'), this.chip(w.rec ? 'recommended ' + w.rec : 'no recommendation'), this.chip(w.kind || '—')],
            secs: this.secs(w.lede, w.sec, uid + '-w' + cur.ref), maxW: 760, key: 'mw:' + cur.key,
          };
        } else {
          rd = { kicker: 'Manuscript', title: 'Nothing here yet', tsz: 36, hasSub: false, sub: '', chips: [], secs: [], maxW: 700, key: 'nv:empty' };
        }
      }
    }

    if (is.questions) {
      const sel = s.ques == null ? 0 : s.ques;
      ql.list = D.questions.map((x, i) => {
        const on = i === sel;
        return { id: x.id, main: x.q, bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', cur: on ? 'true' : undefined, go: () => this.setState({ ques: i }) };
      });
      ql.agenda = { bg: sel === -1 ? '#FBFAF6' : 'transparent', bd: sel === -1 ? '#C9C0AC' : 'transparent', cur: sel === -1 ? 'true' : undefined, go: () => this.setState({ ques: -1 }), n: D.conflicts.filter((c) => c.np).length + D.agenda.unsettled.length + D.agenda.process.length };
      if (sel === -1) {
        // NOW.md once tabled every open conflict's question and positions; its rewrite of 2026-10-05 dropped the
        // table. Without it, the open conflicts are listed from their own records, never left as an empty table.
        const fromNow = D.conflicts.some((c) => c.np);
        const rowsT = fromNow ? D.conflicts.filter((c) => c.np).map((c) => [[['b', c.id]], c.np.q, c.np.pos])
          : D.conflicts.filter((c) => !c.decided).map((c) => [[['b', c.id]], [c.title.replace(/^C\d+\s*—\s*/, '')], [c.subj + (c.kind ? ' · ' + c.kind : '') + ' — Wiki/conflicts/' + c.f + '.md']]);
        const agendaSecs = [];
        if (D.agenda.decided && D.agenda.decided.length) agendaSecs.push([['Decided so far'], -1, '', [['p', D.agenda.decided]]]);
        agendaSecs.push([['The novel — where the sources disagree'], -1, '', [['tb', [[''], [fromNow ? 'question' : 'conflict'], [fromNow ? 'the positions (source, date)' : 'subject · kind — the record']], rowsT, 'lll', 'minmax(0, 0.45fr) minmax(0, 1.5fr) minmax(0, 3fr)']]]);
        if (D.agenda.unsettled.length) agendaSecs.push([['The novel — what no source settles'], -1, '', [['ul', D.agenda.unsettled]]]);
        agendaSecs.push([['Questions for the author'], -1, '', [['ol', D.agenda.process]]]);
        rd = {
          kicker: 'NOW.md · Questions for the author — noted, not waited on', title: 'Everything waiting on the author', tsz: 40,
          hasSub: true, sub: 'Every open question, with where it came from. The work continues without waiting for the answer; when one arrives it is recorded where the question lives.',
          chips: [this.chip(rowsT.length + ' open conflicts', 'rubric'), this.chip(D.agenda.process.length + ' questions in NOW.md')],
          secs: this.secs(null, agendaSecs, uid + '-ag'), maxW: 760, key: 'agenda',
        };
        qr.isAgenda = true;
        qr.decided = this.runs(D.agenda.decided);
        qr.intro = this.runs(D.agenda.intro);
        qr.counts = rowsT.length + ' conflicts, ' + D.agenda.process.length + ' questions in NOW.md';
      } else {
        const x = D.questions[sel];
        rd = {
          kicker: 'Question · Wiki/questions/' + x.f + '.md', title: x.title.replace(/`/g, ''), tsz: x.title.length > 56 ? 30 : 36,
          hasSub: !!x.q, sub: x.q,
          chips: [this.chip(x.status || 'open', x.status === 'open' ? 'rubric' : 'plain'), this.chip('gathered ' + x.first), this.chip(x.raised.length + ' pages raise it')],
          secs: this.secs(x.lede, x.sec, uid + '-q' + sel), maxW: 700, key: 'ques:' + sel,
        };
        qr.isQ = true;
        qr.raised = x.raised.map((i) => this.pageChip(i));
        qr.raisedN = qr.raised.length;
        qr.docs = x.docs.map((di) => {
          const d = D.docs[di];
          return { sig: d.sig, t: d.title, s: d.date, sigBg: d.canon ? '#2B4C8C' : '#E4E9F2', sigFg: d.canon ? '#FBFAF6' : '#2B4C8C', go: () => this.go('corpus', { crow: D.rowBySlug[d.slug] }) };
        });
        qr.docsN = qr.docs.length;
        qr.conf = x.conf.map((ci) => ({ id: D.conflicts[ci].id, t: D.conflicts[ci].title.replace(/^C\d+\s*—\s*/, ''), go: () => this.go('conflicts', { conf: ci }) }));
        qr.hasConf = qr.conf.length > 0;
        qr.path = 'Wiki/questions/' + x.f + '.md';
      }
    }

    if (is.process) {
      const tabs = [['loop', 'The loop'], ['checks', 'Invariants'], ['compare', 'Reconciliations · ' + D.compare.length], ['decisions', 'Decisions · ' + D.decisions.length], ['principles', 'Principles · ' + D.principles.length], ['now', 'NOW.md'], ['goal', 'GOAL.md']];
      proc.tabs = tabs.map((t) => ({ label: t[1], on: ptab === t[0], bd: ptab === t[0] ? '#B0341E' : 'transparent', fw: ptab === t[0] ? 600 : 400, fg: ptab === t[0] ? '#1C1B18' : '#4A463E', go: () => this.setState({ ptab: t[0] }) }));
      const item = (k, t, sub, on, go, kc) => ({ isBtn: true, isGroup: false, isLink: false, k: k, t: t, s: sub || '', hasS: !!sub, kc: kc || '#645F53', bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', go: go });
      const group = (t) => ({ isBtn: false, isGroup: true, isLink: false, t: t });
      const link = (k, t, href) => ({ isBtn: false, isGroup: false, isLink: true, k: k, t: t, href: href });
      if (ptab === 'loop') {
        rd = {
          kicker: '.claude/skills/tools · the loop', title: 'A cycle that names its own next step', tsz: 38, hasSub: true,
          sub: 'The wiki is not built by walking a list of documents: a reconciliation raises a question, the question chooses a document, and the reconciliation of that document raises the next one.',
          chips: [this.chip('pipeline order ' + (V('order.holds') ? 'holds' : 'broken'), V('order.holds') ? 'blue' : 'rubric'), this.chip(V('documents.reconciled') + ' documents through the loop')],
          secs: this.secs(null, [[['The commands, as combinations'], -1, '', [D.commands]], [['What is missing, stated plainly'], -1, '', D.missing]], uid + '-loop'), maxW: 1060, key: 'loop',
        };
        loop.steps = [
          { verb: 'fetch', path: 'Sources/drive/', big: fmt(V('sources.landed')), cap: 'of ' + fmt(V('sources.total')) + ' manifest rows landed as Markdown', how: 'sources.py next · land — the one automated step' },
          { verb: 'extract', path: 'Sources/terms/', big: String(V('documents.with_census')), cap: 'censuses — every candidate term in one document', how: 'capture.py · read.py — the candidate list is written while reading' },
          { verb: 'read', path: 'Sources/notes/', big: String(V('documents.with_note')), cap: 'notes — what a document says, quoted with line numbers', how: 'read.py --find answers a quotation with its line' },
          { verb: 'reconcile', path: 'Wiki/compare/', big: String(V('documents.reconciled')), cap: 'reconciled against the pages · ' + V('judgements.total') + ' judgements', how: 'wiki_index.py · reconcile.py — lookup first, judgement for the rest' },
          { verb: 'gather', path: 'Wiki/candidates/', big: String(V('wiki.pages')), cap: 'pages · ' + V('wiki.conflicts') + ' conflicts · ' + V('wiki.questions') + ' questions', how: 'readings attributed and unmerged; one commit per page' },
          { verb: 'review', path: 'Wiki/terms/', big: '0', cap: 'promoted — the folder does not exist yet', how: 'a person decides; no rule yet for a reviewed page a source contradicts' },
          { verb: 'ask', path: 'graphrag.py', big: V('graphrag.recall_ppr') + '%', cap: 'recall@8 on ' + V('graphrag.cases') + ' cases · ' + V('graphrag.recall_seeds') + '% from seeds', how: 'returns verified quotations, never prose' },
        ].map((x, i) => ({ n: i + 1, verb: x.verb, path: x.path, big: x.big, cap: x.cap, how: x.how, arrow: i > 0, bl: i > 0 ? '#DDD6C6' : 'transparent', color: x.verb === 'review' ? '#B0341E' : x.verb === 'fetch' || x.verb === 'ask' ? '#2B4C8C' : '#1C1B18', vc: x.verb === 'review' ? '#B0341E' : '#645F53' }));
        loop.phases = D.phases.map((p) => ({ n: p.n, t: p.t, d: p.d, cmd: p.cmd }));
      } else if (ptab === 'checks') {
        const selftestTable = ['tb', [['status'], ['suite'], ['what it reported']], D.selftests.map((x) => [[x[0] === 'held' ? ['b', 'held'] : x[0]], [['c', x[1]]], [x[2]]]), 'lll', 'minmax(0, 0.5fr) minmax(0, 1fr) minmax(0, 2.6fr)'];
        rd = {
          kicker: '.claude/skills/tools · 0 · Invariants — run now against this snapshot', title: 'The checks, and what a red one means', tsz: 38, hasSub: true,
          sub: 'A green check is worth what its coverage is worth, so each says what it could not check. None of them uses a model.',
          chips: [this.chip(D.checks.filter((c) => c[1] === 'held').length + ' green', 'blue'), this.chip(D.checks.filter((c) => c[1] === 'red').length + ' red', 'rubric'), this.chip(D.checks.filter((c) => c[1] === 'not run').length + ' not run here')],
          secs: this.secs(null, [[['Self-tests — scripts/selftests.py'], -1, '', [['p', ['Each case carries the exact defect its checker must name, so a case that fails for the wrong reason fails the test. A suite that did not run has not passed.']], selftestTable]]], uid + '-chk'),
          maxW: 1060, key: 'checks',
        };
        chkv.rows = D.checks.map((c, i) => {
          const st = c[1];
          const key = c[0];
          return {
            st: st === 'held' ? 'green' : st === 'red' ? 'red' : 'not run', cmd: 'python3 ' + key, line: c[2],
            bg: st === 'held' ? '#E4E9F2' : st === 'red' ? '#F6E4DC' : '#EFEBE1', fg: st === 'held' ? '#2B4C8C' : st === 'red' ? '#9A2D1A' : '#4A463E',
            red: this.runs(D.redMeans[key] || ['—'], true), bt: i === 0 ? 'transparent' : '#E6E0D2',
          };
        });
      } else if (ptab === 'compare') {
        const sel = s.pcmp == null ? D.compare.length - 1 : s.pcmp;
        pl.head = D.compare.length + ' reconciliation records';
        pl.sub = 'Wiki/compare/ — how each document met the wiki, one record per reconciliation, kept as written.';
        pl.items = D.compare.map((c, i) => item(c.k, c.title.replace(/`/g, ''), c.d >= 0 ? D.docs[c.d].sig + ' · ' + D.docs[c.d].title : 'a comparison of censuses', i === sel, () => this.setState({ pcmp: i }), '#2B4C8C'));
        const c = D.compare[sel];
        const doc = c.d >= 0 ? D.docs[c.d] : null;
        rd = {
          kicker: 'Reconciliation record · Wiki/compare/' + c.f + '.md', title: c.title.replace(/`/g, ''), tsz: c.title.length > 60 ? 28 : 34,
          hasSub: !!doc, sub: doc ? doc.sig + ' · ' + doc.title + ' · ' + doc.date : '',
          chips: doc ? [this.chip('+' + doc.terms + ' pages'), this.chip('+' + doc.readings + ' readings'), this.chip('+' + doc.conflicts + ' conflicts', doc.conflicts ? 'rubric' : 'plain')] : [],
          secs: this.secs(c.lede, c.sec, uid + '-r' + sel), maxW: 740, key: 'cmp:' + sel,
        };
      } else if (ptab === 'decisions') {
        const sel = s.pdec == null ? D.decisions.length - 1 : s.pdec;
        pl.head = D.decisions.length + ' decisions';
        pl.sub = 'One short file per decision, kept permanently: what was chosen, what was rejected, what would change our mind.';
        pl.items = D.decisions.map((d, i) => item(d.id, d.title.replace(/`/g, ''), d.date + ' · ' + d.status, i === sel, () => this.setState({ pdec: i }), '#B0341E'));
        const d = D.decisions[sel];
        rd = {
          kicker: 'Decision ' + d.id + ' · Plan/decisions/' + d.f + '.md', title: d.title.replace(/`/g, ''), tsz: d.title.length > 60 ? 30 : 36, hasSub: true, sub: 'Decided by ' + d.by,
          chips: [this.chip(d.date), this.chip(d.status, /done|applied/.test(d.status) ? 'blue' : 'plain')],
          secs: this.secs(d.lede, d.sec, uid + '-d' + sel), maxW: 720, key: 'dec:' + sel,
        };
      } else if (ptab === 'principles') {
        const sel = s.pprin == null ? 0 : s.pprin;
        pl.head = D.principles.length + ' principles';
        pl.sub = 'Each produced by something that went wrong or worked here, with its evidence. Read before building anything.';
        const items = [];
        let last = '';
        D.principles.forEach((p, i) => {
          if (p.grp !== last) { items.push(group(p.grp)); last = p.grp; }
          items.push(item(p.id, p.t, '', i === sel, () => this.setState({ pprin: i }), '#B0341E'));
        });
        items.push(group('Kept, not yet built'));
        items.push(item('—', 'The catalogue', 'good ideas, each with where it belongs', sel === -1, () => this.setState({ pprin: -1 }), '#645F53'));
        pl.items = items;
        if (sel === -1) {
          rd = { kicker: 'PRINCIPLES.md · the catalogue', title: 'Good ideas kept, not yet built', tsz: 36, hasSub: true, sub: 'None is built. Each is listed with where it belongs, so that picking one up is a small job rather than a re-derivation.', chips: [], secs: this.secs(D.catalogue, [], uid + '-cat'), maxW: 820, key: 'cat' };
        } else {
          const p = D.principles[sel];
          rd = { kicker: 'PRINCIPLES.md · ' + p.grp, title: p.id + ' — ' + p.t, tsz: p.t.length > 44 ? 30 : 36, hasSub: false, sub: '', chips: [], secs: this.secs(p.b, [], uid + '-pr' + sel), maxW: 700, key: 'prin:' + sel };
        }
      } else if (ptab === 'now' || ptab === 'goal') {
        const src = ptab === 'now' ? D.now : D.goal;
        const prefix = uid + '-' + ptab;
        const secs = this.secs(src.lede, src.sec, prefix);
        pl.head = ptab === 'now' ? 'NOW.md' : 'GOAL.md';
        pl.sub = ptab === 'now' ? 'What is open right now — the handover between sessions. Things leave it when they are done.' : 'The project’s general goal: the author’s brief of 2026-09-23, in German. It describes the target, not the repository.';
        pl.items = secs.filter((x) => x.hasHead).map((x, i) => link(String(i + 1), x.label, '#' + x.anchor));
        rd = {
          kicker: ptab === 'now' ? 'NOW.md · the handover between sessions' : 'GOAL.md · Auftrag an Claude Code', title: ptab === 'now' ? 'Now' : (src.title || 'GOAL.md'),
          tsz: ptab === 'now' ? 46 : 30, hasSub: true,
          sub: ptab === 'now' ? 'What is open, what is half-done, and what failed. No counts live on this page; the few in its prose are checked.' : 'German, as written. Where it names paths or tools that do not exist here, the working agreement says what exists.',
          chips: [this.chip(secs.filter((x) => x.hasHead).length + ' sections')], secs: secs, maxW: 760, key: ptab,
        };
      }
    }

    // ------------------------------------------------------------ graph
    const g = { types: [], nodes: [], edges: [], labelsOn: false, labelsLabel: '', toggleLabels: null, hasSel: false, noSel: true, rail: { kind: '', title: '', sub: '', open: null, openLabel: '', clear: null, groups: [] }, top: [], w: D.graph.w, h: D.graph.h };
    if (is.graph) {
      const G = D.graph;
      const on = s.gtypes || { 0: true, 3: true, 4: true, 6: true };
      const sel = s.gsel == null ? -1 : s.gsel;
      const hov = s.ghov == null ? -1 : s.ghov;
      const allLabels = !!s.glabels;
      const names = { links: 'links', reads: 'reads', cites: 'cites', contests: 'contests', raised_by: 'raised by', asks: 'asks', concerns: 'concerns' };
      const colors = ['#1C1B18', '#2B4C8C', '#2B4C8C', '#B0341E', '#B0341E', '#B0341E', '#B0341E'];
      const dashes = ['none', 'none', '2 3', 'none', '5 3', '1.5 3', '6 2 2 2'];
      const baseOp = [0.2, 0.16, 0.12, 0.5, 0.42, 0.32, 0.6];
      g.types = G.types.map((t, i) => ({
        label: names[t] || t, n: D.typeCount[i], color: colors[i], dash: dashes[i], on: !!on[i],
        bg: on[i] ? '#FBFAF6' : 'transparent', bd: on[i] ? '#9A9384' : '#DDD6C6', op: on[i] ? 1 : 0.55,
        go: () => { const nx = {}; Object.keys(on).forEach((k) => { nx[k] = on[k]; }); nx[i] = !on[i]; this.setState({ gtypes: nx }); },
      }));
      g.labelsOn = allLabels;
      g.labelsLabel = allLabels ? 'Showing all' : 'Showing key pages';
      g.toggleLabels = () => this.setState({ glabels: !allLabels });
      const nb = {};
      if (sel >= 0) D.adj[sel].forEach((ei) => { const e = G.edges[ei]; if (on[e[2]]) { nb[e[0]] = true; nb[e[1]] = true; } });
      const plain = [];
      const lit = [];
      G.edges.forEach((e) => {
        if (!on[e[2]]) return;
        const a = G.nodes[e[0]];
        const b = G.nodes[e[1]];
        const touch = sel >= 0 && (e[0] === sel || e[1] === sel);
        const v = { x1: a.x, y1: a.y, x2: b.x, y2: b.y, c: colors[e[2]], d: dashes[e[2]], w: touch ? 1.6 : 1, o: sel >= 0 ? (touch ? 0.9 : 0.05) : baseOp[e[2]] };
        if (touch) lit.push(v); else plain.push(v);
      });
      g.edges = plain.concat(lit);
      g.nodes = G.nodes.map((n, i) => {
        const isSel = i === sel;
        const isNb = !!nb[i];
        const isHov = i === hov;
        let sz = 10;
        let rad = '50%';
        let bg = '#1C1B18';
        let bc = '#FBFAF6';
        let bw = 1;
        let rot = 0;
        let inner = '';
        let tc = '#FBFAF6';
        let label = n.label;
        let aria = '';
        if (n.k === 'term') {
          sz = Math.round(7 + 2.4 * Math.sqrt(n.deg));
          aria = 'Page ' + n.label + ', ' + n.deg + ' links';
          if (isSel) { bg = '#B0341E'; }
        } else if (n.k === 'doc') {
          const d = D.docs[n.ref];
          const canon = !!d.canon;
          sz = 30; rad = '6px'; bg = canon ? '#2B4C8C' : '#E4E9F2'; bc = '#2B4C8C'; inner = d.sig; tc = canon ? '#FBFAF6' : '#2B4C8C';
          label = d.title; aria = 'Document ' + d.sig + ', ' + d.title;
          if (isSel) { bc = '#B0341E'; bw = 2; }
        } else if (n.k === 'conflict') {
          const c = D.conflicts[n.ref];
          sz = 15; rad = '2px'; rot = 45; bg = c.decided ? '#1C1B18' : '#B0341E';
          aria = 'Conflict ' + c.id + ', ' + c.subj;
          if (isSel) { bc = '#1C1B18'; bw = 2; }
        } else {
          sz = 16; bg = '#FBFAF6'; bc = '#B0341E'; bw = 2.5;
          aria = 'Question ' + n.label;
          if (isSel) { bg = '#F6E4DC'; }
        }
        const hit = Math.max(sz + 10, 24);
        const labelled = n.k === 'doc' ? isHov || isSel : isSel || isHov || allLabels || n.k !== 'term' || (sel >= 0 ? isNb : n.deg >= 12);
        const right = n.x > G.w - 170;
        return {
          x: n.x, y: n.y, off: -hit / 2, hit: hit, sz: sz, rad: rad, bg: bg, bc: bc, bw: bw, rot: rot, unrot: -rot, inner: inner, tc: tc,
          op: sel >= 0 && !isSel && !isNb ? 0.25 : 1, z: isSel || isHov ? 4 : isNb ? 3 : n.k === 'doc' ? 2 : 1,
          showR: labelled && !right, showL: labelled && right, label: label,
          lfs: isSel || isHov ? 13 : n.k === 'term' ? 11.5 : 10.5, lfw: isSel ? 600 : 400,
          aria: aria, on: isSel,
          go: () => this.setState({ gsel: isSel ? -1 : i }),
          enter: () => this.setState({ ghov: i }), leave: () => this.setState({ ghov: -1 }),
        };
      });
      g.hasSel = sel >= 0;
      g.noSel = sel < 0;
      if (sel >= 0) {
        const n = G.nodes[sel];
        const buckets = {};
        const order = [];
        D.adj[sel].forEach((ei) => {
          const e = G.edges[ei];
          const t = G.types[e[2]];
          if (t === 'cites') return;
          const out = e[0] === sel;
          const other = out ? e[1] : e[0];
          const on2 = G.nodes[other];
          let label = '';
          if (t === 'links') label = out ? 'Links to' : 'Linked from';
          else if (t === 'reads') label = out ? 'Reads' : 'Read by pages';
          else if (t === 'contests') label = out ? 'Contests pages' : 'Contested in';
          else if (t === 'raised_by') label = out ? 'Raised by pages' : 'Raised in';
          else if (t === 'asks') label = out ? 'Asks documents' : 'Asked by questions';
          else if (t === 'concerns') label = out ? 'Concerns' : 'Concerned in';
          if (!buckets[label]) { buckets[label] = { seen: {}, items: [] }; order.push(label); }
          if (buckets[label].seen[other]) return;
          buckets[label].seen[other] = true;
          const nm = on2.k === 'doc' ? D.docs[on2.ref].sig + ' ' + D.docs[on2.ref].title : on2.k === 'term' ? on2.label : on2.label;
          buckets[label].items.push({ t: nm, bc: on2.k === 'doc' ? '#2B4C8C' : on2.k === 'term' ? '#C9C0AC' : '#B0341E', go: () => this.setState({ gsel: other }) });
        });
        const rail = { kind: '', title: '', sub: '', open: null, openLabel: '', clear: () => this.setState({ gsel: -1 }), groups: [] };
        if (n.k === 'term') {
          const p = D.pages[n.ref];
          rail.kind = 'Page · ' + p.s; rail.title = p.t; rail.sub = p.rd + ' readings · ' + p.out.length + ' links out · ' + p.in.length + ' in';
          rail.open = () => this.go('wiki', { page: n.ref }); rail.openLabel = 'Open the page';
        } else if (n.k === 'doc') {
          const d = D.docs[n.ref];
          rail.kind = 'Document ' + d.sig + ' · ' + d.date; rail.title = d.title; rail.sub = d.cat + ' · ' + d.pages.length + ' pages read it · +' + d.terms + ' pages, +' + d.readings + ' readings, +' + d.conflicts + ' conflicts when read';
          rail.open = () => this.go('corpus', { crow: D.rowBySlug[d.slug] }); rail.openLabel = 'Open in the corpus';
        } else if (n.k === 'conflict') {
          const c = D.conflicts[n.ref];
          rail.kind = 'Conflict · ' + (c.decided ? 'decided' : 'open'); rail.title = c.title; rail.sub = c.kind;
          rail.open = () => this.go('conflicts', { conf: n.ref }); rail.openLabel = 'Open the record';
        } else {
          const x = D.questions[n.ref];
          rail.kind = 'Question · ' + x.status; rail.title = x.title; rail.sub = x.q;
          rail.open = () => this.go('questions', { ques: n.ref }); rail.openLabel = 'Open the question';
        }
        rail.groups = order.map((l) => ({ label: l, n: buckets[l].items.length, items: buckets[l].items }));
        g.rail = rail;
      } else {
        g.top = D.graph.nodes.map((n, i) => ({ n: n, i: i })).filter((o) => o.n.k === 'term').sort((a, b) => b.n.deg - a.n.deg).slice(0, 12).map((o) => ({ t: o.n.label, d: o.n.deg + ' links', go: () => this.setState({ gsel: o.i }) }));
      }
    }

    // ------------------------------------------------------------ corpus
    const railDefault = { has: false, none: false, title: '', slug: '', chips: [], sec: '', status: '', statusFg: '#645F53', isRead: false, sig: '', sigBg: '', sigFg: '', stats: [], note: [], hasNote: false, hasRec: false, openRec: null, pages: [], pagesN: 0, graph: null, close: null, facts: [], fmts: [], tiers: [] };
    const cp = { cats: [], months: [], rows: [], more: false, n: 0, showAll: null, filters: [], q: '', onQ: null, hasCat: false, catName: '', clearCat: null, rail: railDefault, count: '' };
    if (is.corpus) {
      const cf = s.cfilter || 'all';
      const cc = s.ccat == null ? -1 : s.ccat;
      const cq = D.fold((s.cq || '').trim());
      const sel = s.crow == null ? -1 : s.crow;
      const pass = (r) => {
        if (cf === 'landed' && !r.landed) return false;
        if (cf === 'fetch' && r.landed) return false;
        if (cf === 'read' && r.read < 0) return false;
        if (cf === 'canon' && !(r.date >= '2026-05-01')) return false;
        if (cc >= 0 && r.catIdx !== cc) return false;
        if (cq && r.fx.indexOf(cq) < 0) return false;
        return true;
      };
      const list = D.rowsByDate.filter(pass);
      const limit = s.call ? list.length : 120;
      cp.n = list.length;
      cp.more = list.length > limit;
      cp.showAll = () => this.setState({ call: true });
      cp.count = list.length === D.rows.length ? D.rows.length + ' rows' : list.length + ' of ' + D.rows.length + ' rows';
      cp.rows = list.slice(0, limit).map((r) => {
        const on = r.i === sel;
        const readDoc = r.read >= 0 ? D.docs[r.read] : null;
        return {
          t: r.title, slug: r.slug, cat: r.cat, date: r.date, fmt: r.fmt,
          st: readDoc ? readDoc.sig : r.landed ? 'landed' : 'on Drive',
          sBg: readDoc ? (readDoc.canon ? '#2B4C8C' : '#E4E9F2') : 'transparent', sFg: readDoc ? (readDoc.canon ? '#FBFAF6' : '#2B4C8C') : r.landed ? '#2B4C8C' : '#645F53',
          sBd: readDoc ? '#2B4C8C' : 'transparent',
          bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', cur: on ? 'true' : undefined,
          go: () => this.setState({ crow: r.i }),
        };
      });
      const cnt = (fn) => D.rows.filter(fn).length;
      const fl = (key, label, n) => ({
        label: label, n: n, on: cf === key, go: () => this.setState({ cfilter: key, call: false }),
        bg: cf === key ? '#1C1B18' : '#FBFAF6', fg: cf === key ? '#FBFAF6' : '#1C1B18', bd: cf === key ? '#1C1B18' : '#C9C0AC',
      });
      cp.filters = [
        fl('all', 'All', D.rows.length), fl('landed', 'Landed', cnt((r) => r.landed)), fl('fetch', 'On Drive only', cnt((r) => !r.landed)),
        fl('read', 'Read', cnt((r) => r.read >= 0)), fl('canon', 'Canon era', cnt((r) => r.date >= '2026-05-01')),
      ];
      cp.q = s.cq || '';
      cp.onQ = (e) => this.setState({ cq: e.target.value, call: false });
      cp.hasCat = cc >= 0;
      cp.catName = cc >= 0 ? D.corpus.cats[cc] : '';
      cp.clearCat = () => this.setState({ ccat: -1 });
      const maxT = Math.max(1, D.catOrder[0] ? D.catOrder[0].total : 1);
      cp.cats = D.catOrder.map((c) => ({
        name: c.name, desc: c.desc, lw: (100 * c.landed) / maxT, uw: (100 * (c.total - c.landed)) / maxT,
        n: c.landed + ' / ' + c.total, read: c.read ? c.read + ' read' : '', on: cc === c.i,
        bg: cc === c.i ? '#EFEADF' : 'transparent', bd: cc === c.i ? '#C9C0AC' : 'transparent',
        go: () => this.setState({ ccat: cc === c.i ? -1 : c.i, call: false }),
      }));
      const maxM = Math.max.apply(null, D.months.map((m) => m.total).concat([1]));
      const mn = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      cp.months = D.months.map((m) => ({
        lh: Math.round((130 * m.landed) / maxM), uh: Math.round((130 * (m.total - m.landed)) / maxM),
        label: m.m === 1 || m.m === 4 || m.m === 7 || m.m === 10 ? mn[m.m - 1] : '', year: m.m === 1 || m.key === D.months[0].key ? String(m.y) : '',
        band: m.key >= '2026-05' ? '#F6E4DC' : 'transparent', n: m.total ? String(m.total) : '',
        title: m.key + ': ' + m.total + ' rows, ' + m.landed + ' landed, ' + m.read + ' read', hasRead: m.read > 0, read: m.read,
      }));
      if (sel >= 0) {
        const r = D.rows[sel];
        const doc = r.read >= 0 ? D.docs[r.read] : null;
        cp.rail = {
          has: true, none: false, facts: [], fmts: [], tiers: [], title: r.title, slug: r.slug, chips: [this.chip(r.cat, 'plain'), this.chip(r.tier), this.chip(r.fmt), this.chip(r.date)],
          sec: r.sec, status: doc ? 'Read — ' + doc.sig + ' in the reading order' : r.landed ? 'Landed in Sources/drive/, not read yet' : 'On Drive only — not fetched',
          statusFg: doc ? '#2B4C8C' : r.landed ? '#1C1B18' : '#645F53', isRead: !!doc,
          sig: doc ? doc.sig : '', sigBg: doc && doc.canon ? '#2B4C8C' : '#E4E9F2', sigFg: doc && doc.canon ? '#FBFAF6' : '#2B4C8C',
          stats: doc ? [{ k: 'new pages', v: doc.terms }, { k: 'new readings', v: doc.readings }, { k: 'new conflicts', v: doc.conflicts }] : [],
          note: doc ? doc.note.map((n) => ({ runs: this.runs(n) })) : [], hasNote: !!(doc && doc.note && doc.note.length),
          hasRec: !!(doc && doc.rec >= 0), openRec: doc && doc.rec >= 0 ? () => this.go('process', { ptab: 'compare', pcmp: doc.rec }) : null,
          pages: doc ? doc.pages.map((i) => this.pageChip(i)) : [], pagesN: doc ? doc.pages.length : 0,
          graph: doc ? () => this.go('graph', { gsel: D.nodeOf.doc[r.read] }) : null,
          close: () => this.setState({ crow: -1 }),
        };
      } else {
        const fmts = {};
        const tiers = {};
        D.rows.forEach((r) => { fmts[r.fmt] = (fmts[r.fmt] || 0) + 1; tiers[r.tier] = (tiers[r.tier] || 0) + 1; });
        cp.rail = {
          has: false, none: true, chips: [], stats: [], note: [], hasNote: false, hasRec: false, openRec: null, pages: [], pagesN: 0, isRead: false,
          facts: [
            { k: 'manifest rows', v: fmt(D.rows.length) }, { k: 'landed as Markdown', v: fmt(V('sources.landed')) },
            { k: 'distinct documents', v: fmt(V('sources.distinct')) }, { k: 'near-copies left', v: fmt(V('sources.near_copies')) },
            { k: 'copies folded away', v: fmt(D.corpus.folded) }, { k: 'canon era, from 2026-05', v: V('sources.canon_era_landed') + ' / ' + V('sources.canon_era') },
          ],
          fmts: Object.keys(fmts).sort((a, b) => fmts[b] - fmts[a]).map((k) => ({ k: k, v: fmts[k] })),
          tiers: Object.keys(tiers).sort().map((k) => ({ k: k, v: tiers[k] })),
        };
      }
    }

    this._rdKey = screen + ':' + rd.key;
    if (!this._refCb) this._refCb = (el) => { this._reader = el; };

    return {
      is: is, nav: nav, railChecks: railChecks, goChecks: goChecks, meta: D.meta, top: top,
      ids: { search: uid + '-search', wq: uid + '-wq', cq: uid + '-cq' },
      q: q, onQ: onQ, onQKey: onQKey, sr: sr,
      now: now, rd: rd, readerRef: this._refCb,
      w: w, wr: wr, cl: cl, cr: cr, nv: nv, ql: ql, qr: qr, pl: pl, proc: proc, loop: loop, chk: chkv,
      g: g, cp: cp,
    };
  }

  componentDidUpdate() {
    if (this.routable()) {
      const h = this.route();
      const cur = window.location.hash;
      // A section anchor (`#lede`, not `#/…`) stays until the state itself moves on.
      if (h !== cur && (cur.indexOf('#/') === 0 || this._lastRoute !== h)) {
        if (this._fromUrl) window.history.replaceState(null, '', h);
        else window.history.pushState(null, '', h);
      }
      this._lastRoute = h;
      this._fromUrl = false;
    }
    // A session opened by its address or its card is brought into view inside the panel.
    const sess = this.st().sess;
    if (sess && sess !== this._sessShown && typeof document !== 'undefined') {
      const el = document.getElementById('kp-' + (this.props.screen || 'main') + '-sess-' + sess);
      if (el && el.scrollIntoView) el.scrollIntoView({ block: 'nearest' });
    }
    this._sessShown = sess;
    if (this._reader && this._rdKey !== this._rdShown) {
      this._reader.scrollTop = 0;
      // Narrow screens scroll the page, not the reader pane (the media query in ui.html): a new
      // screen starts at the top, a new item on the same screen brings its text into view.
      if (this._rdShown && window.matchMedia && window.matchMedia('(max-width: 860px)').matches) {
        const same = this._rdShown.split(':')[0] === this._rdKey.split(':')[0];
        if (same) this._reader.scrollIntoView({ block: 'start' });
        else window.scrollTo(0, 0);
      }
      this._rdShown = this._rdKey;
    }
  }
}
