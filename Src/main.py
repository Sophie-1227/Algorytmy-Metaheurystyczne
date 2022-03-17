import numpy as np
import tsplib95

def sum(problem):
    res = []
    for tour in problem.tours:
        cost = 0
        for i in range(0, len(tour)-1):
            cost += problem.get_weight(tour[i], tour[i+1])
        cost += problem.get_weight(tour[-1],tour[0])
        res.append(cost)
    return res


def random_solve(problem):
    nodes = np.array(list(problem.get_nodes()))  # lista od 1 do ilosci wierzcholkow
    np.random.shuffle(nodes[1:-1])  # shufflowanie
    problem.tours.append(nodes.tolist())
    print(problem.tours)

if __name__ == '__main__':
    #zapisuje caly obiekt
    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    #wypisanie macierzy
    print(problem.edge_weights)

    #wypisywanie permutacji drogi
    random_solve(problem)

    #wypisywanie funkcji celu
    #ogarnac czy trace_tours zadziala

    #problem.trace_tours([tour])[0]

    #sum problem powinno dzialac ale nie wiem czy dziala xD
    #sum(problem)