from random import *
import random
import numpy as np
import sorting
import time
from matplotlib import pyplot as plt
from matplotlib import animation
from sorting import *
from matplotlib.animation import FuncAnimation


setSize = 50
i=0

ax = plt.axes()
plt.xlim(0,setSize) 
plt.ylim(0,setSize)
ind = np.arange(setSize-1)

numbers = random.sample(range(1, setSize), setSize-1)

for i in range(setSize):        
     numbers = quick_sort(numbers, i) 
     ax.bar(ind,numbers) 
     plt.draw() 
     plt.pause(0.001) 
     if i < setSize-1:
         ax.cla()

plt.show()
