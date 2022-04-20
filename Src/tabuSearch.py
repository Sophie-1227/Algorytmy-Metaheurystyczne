from collections import deque

import self as self
import tsplib95
import time

import numpy as np

from Src.Algorythms.NN_Algorythm import NNA


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

class TabooSearch:

    def update(self, lastSolution: np.array, lastCost: int):
        lastSolution = lastSolution
        lastCost = lastCost

    def basicSearch(self, neighborFunction, startSolution: np.array):
        startTime = time.time()
        NNAPath, NNACost = NNA(problem, 0)
        startSolution = two_opt(problem, NNAPath)[1]

        bestSolution = startSolution
        bestCost = problem.cost(startSolution)

        solution = bestSolution.copy()
        tabooList = deque([], 20)
        tabooList.append(solution)
        while time.time() - startTime < 30:
            neighborBestSolution = np.array([])
            neighborBestCost = np.inf
            for neighborSolution in neighborFunction(solution):
                neighborCost = self.data.cost(neighborSolution)
                (tabooList == neighborSolution).any()
                if neighborCost < neighborBestCost and (tabooList == neighborSolution).any():
                    neighborBestSolution = neighborSolution
                    neighborBestCost = neighborCost
                solution = neighborBestSolution
                cost = neighborBestCost
                tabooList.append(solution)

                if cost < bestCost:
                    bestCost = cost
                    bestSolution = solution

                self.__update(bestSolution, bestCost)
                return bestCost

            def search(self, neighborFunction, startSolution):
                return self.__basic_search(neighborFunction=neighborFunction, startSolution=startSolution)



if __name__ == '__main__':
    problem = tsplib95.load('../Data/bays29/bays29.tsp')
    #print (two_opt(problem))
    taboo = TabooSearch(self)
    print(taboo.basicSearch(self, neighborFunction=None, startSolution=None))