import numpy as np
import tsplib95

problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/berlin52/berlin52.tsp')
mutation_rate = 0.2
dimension = problem.dimension
populations_number = 1000

def firstPopulation(lista, populations_number):
    set = []
    for i in range(populations_number):
        list_i = lista[np.random.shuffle(list(problem.get_nodes), dimension, replace = False)]
        set.append(list_i)
    return np.array(set)

set = firstPopulation(problem.get_nodes, populations_number)
set


def getFitnes(set, problem):
    fitnes_list = np.zeros(populations_number)
    for i in range(populations_number):
        fitnes_list.append(problem.trace_tours([set[i]])[0])
    return fitnes_list

fitnes_list = getFitnes(set, problem)
fitnes_list

def selection(set, fitnes_list):
    total_fitnes = fitnes_list.sum()
    prob_list = fitnes_list/total_fitnes

    a = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)
    b = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)

    a = set[a]
    b = set[b]

    return np.array([a,b])

progenitor_list = selection(set, fitnes_list)
progenitor_list

def createOffspring(p1, p2):
    offspring = p1[0:5]

    for node in p2:
        if not node in offspring:
            offspring = np.concatenate(offspring, [node])
    return offspring

def createPopulationSet(progenitor_list):
    new_set = []
    for i in range(progenitor_list.shape[1]):
        p1, p2 = progenitor_list[0][i], progenitor_list[1][i]
        offspring = createOffspring(p1, p2)
        new_set.append(offspring)
    return new_set

new_set = createPopulationSet(progenitor_list)
new_set

def mutateOffspring(offspring):
    for i in range(int(dimension*mutation_rate)):
        x = np.random.randint(0, dimension)
        y = np.random.randint(0, dimension)

        offspring[x], offspring[y] = offspring[y], offspring[x]
    return offspring

def mutatePopulation(new_set):
    mutated = []
    for offspring in new_set:
        mutated.append(mutateOffspring(offspring))
    return mutated

mutated = mutatePopulation(new_set)
mutated

if __name__ == '__main__':
    best = [-1, np.inf, np.array([])]
    for k in range(100000):
        if k%100 == 0:
            print(k, fitnes_list.min(), fitnes_list.mean())
            fitnes_list = getFitnes(mutated,problem)

        if fitnes_list.min() < best[1]:
            best[0] = k
            best[1] = fitnes_list.min()
            best[2] = np.array(mutated)[fitnes_list.min() == fitnes_list]

        progenitor_list = selection(set, fitnes_list)
        new_set = createPopulationSet(progenitor_list)
        mutated = mutatePopulation(new_set)

    print(best)


"""
Tu coś nie zadziałało z funkcjami, więc podejście numer 2

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
    return fitnes_list

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
    
"""