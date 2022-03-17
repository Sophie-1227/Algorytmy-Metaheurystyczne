import tsplib95
from Src.main import random_solve, evaluate


def k_method_solve():

    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    k = 10
    current = 8397420470283740084749
    k_table = []
    for i in range (k):
        integer = random_solve(problem)
        if current > evaluate(problem):
            current = evaluate(problem)
            k_table = integer
    print(current)
    print(k_table)