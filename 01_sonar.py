
depths = [int(line) for line in open("input","r").readlines()]



print(len( [(i,j) for (i,j) in zip(depths, depths[1:]) if i < j]))
