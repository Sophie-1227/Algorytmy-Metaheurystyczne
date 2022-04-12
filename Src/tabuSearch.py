import tsplib95
import time

import numpy as np

from Src.Algorythms.NN_Algorythm import NNA


def invert(array, i, j):
    length = j-i+1
    temp = []

    for k in range (0,length):
        temp.append(array[k+i-1])

    for k in range (0, length):
        array[i+k-1] = temp[length-k-1]

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

    """
    while time.time() - time_start < 30:
    """

def update(self, last_solution: np.array, last_cost: int):
    last_solution = last_solution
    last_cost = last_cost

def basicSearch(neighboring_function, starting_solution: np.array):
    time_start = time.time()
    NNA_Path, NNA_Cost = NNA(problem, 0)
    startingSolution = two_opt(problem, NNA_Path)[1]
    #
    bestSolution = startingSolution
    bestCost = data.cost(startingSolution)

    solution = bestSolution.copy()
    tabooList = deque([], 20)
    tabooList.append(solution)
    while time.time() - time_start < 30:
        neighboring_best_solution = np.array([])
        neighboring_best_cost = np.inf
        for neighboring_solution in neighboring_function(solution):
            neighboring_cost = self.data.cost(neighboring_solution)
            (taboo_list == neighboring_solution).any()
            if neighboring_cost < neighboring_best_cost and (taboo_list == neighboring_solution).any():
                neighboring_best_solution = neighboring_solution
                neighboring_best_cost = neighboring_cost
            solution = neighboring_best_solution
            cost = neighboring_best_cost
            taboo_list.append(solution)

                if cost < best_cost:
                    best_cost = cost
                    best_solution = solution

            self.__update(best_solution, best_cost)
            return best_cost

        def search(self, neighboring_function, starting_solution):
            return self.__basic_search(neighboring_function=neighboring_function, starting_solution=starting_solution)



if __name__ == '__main__':
    problem = tsplib95.load('../Data/bays29/bays29.tsp')
    print (two_opt(problem))