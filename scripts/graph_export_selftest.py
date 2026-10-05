"""Offline proof: useful reading pages, no database restore or quote dump."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import askdb
import graph_export as atlas
import kg


def fixture():
    nodes = {
        'term:a': {'id':'term:a','type':'term','slug':'a','term':'AEGIS','status':'candidate','surfaces':['AEGIS'],'path':'Wiki/candidates/a.md'},
        'term:b': {'id':'term:b','type':'term','slug':'b','term':'Entropie','status':'candidate','surfaces':['Entropie'],'path':'Wiki/candidates/b.md'},
        'doc:d': {'id':'doc:d','type':'doc','slug':'d','title':'Eine Quelle','date':'2026-01-01'},
        'conflict:C1': {'id':'conflict:C1','type':'conflict','subject':'Zwei Lesarten','status':'offen','path':'Wiki/conflicts/c1-test.md'},
        'question:Q1': {'id':'question:Q1','type':'question','question':'Welche Lesart gilt?','status':'offen','path':'Wiki/questions/q1-test.md'}}
    edges = [dict(source='term:a',target='term:b',type='links',via='Wiki/candidates/a.md:8'),
             dict(source='term:a',target='doc:d',type='reads',via='Wiki/candidates/a.md:2'),
             dict(source='term:a',target='doc:d',type='cites',via='Wiki/candidates/a.md:12',lines=[42]),
             dict(source='conflict:C1',target='term:a',type='contests',via='Wiki/conflicts/c1-test.md:3'),
             dict(source='question:Q1',target='term:a',type='raised_by',via='Wiki/questions/q1-test.md:3'),
             dict(source='question:Q1',target='conflict:C1',type='concerns',via='Wiki/questions/q1-test.md:4')]
    return dict(nodes=nodes,edges=edges,evidence={'a':[{'quote':'NEVER_DUMP_THIS_SOURCE_PASSAGE','doc':'d','line':42,'status':'verified'}]})


class Atlas(unittest.TestCase):
    def test_topics_keep_reading_and_citing_separate(self):
        pages=atlas.render(fixture())
        self.assertIn('Entropie',pages['terms/a.md'])
        self.assertIn('Lesung im Wiki enthalten',pages['terms/a.md'])
        self.assertIn('Im Wiki zitiert',pages['terms/a.md'])
        self.assertIn('ja | ja',pages['terms/a.md'])
        self.assertIn('Zwei Lesarten',pages['terms/a.md'])
        self.assertIn('Welche Lesart gilt?',pages['terms/a.md'])

    def test_no_source_dump_or_lossless_records(self):
        joined='\n'.join(atlas.render(fixture()).values())
        for token in ('NEVER_DUMP_THIS_SOURCE_PASSAGE','L42','"payload"','"ordinal"','evidence:','line:d:'):
            self.assertNotIn(token,joined)
        self.assertFalse(hasattr(atlas,'restore'))
        with self.assertRaises(SystemExit) as error, patch('sys.stderr'):
            kg.main(['restore'])
        self.assertEqual(error.exception.code,2)

    def test_readable_outputs_are_not_derivation_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            before=askdb.inputs(root)
            (root/'Graph').mkdir()
            (root/'Graph/terms.md').write_text('A fabricated assertion.')
            self.assertEqual(askdb.inputs(root),before)

    def test_recommendation_is_not_presented_as_decision(self):
        heads={'W1':{'file':'Plan/weichen/w1.md','status':'offen','deps':[],'empfehlung':'B'}}
        result=atlas.render(fixture(),heads,[('Plan/decisions/001.md','001 — An actual record')])
        self.assertIn('Empfehlung, nicht Beschluss',result['decisions.md'])
        self.assertIn('Entscheidungsakten',result['decisions.md'])
        self.assertIn('Plan/decisions/001.md',result['decisions.md'])

    def test_missing_data_is_visible(self):
        result=atlas.render(fixture())
        self.assertIn('Keine Quellenbeziehung',result['terms/b.md'])
        self.assertIn('keine Vollständigkeitsprüfung',result['terms/b.md'])
        self.assertIn('nicht gemessen',result['discovery.md'])

    def test_generation_is_deterministic(self):
        self.assertEqual(atlas.render(fixture()),atlas.render(fixture()))

    def test_drift_names_stale_missing_and_orphaned_pages(self):
        """SPEC.md step 3: `kg.py export --check` fails when Graph/ is not what an export would write."""
        pages=atlas.render(fixture())
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)
            for path,content in pages.items():
                (d/path).parent.mkdir(parents=True,exist_ok=True)
                (d/path).write_text(content,encoding='utf-8')
            self.assertEqual(atlas.drift(pages,d),[])
            (d/'terms/a.md').write_text(pages['terms/a.md']+'edited',encoding='utf-8')
            (d/'terms/b.md').unlink()
            (d/'terms/gone.md').write_text(atlas.MARKER+'old',encoding='utf-8')
            (d/'terms/hand.md').write_text('a page the renderer does not own',encoding='utf-8')
            self.assertEqual(atlas.drift(pages,d),['stale: terms/a.md','missing: terms/b.md','orphaned: terms/gone.md'])

    def test_session_hook_initializes_local_and_remote(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'scripts').mkdir()
            (root/'scripts/knowledge.py').write_text("import sys; from pathlib import Path; Path('started').write_text(' '.join(sys.argv[1:])); print('initialized')")
            for remote in ('false','true'):
                done=subprocess.run(['bash',str(askdb.ROOT/'.claude/hooks/session-start.sh')],env={'PATH':os.environ['PATH'],'HOME':os.environ['HOME'],'CLAUDE_PROJECT_DIR':str(root),'CLAUDE_CODE_REMOTE':remote},capture_output=True,text=True)
                self.assertEqual(done.returncode,0)
                self.assertEqual((root/'started').read_text(),'init --profile research')


if __name__=='__main__':
    unittest.main(verbosity=2)
