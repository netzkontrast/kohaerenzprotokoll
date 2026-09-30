// current-main: Terms citing a changed source; structural impact only
MATCH (t:Core)-[r:CITES]->(d:Core {id:$doc}) RETURN t.id AS term, r.via AS via ORDER BY t.id LIMIT 30
