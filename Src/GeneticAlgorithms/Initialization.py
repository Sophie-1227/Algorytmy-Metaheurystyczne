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

    a = np.random.choice(list(range(len(population_set))), len(population_set), replace = True)
    b = np.random.choice(list(range(len(population_set))), len(population_set), replace = True)

    a = population_set[a]
    b = population_set[b]

    return np.array([a,b])

def pairsCrossover(a, b):
    offspring = a[0:5]
    for node in b:
        if not node in offspring:
            offspring = np.concatenate(offspring,[node])
    return offspring

def matePairs(progenitor_list):
    new_set = []
    for i in range(progenitor_list.shape[1]):
        a, b = progenitor_list[0][i], progenitor_list[1][i]
        offspring = pairsCrossover(a, b)
        new_set.append(offspring)
    return new_set

def mutateOffspring(offspring, problem):
    for i in range(int((problem.get_nodes)*mutation_rate)):
        a = np.random.randint(0, problem.get_nodes)
        b = np.random.randint(0, problem.get_nodes)

        offspring[a], offspring[b] = offspring[b], offspring[a]
    return offspring

def mutatePopulation(new_set, problem):
    mutated = []
    for ofspring in new_set:
        mutated.append(mutateOffspring(ofspring, problem))
    return mutated