import numpy as np

pair_out = lambda pair : [int(pair[0]) , int(pair[1])]
fold_out = lambda fold : (1 if fold[0][-1] == "x" else 0, int(fold[1]))
lines, folds = [sect.strip() for sect in open("input","r").read().split("\n\n")]
coords = [pair_out(line.strip().split(",")) for line in lines.split()]

len0 = max([a for [a,b] in coords]) + 1
len1 = max([b for [a,b] in coords]) + 1

folds = [fold.split("=") for fold in [line for line in folds.split("\n")]]
folds = [fold_out(fold) for fold in folds]

dots = np.zeros((len0,len1))

def print_dots(a):
    print(np.sum(a))
    for line in np.rot90(np.transpose(a), k=2):
        print(''.join(['1 ' if tf else '  ' for tf in line]))

for (x,y) in coords: # DON'T FORGET ROW/COL VS X/Y!!!!!!!!!!!
    dots[x][y] = 1
#print(len(coords),coords)
#print(len(folds), folds)

for axis, val in folds:

    print(np.shape(dots), np.sum(dots))
#    print(val, axis)

    len0 = len(dots)
    len1 = len(dots[0])

    if axis == 0:
        fold_A = dots[:,:val]
        fold_B = dots[:,val+1:]
        len_A = len(fold_A[0])
        len_B = len(fold_B[0])
        pad_amount = abs(len_A-len_B)

        if len_A > len_B: # Fold A is bigger 
            flip_B = np.flip(fold_B,1)
            pad_amount = abs(len_A - len_B)
            padded = np.pad(flip_B, ((0,0),(pad_amount,0)))
            new_dots = np.logical_or(padded, fold_A)
        else: #fold B is bigger
            flip_A = np.flip(fold_A,1)
            pad_amount = abs(len_A - len_B)
            padded = np.pad( flip_A, ((0,0),(0,pad_amount)) )
            new_dots = np.logical_or(padded, fold_B)
    else: 
        fold_A = dots[:val,:]
        fold_B = dots[val+1:,:]
        len_A = len(fold_A)
        len_B = len(fold_B)
        pad_amount = abs(len_A-len_B)

        if len_A > len_B: # Fold A is bigger, flip B, pad, and add 
            flip_B = np.flip(fold_B,0)
            padded = np.pad(flip_B, ((pad_amount,0),(0,0)) )
            new_dots = np.logical_or(padded, fold_A)

        else: #fold B is bigger
            flip_A = np.flip(fold_A,0)
            padded = np.pad(flip_A, ((0,pad_amount),(0,0)))
            new_dots = np.logical_or(padded, fold_B)


    dots = new_dots.copy()
print_dots(dots)
