import numpy as np

digits = lambda line: [int(char) for char in line]
grid_list = [digits(line.strip()) for line in open("input2","r").readlines()]

grid = np.array(grid_list)

# neighbor positions:
# 1 2 3
# 4 0 5
# 6 7 8
NEIGHBORS = (   (-1,-1), (-1,0), (-1,1),
                (0,-1), (0,0), (0,1),
                (1,-1), (1,0), (1,1) )

HEIGHT,WIDTH = grid.shape

total = 0

def grow(row,col):
    global total
    grid[row][col] += 1

    if grid[row][col] == 10: # FLASH
        total += 1
        for drow,dcol in NEIGHBORS :
            this_row = drow + row
            this_col = dcol + col

            if (0 <= this_row < HEIGHT and 
                0 <= this_col < WIDTH):
                grow(this_row,this_col)

turn = 0
while True:

    for (row,col),octopus in np.ndenumerate(grid):
        grow(row,col)

    flashcount = 0
    for (row,col),octopus in np.ndenumerate(grid):

        if octopus >= 10:
            grid[row][col] = 0
            flashcount += 1

    turn += 1
    print(grid)
    print(total)
    print("turn: ", turn)
    if flashcount == 100:
        break

