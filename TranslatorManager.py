import networkx as nx

class TranslatorManager:
    tableList = None
    tableStructures = {}
    relationList = None
    dbconnector = None
    foreign_key_list = []
    skip_table_list= ['nicer_but_slower_film_list']

    def __init__(self, dbConnector):
        self.dbconnector = dbConnector
        self.tableList = self._getTableList()
        self.tableStructures = self._getTableStructures()
        self.foreign_key_list = self._getForeignKeys()
        print (self.foreign_key_list)

    def _getTableList(self):
        sql =   """SELECT table_name 
                FROM information_schema.tables WHERE table_schema = 'public' 
                ORDER BY table_schema,table_name;"""
        return self.dbconnector.execute(sql)

    def _getForeignKeys(self):
        sql= """
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
            WHERE CONSTRAINT_NAME IN (
                SELECT CONSTRAINT_NAME
                FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS)
            ORDER BY TABLE_NAME;
        """
        return self.dbconnector.execute(sql)

    def _getTableStructures(self):
        structures = {}
        for (tableName,) in self.tableList:
            sql =   """select column_name from INFORMATION_SCHEMA.COLUMNS 
                    where table_name = '""" + tableName + """';"""
            columnNames = self.dbconnector.execute(sql)
            structures[tableName]= [columnName for (columnName,) in columnNames]
        return structures

    def translate(self):
        graph = nx.DiGraph()

        for (table_name,) in self.tableList:
            if table_name in self.skip_table_list: continue
            graph = self._buildNodesFromTable(graph, table_name)

        graph = self._buildRelations(graph)
        return graph

    def _buildNodesFromTable(self, graph, table_name):
        table_entries = self.dbconnector.execute("""SELECT * from """ + table_name + """ limit 10;""")
        for table_entry in table_entries:
            node_id = table_name + '_' + str(table_entry[0])
            attributes = table_entry[1:]

            graph.add_node(node_id)
            for attribute in attributes:
                if (attribute,) in self.foreign_key_list: continue
            if isinstance(attribute, list):
                for element in attribute:
                    graph.add_node(element)
                    graph.add_edge(node_id, element)
                continue
            graph.add_node(attribute)
            graph.add_edge(node_id, attribute)
            return graph

    def _buildRelations(self, graph):
        return graph
