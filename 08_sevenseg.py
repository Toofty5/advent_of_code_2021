lines = [line for line in open("input","r")]

digits = []
outputs = []

total = 0

for d, o in [line.split("|") for line in lines]:
    these_digits = d.strip().split()
    this_output = o.strip().split()

    
    digits.append(these_digits)
    outputs.append(this_output)

print(total)
