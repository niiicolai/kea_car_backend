import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, Session as Neo4jSession

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


def read_cypher_file():
    try:
        with open('./scripts/neo4j_insert_data.cypher', 'r') as file:
            return file.read()
    except FileNotFoundError:
        with open('neo4j_insert_data.cypher', 'r') as file:
            return file.read()

def remove_all_constraints_and_nodes(session: Neo4jSession):
    # Remove all constraints
    constraints = session.run("SHOW CONSTRAINTS")
    for record in constraints:
        constraint_name = record["name"]
        session.run(f"DROP CONSTRAINT {constraint_name}")

    # Remove all nodes
    session.run("MATCH (n) DETACH DELETE n")

if __name__ == '__main__':
    cypher_queries = read_cypher_file()

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        remove_all_constraints_and_nodes(session)
        queries = cypher_queries.split(';')
        for query in queries:
            query = query.strip()
            if query and not query.startswith('//'):
                session.run(query)
    driver.close()