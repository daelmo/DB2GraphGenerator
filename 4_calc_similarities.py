from src.Graph_Similarity_Calculator import Graph_Similarity_Calculator
from src.Vector_Similarity_Calculator import Vector_Similarity_Calculator


def read_vector_file():
    return 0

path = 'data/4_filmlists/'
version = '3'
movie_name = 'movies_4'


if __name__ == '__main__':
    graphSimilarityCalculator = Graph_Similarity_Calculator()
    vectorSimilarityCalculator = Vector_Similarity_Calculator()

    with open(path + version + '_graphAdjacency_'+ movie_name, 'w+') as file:
        for item in graphSimilarityCalculator.calc_AdjacencySimilarity(movie_name):
            file.write("%s\n" % item)

    with open(path + version + '_graphPPageRank_'+ movie_name, 'w+') as file:
        for item in graphSimilarityCalculator.calc_PPageRankSimilarity(movie_name):
            file.write("%s\n" % item)

    with open(path + version + '_vectorPPageRank_'+ movie_name, 'w+') as file:
        for item in vectorSimilarityCalculator.calc_PPageRankSimilarity(movie_name):
            file.write("%s\n" % item)

    with open(path + version + '_vectorAdjacency_'+ movie_name, 'w+') as file:
        for item in vectorSimilarityCalculator.calc_AdjacencySimilarity(movie_name):
            file.write("%s\n" % item)
