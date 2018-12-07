#!/usr/bin/python
import networkx as nx
from DBConnector import DBConnector
from TranslatorManager import TranslatorManager

if __name__ == '__main__':
    with DBConnector() as dbconnector:
        translatormanager = TranslatorManager(dbconnector)
        graph = translatormanager.translate(dbconnector)

        print(graph.nodes())
        print(graph.edges())
        #print(graph.number_of_nodes())