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

  fmt(n) { return typeof n === 'number' ? n.toLocaleString('en-US') : String(n); }

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

  pageChip(i) {
    const p = this.kp().pages[i];
    return { t: p.t, go: () => this.go('wiki', { page: i }) };
  }

  renderVals() {
    const D = this.kp();
    const s = this.st();
    const V = D.val;
    const fmt = (n) => this.fmt(n);
    const SCREENS = ['now', 'wiki', 'conflicts', 'questions', 'graph', 'corpus', 'process'];
    let screen = s.screen || this.props.screen || 'now';
    if (SCREENS.indexOf(screen) < 0) screen = 'now';
    const uid = 'kp-' + (this.props.screen || 'main');
    const ptab = s.ptab || 'loop';
    const is = {
      now: screen === 'now', wiki: screen === 'wiki', conflicts: screen === 'conflicts', questions: screen === 'questions',
      graph: screen === 'graph', corpus: screen === 'corpus', process: screen === 'process',
    };
    is.procList = is.process && (ptab === 'compare' || ptab === 'decisions' || ptab === 'principles' || ptab === 'now' || ptab === 'goal');
    is.readerLayout = is.wiki || is.conflicts || is.questions || is.process;
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
    const now = { tiles: [], agenda: [], unsettled: [], log: [], handover: [], l1: '', l2: '', l3: '', logSub: '', selftests: '', stDot: '#2B4C8C' };
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
      now.unsettled = D.agenda.unsettled.map((u) => ({ runs: this.runs(u) }));
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
      now.handover = D.agenda.handover.map((h) => ({ runs: this.runs(h) }));
      now.selftests = held + ' held · ' + failed + ' failed · ' + (D.selftests.length - held - failed) + ' not run in this container';
      now.stDot = failed ? '#B0341E' : '#2B4C8C';
    }

    // ------------------------------------------------------------ reader + lists
    let rd = { kicker: '', title: '', tsz: 40, hasSub: false, sub: '', chips: [], secs: [], maxW: 700, key: screen };
    const w = { q: '', onQ: null, filters: [], docs: [], list: [], empty: false, count: '' };
    const wr = { toc: [], tocN: 0, out: [], outN: 0, outNone: true, inn: [], inN: 0, inNone: true, cx: [], hasCx: false, qx: [], hasQx: false, reads: [], sf: [], hasSf: false, evN: 0, evV: 0, evU: 0, evX: 0, ev0: 0, ev1: 0, ev2: 0, graph: null };
    const cl = { list: [], head: '', sub: '' };
    const cr = { hasNp: false, q: [], pos: [], decided: false, status: '', pages: [], pagesN: 0, qs: [], hasQs: false, path: '', first: '', src: '' };
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

    if (is.questions) {
      const sel = s.ques == null ? 0 : s.ques;
      ql.list = D.questions.map((x, i) => {
        const on = i === sel;
        return { id: x.id, main: x.q, bg: on ? '#FBFAF6' : 'transparent', bd: on ? '#C9C0AC' : 'transparent', cur: on ? 'true' : undefined, go: () => this.setState({ ques: i }) };
      });
      ql.agenda = { bg: sel === -1 ? '#FBFAF6' : 'transparent', bd: sel === -1 ? '#C9C0AC' : 'transparent', cur: sel === -1 ? 'true' : undefined, go: () => this.setState({ ques: -1 }), n: D.conflicts.filter((c) => c.np).length + D.agenda.unsettled.length + D.agenda.process.length };
      if (sel === -1) {
        const rowsT = D.conflicts.filter((c) => c.np).map((c) => [[['b', c.id]], c.np.q, c.np.pos]);
        const agendaSecs = [];
        if (D.agenda.decided && D.agenda.decided.length) agendaSecs.push([['Decided so far'], -1, '', [['p', D.agenda.decided]]]);
        agendaSecs.push([['The novel — where the sources disagree'], -1, '', [['tb', [[''], ['question'], ['the positions (source, date)']], rowsT, 'lll', 'minmax(0, 0.45fr) minmax(0, 1.5fr) minmax(0, 3fr)']]]);
        agendaSecs.push([['The novel — what no source settles'], -1, '', [['ul', D.agenda.unsettled]]]);
        agendaSecs.push([['The process — the author’s call'], -1, '', [['ul', D.agenda.process]]]);
        rd = {
          kicker: 'NOW.md · Questions for the author — noted, not waited on', title: 'Everything waiting on the author', tsz: 40,
          hasSub: true, sub: 'Every open question, with where it came from. The work continues without waiting for the answer; when one arrives it is recorded where the question lives.',
          chips: [this.chip(rowsT.length + ' open conflicts', 'rubric'), this.chip(D.agenda.unsettled.length + ' unsettled'), this.chip(D.agenda.process.length + ' about the process')],
          secs: this.secs(null, agendaSecs, uid + '-ag'), maxW: 760, key: 'agenda',
        };
        qr.isAgenda = true;
        qr.decided = this.runs(D.agenda.decided);
        qr.intro = this.runs(D.agenda.intro);
        qr.counts = rowsT.length + ' conflicts, ' + D.agenda.unsettled.length + ' questions about the novel, ' + D.agenda.process.length + ' about the process';
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
      w: w, wr: wr, cl: cl, cr: cr, ql: ql, qr: qr, pl: pl, proc: proc, loop: loop, chk: chkv,
      g: g, cp: cp,
    };
  }

  componentDidUpdate() {
    if (this._reader && this._rdKey !== this._rdShown) {
      this._reader.scrollTop = 0;
      this._rdShown = this._rdKey;
    }
  }
}
