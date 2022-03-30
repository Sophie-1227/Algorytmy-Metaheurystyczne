import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from two_opt import two_opt
import matplotlib.pyplot as plt
from Src.NN_Algorythm import NNA
from Src.NN_Algorythm import NNA
from Src.krandom import krandom


#koszt od wielkosci instancji
def kRandomPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,1000):
        ypoints.append(krandom(problem, i)[1])
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Value of k')
    plt.ylabel('Tour length')
    plt.title('K-random method plot')
    plt.show()


# w zaleznosci od wierzcholka poczatkowego sa rozne drogi
def NN_AlgorythmPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,len(list(problem.get_nodes()))+1):
        ypoints.append(NNA(problem,i)[1])
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Starting point')
    plt.ylabel('Cost')
    plt.title('Nearest Neighbour plot')
    plt.show()


# droga rozwiazana przez two_opt
def twoOptTourPlot(problem):
    c_list, cost = two_opt(problem)
    plt.plot([problem.get_display(c_list[i%len(c_list)])[0] for i in range(len(c_list)+1)],
             [problem.get_display(c_list[i%len(c_list)])[1] for i in range(len(c_list)+1)])
    plt.show()


# rozne wierzcholki startowe
def NNAPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,30):
        starting, length  = NNA(problem, i)
        xpoints.append(i)
        ypoints.append(length)

    plt.plot(xpoints, ypoints, 'o')
    plt.xlabel('Starting point')
    plt.ylabel('Tour length')
    plt.title('NN-method plot')
    plt.show()
