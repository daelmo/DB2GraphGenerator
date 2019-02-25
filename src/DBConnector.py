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
        return psycopg2.connect(host="localhost", database="kaggle", user="postgres", password="password")

    def _closeConnection(self):
        self.connection.close()

    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


