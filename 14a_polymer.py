import itertools as it

lines = [line.strip() for line in open("input2","r").readlines()]

template = [char for char in lines[0]]

split_lines = [line.split(" -> ") for line in lines[2:]]
pair_dict = {(a[0],a[1]):b for a,b in split_lines}
zipped = list(zip(template, template[1:]))

poly_dict = {}
counts = {}

def d_add(d, pair, count=1):
    if pair in d:
        d[pair] += count 
    else:
        d[pair] = count 

def d_sub(d,pair, count=1):
    d[pair] -= count
    if d[pair] == 0:
        d.pop(pair)

for e in template:
    d_add(counts, e)

for pair in zipped:
    d_add(poly_dict, pair)


for i in range(40):
    new_poly = poly_dict.copy()
    for a,b in poly_dict:
        count = poly_dict[(a,b)]
        new_element = pair_dict[(a,b)]
        d_add(new_poly, (a,new_element),count)
        d_add(new_poly, (new_element,b),count)
        d_sub(new_poly, (a,b),count)
        d_add(counts, new_element, count = count)
    poly_dict = new_poly

    for thing in poly_dict.items():
        print(thing)
    print(counts)

vals = counts.values()
print(max(vals), min(vals), max(vals)-min(vals))
