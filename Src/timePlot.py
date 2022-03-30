import matplotlib.pyplot as plt
from datetime import datetime

from Src.krandom import krandom
from Src.two_opt import two_opt


def kRandomTimePlot(problem):

    xpoints = []
    ypoints = []
    for i in range(1, 1000):
        startTime = datetime.now()
        ypoints.append(krandom(problem, i))
        xpoints.append((datetime.now() - startTime).microseconds)
        #print(ypoints)

    plt.plot(xpoints, ypoints,'o')
    plt.xlabel('Time of execusion [microseconds]')
    plt.ylabel('Tour length')
    plt.title('Execution time')
    plt.show()

def two_optTimePlote(problem):

    xpoints = []
    ypoints = []
    for i in range(1, 10):
        startTime = datetime.now()
        ypoints.append(two_opt(problem))
        xpoints.append((datetime.now() - startTime).microseconds)
        #print(ypoints)

    plt.plot(xpoints, ypoints,'o')
    plt.xlabel('Time of execusion [microseconds]')
    plt.ylabel('Tour length')
    plt.title('Execution time')
    plt.show()

"""
def everyAlgPlot(problem)

    startTime = datetime.now()
    tour, starting = NNA(problem, 0)
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
"""