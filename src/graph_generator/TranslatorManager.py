import networkx as nx
import pandas as pd
import numpy as np

class TranslatorManager:
    tableList = None
    tableStructures = {}
    relationList = None
    dbconnector = None
    foreign_key_list = []
    skip_table_list= []
    schema_name = 'public'

    def __init__(self, dbConnector):
        self.dbconnector = dbConnector
        self.tableList = self._getTableList()
        self.tableStructures = self._getTableStructures()
        self.foreign_key_list = self._getForeignKeys()
        self.relationList, self.mn_relationList = self._getRelationLists()

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
            if table_name in self.skip_table_list or table_name is 'movies_genres': continue
            graph = self._buildNodesFromTableAttributes(graph, table_name)

        graph = self._buildRelations(graph)
        graph = self._buildMNRelations(graph)
        return graph

    def _buildNodesFromTableAttributes(self, graph, table_name):
        if table_name == 'movies_genres':
            return graph
        table_entries = self.dbconnector.execute("""SELECT * from """ + self.schema_name + '.' + table_name + ';')
        attribute_ids = {}
        i = 0

        for table_row in table_entries:
            row_id = table_name + '_' + str(table_row[0])
            attributes = table_row[1:]

            graph.add_node(row_id)

            for attribute in attributes:
                if (attribute,) in self.foreign_key_list: continue

                if attribute not in attribute_ids.values():
                    attribute_ids['attribute_' + str(i)] = attribute
                    attribute_id = 'attribute_' + str(i)
                    i += 1
                else:
                    attribute_id = list(attribute_ids.keys())[list(attribute_ids.values()).index(attribute)]

                graph.add_node(attribute_id)
                graph.add_edge(row_id, attribute_id)
        return graph

    def _buildMNRelations(self, graph):
        df = self.mn_relationList
        for x in range(0, int(len(df.index) / 2)):
            sql = 'SELECT ' + df.iloc[[2 * x]][1].to_string(index=False) + ',' + df.iloc[[2 * x + 1]][1].to_string(
                index=False) + \
                  ' from public.' + df.iloc[[2 * x]][0].to_string(index=False) + ';'
            table_entries = self.dbconnector.execute(sql)
            for from_table, to_table in table_entries:
                start_node_id = df.iloc[[2 * x]][2].to_string(index=False) + '_' + str(from_table)
                end_node_id = df.iloc[[2 * x + 1]][2].to_string(index=False) + '_' + str(to_table)
                graph.add_edge(start_node_id, end_node_id)
                graph.add_edge(end_node_id, start_node_id)
        return graph

    def _getMNTables(self):
        sql = '''
               SELECT 
                   a.TABLE_NAME
               FROM 
                  INFORMATION_SCHEMA.TABLE_CONSTRAINTS A
               JOin INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE B
               ON  A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
               WHERE A.CONSTRAINT_TYPE = 'PRIMARY KEY'
               GROUP BY a.table_name, b.constraint_name
               HAVING COUNT(*) > 1;
       	        '''
        mn = self.dbconnector.execute(sql)
        result = [x for (x,) in mn]
        return ['movies_genres']

    def _buildRelations(self, graph):
        for index, row in self.relationList.iterrows():
            table_entries = self.dbconnector.execute('''SELECT *,'''+ row[1] +''' from ''' + self.schema_name + '.' + row[0] + '; ')
            for table_entry in table_entries:
                start_node_id = row[0] + '_' + str(table_entry[0])
                end_node_id = row[2] + '_' + str(table_entry[-1])
                graph.add_edge(start_node_id, end_node_id)
        return graph

    def _getRelationLists(self):
        mn_relation_list = self._getMNTables()
        sql = '''SELECT 
        tc.table_name, 
        kcu.column_name, 
        ccu.table_name AS foreign_table_name,
        ccu.column_name AS foreign_column_name 
        FROM 
        information_schema.table_constraints AS tc 
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name 
          AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
          AND ccu.table_schema = tc.table_schema
        WHERE constraint_type = 'FOREIGN KEY'; '''
        relations = pd.DataFrame(self.dbconnector.execute(sql))
        simple_relations = relations[-relations[0].isin(mn_relation_list)]
        mn_relations = relations[relations[0].isin(mn_relation_list)]
        print(simple_relations)
        print(mn_relations)
        return simple_relations, mn_relations








