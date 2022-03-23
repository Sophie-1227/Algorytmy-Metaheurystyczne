import numpy as np

#lepsza metoda tego na dole
def krandom(problem, k):
    if k < 1:
        return
    #np.inf --> nieskonczonosc
    cost = np.inf
    tour = []
    for _ in range(k):
        curTour = list(problem.get_nodes())
        np.random.shuffle(curTour)
        curCost = problem.trace_tours([curTour])[0]
        if cost > curCost:
            cost = curCost
            tour = curTour
    problem.tours.append(tour)
    print(tour)
    print(cost)


"""
#implementacja algorytmu k-random
def k_method_solve(problem, k):

    #k - ilosc losowan (prob)

    current = 8397420470283740084749
    for i in range(k):
        temporary = random_solve(problem)
        if current > evaluate(problem):
            current = evaluate(problem)
            k_table = temporary
    print(k_table)
    # TODO ogarnac zapis do tablicy i wypisywanie
"""