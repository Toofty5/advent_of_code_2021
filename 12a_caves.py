lines = [line.strip().split("-") for line in open("input", "r").readlines()]

node_dict = {}

for a,b in lines:
    if a in node_dict:
        node_dict[a].append(b)
    else:
        node_dict[a] = [b]
    if b in node_dict:
        node_dict[b].append(a)
    else:
        node_dict[b] = [a]

for node in node_dict:
    print(node, node_dict[node])

def traverse(visited, start_node, small_cave): # return list of lists
#    print(visited, start_node, small_cave)
    if start_node == 'end':
        return [['end']]

    return_me = []

    for link in node_dict[start_node]:
        if link != "start":
            if link[0].isupper() or link not in visited :
                next_paths = traverse(visited + [start_node],link, small_cave)
                for path in next_paths:
                    return_me.append( [start_node] + path )
            elif not small_cave: #not upper and is visited
                next_paths = traverse(visited + [start_node],link, True)
                for path in next_paths:
                    return_me.append( [start_node] + path )


    return return_me

paths = traverse([],"start", False)
print(len(paths))
