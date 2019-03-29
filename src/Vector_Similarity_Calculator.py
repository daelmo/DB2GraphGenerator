import numpy as np
import pandas as pd
import networkx as nx

class Vector_Similarity_Calculator:

    def __init__(self):
        temp = np.fromfile('data/3_vectors/kaggle2_ppr.bin', dtype=np.dtype(np.float32))
        temp = temp.reshape((int(len(temp)/128), 128))
        self.PPRvectors = pd.DataFrame(temp).T


        temp = np.fromfile('data/3_vectors/kaggle2_neigh.bin', dtype=np.dtype(np.float32))
        temp = temp.reshape((int(len(temp)/128), 128))
        self.ASvectors = pd.DataFrame(temp).T

        self.graph = nx.read_edgelist('data/1_edge_list/kaggle.edgelist')
        self.nodes = list(self.graph.nodes)

    def calc_PPageRankSimilarity(self, movie_name):
        movie_id = self.get_movieid_index(movie_name)
        dot_values = self.PPRvectors[movie_id].dot(self.PPRvectors)
        diff_values = abs(dot_values - dot_values[movie_id])
        rank_values = diff_values.sort_values()
        movie_index = rank_values.index.values
        print(len(self.nodes))
        print(len(movie_index))
        movie_names = [self.nodes[x] for x in movie_index]
        return movie_names

    def calc_AdjacencySimilarity(self, movie_name):
        movie_id = self.get_movieid_index(movie_name)
        dot_values = self.ASvectors[movie_id].dot(self.ASvectors)
        diff_values = abs(dot_values - dot_values[movie_id])
        rank_values = diff_values.sort_values()
        movie_index = rank_values.index.values
        print(len(self.nodes))
        print(len(movie_index))
        movie_names = [self.nodes[x] for x in movie_index]
        return movie_names


    def get_movieid_index(self, movieid):
        return self.nodes.index(movieid)



