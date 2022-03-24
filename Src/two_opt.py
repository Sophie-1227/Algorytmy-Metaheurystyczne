#from py2opt.routefinder import RouteFinder

def invert(*array, i, j):
    length = j-i+1
    temp = [length]

    for k in range (1,length):
        temp[k] = array[k+i]

    for k in range (1, length):
        array[i+k] = temp[length-k]


def two_opt(problem):
    dimension = problem.dimension
    point = list(range(1,dimension+1))
    curList = list(problem.get_nodes())
    tempList = curList.copy()
    endList = curList.copy()

    while True:
        for i in range(1, dimension):
            for j in range (1, i+1):
                endList = curList.copy()
                invert(endList, j, i)

                if problem.trace_tours([endList])[0]<problem.trace_tours([tempList])[0]:
                    tempList = endList.copy()
        if problem.trace_tours([curList])[0] == problem.trace_tours([tempList])[0]:
            return curList
        curList = tempList.copy()
