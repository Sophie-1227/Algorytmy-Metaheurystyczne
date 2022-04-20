from collections import deque
from urllib.request import DataHandler

import self as self
import tsplib95
import time

import numpy as np

from Src.Algorythms.NN_Algorythm import NNA
from Src.utils import evaluate

def invert_m(solution: np.array) -> np.array:
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = np.concatenate((solution[:i], solution[i:j + 1][::-1], solution[j + 1:]))
            yield neighbour

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
        cost += problem.get_weight((tour[i], tour[i + 1]))
    cost += problem.get_weight((tour[-1], tour[0]))
    return cost

class TabooSearch:

    def __init__(self):
        self.problem = tsplib95.load('../Data/bays29/bays29.tsp')



    def __update(self, last_solution: np.array, last_cost: int):
        self.last_solution = last_solution
        self.last_cost = last_cost

    def basicSearch(self, neighboring_function, starting_solution: np.array):
        time_start = time.time()
        NNA_Path, NNA_Cost = NNA(problem, 0)
        starting_solution, best_cost = two_opt(problem, NNA_Path)
        best_solution = starting_solution

        solution = best_solution.copy()
        taboo_list = deque([], 20) # <- struktura listy tabu - Kolejka?
        taboo_list.append(solution)
        while time.time() - time_start < 30: # <- Warunek stopu = czas
            neighboring_best_solution = np.array([])
            neighboring_best_cost = np.inf

            for neighboring_solution in neighboring_function(solution):
                if not any([x.all() for x in neighboring_solution == taboo_list]): # If neighboring solution is not in taboo list
                    if  get_cost(problem, neighboring_solution) < neighboring_best_cost:
                        neighboring_best_solution = neighboring_solution
                        neighboring_best_cost = get_cost(problem, neighboring_best_solution)

            solution = neighboring_best_solution
            cost = neighboring_best_cost
            taboo_list.append(solution)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        self.__update(best_solution, best_cost)
        return best_cost

    pass

    def search(self, neighboring_function, starting_solution):
        return self.__basic_search(neighboring_function=neighboring_function, starting_solution=starting_solution)




if __name__ == '__main__':
    problem = tsplib95.load('../Data/bays29/bays29.tsp')
    #print (two_opt(problem))
    NNAPath, NNACost = NNA(problem, 0)
    startSolution, bestCost = two_opt(problem, NNAPath)
    taboo = TabooSearch()
    print(taboo.basicSearch(neighboring_function = invert_m, starting_solution = startSolution))