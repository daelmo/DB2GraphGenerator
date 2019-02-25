import networkx as nx

class Graph_Similarity_Calculator:

    def __init__(self):
        self.graph = nx.read_edgelist('data/1_edge_list/kaggle.edgelist')

    def calc_PPageRankSimilarity(self, node1):
        rank_dict = nx.pagerank(self.graph, alpha=0.85, personalization={node1: 1})
        rank_dict = {key: abs(rank_dict[key] - rank_dict.get(node1, 0)) for key in rank_dict.keys()}
        sorted_by_value = sorted(rank_dict.items(), key=lambda kv: kv[1])
        movie_index = [x[0] for x in sorted_by_value]
        return movie_index

    def calc_AdjacencySimilarity(self, index1):
        return 0
