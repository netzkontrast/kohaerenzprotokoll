// proposed-discovery: Unread source candidates for a registered question
MATCH (q:SearchQuery {id:$query})-[r:P_RETRIEVED]->(h:Hit)-[:AT_DOC]->(d:Core) WHERE d.read_status = 'unread' AND h.freshness = 'current' RETURN d.id AS doc, h.first_line AS first_line, h.last_line AS last_line, r.method AS method, r.rank AS rank ORDER BY r.rank LIMIT 8
