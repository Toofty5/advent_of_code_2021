import numpy as np
to_digits = lambda line: [int(char) for char in line]

cave = [to_digits(line.strip()) for line in open("input","r")]
LEN0,LEN1 = np.shape(cave)
ROOT = (LEN0-1,LEN1-1)

nei_dict = {}

for line in cave:
    print(line)


topo_dict = {} # coords:cost to root from coords
def print_dict(d):
    test = [[0]*10]*10
    for (row, col), val in d.items():
        test[row][col] = val
    for line in test:
        print(line)


def traverse(coords, cost_so_far):

    row,col = coords
    this_node = cave[row][col]
    new_cost = this_node + cost_so_far


    if coords in topo_dict:
        if new_cost <= topo_dict[coords]:
            topo_dict[coords] = new_cost
            return
    
    else:
        topo_dict[coords] = new_cost

        if row > 0 :
            u = cave[row-1][col]
        if row < LEN0 - 1:
            d = cave[row+1][col]
        if col > 0: 
            l = cave[row][col-1]
        if col < LEN1 - 1:
            r = cave[row][col+1]

    print_dict(topo_dict)
    # this is going depth first.  Need breadth first
    breakpoint()

def path(node, cost_so_far):
    row, col = node
    if node == ROOT:
        print("Root found!")
        print("Cost ", cost_so_far)
        return 
    else:
        paths = {}
        if row > 0:
            paths[row-1,col] = topo_dict[row-1,col]
        if row < LEN0 - 1:
            paths[row+1,col] = topo_dict[row+1,col]
        if col > 0: 
            paths[row,col-1] = topo_dict[row,col-1]
        if col < LEN1 - 1:
            paths[row,col+1] = topo_dict[row,col+1]

        next_path = min(paths.items(), key=lambda x: x[1])
        print(paths)
        print(next_path)
        print(cost_so_far)

        path(next_path[0], cost_so_far + cave[row][col])

traverse(ROOT, 0)
print(topo_dict)


#path((0,0),0)
