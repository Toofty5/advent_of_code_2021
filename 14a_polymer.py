import itertools as it

lines = [line.strip() for line in open("input2","r").readlines()]

template = [char for char in lines[0]]

split_lines = [line.split(" -> ") for line in lines[2:]]
pair_dict = {(a[0],a[1]):b for a,b in split_lines}



for i in range(10):
    print(i)
    pairs = zip(template, template[1:])
    triplets = [[a, pair_dict[(a,b)] ,b] for (a,b) in pairs]
    template = list(it.chain(triplets[0], *[t[1:] for t in triplets[1:]]))
    


elements = set(template)
for i in elements:
    print(i, template.count(i))
breakpoint()
