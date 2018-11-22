import psycopg2

class DBConnector:
    def __init__(self):
        self.connection = self._createConnection()

    def __enter__(self):
        return self


    def __exit__(self, type, value, traceback):
        self.connection.commit()
        self._closeConnection()

    def _createConnection(self):
        return psycopg2.connect(host="localhost",database="guentherdb", user="demo_user", password="password")

    def _closeConnection(self):
        self.connection.close()

    def execute(self, sql):
        print(sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


