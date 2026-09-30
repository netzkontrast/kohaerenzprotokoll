// current-main: Fetch verified evidence for a term
MATCH (t:Core {id:$term})-[:HAS_EVIDENCE]->(e:Evidence)-[r:CITED_FROM]->(d:Core) WHERE e.status = 'verified' RETURN e.id AS evidence_id, e.payload AS evidence, d.id AS doc, r.line AS line ORDER BY e.id LIMIT 12
