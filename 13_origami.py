import numpy as np

pair_out = lambda pair : [int(pair[0]) , int(pair[1])]
fold_out = lambda fold : (1 if fold[0][-1] == "x" else 0, int(fold[1]))
lines, folds = [sect.strip() for sect in open("input3","r").read().split("\n\n")]
coords = [pair_out(line.strip().split(",")) for line in lines.split()]

len0 = max([a for [a,b] in coords]) + 1
len1 = max([b for [a,b] in coords]) + 1

folds = [fold.split("=") for fold in [line for line in folds.split("\n")]]
folds = [fold_out(fold) for fold in folds]

dots = np.zeros((len0,len1))

for (x,y) in coords: # DON'T FORGET ROW/COL VS X/Y!!!!!!!!!!!
    dots[x][y] = 1
print(dots)
print(folds)

for axis, val in folds:
    len0 = len(dots)
    len1 = len(dots[1])
    if axis == 0:
        fold_A = dots[:val,:]
        fold_B = dots[val+1:,:]

        if val > len0/2: # Fold A is bigger, flip B, pad, and add 
            new_dots = np.logical_or(np.pad(np.flip(fold_B, axis), ((val - len(fold_B),0),(0,0))), fold_A)
        else: #fold B is bigger
            breakpoint()
            new_dots = np.logical_or(np.pad(np.flip(fold_A, axis), ((0,len(fold_B) - val),(0,0))), fold_B)
    else:
        fold_A = dots[:,:val]
        fold_B = dots[:,val+1:]

        if val > len1/2: # Fold A is bigger, flip B, pad, and add 
            new_dots = np.logical_or(np.pad(np.flip(fold_B, axis), ((0,0),(val - len(fold_B[0]),0))), fold_A)
        else: #fold B is bigger
            breakpoint()
            new_dots = np.logical_or(np.pad(np.flip(fold_A, axis), ((0,0),(0,len(fold_B[0]) - val))), fold_B)
    dots = new_dots
    print(np.sum(dots))
