// proposed-discovery: Decision sheets whose recorded search hit a changed document
MATCH (s:Sheet)-[:HAS_QUERY]->(q:SearchQuery)-[:P_RETRIEVED]->(h:Hit)-[:AT_DOC]->(d:Core {id:$doc}) RETURN DISTINCT s.id AS sheet, q.id AS query ORDER BY s.id LIMIT 20
