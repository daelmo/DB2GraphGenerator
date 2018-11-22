#!/usr/bin/python

from DBConnector import DBConnector

if __name__ == '__main__':
    with DBConnector() as dbconnector:

        dbconnector = DBConnector()
        db_version = dbconnector.execute("""SELECT version();""")

        print(db_version)
