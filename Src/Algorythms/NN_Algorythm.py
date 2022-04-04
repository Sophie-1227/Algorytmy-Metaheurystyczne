import random as rand
import numpy as np

def NNA(problem, k):
    dimension = problem.dimension

    if k==0 :
        starting = rand.randint(1, dimension)
    else:
        starting = k



    endList = []
    avaibleList = list(problem.get_nodes())
    previouPoint = starting
    endList.append(starting)
    avaibleList.remove(starting)

    while len(avaibleList) != 0:
        bestCost = np.inf #przypisujemy infnum do długości trasy, żeby mieć pewność, że każda z podanych jest od niej mniejsza
        for i in avaibleList:
            curCost = problem.get_weight(*(endList[-1], i))

            if bestCost > curCost:
                bestCost = curCost
                previouPoint = i

        avaibleList.remove(previouPoint)
        endList.append(previouPoint)

    problem.tours.append(endList)
    return endList, problem.trace_tours([endList])[0]