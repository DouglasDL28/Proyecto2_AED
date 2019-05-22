from neo4j import GraphDatabase
from Database import Database
from Classes.Career import *

uri = "bolt://localhost:7687"

driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
db = Database("bolt://localhost:7687", "neo4j","password")

res = []
query = db.recommend("Matemática", "Elon Musk", "Programa")
for record in query:
    res.append(Career(record[0]["nombre"], record[0]["facultad"]))

for c in res:
    print(c.name)
    print(c.faculty)

