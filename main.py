import random
import numpy as np
from matplotlib import pyplot as plt
from sorting import *
from matplotlib.animation import FuncAnimation
#set sample size
sampleSize = 50

#x-asis definition
ind = np.arange(sampleSize-1)

#generates random number
numbers = random.sample(range(1, sampleSize), sampleSize-1)

#makes a array with each element with sorted run
for i in range(sampleSize):
    iteration = countSort(numbers[:], i)
    plt.bar(ind,iteration)
    plt.pause(0.1)
    print(iteration)
    if i < sampleSize:
        plt.cla()


#does not close window
plt.show()
