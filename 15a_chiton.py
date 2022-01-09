import numpy as np
np.set_printoptions(suppress=True)

TILES = 5

tile = np.array([[int(char) for char in line.strip()] for line in open("input","r").readlines()])

inc_mod = np.vectorize(lambda x,y: x+y-9 if (x+y) > 9 else x+y)

tile_col = np.concatenate([inc_mod(tile, i) for i in range(5)], axis=0)
topo_array = np.concatenate([inc_mod(tile_col, i) for i in range(5)], axis=1)

cost_array = np.zeros(topo_array.shape)
INF = 99999
cost_array.fill(INF)

NUM_ROWS, NUM_COLS = topo_array.shape

print(topo_array.shape)
def main() :
    #start_node = (NUM_ROWS-1, NUM_COLS-1)
    start_node = (0,0)
    cost_array[start_node] = 0

    queue = [start_node]

    while queue != []:
        #print(np.array(list(zip(topo_array[:10,:10], cost_array[:10,:10]))))
        this_node = queue.pop(0)
        
        queue.extend(heavier_neighbors(this_node))

        for next_node in neighbors(this_node):
            build_topo(next_node, cost_array[this_node])
    print(topo_array)
    print(cost_array)



def neighbors(this_node):  # return VISITED neighbors
    this_row,this_col = this_node
    neighbors = []

    if this_row > 0: 
        up = (this_row - 1, this_col)
        neighbors.append(up)
    if this_row < NUM_ROWS - 1:
        down = (this_row + 1, this_col)
        neighbors.append(down)
    if this_col > 0:
        left = (this_row, this_col - 1)
        neighbors.append(left)
    if this_col < NUM_COLS - 1:
        right = this_row, this_col + 1
        neighbors.append(right)

    #neighbors.sort(key = lambda x: topo_array[x]) 
    return neighbors

def heavier_neighbors(this_node):  # return HEAVIER neighbors
    return [nei for nei in neighbors(this_node) if cost_array[nei] > cost_array[this_node]+ topo_array[nei]]


# replace item in cost_array if new cost is cheaper.
def build_topo(this_node, cost_so_far): 
    new_cost = topo_array[this_node] + cost_so_far
    if(cost_array[this_node] > new_cost):
        cost_array[this_node] = new_cost


    
if __name__ == "__main__" :
    main()
