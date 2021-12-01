lines = [int(line) for line in open("input","r").readlines()]


current_depth = lines[0]
total = 0
for line in lines[1:]:
    if line > current_depth:
        total += 1
    current_depth = line

print(total)
