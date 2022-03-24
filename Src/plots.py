import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.krandom import krandom


def ploting(problem):
    xpoints = []
    ypoints = []
    for i in range(1,10000, 100):
        xpoints.append(krandom(problem, i))
        ypoints.append(i)

    plt.plot(ypoints, xpoints)
    plt.show()