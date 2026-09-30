// proposed-discovery: Explicit prerequisites, never automatic decision ordering
MATCH (s:Sheet {id:$sheet})-[r:DEPENDS_ON]->(b:Sheet) RETURN b.id AS prerequisite, b.status AS status, r.via AS via ORDER BY b.id LIMIT 20
