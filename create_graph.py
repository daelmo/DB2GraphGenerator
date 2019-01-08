#!/usr/bin/python
from DBConnector import DBConnector
from graph_generator.TranslatorManager import TranslatorManager

if __name__ == '__main__':
    with DBConnector() as dbconnector:
        translatormanager = TranslatorManager(dbconnector)
        graph = translatormanager.translate()

        print(graph.number_of_nodes())