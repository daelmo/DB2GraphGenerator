import networkx as nx

class TranslatorManager:
    tableList = None
    tableStructures = {}
    relationList = None
    dbConnector = None
    skip_table_list= ['nicer_but_slower_film_list']

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
        graph = nx.DiGraph()

        for (table,) in self.tableList:
            if table in self.skip_table_list: continue
            table_entries = dbconnector.execute("""SELECT * from """ + table +""" limit 10;""")

            for table_entry in table_entries:
                node_id = table + '_' + str(table_entry[0])
                attributes = table_entry[1:]

                graph.add_node(node_id)
                for attribute in attributes:
                    if isinstance(attribute, list):
                        for element in attribute:
                            graph.add_node(element)
                            graph.add_edge(node_id, element)
                        continue
                    graph.add_node(attribute)
                    graph.add_edge(node_id, attribute)


        return graph