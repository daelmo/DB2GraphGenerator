
movie_name = 'movies_1'
path = 'data/4_filmlists/'
version = '1'


def calcSpearman(rank_list1, rank_list2):
    return 0

if __name__ == '__main__':
    #load files
    adjacencyVectorFile = open(path + version + '_vectorAdjacency_' + movie_name, 'r')
    adjacencyGraphFile = open(path + version + '_graphAdjacency_' + movie_name, 'r')
    ppagerankGraphFile = open(path + version + '_graphPPageRank_' + movie_name, 'r')
    ppagerankVectorFile = open(path + version + '_vectorPPageRank_' + movie_name, 'r')

    adjacencyGraphArray = adjacencyGraphFile.read().split('\n')
    adjacencyVectorArray =  adjacencyVectorFile.read().split('\n')
    ppagerankGraphArray = ppagerankGraphFile.read().split('\n')
    ppagerankVectorArray = ppagerankVectorFile.read().split('\n')

    adjacencyGraphArray = list(filter(None, adjacencyGraphArray))
    adjacencyVectorArray = list(filter(None, adjacencyVectorArray))
    ppagerankVectorArray = list(filter(None, ppagerankVectorArray))
    ppagerankGraphArray = list(filter(None, ppagerankGraphArray))

    print(calcSpearman(ppagerankVectorArray, ppagerankGraphArray))



