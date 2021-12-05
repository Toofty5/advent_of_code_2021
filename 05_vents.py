import numpy as np

lines = [line.split() for line in open("input", "r")]

segments = []

for line in lines:
    x1,y1 = map(int,line[0].split(","))
    x2,y2 = map(int,line[2].split(","))

    if x1 > x2:   
        x1,x2 = x2,x1
        y1,y2 = y2,y1
    if x1 == x2 and y2 < y1:
        y1,y2 = y2,y1

    segments.append((x1,y1,x2,y2))

total = 0 
grid = np.zeros([1000,1000])
print(grid)

for x1,y1,x2,y2 in segments:

    if x1==x2: # vertical 
        for y in range(y1,y2+1):
            if grid[x1,y] == 1:
                total += 1
            grid[x1,y] += 1

    elif y1==y2: # horizontal
        for x in range(x1,x2+1):
            if grid[x,y1] == 1:
                total += 1
            grid[x,y1] += 1

    else:
        for dx in range(x2-x1+1):
            if y1>y2:
                dy = -dx
            else:
                dy = dx

            if grid[x1+dx,y1+dy] == 1:
                total += 1
            
            grid[x1+dx , y1+dy] += 1

print(total)
