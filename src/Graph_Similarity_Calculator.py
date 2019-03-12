import networkx as nx
import numpy as np

class Graph_Similarity_Calculator:

    def __init__(self):
        self.graph = nx.read_edgelist('data/1_edge_list/kaggle.edgelist', create_using=nx.DiGraph)

    def calc_PPageRankSimilarity(self, node1):
        rank_dict = nx.pagerank(self.graph, alpha=0.85, personalization={node1: 1})
        rank_dict = {key: abs(rank_dict[key] - rank_dict.get(node1, 0)) for key in rank_dict.keys()}
        sorted_by_value = sorted(rank_dict.items(), key=lambda kv: kv[1])
        movie_index = [x[0] for x in sorted_by_value]
        print(len(movie_index))
        return movie_index

    def calc_AdjacencySimilarity(self, node1):
        all_nodes = np.array(self.graph.nodes)
        outgoing_edges = self.graph.out_edges(node1)
        similarity = [ 1/len(outgoing_edges) if (node1, node) in self.graph.in_edges(node) else 0 for node in all_nodes]
        sortindex = np.argsort(similarity)
        movie_index = list(all_nodes[-sortindex])
        print(len(movie_index))
        return movie_index

