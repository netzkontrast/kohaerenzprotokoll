// current-main: Existing conflict records involving a term
MATCH (c:Core)-[r:CONTESTS]->(t:Core {id:$term}) RETURN c.id AS record, c.payload AS detail, r.via AS via ORDER BY c.id LIMIT 12
