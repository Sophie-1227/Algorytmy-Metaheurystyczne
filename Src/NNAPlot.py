import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.NNA import NNA
from Src.NN_Algorythm import NN_algo

# dlugosc trasy w zaleznosci od punktu startowego z wykorzystaniem NN Alg
def ploting(problem):
    xpoints = []
    ypoints = []
    for i in range(1,30):
        starting, length  = NNA(problem, i)
        xpoints.append(i)
        ypoints.append(length)

    plt.plot(xpoints, ypoints, 'o')
    plt.xlabel('Tour length')
    plt.ylabel('Starting point')
    plt.title('NN-method plot')
    plt.show()