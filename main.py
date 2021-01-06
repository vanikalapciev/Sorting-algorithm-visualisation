from graphics import *
from random import *
import random

def main():
    win = GraphWin("Visualisation", 500, 500)
    win.setBackground('gray')
    numbers = random.sample(range(1, 500), 250)
    i=1
    j=0
    while i < 500:
        number = randint(0, 500)
        win.create_line(i, 500, i, 500-numbers[j])
        j += 1
        i += 2
    
    win.getMouse()
    win.close()
main()