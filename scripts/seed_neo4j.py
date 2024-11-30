import os
from dotenv import load_dotenv
from datetime import datetime
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
    start_time = datetime.now()
    print(f"SEED_NEO4J: {start_time}: Starting Neo4j database restore:\n"
          f"Neo4j URI: {NEO4J_URI}\n"
          f"Neo4j User: {NEO4J_USER}\n"
          f"Neo4j Password: {NEO4J_PASSWORD}")
    try:
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
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"Successfully restored the Neo4j database, it took {duration} seconds.")
    except Exception as error:
        print(f"Error {error.__class__.__name__} caught during Neo4j Database restore:\n"
              f"{error}")
