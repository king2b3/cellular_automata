#   Bayley King
#   Python 3.8.6
#   Challenge to implement conways game of life in one night
#   Uses ffmpeg and matplotlib 

import matplotlib.pyplot as plt
from itertools import product
import numpy as np
import time
import os
output_folder = 'outputs/'


def plot_current_generation(filename,iteration,space_array):
    filename = path+filename+'_'+str(iteration)+'.png'
    plt.imshow(space_array,cmap='Greys')
    plt.axis('off')
    plt.savefig(filename)


def createSpace(size):
    return np.zeros((size,size))#,dtype=bool)

def createRandomSpace(size):
    return np.random.randint(2,size=(size,size))

def neighbors(cell,size):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

def checkConditions(array,size):
    test_array = array.copy()
    for row in range(size):
        for col in range(size):
            temp = list(neighbors((row,col),size))
            val = []
            for vals in temp:
                val.append(space[vals[0],vals[1]])
            val = sum(val)
            if array[row][col] == 0:
                if val == 3:
                    test_array[row][col] = 1
            else:
                if val < 2 or val > 3:
                    test_array[row][col] = 0
 
    return test_array

path = output_folder+str(time.time())
os.mkdir(path)
#space = createSpace(100)
space = createRandomSpace(100)

for i in range(1,1000):
    space = checkConditions(space,100)
    plot_current_generation('/test',i,space)
