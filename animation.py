import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from matplotlib import animation
fig, ax = plt.subplots()
ax.set_xlim(1, 7)
ax.set_ylim(1, 7)

ax.plot([7, 7],[4, 5], color = "black")

carA = Rectangle((2, 6), 2, 1, color = "gray")
carB = Rectangle((4, 6), 3, 1, color = "sandybrown")
carC = Rectangle((2, 5), 2, 1, color = "goldenrod")
carD = Rectangle((5, 5), 2, 1, color = "mediumspringgreen")
carE = Rectangle((4, 4), 1, 2, color = "darkcyan")
carF = Rectangle((1, 3), 2, 1, color = "slateblue")
carG = Rectangle((3, 3), 1, 2, color = "darkorchid")
carH = Rectangle((4, 3), 2, 1, color = "purple")
carI = Rectangle((6, 3), 1, 2, color = "magenta")
carJ = Rectangle((5, 2), 2, 1, color = "hotpink")
carK = Rectangle((1, 1), 1, 2, color = "sienna")
carL = Rectangle((3, 1), 1, 2, color = "forestgreen")
carX = Rectangle((1, 4), 2, 1, color = "red")

moving = [carJ, carI, carH, carE, carD, carA, carC, carG, carL, carJ, carE, carH, carI, carH, 
          carE, carJ, carL, carE, carX, carG, carB, carI, carX]

directionx = [4, 6, 5, 4, 4, 1, 1, 3, 3, 2, 4, 4, 6, 5, 4, 5, 3, 4, 4, 3, 3, 6, 5]

directiony = [2, 1, 3, 3, 5, 6, 5, 5, 3, 2, 1, 3, 4, 3, 3, 2, 1, 2, 4, 4, 6, 5, 4]

def init():
    ax.add_patch(carA)
    ax.add_patch(carB)
    ax.add_patch(carC)
    ax.add_patch(carD)
    ax.add_patch(carE)
    ax.add_patch(carF)
    ax.add_patch(carG)
    ax.add_patch(carH)
    ax.add_patch(carI)
    ax.add_patch(carJ)
    ax.add_patch(carK)
    ax.add_patch(carL)
    ax.add_patch(carX)

    return carA, carB, carC, carD, carE, carF, carG, carH, carI, carJ, carK, carL, carX

def animate(i):
    moving[i].set_xy([directionx[i], directiony[i]])
    return moving[i]

rushHour = animation.FuncAnimation(fig, animate,
                               frames = len(directionx),
                               interval = 500,
                               init_func = init,
                               repeat = False)

f = r"c://Users/judit/Documents/Algoritmen_Heuristieken/JuLiDy/animation.gif" 
writergif = animation.PillowWriter(fps = 2) 
rushHour.save(f, writer = writergif)

plt.show()
