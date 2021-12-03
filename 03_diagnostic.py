import numpy as np

lines = [[int(char) for char in line.strip()] for 
        line in open("input","r").readlines()]


arr = np.array(lines)
print(arr)

sums = list(np.sum(arr, axis=0))
gamma = int("".join(['0' if item <500 else '1' for item in sums ]),2)
epsilon = int("".join(['0' if item >500 else '1' for item in sums ]),2)

print(gamma* epsilon)
