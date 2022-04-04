from Src.RandomDataGenerator import RandomDataGenerator


def randomDataPlot():
    generator = RandomDataGenerator()

    for i in range (10, 110, 10):
        generator.symmetricMatrix("MyData", i)

    kRandomData = []
    NNData = []
    ENNData = []
    TwoOPTData = []

