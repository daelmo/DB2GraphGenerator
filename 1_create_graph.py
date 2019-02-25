#!/usr/bin/python
from src.DBConnector import DBConnector
from src.graph_generator.TranslatorManager import TranslatorManager
import networkx as nx

if __name__ == '__main__':
    with DBConnector() as dbconnector:
        translatormanager = TranslatorManager(dbconnector)
        graph = translatormanager.translate()
        nx.write_edgelist(graph, 'data/1_edge_list/kaggle.edgelist', data=False)

        print(graph.number_of_nodes())