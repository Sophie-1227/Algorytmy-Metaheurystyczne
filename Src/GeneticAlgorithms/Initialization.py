import numpy as np
import tsplib95
import statistics

from Src.Algorythms.two_opt import two_opt

problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.tsp')
mutation_rate = 0.3
dimension = problem.dimension
populations_number = 100

def firstPopulation(lista, populations_number):
    set = []
    for i in range(populations_number):
        #lista = list(lista)
        lista = two_opt(problem)[0]
        #np.random.shuffle(lista)
        set.append(lista)
    return np.array(set)


def getFitnes(set, problem):
    fitnes_list = []
    for i in set:
        c = list(i)
        x = problem.trace_tours([c])
        fitnes_list.append(x)
    return fitnes_list

def selection(set, fitnes_list):
    prob_list = []

    total_fitnes = sum(fitnes_list)
    for i in fitnes_list:
        n = i/total_fitnes
        prob_list.append(n)

    a = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)
    b = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace = True)

    a = set[a]
    b = set[b]

    return np.array([a,b])
# lista przodkow


def createOffspring(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    offspring = p1[0:5]
    for node in p2:
        if not node in offspring:
            offspring.append(node)
            #offspring = np.concatenate(offspring, [node])
    return offspring

def createPopulationSet(progenitor_list):
    new_set = []
    for i in range(progenitor_list.shape[1]):
        p1, p2 = progenitor_list[0][i], progenitor_list[1][i]
        offspring = createOffspring(p1, p2)
        new_set.append(offspring)
    return new_set



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


if __name__ == '__main__':

    best = np.inf
    # ilosc instancji
    for k in range(1000):
        set = firstPopulation(problem.get_nodes(), populations_number)
        fitnes_list = getFitnes(set, problem)
        fitnes_list = sum(fitnes_list,[])
        progenitor_list = selection(set, fitnes_list)
        new_set = createPopulationSet(progenitor_list)
        mutated = mutatePopulation(new_set)
        # sprawdzenie najlepszego ze 100 wykonan
        if k%100 == 0 and k != 0:
            print(k, min(fitnes_list), statistics.mean(fitnes_list))
            fitnes_list = getFitnes(mutated,problem)
            fitnes_list = sum(fitnes_list, [])

        if min(fitnes_list) < best:
            best = min(fitnes_list)

        # tworzy nowy set danych
    progenitor_list = selection(set, fitnes_list)
    new_set = createPopulationSet(progenitor_list)
    mutated = mutatePopulation(new_set)

    print(best)