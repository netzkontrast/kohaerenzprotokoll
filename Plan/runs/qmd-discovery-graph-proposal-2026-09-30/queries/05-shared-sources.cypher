// current-main: Two terms citing the same document; no inferred relationship
MATCH (a:Core {id:$left})-[ra:READS]->(d:Core)<-[rb:READS]-(b:Core {id:$right}) RETURN d.id AS doc, ra.via AS left_via, rb.via AS right_via ORDER BY d.id LIMIT 12
