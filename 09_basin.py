import numpy as np

lines = [line.strip() for line in open("input","r").readlines()]
vals = []

for line in lines:
    vals.append([int(char) for char in line])

val_array = np.array(vals)

total = 0

low_points = [] 

def adjacents(coords): # depths of all the adjacents
    x,y = coords

    adj= []
    if x > 0:
        adj.append(val_array[x-1, y])
    if x < val_array.shape[0]-1:
        adj.append(val_array[x+1, y])
    if y > 0:
        adj.append(val_array[x, y-1])
    if y < val_array.shape[1]-1:
        adj.append(val_array[x, y+1])
        
    return adj

for (x,y),val in np.ndenumerate(val_array):

    adj = adjacents((x,y))

    if val < min(adj):
        total += val + 1
        low_points.append((x,y))


print(total)
print(low_points)


