#!/usr/bin/python
import networkx as nx
from DBConnector import DBConnector

if __name__ == '__main__':
    with DBConnector() as dbconnector:

        dbconnector = DBConnector()
        db_version = dbconnector.execute("""SELECT * from actor limit 10;""")

        print(db_version)
