from os import getenv

from neo4j import GraphDatabase


uri = getenv('NEO4J_URI')
user = getenv('NEO4J_USER')
password = getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver(uri, auth=(user, password))
