(() => {
  const failures = []; const expect = (ok, why) => { if (!ok) failures.push(why); };
  const c = new Component(); c.props = {}; c.state = { screen: 'questions', qt: 'reading', rt: 'aegis' };
  const d = c.kp(); const view = () => c.questionWorkshop();
  expect(view().count === '100 Fragen' && view().list.length === 25, 'a primary term gets exactly 100 prompts and 25 rendered rows');
  c.state.rkind = 'cross'; expect(view().count === '60 Fragen', 'cross-term filter contains only 60 cross questions');
  c.state.rkind = 'direct'; expect(view().count === '40 Fragen', 'direct filter contains only 40 term questions');
  c.state.rkind = ''; c.state.rq = 'zxzzunfindable'; expect(view().empty, 'empty search explains itself');
  c.state.rq = ''; c.state.rqpage = 99; expect(view().pageLabel === 'Seite 4 von 4' && view().nextDisabled, 'pagination clamps after a filter change');
  c.state.rqpage = 0; c.state.rqi = 'RQ-aegis-001';
  expect(view().hasSelection && view().links.length === 1, 'selection exposes its originating term');
  view().onNote({ target: { value: 'Eine lokale Antwort' } }); view().onNoteStatus({ target: { value: 'answered' } });
  expect(view().note === 'Eine lokale Antwort' && view().noteStatus === 'answered', 'notes and local status persist in component state');
  c.state.rstatus = 'answered'; expect(view().count === '1 Fragen', 'local status filter returns only the answered note');
  c.state.rstatus = ''; c.state.rmentions = true; expect(parseInt(view().count, 10) > 100, 'related-term mode also includes incoming comparisons');
  c.state.rmentions = false;
  const text = c.readingExport([d.readingById['RQ-aegis-001']], c.state.rnotes);
  expect(text.includes('Eine lokale Antwort') && text.includes('RQ-aegis-001') && text.includes('Wiki/questions/reading/aegis.json'), 'export carries identity, file and answer');
  expect(view().prompt.includes('RQ-aegis-001') && !view().prompt.includes('Selbstbild als Bewahrer'), 'handover prompt refers to local records without copying their text');
  const at = d.pages.findIndex((p) => p.s === 'kishotenketsu');
  c.state = { screen: 'wiki', page: at, wf: 'terms' }; const wiki = c.renderVals();
  expect(wiki.w.list.some((p) => p.t === 'Kishōtenketsu') && wiki.w.views.some((t) => t.label === 'Begriffsseite' && !t.disabled), 'term page is discoverable through its own filter and tab');
  c.state.wview = 'promotion'; expect(c.renderVals().rd.secs.length > 0, 'promotion dossier is populated');
  c.state = { screen: 'questions', qt: 'reading', rt: 'aegis', rqi: 'RQ-aegis-100' };
  const back = c.unroute(c.route()); expect(back.rqi === 'RQ-aegis-100' && back.rqpage === 3, 'a deep link opens its question and page');
  const base = c.unroute('#/wiki/aegis'); expect(base.wview === null, 'browser history does not leak the previous wiki layer');
  // the Schreibtisch (decision 030): the grid, a chapter's address, a scene's address with its chapter, marks
  const K = d.novel.desk;
  expect(K.chapters.length === 41 && c.novelEntries('schreibtisch').filter((x) => x.kind === 'desk').length === 41, 'the Schreibtisch lists Kap 0–40, every chapter once');
  c.state = { screen: 'manuscript', mtab: 'schreibtisch', msel: 'kap-01' };
  const dk = c.renderVals();
  expect(dk.desk.isChapter && dk.rd.title.indexOf('Kap 1') === 0 && c.unroute(c.route()).msel === 'kap-01', 'a chapter of the Schreibtisch has its address and its briefing');
  expect(dk.desk.weichen.every((w) => w.copyLabel && typeof w.copy === 'function'), 'every open Weiche of the chapter hands over a copyable answer prompt');
  expect(c.unroute('#/manuscript/schreibtisch/kap-99/szene-1') === null || !c.unroute('#/manuscript/schreibtisch/kap-99/szene-1').msel, 'a scene address of a chapter that is not there opens nothing');
  c.state = { screen: 'manuscript', mtab: 'schreibtisch', msel: 'regeln' };
  const rl = c.renderVals();
  expect(rl.desk.isRules && rl.rd.secs.length === 1 && rl.desk.rules.length === K.rules.filter((r) => r.status === 'offen').length, 'the register shows every rule and a prompt for each open one');
  const scene = { f: 'Manuscript/kap-01/szene-9-fixture.md', k: 9, t: 'Fixture', status: 'entwurf', w: 12, beats: 'b', beatsOn: '', paras: ['Erster Absatz.', 'Zweiter Absatz.'], checked: '', checkStale: true, briefingBehind: false, approved: '' };
  c.state = { screen: 'manuscript', mtab: 'schreibtisch', dmarks: {} };
  c.saveMark(scene.f, 1, { m: 'falsch', note: 'hier nicht' }); c.saveMark(scene.f, 7, { m: 'frage' });
  const ex = c.marksExport(K.chapters[1], scene, c.state.dmarks);
  expect(ex.includes('¶2 — falsch') && ex.includes('hier nicht') && !ex.includes('¶8'), 'a mark on a paragraph that is not there stays out of the export');
  expect(ex.includes('manuscript.py approve kap-01 9 --words') && !ex.includes('freigegeben'), 'the export names the approval command and approves nothing');
  c.saveMark(scene.f, 1, { m: 'none', note: '' }); c.saveMark(scene.f, 7, { m: 'none' });
  expect(!c.state.dmarks[scene.f], 'a cleared mark leaves no trace');
  // the start page (records.py): a record's address, answers kept by depth, the file that leaves the browser
  if (d.records.records.length) {
    const r0 = d.records.records[0];
    c.state = { screen: 'now', rec: r0.id, answers: {} };
    expect(c.unroute(c.route()).rec === r0.id && c.renderVals().now.hasRec && c.renderVals().now.rc.title === r0.t, 'a record has its address and its report card');
    const open = r0.qs.filter((q) => !q.answer);
    open.forEach((q) => c.saveAnswer(q.id, q.depth === 1 ? { yes: false } : q.depth === 2 ? { option: q.options[0][0] } : { words: 'Nur meine Worte.' }));
    const f = c.answerFile(r0, c.state.answers, new Date(Date.UTC(2026, 9, 26, 18, 0, 0)));
    expect(!open.length || (f && f.name === r0.id + '-20261026T180000Z.json' && f.body.by === 'author' && f.body.answers.length === open.length), 'every open question answered by depth goes into one answer file, named for its session and time, by the author');
    const d3 = open.find((q) => q.depth === 3);
    if (d3) { c.saveAnswer(d3.id, { words: '   ' }); expect(!c.answerFile(r0, c.state.answers).body.answers.some((x) => x.question === d3.id), 'a depth-3 answer without words is not exported'); }
    const d1 = open.find((q) => q.depth === 1);
    if (d1) { c.saveAnswer(d1.id, { yes: null }); expect(!c.state.answers[d1.id], 'clearing an answer leaves no trace'); }
    expect(c.answerFile(r0, {}) === null, 'nothing answered, nothing to save');
  }
  const original = d.selftests; d.selftests = [['not run', 'fixture', 'no run']];
  expect(c.renderVals().railChecks.find((x) => x.label === 'Self-tests').dot === '#9A9384', 'a skipped test is unknown, never a green pass');
  d.selftests = original;
  console.log(JSON.stringify(failures));
})();
