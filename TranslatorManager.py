import networkx as nx

class TranslatorManager:
    tableList = None
    tableStructures = {}
    relationList = None
    dbConnector = None

    def __init__(self, dbConnector):
        self.dbConnector = dbConnector
        self.tableList = self._getTableList()
        self.tableStructures = self._getTableStructures()
        print (self.tableStructures)

    def _getTableList(self):
        sql =   """SELECT table_name 
                FROM information_schema.tables WHERE table_schema = 'public' 
                ORDER BY table_schema,table_name;"""
        return self.dbConnector.execute(sql)

    def _getTableStructures(self):
        structures = {}
        for (tableName,) in self.tableList:
            sql =   """select column_name from INFORMATION_SCHEMA.COLUMNS 
                    where table_name = '""" + tableName + """';"""
            columnNames = self.dbConnector.execute(sql)
            structures[tableName]= [columnName for (columnName,) in columnNames]
        return structures

    def translate(self, dbconnector):
        graph = nx.Graph()

        # get list of tables

        # get first table

        db_version = dbconnector.execute("""SELECT first_name from actor limit 10;""")
        print(db_version)

        # first table to nodes

        [graph.add_node(actor) for (actor,) in db_version]

        return graph