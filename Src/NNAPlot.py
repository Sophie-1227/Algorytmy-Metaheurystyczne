import matplotlib.pyplot as plt

from Src.NN_Algorythm import NNA


# dlugosc trasy w zaleznosci od punktu startowego z wykorzystaniem NN Alg
def NNAPlot(problem):
    xpoints = []
    ypoints = []
    for i in range(1,30):
        starting, length  = NNA(problem, i)
        xpoints.append(i)
        ypoints.append(length)

    plt.plot(xpoints, ypoints, 'o')
    plt.xlabel('Starting point')
    plt.ylabel('Tour length')
    plt.title('NN-method plot')
    plt.show()