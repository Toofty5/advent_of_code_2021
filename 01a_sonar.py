
depths = [int(line) for line in open("input","r").readlines()]

windows = zip(depths, depths[1:],depths[2:])

sums = [sum(thing) for thing in windows]

print(len([(i,j) for (i,j) in zip(sums, sums[1:]) if i < j]))
