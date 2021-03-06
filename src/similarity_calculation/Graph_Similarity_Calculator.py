import networkx as nx
import numpy as np

class Graph_Similarity_Calculator:

    def __init__(self):
        self.graph = nx.read_edgelist('data/1_edge_list/kaggle_numbers_bidi.edgelist', create_using=nx.DiGraph)
        print(len(self.graph.nodes))
        print(len(self.graph.edges))

    def calc_PPageRankSimilarity(self, node1):
        rank_dict = nx.pagerank(self.graph, alpha=0.85, personalization={node1: 1})
        rank_dict = {key: abs(rank_dict[key] - rank_dict.get(node1, 0)) for key in rank_dict.keys()}
        sorted_by_value = sorted(rank_dict.items(), key=lambda kv: kv[1])
        movie_index = [x[0] for x in sorted_by_value]
        return movie_index

    def calc_AdjacencySimilarity(self, node1):
        temp = list(map(int, self.graph.nodes))
        temp.sort()
        all_nodes = np.array(list(map(str, temp)))
        outgoing_edges = self.graph.out_edges(node1)
        similarity = [ 1/len(outgoing_edges) if (node1, node) in self.graph.out_edges(node) else 0 for node in all_nodes]
        sortindex = np.argsort(similarity)
        movie_index = list(all_nodes[sortindex[::-1]])
        return movie_index

