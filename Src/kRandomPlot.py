import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.krandom import krandom


def kRandomPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,1000):
        ypoints.append(krandom(problem, i))
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Value of k')
    plt.ylabel('Tour length')
    plt.title('K-random method plot')
    plt.show()