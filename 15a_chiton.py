import numpy as np

topo_array = np.array([[int(char) for char in line.strip()] for line in open("input","r").readlines()])
NUM_ROWS, NUM_COLS = topo_array.shape

cost_array = np.zeros(topo_array.shape)
INF = 999
cost_array.fill(INF)


def main() :
    start_node = (NUM_ROWS-1, NUM_COLS-1)
    cost_array[start_node] = topo_array[start_node]

    queue = [start_node]

    while queue != []:
        
        this_node = queue.pop(0)
        queue.extend(unvisited_neighbors(this_node))

        for next_node in neighbors(this_node):
            build_topo(next_node, cost_array[this_node])
    print(topo_array)
    print(cost_array)
    print(topo_array.shape)
    print("don't forget to subtract the cost of the first node!")

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

    neighbors.sort(key = lambda x: topo_array[x]) 
    return neighbors

def unvisited_neighbors(this_node):  # return UNVISITED neighbors
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

    neighbors.sort(key = lambda x: topo_array[x]) 
    return neighbors


def build_topo(this_node, cost_so_far):
    new_cost = topo_array[this_node] + cost_so_far
    if(cost_array[this_node] > new_cost):
        cost_array[this_node] = new_cost


    
if __name__ == "__main__" :
    main()
