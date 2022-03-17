from main import random_solve
import tsplib95

from main import random_solve
from main import sum


def k_method_solve():

    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    k = 1000
    current = 8397420470283740084749
    for i in range (k):
        integer = random_solve(problem)
        if current > sum(problem):
            current = sum(problem)
            table = integer

    print(table)