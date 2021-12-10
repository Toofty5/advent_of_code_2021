import numpy as np

lines = [line.strip() for line in open("input2","r").readlines()]
vals = []

for line in lines:
    vals.append([int(char) for char in line])

val_array = np.array(vals)
MAP_WIDTH = val_array.shape[0]
MAP_HEIGHT = val_array.shape[1]

total = 0

low_points = [] 


def edge(coords):
    x,y = coords

    adj= []
    if x > 0:
        adj.append((x-1, y))
    if x < val_array.shape[0]-1:
        adj.append((x+1, y))
    if y > 0:
        adj.append((x, y-1))
    if y < val_array.shape[1]-1:
        adj.append((x, y+1))
        
    return adj



for (x,y),val in np.ndenumerate(val_array):

    adjacents = edge((x,y))

    if val < min([val_array[coord[0]][coord[1]] for coord in adjacents]):
        total += val + 1
        low_points.append((x,y))

# basins tracks coords
# basin_map tracks basin that each point belongs to

basins = {}
basin_map = np.ndarray(val_array.shape)
basin_map.fill(-1)

for lp in low_points:
    basins[lp] = [lp]

    queue = [lp]

    while queue != []:
        this_node = queue.pop(0)

        for x,y in edge(this_node):
            if val_array[x][y] < 9 and (x,y) not in basins[lp]:
                basins[lp].append((x,y))
                queue.append((x,y))

for key in basins:
    print(basins[key], len(basins[key]))

top3 = [0,0,0]

for key in basins:
    top3.append(len(basins[key]))
    top3.remove(min(top3))

print(top3)
answer = 1
for i in top3:
    answer *= i
print(answer)

