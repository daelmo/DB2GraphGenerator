#!/usr/bin/python
import psycopg2




conn = psycopg2.connect(host="localhost",database="guentherdb", user="demo_user", password="password")

# create a cursor
cur = conn.cursor()
cur.execute("""SELECT title FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema');""")

# display the PostgreSQL database server version
db_version = cur.fetchall()
print(db_version)

# close the communication with the PostgreSQL
cur.close()