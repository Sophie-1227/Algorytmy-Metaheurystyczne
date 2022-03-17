import tsplib95
from Src.main import random_solve, evaluate

#implementacja algorytmu k-random
def k_method_solve():

    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    #k - ilosc losowan (prob)
    k = 1000
    current = 8397420470283740084749
    for i in range (k):
        temporary = random_solve(problem)
        if current > evaluate(problem):
            current = evaluate(problem)
            k_table = temporary
    print(k_table)
    # TODO ogarnac zapis do tablicy i wypisywanie