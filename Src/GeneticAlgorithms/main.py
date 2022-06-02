import numpy as np
import tsplib95

if __name__ == '__main__':
    problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.tsp')
    set = problem.get_nodes()
    print(list(set))
    problem.trace_tours()