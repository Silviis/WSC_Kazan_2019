from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

path = "/home/silvis/code/python/img_to_path/"
# path = "C:/Users/Eetu Silvenoinen/Desktop/WorldSkills Kazan 2019/WSC_Kazan/"

temp=Image.open(path + "map.bmp")
temp=temp.convert('1')      # Convert to black&white
A = np.array(temp)
new_A=np.empty((A.shape[0],A.shape[1]),None)    #New array with same size as A

for i in range(len(A)):       
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j] = int(1)
        else:
            new_A[i][j] = int(0)
np.savetxt(path + "grid.txt", np.int_(new_A),
fmt="%d", comments='')   # Save map as grid to a file

matrix = np.loadtxt(path + "grid.txt", delimiter=" ")
grid = Grid(matrix=matrix)
start = grid.node(1, 1)
end = grid.node(390, 196)
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)     # Calculate optimal path with A*
path, runs = finder.find_path(start, end, grid)

# Plot data to matplotlib chart
img = plt.imread("map.bmp")
fig, ax = plt.subplots()
ax.imshow(img)
zip(*path)
plt.scatter(*zip(*path),s=2)
plt.show()