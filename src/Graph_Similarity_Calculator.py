import numpy as np
import networkx as nx


class Graph_Similarity_Calculator:

    def __init__(self):
        self.graph = nx.read_edgelist('data/1_edge_list/graph.edgelist')


    def calc_SimRank(self, graph, node1, node2):
        return 0

    def calc_PPageRank(self, graph, node1, node2):
        return 0

    def calc_AdjacencySimilarity(self, graph, node1, node2):
        return 0
