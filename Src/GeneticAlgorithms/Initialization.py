import numpy as np

replace = False
def genesis(problem, n_population):

    population_set = []
    #problemLength = problem.dimension
    for i in range(n_population):
        #getting a random first solution
        cur = np.random.shuffle(list(problem.get_nodes()))
        replace = False
        sol_i = [cur, problem.get_nodes, replace]
        population_set.append(sol_i)
    return np.array(population_set)

def getFitnes(population_set, problem, n_population):
    fitnes_list = np.zeros(problem.dimension)
    for i in range(n_population):
        fitnes_list.append(problem.trace_tours([population_set[i]])[0])

def selection(population_set, fitnes_list):
    total_fitnes = fitnes_list.sum()

    a = np.random.choice(list(len(population_set))), len(population_set)
    b = np.random.choice(list(len(population_set))), len(population_set)

