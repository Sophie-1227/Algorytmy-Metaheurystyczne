import matplotlib.pyplot as plt
from two_opt import two_opt


def twoOptTourPlot(problem):
    c_list, cost = two_opt(problem)
    plt.plot([problem.get_display(c_list[i%len(c_list)])[0] for i in range(len(c_list)+1)],
             [problem.get_display(c_list[i%len(c_list)])[1] for i in range(len(c_list)+1)])
    plt.show()
