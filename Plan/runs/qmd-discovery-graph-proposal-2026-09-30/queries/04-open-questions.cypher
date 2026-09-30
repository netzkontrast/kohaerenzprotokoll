// current-main: Existing questions raised by a term
MATCH (q:Core)-[r:RAISED_BY]->(t:Core {id:$term}) RETURN q.id AS question, q.payload AS detail, r.via AS via ORDER BY q.id LIMIT 12
