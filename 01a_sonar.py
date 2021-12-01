lines = [int(line) for line in open("input","r").readlines()]

current_window = sum(lines[0:3])
total = 0

for i in range(len(lines) - 2):
    window = sum(lines[i:i+3])
    if window > current_window:
        total += 1
    current_window = window
   

print(total)
