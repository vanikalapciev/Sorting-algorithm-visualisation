from random import *
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


setSize = 100
i = 1

numbers = random.sample(range(1, setSize), setSize-1)
ind = np.arange(setSize-1)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind,numbers)
plt.show()
