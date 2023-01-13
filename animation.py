# Import libraries
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from matplotlib import animation

# Based on https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
# Create plot
fig, ax = plt.subplots()
ax.set_xlim(1, 7)
ax.set_ylim(1, 7)

# Create the line that is the exit
ax.plot([7, 7],[4, 5], color = "black")

# Define the cars with their colour and position
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

# Create an array to define which car has to move
moving = [carJ, carI, carH, carE, carD, carA, carC, carG, carL, carJ, carE, carH, carI, carH, 
          carE, carJ, carL, carE, carX, carG, carB, carI, carX]

# Create an array to define the placement on the x-axis
directionx = [4, 6, 5, 4, 4, 1, 1, 3, 3, 2, 4, 4, 6, 5, 4, 5, 3, 4, 4, 3, 3, 6, 5]

# Create an array to define the placement on the x-axis
directiony = [2, 1, 3, 3, 5, 6, 5, 5, 3, 2, 1, 3, 4, 3, 3, 2, 1, 2, 4, 4, 6, 5, 4]

# Based on https://stackoverflow.com/questions/31921313/matplotlib-animation-moving-square
def init():
    """Initialize the graph and add the cars
    post: all shapes are added to the graph.
    """
    # Add cars to the graph
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
    """ Move the cars in the moving array to the right place
    post: the shape in the moving array is updated to the given position
    """
    # Move the car to the given place
    moving[i].set_xy([directionx[i], directiony[i]])
    return moving[i]

# Based on https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
# Create animation
rushHour = animation.FuncAnimation(fig, animate, frames = len(directionx), interval = 500,
                                   init_func = init, repeat = False)

# Based on https://holypython.com/how-to-save-matplotlib-animations-the-ultimate-guide/
# Save animation as an gif-file
f = r"c://Users/judit/Documents/Algoritmen_Heuristieken/JuLiDy/animation.gif" 
writergif = animation.PillowWriter(fps = 2) 
rushHour.save(f, writer = writergif)

# Show animation
plt.show()