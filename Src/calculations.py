import numpy as np
import tsplib95


if __name__ == '__main__':
     problem = tsplib95.load('../Data/bays29/bays29.tsp')
     #print(type(problem))