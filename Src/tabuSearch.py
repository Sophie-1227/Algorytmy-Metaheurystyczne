from collections import deque

import tsplib95
import time

import numpy as np

from Src.Algorythms.NN_Algorythm import NNA


def tabuInvert(solution: list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbours.append(solution[:i] + solution[i:j + 1][::-1] + solution[j + 1:])
    return neighbours

def tabuSwap(solution: list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(len(solution)):
            neighbours = solution.copy()
            temp = neighbours[i]
            neighbours[i] = neighbours[j]
            neighbours[j] = temp
    return neighbours

def invert(array, i, j):
    length = j - i + 1
    temp = []

    for k in range(0, length):
        temp.append(array[k + i - 1])

    for k in range(0, length):
        array[i + k - 1] = temp[length - k - 1]

def two_opt(problem, curList = None):
    if curList == None:
        curList = list(problem.get_nodes())

    dimension = problem.dimension
    #curList = list(problem.get_nodes())
    np.random.shuffle(curList)
    tempList = curList.copy()

    while True:
        for i in range(1, dimension+1):
            for j in range (1, i+1):
                endList = curList.copy()
                invert(endList, j, i)

                if problem.trace_tours([endList])[0]<problem.trace_tours([tempList])[0]:
                    tempList = endList.copy()
        if problem.trace_tours([curList])[0] == problem.trace_tours([tempList])[0]:
            return curList, problem.trace_tours([curList])[0]
        curList = tempList.copy()
    print(curList)
    print(problem.trace_tours([curList])[0])

def get_cost(problem: tsplib95.models.StandardProblem, tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += problem.get_weight(*(tour[i], tour[i + 1]))
    cost += problem.get_weight(*(tour[-1], tour[0]))
    return cost

class TabooSearch:

    def basicSearch(self, neighbourFunction, starting: np.array,problem, k):
        startTime = time.time()
        NNA_Path, NNA_Cost = NNA(problem, 0)
        starting, endCost = two_opt(problem, NNA_Path)
        endList = starting
        solution = endList.copy()
        lengthDeque = problem.dimension
        tabooList = deque([], k*lengthDeque) # <- struktura listy tabu deque
        tabooList.append(solution)
        while time.time() - startTime < 5: # <- Warunek stopu = czas
            neighborEndList = np.array([])
            neighborEndCost = np.inf

            for newNeighbor in (n for n  in neighbourFunction(solution) if n not in tabooList):
                    if  get_cost(problem, newNeighbor) < neighborEndCost:
                        neighborEndList = newNeighbor
                        neighborEndCost = get_cost(problem, neighborEndList)

            solution = neighborEndList
            cost = neighborEndCost
            tabooList.append(solution)

            if cost < endCost:
                endCost = cost
                endList = solution

        self.__update(endList, endCost)
        return endCost

    def __update(self, endTour: np.array, finalCost: int):
        self.endTour = endTour
        self.finalCost = finalCost

if __name__ == '__main__':
    problem = tsplib95.load('../Data/bays29/bays29.tsp')
    NNAPath, NNACost = NNA(problem, 0)
    startSolution, endCost = two_opt(problem, NNAPath)
    print(endCost)
    taboo = TabooSearch()
    for i in range (1,10,2):
        print(taboo.basicSearch(neighbourFunction = tabuInvert, starting = startSolution, problem = problem, k=i))