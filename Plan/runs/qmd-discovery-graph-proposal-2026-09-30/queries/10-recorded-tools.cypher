// proposed-operations: Command for a skill, as explicitly declared by a maintained registry
MATCH (s:Skill {id:$skill})-[r:USES_COMMAND]->(c:Command) RETURN c.invocation AS invocation, r.via AS via ORDER BY c.id LIMIT 10
