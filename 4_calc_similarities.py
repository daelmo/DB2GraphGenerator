
from src.Graph_Similarity_Calculator import Graph_Similarity_Calculator
from src.Vector_Similarity_Calculator import Vector_Similarity_Calculator


def read_vector_file():
    return 0



if __name__ == '__main__':
    graphSimilarityCalculator = Graph_Similarity_Calculator()
    vectorSimilarityCalculator = Vector_Similarity_Calculator()

    movie_name = 'movies_1'

    #print(graphSimilarityCalculator.calc_AdjacencySimilarity(movie_name))
    #print(graphSimilarityCalculator.calc_PPageRankSimilarity(movie_name))
    print(vectorSimilarityCalculator.calc_PPageRankSimilarity(movie_name))
    print(vectorSimilarityCalculator.calc_AdjacencySimilarity(movie_name))

