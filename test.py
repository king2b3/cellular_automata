import numpy
import random
from itertools import product

def neighbours(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

space = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]

])

size = 3

for row in range(size):
    for col in range(size):
        temp = list(neighbours((row,col)))
        val = []
        for vals in temp:
            val.append(space[vals[0],vals[1]])
        print(sum(val))
