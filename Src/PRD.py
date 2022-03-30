import tsplib95

from Src.Algorythms.NN_Algorythm import NNA
from Src.Algorythms.NN_Algorythm_Ext import ENNA
from Src.Algorythms.krandom import krandom
from Src.Algorythms.two_opt import two_opt


def PRD_calc(problem):

    _,costKRandom = krandom(problem, 1000)
    _,costTwo_Opt = two_opt(problem)
    _,cost_NNA = NNA(problem)
    _,costNNA_Ext = ENNA(problem)
    solution = tsplib95.load_solution('../Data/bays29/bays29.opt.tour')
    opt = problem.trace_tours(solution.tours)[0]
    print(solution.tours)

    # procentowo
    print(PRD(costKRandom,opt))
    print(PRD(costTwo_Opt,opt))
    print(PRD(cost_NNA,opt))
    print(PRD(costNNA_Ext,opt))


def PRD(tour, opt):
    return 100 * (tour - opt) / opt