import numpy as np
import tsplib95
import statistics

problem = tsplib95.load('/Users/grelewski/PycharmProjects/Metaheurystyka1/Data/bays29/bays29.tsp')
mutation_rate = 0.7
dimension = problem.dimension
populations_number = 100


def firstPopulation(lista, populations_number):
    set = []
    for i in range(populations_number):
        lista = list(lista)
        # lista = two_opt(problem)[0]
        np.random.shuffle(lista)
        set.append(lista)
    return set


def getFitnes(set, problem):
    fitnes_list = []
    for i in set:
        c = i[:]
        x = problem.trace_tours([c])
        fitnes_list.append(x)
    return fitnes_list


def selection(set, fitnes_list):
    prob_list = []

    total_fitnes = sum(fitnes_list)
    for i in fitnes_list:
        n = i / total_fitnes
        prob_list.append(n)

    a = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace=True)
    b = np.random.choice(list(range(len(set))), len(set), p=prob_list, replace=True)

    off_a = []
    for k in a:
        off_a.append(set[k])
    off_b = []
    for k in b:
        off_b.append(set[k])

    return off_a, off_b


# lista przodkow


def createOffspring(p1, p2):
    piv1 = np.random.randint(0, len(p1))
    piv2 = np.random.randint(0, len(p1))
    if piv1 > piv2:
        piv1, piv2 = piv2, piv1
    offspring = [0 for _ in range(len(p1))]
    used = [False for _ in range(len(p1))]
    for i in range(piv1, piv2):
        offspring[i] = p1[i]
        used[p1[i]-1] = True
    k = 0
    for i in range(0, piv1):
        while used[p2[k]-1]:
            k += 1
        offspring[i] = p2[k]
        used[p2[k]-1] = True
    for i in range(piv2, len(p1)):
        while used[p2[k]-1]:
            k += 1
        offspring[i] = p2[k]
        used[p2[k] - 1] = True
    return offspring


def createPopulationSet(a, b):
    new_set = []
    for i in range(len(a)):
        offspring = createOffspring(a[i], b[i])
        new_set.append(offspring)
    return new_set



def mutateOffspring(offspring):
    for _ in range(np.random.randint(1, 10)):
        x = np.random.randint(0, dimension)
        y = np.random.randint(0, dimension)

        offspring[x], offspring[y] = offspring[y], offspring[x]
    return offspring


def mutatePopulation(new_set):
    mutated = []
    for offspring in new_set:
        if np.random.random() < mutation_rate:
            mutated.append(mutateOffspring(offspring))
        else:
            mutated.append(offspring)
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
