import tsplib95

if __name__ == '__main__':
    problem = tsplib95.load('../Data/bays29/bays29.tsp')
    opt = tsplib95.load('../Data/bays29/bays29.opt.tour')

    #problem.tours = opt.tours
    print(problem)
    #print(opt.tours)
    #print(problem.trace_tours(problem.tours))
