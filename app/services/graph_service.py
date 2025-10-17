from os import getenv

from neo4j import GraphDatabase, Query


uri = getenv('NEO4J_URI')
user = getenv('NEO4J_USER')
password = getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver(uri, auth=(user, password))
CYPHER = Query("""
    MERGE (u:User {id: $uid})
    MERGE (s:Symptom {name: $symptom})
    MERGE (u)-[:EXHIBITS {intensity: $intensity}]->(s)
""")

def _add_symptom_tx(tx, uid, symptom, intensity):
    tx.run(CYPHER, uid=uid, symptom=symptom, intensity=intensity)

def add_symptom_node(uid, symptom, intensity):
    with driver.session() as session:
        session.execute_write(_add_symptom_tx, uid, symptom, intensity)
