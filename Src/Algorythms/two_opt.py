import numpy as np

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
    point = list(range(1,dimension+1))
    #curList = list(problem.get_nodes())
    #np.random.shuffle(curList)
    tempList = curList.copy()
    endList = curList.copy()

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
    #print(curList)
    #print(problem.trace_tours([curList])[0])