// proposed-discovery: Which retrieval run produced a hit, with query and snapshot
MATCH (run:SearchRun)-[:RAN]->(q:SearchQuery {id:$query})-[r:P_RETRIEVED]->(h:Hit) RETURN run.id AS run, run.snapshot_hash AS snapshot_hash, q.text AS query, h.id AS hit, r.method AS method, r.rank AS rank ORDER BY r.rank LIMIT 12
