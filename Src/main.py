import numpy as np
import tsplib95

from Src.NNAPlot import NNAPlot
from Src.PRD import PRD_calc
from Src.dataPlots import NN_AlgorythmPlot, twoOptTourPlot
from Src.timePlots import kRandomTimePlot, two_optTimePlot
from Src.two_opt_GRD import two_opt_GRD
from Src.utils import random_solve

if __name__ == '__main__':

    #wczytuje i zapisuje caly obiekt
    problem = tsplib95.load('../Data/bays29/bays29.tsp')

    """--- PLOTS ---"""
    twoOptTourPlot(problem)
    NNAPlot(problem)
    kRandomTimePlot(problem)
    two_optTimePlot(problem)
    NN_AlgorythmPlot(problem)
    two_optTimePlot(problem)

    PRD_calc(problem)
    two_opt_GRD(problem)