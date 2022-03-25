import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.NN_Algorythm import NN_algo


def ploting(problem):
    xpoints = []
    ypoints = []
    for i in range(1,30):
        length, starting = NN_algo()
        xpoints.append(starting)
        ypoints.append(length)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Tour length')
    plt.ylabel('Starting point')
    plt.title('NN-method plot')
    plt.show()