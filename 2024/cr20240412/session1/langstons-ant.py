# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Langston's Ant
# ## What do we work on? ⬜🐜⬛
#
# ![](https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif)
#
# ## Langston's ant! ⬜🐜⬛
#
# Squares on a plane are colored either black or white.
#
# An "ant" behaves like this
#
# - at white square, turn 90° clockwise, flip the color of the square
# - at black square, turn 90° counter-clockwise, flip the color of the square,
#
# then move forward one unit.

# %%
grid = "wwbw"
grid

# %%
w = "w"
b = "b"
grid = [[w,w],[b,w]]
grid


# %%
ant = [[0,0],["^", 0]]

# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
grid = np.array([[0,0],[1,0]])
grid

# %%
plt.pcolormesh(np.flipud(grid), cmap="gray_r")

# %%
DIRECTIONS = ["^", ">", "v", "<"]

class Ant:
    def __init__(self, coordinates, direction):
        self.coordinates = coordinates
        self.direction = direction
    def __repr__(self): 
        return f"Ant({self.coordinates},{self.direction})"
    def move(self):
        self.coordinates[1] += 1
        self.direction= DIRECTIONS[(DIRECTIONS.index(self.direction) + 1) % 4]
        
ant = Ant([0, 0], "^")
print(ant)
ant.move()
print(ant)
ant.move()
print(ant)
ant.move()
print(ant)
ant.move()
ant


# %%

# %%
def drawLangton(grid, ant):

    fig,ax = plt.subplots()
    ax.pcolormesh(np.flipud(grid), cmap="gray_r")
    ax.scatter(*(np.array(ant.coordinates)+np.array([0.5,0.5])), marker=ant.direction, color="red", s=1000)
drawLangton(grid, ant)

# %%
# if ant.direction("^"):

ant = Ant([0,0], '^')
# move up
ant.coordinates[1] += 1
# move down
ant.coordinates[1] -= 1
# move right
ant.coordinates[0] += 1

ant

# %%
whos

# %%
drawLangton(grid, ant)

# %%
from time import sleep

for tick in range (1,4):
    ant.move()
    drawLangton(grid, ant)
    sleep(1)

# %%
from matplotlib.animation import FuncAnimation
ant = Ant([0,0], '^')

fig,ax = plt.subplots()
quad = ax.pcolormesh(np.flipud(grid), cmap="gray_r")
scatter = ax.scatter(*(np.array(ant.coordinates)+np.array([0.5,0.5])), marker=ant.direction, color="red", s=1000)

def update(frame):
    ant.move()
    scatter.set_offsets(*(np.array(ant.coordinates)+np.array([0.5,0.5])))   
    return scatter

animation = FuncAnimation(fig, update, frames = 10, interval = 2000)
animation

# %%
