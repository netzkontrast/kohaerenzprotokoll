"""Offline Cypher compatibility probe. All names/text here are synthetic.

This creates a demonstration graph, not the project's full corpus graph.
No repository file, production database, model or MCP server is accessed.
"""
import argparse
import json
from importlib.metadata import version
from pathlib import Path
from graphqlite import Graph

BASE = Path(__file__).resolve().parent

def fixture():
    def core(key, kind, **extra):
        return (key, {'kind':kind,'payload':json.dumps({'id':key,'type':kind,**extra}),**extra}, 'Core')
    nodes=[core('term:aegis','term'),core('term:kael','term'),
           core('doc:source-a','doc',read_status='reconciled'),core('doc:source-b','doc',read_status='unread'),
           core('conflict:C1','conflict',status='open'),core('question:Q1','question',status='open'),
           ('evidence:demo',{'status':'verified','payload':json.dumps({'quote':'Synthetic verified quotation.','doc':'source-a','line':12})},'Evidence'),
           ('sheet:W9',{'status':'offen'},'Sheet'),('sheet:W7',{'status':'offen'},'Sheet'),
           ('query:juna',{'text':'Wann erscheint Juna direkt?'},'SearchQuery'),
           ('run:demo',{'snapshot_hash':'synthetic-snapshot'},'SearchRun'),
           ('hit:a',{'first_line':12,'last_line':12,'freshness':'current'},'Hit'),
           ('hit:b',{'first_line':20,'last_line':24,'freshness':'current'},'Hit'),
           ('claim:demo',{'predicate':'DEMO_RELATION','quote':'Synthetic relation proposal.','quote_status':'placed','review_status':'pending','line':12},'Claim'),
           ('skill:graph-context',{},'Skill'),
           ('command:kg-context',{'invocation':'.venv-graphqlite/bin/python scripts/kg.py context <question>'},'Command')]
    edges=[('term:aegis','doc:source-a',{'via':'Wiki/candidates/aegis.md:2'},'READS'),
           ('term:aegis','doc:source-a',{'via':'Wiki/candidates/aegis.md:8'},'CITES'),
           ('term:kael','doc:source-a',{'via':'Wiki/candidates/kael.md:2'},'READS'),
           ('term:aegis','evidence:demo',{'via':'Wiki/candidates/aegis.md:8'},'HAS_EVIDENCE'),
           ('evidence:demo','doc:source-a',{'line':12,'via':'Sources/drive/source-a.md:12'},'CITED_FROM'),
           ('conflict:C1','term:aegis',{'via':'Wiki/conflicts/c1.md:4'},'CONTESTS'),
           ('question:Q1','term:aegis',{'via':'Wiki/questions/q1.md:4'},'RAISED_BY'),
           ('sheet:W9','sheet:W7',{'via':'Plan/weichen/w9-juna.md:4'},'DEPENDS_ON'),
           ('sheet:W9','query:juna',{},'HAS_QUERY'),('run:demo','query:juna',{},'RAN'),
           ('query:juna','hit:a',{'method':'bm25','rank':1},'P_RETRIEVED'),
           ('query:juna','hit:b',{'method':'vector','rank':2},'P_RETRIEVED'),
           ('hit:a','doc:source-a',{},'AT_DOC'),('hit:b','doc:source-b',{},'AT_DOC'),
           ('claim:demo','term:aegis',{},'SUBJECT'),('claim:demo','term:kael',{},'OBJECT'),
           ('claim:demo','doc:source-a',{},'CITED_FROM'),
           ('skill:graph-context','command:kg-context',{'via':'demo-registry.json:1'},'USES_COMMAND')]
    return nodes,edges

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--db',default=':memory:',help='Optional NEW scratch .db path, never a production DB')
    args=ap.parse_args()
    if version('graphqlite')!='0.8.0':
        raise SystemExit('GraphQLite 0.8.0 required')
    if args.db!=':memory:' and Path(args.db).exists():
        raise SystemExit('Refusing to replace an existing database')
    g=Graph(args.db)
    try:
        nodes,edges=fixture(); g.insert_graph_bulk(nodes,edges)
        result=[]
        for q in json.loads((BASE/'query-catalog.json').read_text()):
            rows=g.query(q['query'],q['params'])
            assert len(rows)==q['expected'],(q['id'],rows)
            result.append({'id':q['id'],'schema':q['schema'],'rows':len(rows),'status':'passed'})
        # Two kinds of edge between the same pair must survive.
        assert len(g.query('MATCH (a:Core {id:$term})-[r]->(d:Core {id:$doc}) RETURN type(r) AS kind',{'term':'term:aegis','doc':'doc:source-a'}))==2
        # A quoted identifier cannot expand the selected graph neighbourhood.
        assert g.query('MATCH (t:Core {id:$term}) RETURN t.id AS id',{'term':"term:aegis') DELETE n //"})==[]
        report={'graphqlite':version('graphqlite'),'scope':'synthetic demonstration only','queries':result,'parallel_edges':'passed','parameter_binding':'passed'}
        (BASE/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2))
    finally:
        g.close()

if __name__=='__main__':
    main()
