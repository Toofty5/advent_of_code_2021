import numpy as np

topo_array = np.array([[int(char) for char in line.strip()] for line in open("input2","r").readlines()])
NUM_ROWS, NUM_COLS = topo_array.shape

cost_array = np.zeros(topo_array.shape)
INF = 999
cost_array.fill(INF)


def main() :
    #start_node = (NUM_ROWS-1, NUM_COLS-1)
    start_node = (0,0)
    cost_array[start_node] = 0

    queue = [start_node]

    while queue != []:
        #print(np.array(list(zip(topo_array[:10,:10], cost_array[:10,:10]))))
        this_node = queue.pop(0)
        queue.extend(unvisited_neighbors(this_node))

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

def unvisited_neighbors(this_node):  # return UNVISITED neighbors
    return [nei for nei in neighbors(this_node) if cost_array[nei] == INF]


# replace item in cost_array if new cost is cheaper.
def build_topo(this_node, cost_so_far): 
    new_cost = topo_array[this_node] + cost_so_far
    if(cost_array[this_node] > new_cost):
        cost_array[this_node] = new_cost


    
if __name__ == "__main__" :
    main()
