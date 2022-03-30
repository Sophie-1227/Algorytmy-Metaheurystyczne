#NEW VERSION OF EXTENTED NNA, I HAVE NO IDEA WHEATER ITS LEAGAL OR NOT
from Src.NN_Algorythm import NNA
import numpy as np


def ENNA(problem):
    bestDistance = np.inf
    for i in list(problem.get_nodes()):
        curTour, curDistance = NNA(problem, i)
        if curDistance < bestDistance:
            bestDistance = curDistance
            bestTour = curTour.copy()

    print(bestTour, bestDistance)