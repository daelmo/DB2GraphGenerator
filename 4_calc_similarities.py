from src.similarity_calculation.Graph_Similarity_Calculator import Graph_Similarity_Calculator
from src.similarity_calculation.Vector_Similarity_Calculator import Vector_Similarity_Calculator
import time


def read_vector_file():
    return 0

path = 'data/4_filmlists/'
version = '5'
movie_name = '200000004'


if __name__ == '__main__':
    graphSimilarityCalculator = Graph_Similarity_Calculator()
    vectorSimilarityCalculator = Vector_Similarity_Calculator()

    print('---graphAdjacency---')
    start = time.time()
    with open(path + version + '_graphAdjacency_'+ movie_name, 'w+') as file:
        for item in graphSimilarityCalculator.calc_AdjacencySimilarity(movie_name):
            file.write("%s\n" % item)
    end = time.time()
    print(end - start)

    print('---graphPPrank---')
    start = time.time()
    with open(path + version + '_graphPPageRank_'+ movie_name, 'w+') as file:
        for item in graphSimilarityCalculator.calc_PPageRankSimilarity(movie_name):
            file.write("%s\n" % item)
    end = time.time()
    print(end - start)

    print('---vectorPPRank---')
    start = time.time()
    with open(path + version + '_vectorPPageRank_'+ movie_name, 'w+') as file:
        for item in vectorSimilarityCalculator.calc_PPageRankSimilarity(movie_name):
            file.write("%s\n" % item)
    end = time.time()
    print(end - start)

    print('---vectorAdjacency---')
    start = time.time()
    with open(path + version + '_vectorAdjacency_'+ movie_name, 'w+') as file:
        for item in vectorSimilarityCalculator.calc_AdjacencySimilarity(movie_name):
            file.write("%s\n" % item)
    end = time.time()
    print(end - start)

    print('---vectorSimrank---')
    start = time.time()
    with open(path + version + '_vectorSimRank_'+ movie_name, 'w+') as file:
        for item in vectorSimilarityCalculator.calc_SimRankSimilarity(movie_name):
            file.write("%s\n" % item)
    end = time.time()
    print(end - start)
