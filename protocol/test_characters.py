"""Ten locally derived CQs, NOT a transcription of unavailable CQ-SPARQL.xlsx."""
import copy
import tempfile
import unittest
from pathlib import Path

from characters import chapter_events, load, validate


class CompetencyQuestions(unittest.TestCase):
    def setUp(self):
        self.data = load(Path(__file__).parent / 'fixtures/synthetic.json')

    def test_01_figure_to_instances(self):
        self.assertEqual([i['id'] for i in self.data['instances'] if i['figure_id'] == 'f-ada'], ['i-ada', 'i-ada-two'])

    def test_02_instance_to_figure(self):
        self.assertEqual(self.data['instances'][0]['figure_id'], 'f-ada')

    def test_03_instance_traits(self):
        self.assertEqual(self.data['instances'][0]['trait_ids'], ['t-watchful'])
        self.assertEqual(self.data['instances'][2]['trait_ids'], [])

    def test_04_origin_types(self):
        self.assertEqual({f['origin'] for f in self.data['figures']}, {'originalCharacter', 'fanfictionCharacter'})

    def test_05_event_role(self):
        self.assertEqual(self.data['events'][0]['roles'], [{'instance_id': 'i-ada', 'role_id': 'er-witness'}])

    def test_06_relationship_node(self):
        relation = self.data['relationships'][0]
        self.assertEqual(relation['id'], 'r-alliance')
        self.assertEqual({p['instance_id'] for p in relation['participants']}, {'i-ada', 'i-bex'})

    def test_07_relationship_role_vocabulary(self):
        self.assertEqual({p['role_id'] for p in self.data['relationships'][0]['participants']}, {'rr-ally'})

    def test_08_state_change_at_event(self):
        state = self.data['transitions'][0]
        self.assertEqual((state['instance_id'], state['event_id'], state['before'], state['after']), ('i-ada', 'e-alarm', 'calm', 'alert'))

    def test_09_fabula_syuzhet(self):
        self.assertEqual([e['id'] for e in sorted(self.data['events'], key=lambda e: e['position'])], ['e-arrival', 'e-alarm'])
        self.assertEqual([e['id'] for e in chapter_events(self.data, 'c-opening')], ['e-alarm', 'e-arrival'])

    def test_10_session_is_not_canon(self):
        with self.assertRaisesRegex(ValueError, 'session proposal'):
            chapter_events(self.data, 'c-opening', canon=True)

    def test_invalid_inputs(self):
        mutations = [
            lambda d: d['instances'][0].update(figure_id='missing'),
            lambda d: d['events'][0]['roles'][0].update(role_id='rr-ally'),
            lambda d: d['transitions'][0].update(instance_id='i-ada-two'),
            lambda d: d['relationships'][0]['participants'][1].update(instance_id='i-ada-two'),
            lambda d: d['instances'][0].update(player_id='player'),
            lambda d: d['figures'][0].update(origin='unknown'),
            lambda d: d['events'][1].update(position=0),
            lambda d: d['chapters'][0].update(event_ids=['missing']),
            lambda d: d['transitions'][0].update(after='calm'),
            lambda d: d['figures'].append(copy.deepcopy(d['figures'][0])),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data = copy.deepcopy(self.data)
                mutate(data)
                with self.assertRaises(ValueError):
                    validate(data)

    def test_promotion_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.data['chapters'][0]['promotion'] = {'decision_path': 'Plan/decisions/fixture.md'}
            with self.assertRaises(ValueError):
                chapter_events(self.data, 'c-opening', canon=True, root=root)
            path = root / 'Plan/decisions/fixture.md'
            path.parent.mkdir(parents=True)
            path.write_text('Synthetic approval fixture, not novel canon.')
            self.assertEqual(len(chapter_events(self.data, 'c-opening', canon=True, root=root)), 2)
            self.data['chapters'][0]['promotion']['decision_path'] = '../../outside.md'
            with self.assertRaises(ValueError):
                chapter_events(self.data, 'c-opening', canon=True, root=root)


if __name__ == '__main__':
    unittest.main()
