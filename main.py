from random import *
import random
import numpy as np
import sorting
import time
from matplotlib import pyplot as plt
from matplotlib import animation
from sorting import bubblesort
from _ast import Print
from matplotlib.animation import FuncAnimation


setSize = 100
i=0
ind = np.arange(setSize-1)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1], animated=True)

numbers = random.sample(range(1, setSize), setSize-1)
numberArray = [numbers]
'''
while i < setSize:
    numbers = bubblesort(numbers, i)
    numberArray.append(numbers)
    ax.bar(ind,numbers)
    i += 1

print(numberArray)
'''
def animate(i):
    numbers = bubblesort(numbers, i)
    ax.bar(ind,numbers)
    return ax

#ax.bar(ind,numbers)
ani = FuncAnimation(fig, animate, blit=True)
plt.show()    
plt.show()

