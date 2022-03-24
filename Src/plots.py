import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from Src.krandom import krandom


def ploting(problem):
    xpoints = []
    ypoints = []
    for i in range(1,100000):
        xpoints[i] = krandom(problem, i)
        ypoints[i] = i

    plt.plot(xpoints, ypoints)
    plt.show()