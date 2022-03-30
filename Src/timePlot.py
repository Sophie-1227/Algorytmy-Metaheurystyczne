import matplotlib.pyplot as plt
from datetime import datetime
import networkx as nx
import numpy as np

from Src.krandom import krandom
from Src.NN_Algorythm import NN_algo
from Src.ExtendedNN_Algorythm import ENN_algo
from Src.two_opt import two_opt


def timePlot(problem):
    xpoints = []
    ypoints = []

    startTime = datetime.now()
    ypoints.append(krandom(problem, 10000))
    xpoints.append((datetime.now() - startTime).total.seconds())

    startTime = datetime.now()
    tour, starting = NN_algo(problem)
    ypoints.append(tour)
    xpoints.append((datetime.now() - startTime).total.seconds())

    startTime = datetime.now()
    tour, endList = ENN_algo(problem)
    ypoints.append(tour)
    xpoints.append((datetime.now() - startTime).total.seconds())

    startTime = datetime.now()
    endList, tour = two_opt(problem)
    ypoints.append(tour)
    xpoints.append((datetime.now() - startTime).total.seconds())

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time of execusion')
    plt.ylabel('Tour length')
    plt.title('Time comperision between methods')
    plt.show()
