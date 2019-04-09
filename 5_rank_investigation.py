import pandas as pd
import networkx as nx
import numpy as np
import pickle
from src.DBConnector import DBConnector

movie_name = '200000004'
path = 'data/4_filmlists/'
version = '4'

def _load_ranks():
    adjacencyVectorFile = open(path + version + '_vectorAdjacency_' + movie_name, 'r')
    adjacencyGraphFile = open(path + version + '_graphAdjacency_' + movie_name, 'r')
    ppagerankGraphFile = open(path + version + '_graphPPageRank_' + movie_name, 'r')
    ppagerankVectorFile = open(path + version + '_vectorPPageRank_' + movie_name, 'r')

    adjacencyGraphArray = adjacencyGraphFile.read().split('\n')
    adjacencyVectorArray = adjacencyVectorFile.read().split('\n')
    ppagerankGraphArray = ppagerankGraphFile.read().split('\n')
    ppagerankVectorArray = ppagerankVectorFile.read().split('\n')

    adjacencyGraphArray = list(filter(None, adjacencyGraphArray))
    adjacencyVectorArray = list(filter(None, adjacencyVectorArray))
    ppagerankVectorArray = list(filter(None, ppagerankVectorArray))
    ppagerankGraphArray = list(filter(None, ppagerankGraphArray))

    return adjacencyGraphArray, adjacencyVectorArray, ppagerankVectorArray, ppagerankGraphArray


def _get_names_for(dbconnector, movie_array):
    table_ids = [_get_tablename_id_for(movie) for movie in movie_array]
    for table_name, id in table_ids:
        if table_name == 'attributes':
            _get_attribute(id)
            continue
        sql = "select * from public."+ table_name + " where id=" + str(id) + ";"
        print(dbconnector.execute(sql))



def _get_tablename_id_for(movie_name):

    first_digit = int(movie_name[:1])
    if first_digit == 1:
        return "directors", int(movie_name) - 100000000
    elif first_digit == 2:
        return "movies", int(movie_name) - 200000000
    elif first_digit == 3:
        return "genres", int(movie_name) - 300000000
    elif first_digit == 5:
        return "attributes", movie_name

    print(first_digit)

def _get_attribute(id):
    print(attribute_dict.get(int(id)))


def _get_movie_ranks(list, ids):
    return [list.index(str(id)) for id in ids]



if __name__ == '__main__':
    adjacencyGraphArray, adjacencyVectorArray, ppagerankVectorArray, ppagerankGraphArray = _load_ranks()

    print(len(adjacencyGraphArray))

    with (open('attributes_dict.txt', "rb")) as openfile:
        attribute_dict = pickle.load(openfile)


        with DBConnector() as dbconnector:
            print('-------pprGraph---------')
            print(_get_names_for(dbconnector, ppagerankGraphArray[:15]))
            print('--------adjGraph--------')
            print(_get_names_for(dbconnector, adjacencyGraphArray[:15]))
            print('---------adjVect-------')
            print(_get_names_for(dbconnector, adjacencyVectorArray[:15]))
            print('--------pprVect--------')
            print(_get_names_for(dbconnector, ppagerankVectorArray[:15]))
            print('----------------')
            print('----------------')

    print('\n \n \n Star Wars')
    movie_ids = [4,1330,1331,1332, 6578, 27378, 30898, 32790]
    movie_ids = [200000000 + id for id in movie_ids ]
    similars = [100003078, 500000012, 500000013]
    print('--------pprVect--------')
    print(_get_movie_ranks(ppagerankVectorArray, movie_ids))
    print(_get_movie_ranks(ppagerankVectorArray, similars))
    print('-------pprGraph---------')
    print(_get_movie_ranks(ppagerankGraphArray, movie_ids))
    print(_get_movie_ranks(ppagerankGraphArray, similars))
    print('---------adjVect-------')
    print(_get_movie_ranks(adjacencyVectorArray, movie_ids))
    print(_get_movie_ranks(adjacencyVectorArray, similars))
    print('--------adjGraph--------')
    print(_get_movie_ranks(adjacencyGraphArray, movie_ids))
    print(_get_movie_ranks(adjacencyGraphArray, similars))



    print('\n \n \n Star Trek')
    movie_ids = [116, 118, 121,132, 136,138, 154, 160, 161,162]
    similars = [500000348, 100015824, 500000349]
    movie_ids = [200000000 + id for id in movie_ids ]
    print('--------pprVect--------')
    print(_get_movie_ranks(ppagerankVectorArray, movie_ids))
    print(_get_movie_ranks(ppagerankVectorArray, similars))
    print('-------pprGraph---------')
    print(_get_movie_ranks(ppagerankGraphArray, movie_ids))
    print(_get_movie_ranks(ppagerankGraphArray, similars))
    print('---------adjVect-------')
    print(_get_movie_ranks(adjacencyVectorArray, movie_ids))
    print(_get_movie_ranks(adjacencyVectorArray, similars))
    print('--------adjGraph--------')
    print(_get_movie_ranks(adjacencyGraphArray, movie_ids))
    print(_get_movie_ranks(adjacencyGraphArray, similars))

