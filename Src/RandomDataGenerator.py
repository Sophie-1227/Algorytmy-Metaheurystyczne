import os
import shutil
import sys

import tsplib95.models
import numpy as np


class RandomDataGenerator:
    DATASET_DIR_NAME = "RandomDataset"

    def __init__(self):
        pass

    def createDir(self):
        if self.DATASET_DIR_NAME not in os.listdir((os.getcwd())):
            os.mkdir(self.DATASET_DIR_NAME)

    def removeDir(self):
        if self.DATASET_DIR_NAME in os.listdir(os.getcwd()):
            shutil.rmtree(self.DATASET_DIR_NAME)

    def createRandomDataset(self, name, matrix: list, fileType=".tsp"):
        self.createDir()
        dimension = len(matrix)
        datasetName = f"{name}{dimension}"
        if datasetName in os.listdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME)):
            sys.exit(f"{datasetName} file already exists, please try again")
        os.mkdir(os.path.join(os.getcwd(), self.DATASET_DIR_NAME, datasetName))

        problem = tsplib95.models.StandardProblem.parse("")
        problem.dimension = dimension
        problem.name = datasetName
        problem.type = "TSP"
        problem.comment = f"{dimension} nodes generated to conduct algorithm efficiency"
        problem.edge_weight_type = "EXPLICIT"
        problem.edge_weight_format = "FULL MATRIX"
        problem.display_data_type = "TWOD_DISPLAY"
        problem.edge_weights = matrix
        path = os.path.join(os.getcwd(), self.DATASET_DIR_NAME, datasetName, f"{datasetName}{fileType}")
        problem.save(path)
        with open(path, 'a') as file:
            file.write("\n")

    def symmetricMatrix(self, name: str, dimension: int, maxValue=10000):
        matrix = np.random.randint(0, maxValue, (dimension, dimension))
        for i in range(dimension):
            matrix[i][i] = 0 #"zerujemy" nasz matrix, ale jednocześnie deklarujemy go, aby uniknąć błędów o niepoprawnym odwałaniu do elementu
        for r in range(dimension): #rows
            for c in range(dimension): #columns
                matrix[c][r] = matrix[r][c] #symetryczność
        self.createRandomDataset(name, list(matrix))

    def asymmetricMatrix(self, name: str, dimension: int, maxValue=10000):
        matrix = np.random.randint(0, maxValue, (dimension, dimension))
        for i in range(dimension):
            matrix[i][i] = 0
        self.createRandomDataset(name, list(matrix), ".atsp")

