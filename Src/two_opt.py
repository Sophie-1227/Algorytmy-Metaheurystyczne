#from py2opt.routefinder import RouteFinder

def invert(*array: int, i: int, j: int):
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

                if endList.random_solve()<tempList.random_solve():
                    tempList = endList.copy()
        if curList.random_solve() == tempList.random_solve():
            return curList
        curList = tempList.copy()
