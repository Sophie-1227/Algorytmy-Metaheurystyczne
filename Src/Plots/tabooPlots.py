import tsplib95
import numpy as np
from matplotlib import pyplot as plt

from Src.Algorythms.NN_Algorythm import NNA
from Src.tabuSearch import TabooSearch, two_opt, tabuInvert
#plots for taboo search

def listLengthPlot():
    xpoints = []
    ypoints = []
    xpoints.append(0)
    ypoints.append(startSolution)
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
    xpoints.append(0)
    ypoints.append(startSolution)
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

def averageListLength():
    sucess = 0
    sucessIterations = 0
    defeat = 0
    defeatIteration = 0
    iRange = 2
    jRange = 3
    #totalIterations = jRange*iRange
    for i in range(1, iRange):
        for j in range(1, jRange):
            startSolution, endCost = two_opt(problem, NNAPath)
            #startSolution = list(problem.get_nodes())
            #np.random.shuffle(startSolution)
            #endCost = problem.trace_tours([startSolution])[0]
            temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=startSolution, endCost=endCost, problem=problem, k=i, maxTime=10)[1]
            if temp<endCost:
                sucess += i
                sucessIterations +=1
            elif endCost == problem.trace_tours(localSolution.tours)[0]:
                continue
            elif temp>=endCost:
                defeat += i
                defeatIteration +=1

    if sucessIterations == 0:
        avarageLength = iRange
    else:
        avarageLength = sucess/sucessIterations
    print("Średnia długość listy ze zmianą wyniku:")
    print(avarageLength)
    bestListLength = avarageLength

    if defeatIteration ==0:
        avarageLength = 0
    else:
        avarageLength = defeat/defeatIteration
    print("Średnia długość lisy bez zmiany wyniku:")
    print(avarageLength)

    return bestListLength

def optimizedListLength(bestListLength):
    xpoints = []
    ypoints = []
    y7points = []
    x7points = []
    y3points = []
    x3points = []
    suma = 0
    ypoints.append(startSolution)
    xpoints.append(0)
    y7points.append(startSolution)
    x7points.append(0)
    y3points.append(startSolution)
    x3points.append(0)
    temp = startSolution.copy()
    while ypoints[-1] != localSolution or suma>20:
        ypoints.append(taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=ypoints[-1], problem=problem, k=bestListLength, maxTime=10)[1])
        temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=ypoints[-2], problem=problem, k=bestListLength,
                          maxTime=10)[0]
        suma += 10
        xpoints.append(suma)

    suma = 0
    temp = startSolution.copy()
    while y7points != localSolution or suma>20:
        y7points.append(
            taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=y7points[-1], problem=problem,
                              k=(7/problemLength), maxTime=10)[1])
        temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=y7points[-2], problem=problem, k=(7/problemLength),
                                 maxTime=10)[0]
        suma += 10
        x7points.append(suma)

    temp = startSolution.copy()
    suma = 0
    while y7points != localSolution or suma>20:
        y7points.append(
            taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=y3points[-1], problem=problem,
                              k=3, maxTime=10)[1])
        temp = taboo.basicSearch(neighbourFunction=tabuInvert, starting=temp, endCost=y3points[-2], problem=problem,
                                 k=3, maxTime=10)[0]
        suma += 10
        x3points.append(suma)

    plt.plot(xpoints, ypoints, label="calculated avarage taboo list length")
    plt.plot(y7points, x7points, label="taboo list length = 7")
    plt.plot(y3points, x3points, label="taboo list length = 3n")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    taboo = TabooSearch()
    problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.tsp')
    localSolution = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.opt.tour')
    problemLength = problem.dimension
    NNAPath, NNACost = NNA(problem, 0)
    startSolution, endCost = two_opt(problem, NNAPath)
    #listLengthPlot()
    #timeVsResult(maxTimeIteration=15)
    temp = averageListLength()
    optimizedListLength(temp)
