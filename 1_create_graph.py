#!/usr/bin/python
import networkx as nx
from src.DBConnector import DBConnector
from src.graph_generator.TranslatorManager import TranslatorManager


if __name__ == '__main__':
    with DBConnector() as dbconnector:
        translator_manager = TranslatorManager(dbconnector)
        graph = translator_manager.translate()
        nx.write_edgelist(graph, 'data/1_edge_list/kaggle_numbers_bidi.edgelist', data=False)

        print(graph.number_of_nodes())
