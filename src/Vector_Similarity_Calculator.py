import numpy as np
import pandas as pd
import networkx as nx

class Vector_Similarity_Calculator:

    def __init__(self):
        temp = np.fromfile('data/3_vectors/kaggle.bin', dtype=np.dtype(np.float32))
        self.PPRvectors = pd.DataFrame(np.split(temp, 128))
        temp = np.fromfile('data/3_vectors/kaggle.bin', dtype=np.dtype(np.float32))
        self.ASvectors = pd.DataFrame(np.split(temp, 128))
        self.graph = nx.read_edgelist('data/1_edge_list/kaggle.edgelist')
        self.nodes = list(self.graph.nodes)


        print(self.ASvectors.shape)
        print(self.PPRvectors)

    def calc_PPageRankSimilarity(self, index1):
        dot_values = self.PPRvectors[index1].dot(self.PPRvectors)
        dot_values - dot_values
        return

    def calc_AdjacencySimilarity(self, index1):
        sim_values = self.ASvectors[index1].dot(self.ASvectors)
        return


    def get_movieid_index(self, movieid):
        return self.nodes.index(movieid)



