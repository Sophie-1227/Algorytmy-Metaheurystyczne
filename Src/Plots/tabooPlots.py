from matplotlib import pyplot as plt

from Src.tabuSearch import TabooSearch, two_opt, problem, NNAPath, tabuInvert, solution

taboo = TabooSearch()
startSolution, endCost = two_opt(problem, NNAPath)

def listLengthPlot():
    xpoints = []
    ypoints = []
    for i in range(1,11,2):
        ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution, endCost=endCost, problem = problem, k=i, maxTime=10)[1])
        xpoints.append(i)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Taboo list len (times dimension)')
    plt.ylabel('Tour length')
    plt.title('Result vs taboo list length')
    plt.show()

def timeVsResult(maxTimeIteration):
    xpoints = []
    ypoints = []

    ypoints.append(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution,endCost=endCost, problem = problem, k=3, maxTime=maxTimeIteration)[1])
    temp = taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution,endCost=endCost, problem = problem, k=3, maxTime=maxTimeIteration)[0]
    sum = maxTimeIteration
    xpoints.append(sum)

    for i in range(10):
        ypoints.append(taboo.basicSearch(neighbourFunction=tabuInvert,starting=temp, endCost=ypoints[-1], problem=problem, k=3, maxTime=maxTimeIteration)[1])
        temp = taboo.basicSearch(neighbourFunction = tabuInvert, starting = temp, endCost=ypoints[-2], problem = problem, k=3, maxTime=maxTimeIteration)[0]
        sum += maxTimeIteration
        xpoints.append(sum)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time')
    plt.ylabel('Tour length')
    plt.title('Results in time')
    plt.show()

if __name__ == '__main__':
    listLengthPlot()
    timeVsResult(maxTimeIteration=15)


def avarageListLength():
    sucess = 0
    totalIterations = 100
    for i in range(10):
        for j in range(10):
            startSolution, endCost = two_opt(problem, NNAPath)
            temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=startSolution, endCost=endCost, problem=problem, k=i, maxTime=10)[1]
            if temp<startSolution:
                sucess += j
            elif startSolution == problem.trace_tours(solution.tours)[0]:
                totalIterations =-1

    avarageLength = sucess//totalIterations
    print(avarageLength)