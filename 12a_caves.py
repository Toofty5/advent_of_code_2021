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

def traverse(visited, start_node): # return list of lists
    print(visited, start_node)
    if start_node == 'end':
        return [['end']]

    return_me = []

    for link in node_dict[start_node]:
        if link not in visited:
            visited[link] = 0

        if link[0].isupper() or visited[link] < 2 :
            visited[start_node] += 1
            next_paths = traverse(visited,link)
            for path in next_paths:
                return_me.append( [start_node] + path )

    return return_me

paths = traverse({"start":0},"start")
for path in paths:
    print(path)
print(len(paths))
