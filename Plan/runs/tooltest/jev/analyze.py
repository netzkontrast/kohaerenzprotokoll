import json

results = json.load(open('/tmp/analysis.json'))

LEVEL_TO_DECISION = {0:'two-terms', 1:'judgement', 2:'one-term'}

def jev_decision(row, attempt):
    noul = row[f'jev_noul_a{attempt}']
    score = row[f'jev_score_a{attempt}']
    if noul > 0.5:
        return 'not-a-term'
    lvl = round(score)
    lvl = max(0, min(2, lvl))
    return LEVEL_TO_DECISION[lvl]

for row in results:
    row['jev_decision_a1'] = jev_decision(row, 1)
    row['jev_decision_a2'] = jev_decision(row, 2)
    row['repeat_agree'] = row['jev_decision_a1'] == row['jev_decision_a2']

classes = ['one-term','judgement','two-terms','not-a-term']
per_class = {c: {'n':0, 'agree':0, 'disagree':[]} for c in classes}

for row in results:
    p = row['person']
    per_class[p]['n'] += 1
    if row['jev_decision_a1'] == p:
        per_class[p]['agree'] += 1
    else:
        per_class[p]['disagree'].append(row)

overall_agree = sum(v['agree'] for v in per_class.values())
overall_n = sum(v['n'] for v in per_class.values())

repeat_agree_count = sum(1 for r in results if r['repeat_agree'])

print(f"Overall agreement (attempt 1 vs person): {overall_agree}/{overall_n} = {overall_agree/overall_n:.3f}")
print(f"Repeat consistency (attempt1 == attempt2 decision): {repeat_agree_count}/{len(results)} = {repeat_agree_count/len(results):.3f}")
print()
for c in classes:
    v = per_class[c]
    n = v['n']
    if n == 0:
        print(f"{c}: n=0")
        continue
    print(f"{c}: {v['agree']}/{n} = {v['agree']/n:.3f}")

print()
print("=== Difference lists (P27), by surface pair, with probabilities where they differ ===")
for c in classes:
    v = per_class[c]
    if not v['disagree']:
        continue
    print(f"\n-- person said {c}, Jev disagreed --")
    for row in v['disagree']:
        surf = ' / '.join(row['surfaces'])
        print(f"  {row['id']} [{surf}]  person={row['person']}  jev_a1={row['jev_decision_a1']} (score={row['jev_score_a1']}, conf={row['jev_conf_a1']}, probs={row['jev_probs_a1']}, noul={row['jev_noul_a1']})  jev_a2={row['jev_decision_a2']} (score={row['jev_score_a2']}, noul={row['jev_noul_a2']})")

json.dump(results, open('/tmp/analysis_scored.json','w'), ensure_ascii=False, indent=1)
