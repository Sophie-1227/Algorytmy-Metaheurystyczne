import matplotlib.pyplot as plt
import time

from Src.Algorythms.krandom import krandom
from Src.Algorythms.two_opt import two_opt


def kRandomTimePlot(problem):

    xpoints = []
    ypoints = []
    for i in range(1, 10):
        startTime = time.time_ns()
        krandom(problem, i)
        totalTime = (time.time_ns() - startTime)
        ypoints.append(totalTime)
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time of execusion [microseconds]')
    plt.ylabel('Tour length')
    plt.title('k-random Execution time')
    plt.show()

def two_optTimePlot(problem):

    xpoints = []
    ypoints = []
    for i in range(1, 10):
        startTime = time.time_ns()
        two_opt(problem)
        totalTime = (time.time_ns() - startTime)
        ypoints.append(totalTime)
        xpoints.append(i)
        #print(ypoints)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time of execusion [microseconds]')
    plt.ylabel('Tour length')
    plt.title('2 OPT Execution time')
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