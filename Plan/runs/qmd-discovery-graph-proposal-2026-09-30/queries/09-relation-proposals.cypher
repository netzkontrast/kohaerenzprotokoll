// proposed-extraction: Attributed source-specific relation candidates for review
MATCH (c:Claim)-[:SUBJECT]->(s:Core {id:$term}), (c)-[:OBJECT]->(o:Core), (c)-[:CITED_FROM]->(d:Core) WHERE c.quote_status = 'placed' RETURN c.id AS claim, c.predicate AS predicate, o.id AS object, c.quote AS quote, d.id AS doc, c.line AS line, c.review_status AS review_status ORDER BY c.id LIMIT 12
