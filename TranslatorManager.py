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

        for (table,) in self.tableList:
            print(table)
            # get first table

            table_entries = dbconnector.execute("""SELECT * from """ + table + """ limit 10;""")
            print(table_entries)


            for table_entry in table_entries:
                # first tableids to nodes
                graph.add_node(table_entry[0])

                # attributes to nodes
                graph.add_nodes_from(table_entry[1:])

                # append attributes to id nodes

                for attribute in table_entry[1:]:
                    graph.add_edge(table_entry[0], attribute)
                    print(attribute)

            break

        return graph