import pandas as pd
import networkx as nx
import numpy as np
from scipy import stats


movie_name = '200000004'
path = 'data/4_filmlists/'
version = '4'


def calcSpearman(rank_list1, rank_list2, sorted_list):
    sorted_ranks1 = [rank_list1.index(movie) +1 for movie in sorted_movie_list]
    sorted_ranks2 = [rank_list2.index(movie) +1 for movie in sorted_movie_list]
    spearman_table = pd.DataFrame({'list1': sorted_ranks1, 'list2': sorted_ranks2})
    spearman_table['diff'] = spearman_table['list1'] - spearman_table['list2']
    spearman_table['diff_square'] = spearman_table['diff'] * spearman_table['diff']
    sum = spearman_table['diff_square'].sum()
    n_observations = len(rank_list1)
    result = 1 - (6 * sum / (n_observations * (n_observations*n_observations -1)))
    return result


if __name__ == '__main__':
    
    adjacencyVectorFile = open(path + version + '_vectorAdjacency_' + movie_name, 'r')
    adjacencyGraphFile = open(path + version + '_graphAdjacency_' + movie_name, 'r')
    ppagerankGraphFile = open(path + version + '_graphPPageRank_' + movie_name, 'r')
    ppagerankVectorFile = open(path + version + '_vectorPPageRank_' + movie_name, 'r')
    simrankVectorFile = open(path + version + '_vectorSimRank_' + movie_name, 'r')

    adjacencyGraphArray = adjacencyGraphFile.read().split('\n')
    adjacencyVectorArray =  adjacencyVectorFile.read().split('\n')
    ppagerankGraphArray = ppagerankGraphFile.read().split('\n')
    ppagerankVectorArray = ppagerankVectorFile.read().split('\n')
    simrankVectorArray = simrankVectorFile.read().split('\n')

    adjacencyGraphArray = list(filter(None, adjacencyGraphArray))
    adjacencyVectorArray = list(filter(None, adjacencyVectorArray))
    ppagerankVectorArray = list(filter(None, ppagerankVectorArray))
    ppagerankGraphArray = list(filter(None, ppagerankGraphArray))
    simrankVectorArray = list(filter(None, simrankVectorArray))

    sorted_movie_list = sorted(ppagerankGraphArray)

    print('print spearman results')
    print('pprVector - pprGraph:')
    print(stats.spearmanr(ppagerankVectorArray[:15], ppagerankGraphArray[:15]))

    print(' \n pprVector - adj Vector')
    print(stats.spearmanr(ppagerankVectorArray[:15], adjacencyVectorArray[:15]))

    print(' \n adjVector - adj Graph')
    print(stats.spearmanr(adjacencyVectorArray[:15], adjacencyGraphArray[:15]))

    print('\n adjGraph - ppGraph')
    print(stats.spearmanr(adjacencyGraphArray[:15], ppagerankGraphArray[:15]))

    print('\n Check: adjGraph - adjGraph')
    print(stats.spearmanr(adjacencyGraphArray[:15], adjacencyGraphArray[:15]))

    print(' \n adjVector -simrankVector')
    print(stats.spearmanr(adjacencyVectorArray[:15], simrankVectorArray[:15]))

    print('pprVector - simrankVector:')
    print(stats.spearmanr(ppagerankVectorArray[:15], simrankVectorArray[:15]))

    #graph = nx.read_edgelist('data/1_edge_list/kaggle_numbers.edgelist', create_using=nx.DiGraph)
    #print('\n adjVector - random list')
    #print(type(graph.nodes))
    #print(calcSpearman(adjacencyVectorArray, list(graph.nodes), sorted_movie_list))



