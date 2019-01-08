#!/usr/bin/python
from DBConnector import DBConnector
from graph_generator.TranslatorManager import TranslatorManager
import networkx as nx

if __name__ == '__main__':
    with DBConnector() as dbconnector:
        translatormanager = TranslatorManager(dbconnector)
        graph = translatormanager.translate()
        nx.write_edgelist(graph, 'data/edge_list/graph.edgelist')

        print(graph.number_of_nodes())