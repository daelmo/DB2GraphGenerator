
from src.Graph_Similarity_Calculator import Graph_Similarity_Calculator
from src.Vector_Similarity_Calculator import Vector_Similarity_Calculator


def read_vector_file():
    return 0



if __name__ == '__main__':
    graphSimilarityCalculator = Graph_Similarity_Calculator()
    vectorSimilarityCalculator = Vector_Similarity_Calculator()

    #print(graphSimilarityCalculator.calc_PPageRank())

    print(graphSimilarityCalculator.calc_AdjacencySimilarity('movies_1'))
    print(graphSimilarityCalculator.calc_PPageRankSimilarity('movies_2'))
    print(vectorSimilarityCalculator.calc_PPageRankSimilarity(id1))
    print(vectorSimilarityCalculator.calc_AdjacencySimilarity(id1))

