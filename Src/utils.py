# metody napisane przed odkryciem innych metod z tsplib95, ktore je zastapily

import numpy as np

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