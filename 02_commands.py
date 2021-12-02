x = 0
y = 0
aim = 0

lines = [line.strip().split() for line in open("input","r").readlines()]
print(lines)

parsed = [(direction, int(dist)) for (direction,dist) in lines]

for (direction, dist) in parsed:
    if direction == "up":
        aim -= dist
    elif direction == "down":
        aim += dist
    elif direction == "forward":
        y += aim * dist
        x += dist

print (x*y)
