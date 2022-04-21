from matplotlib import pyplot as plt

from Src.tabuSearch import TabooSearch, tabuInvert, startSolution, problem

taboo = TabooSearch()

def listLengthPlot():
    xpoints = []
    ypoints = []
    for i in range(1,11,2):
        ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution, problem = problem, k=i, maxTime=10))
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Taboo list len (times dimension)')
    plt.ylabel('Tour length')
    plt.title('Result vs taboo list length')
    plt.show()

def timeVsResult(maxTimeIteration):
    xpoints = []
    ypoints = []

    ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution, problem = problem, k=3, maxTime=maxTimeIteration))
    sum = maxTimeIteration
    xpoints.append(sum)

    for i in range(10):
        ypoints.append(taboo.basicSearch(neighbourFunction=tabuInvert, starting=ypoints[-1], problem=problem, k=3, maxTime=maxTimeIteration))
        sum += maxTimeIteration
        xpoints.append(sum)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time')
    plt.ylabel('Tour length')
    plt.title('Results in time')
    plt.show()
