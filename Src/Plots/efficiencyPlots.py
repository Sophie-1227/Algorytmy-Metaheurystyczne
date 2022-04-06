import tsplib95
import time

from matplotlib import pyplot as plt

from Src.Algorythms.NN_Algorythm import NNA
from Src.Algorythms.NN_Algorythm_Ext import ENNA
from Src.Algorythms.krandom import krandom
from Src.Algorythms.two_opt import two_opt
from Src.RandomDataGenerator import RandomDataGenerator


def randomDataPlot():
    generator = RandomDataGenerator()
    generator.removeDir()

    for i in range (10, 110, 10):
        generator.symmetricMatrix("MyData", i)

    kRandomData = []
    NNData = []
    ENNData = []
    TwoOPTData = []
    xpoints = []

    for i in range(10, 110, 10):
        problem = tsplib95.load(f'../Src/RandomDataset/MyData{i}/MyData{i}.tsp')
        xpoints.append(i)
        startTime = time.time_ns()
        two_opt(problem)
        totalTime = (time.time_ns() - startTime)
        TwoOPTData.append(totalTime)

        startTime = time.time_ns()
        ENNA(problem)
        totalTime = (time.time_ns() - startTime)
        ENNData.append(totalTime)

        startTime = time.time_ns()
        NNA(problem, 0)
        totalTime = (time.time_ns() - startTime)
        NNData.append(totalTime)

        startTime = time.time_ns()
        krandom(problem, 1000)
        totalTime = (time.time_ns() - startTime)
        NNData.append(totalTime)

        plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])

        plt.plot(range(10,110,10), kRandomData)
        plt.plot(range(10,110,10), NNData)
        plt.plot(range(10,110,10), ENNData)
        plt.plot(range(10,110,10), TwoOPTData)

        plt.legend(['krandom', 'NN_Algorithm', 'Extended_NN_Algorithm', '2-OPT'], loc='upper left')

        plt.show()

