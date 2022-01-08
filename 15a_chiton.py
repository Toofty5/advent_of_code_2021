import numpy as np

val_arr = np.array([[int(char) for char in line.strip()] for line in open("input","r").readlines()])
NUM_ROWS, NUM_COLS = val_arr.shape

topo_array = np.zeros(val_arr.shape)
INF = 9999
topo_array.fill(INF)
print(val_arr)



def main() :
    start_node = (NUM_ROWS-1, NUM_COLS-1)

    build_topo(start_node, 0)
    print(topo_array)


def build_topo(this_node, cost_so_far):
    new_cost = val_arr[this_node] + cost_so_far
    topo_array[this_node] = new_cost
    

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

    neighbors.sort(key = lambda x: val_arr[x]) 

    for nei in neighbors:
        if topo_array[nei] == INF:
            build_topo(nei, new_cost)
    
if __name__ == "__main__" :
    main()
