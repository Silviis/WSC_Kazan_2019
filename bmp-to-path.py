from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import simplejson

#filepath = "/home/silvis/code/WSC_Kazan_2019/"
filepath = "C:/Users/Eetu Silvenoinen/Desktop/WorldSkills Kazan 2019/WSC_Kazan/"

temp=Image.open(filepath + "map.bmp")
temp=temp.convert('1')      # Convert to black&white
A = np.array(temp)
new_A=np.empty((A.shape[0],A.shape[1]),None)    #New array with same size as A

for i in range(len(A)):       
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j] = int(0)
        else:
            new_A[i][j] = int(1)
np.savetxt(filepath + "grid.txt", np.int_(new_A),
fmt="%d", comments='')   # Save map as grid to a file

matrix = np.loadtxt(filepath + "grid.txt", delimiter=" ")
grid = Grid(matrix=matrix)
start = grid.node(50, 0)
end = grid.node(0, 40)
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)     # Calculate optimal path with A*
path, runs = finder.find_path(start, end, grid)

prev = [-1,-1]
result = []
for i in range (len(path)):
    if list(path[i])[0] == prev[0]:
        result.append(path[i])
        print(prev)
    elif list(path[i])[1] == prev[1]:
        result.append(path[i])

    prev = list(path[i])
print(result,path)

f = open("path.txt","w")
simplejson.dump(path,f)
f.close()

"""# Plot data to matplotlib chart
img = plt.imread("map.bmp")
fig, ax = plt.subplots()
ax.imshow(img)
zip(*path)
plt.scatter(*zip(*path),s=2)



plt.show()"""