import numpy as np

topo_array = np.array([[int(char) for char in line.strip()] for line in open("input","r").readlines()])
NUM_ROWS, NUM_COLS = topo_array.shape

cost_array = np.zeros(topo_array.shape)
INF = 999
cost_array.fill(INF)

print(topo_array)



def main() :
    start_node = (NUM_ROWS-1, NUM_COLS-1)

    build_topo(start_node, 0)

    print(cost_array)

def get_neighbors(this_node):  # return UNVISITED neighbors
    
    this_row,this_col = this_node
    neighbors = []

    if this_row > 0: 
        up = (this_row - 1, this_col)
        if cost_array[up] == INF:
            neighbors.append(up)
    if this_row < NUM_ROWS - 1:
        down = (this_row + 1, this_col)
        if cost_array[down] == INF:
            neighbors.append(down)
    if this_col > 0:
        left = (this_row, this_col - 1)
        if cost_array[left] == INF:
            neighbors.append(left)
    if this_col < NUM_COLS - 1:
        right = this_row, this_col + 1
        if cost_array[right] == INF:
            neighbors.append(right)

    return neighbors


def build_topo(this_node, cost_so_far):
    new_cost = topo_array[this_node] + cost_so_far
    cost_array[this_node] = new_cost

    neighbors = get_neighbors(this_node)
    
    neighbors.sort(key = lambda x: topo_array[x]) 
    
    if neighbors ==[]:
        return

    for nei in neighbors:
        cost_array[nei] = new_cost + topo_array[nei]

    
if __name__ == "__main__" :
    main()
