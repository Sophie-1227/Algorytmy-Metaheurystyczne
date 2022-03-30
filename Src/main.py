import numpy as np
import tsplib95

from Src.ExtendedNN_Algorythm import ENN_algo
from Src.NNA import NNA
from Src.NNAPlot import ploting
from Src.NN_Algorythm import NN_algo
from Src.krandom import krandom
from Src.kRandomPlot import kRandomPlot
from Src.timePlot import kRandomTimePlot
from Src.two_opt import two_opt


def evaluate(problem):
    res = []
    for tour in problem.tours:
        cost = 0
        for i in range(0, len(tour)-1):
            cost += problem.get_weight(tour[i], tour[i+1])
        cost += problem.get_weight(tour[-1],tour[0])
        #res.append(cost)
    return cost

#tworzy permutacje trasy
def random_solve(problem):
    nodes = np.array(list(problem.get_nodes()))  #lista od 1 do ilosci wierzcholkow
    np.random.shuffle(nodes[1:-1])  #shufflowanie listy
    return nodes.tolist()
    #print(problem.tours)

if __name__ == '__main__':
    #zapisuje caly obiekt
    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    #wypisanie macierzy
    #print(problem.edge_weights)

    #wypisywanie permutacji drogi
    #tour = random_solve(problem)

    #wypisywanie funkcji celu (ZROBIC)
    #ogarnac czy trace_tours zadziala
    #podaje tablice sciezek
    #zwraca tablice kosztow
    #problem.trace_tours([tour])[0]

    #suma wszystkich wag
    #print(evaluate(problem))

    #k_method.k_method_solve(problem,1000)
    #krandom(problem, 1000)


    #NN_algo(problem, 0)

    #ENN_algo(problem)

    #print(two_opt(problem))

    #kRandomPlot(problem)
    #kRandomTimePlot(problem)

    #ploting(problem)

    NNA(problem, 0)
