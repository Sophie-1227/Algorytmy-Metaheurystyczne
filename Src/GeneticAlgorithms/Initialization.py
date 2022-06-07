import numpy as np
import tsplib95

problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/berlin52/berlin52.tsp')
mutation_rate = 0.2
dimension = problem.dimension
populations_number = 1000

def firstPopulation(lista, populations_number):
    set = []
    for i in range(populations_number):
        lista = list(lista)
        np.random.shuffle(list(lista))
        set.append(lista)

    return np.array(set)

set = firstPopulation(problem.get_nodes(), populations_number)


def getFitnes(set, problem):
    fitnes_list = []
    for i in set:
        c = list(i)

        print(c)
        x = problem.trace_tours([c])
        fitnes_list.append(x)
    return fitnes_list

fitnes_list = getFitnes(set, problem)
fitnes_list

def selection(set, fitnes_list):
    total_fitnes = sum(fitnes_list)
    prob_list = fitnes_list/total_fitnes

    a = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)
    b = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)

    a = set[a]
    b = set[b]


    return np.array([a,b])
# lista przodkow
progenitor_list = selection(set, fitnes_list)

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