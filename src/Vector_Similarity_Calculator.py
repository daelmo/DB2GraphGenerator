import numpy as np
import pandas as pd

class Vector_Similarity_Calculator:

    def __init__(self):
        temp = np.fromfile('data/3_vectors/test.bin', dtype=np.dtype(np.float32))
        self.vectors = pd.DataFrame(np.split(temp, 128))
        print(self.vectors.shape)
        print(self.vectors)

    def calc_vector_similarity(vector1, vector2):
        return 0
