// proposed-discovery: Ranked reading candidates for one decision sheet
MATCH (s:Sheet {id:$sheet})-[:HAS_QUERY]->(q:SearchQuery)-[r:P_RETRIEVED]->(h:Hit)-[:AT_DOC]->(d:Core) RETURN q.text AS query, d.id AS doc, h.first_line AS line, h.freshness AS freshness, r.method AS method, r.rank AS rank ORDER BY r.rank LIMIT 12
