import random
import numpy as np
from matplotlib import pyplot as plt
from sorting import *

#set sample size
sampleSize = 100

#defines bar chart
ax = plt.axes()
plt.xlim(0,sampleSize) 
plt.ylim(0,sampleSize)
ind = np.arange(sampleSize-1)

numbers = random.sample(range(1, sampleSize), sampleSize-1)
sortArray = [numbers]

#makes a array with each element with sorted run
for i in range(sampleSize):
    run = bubble_sort(numbers[:], i)
    sortArray.append(run)

#animates sorting
for i in range(sampleSize+1):
    ax.bar(ind,sortArray[i])
    plt.draw() 
    plt.pause(0.01)
    if i < sampleSize:
        ax.cla()
        
plt.show()
