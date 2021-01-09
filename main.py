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
sortArray = [numbers]

#makes a array with each element with sorted run
for i in range(sampleSize):
    run = merge_sort(numbers[:], i)
    sortArray.append(run)
    print(run)

#animates sorting
for i in range(sampleSize+1):
    plt.bar(ind,sortArray[i])
    plt.pause(0.1)
    if i < sampleSize:
        plt.cla()

#does not close window
plt.show()
