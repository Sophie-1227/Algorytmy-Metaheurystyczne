import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.krandom import krandom


def kRandomPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,100000):
        ypoints.append( krandom(problem, i))
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Tour length')
    plt.ylabel('Value of k')
    plt.title('K-random method plot')
    plt.show()