def parse_edges(filepath):
    with open(filepath) as file:
        lines = [ln.strip() for ln in file.readlines()]

    edges = {}
    for line in lines:
        nodes = line.split(' <-> ')
        edges[nodes[0]] = nodes[1].split(', ')

    return edges


def find_connected_to(node='0', edges=None):
    nodes = set(node)

    if not edges:
        return nodes

    to_connect = set(edges[node])
    while to_connect:
        target = to_connect.pop()
        if not target in nodes:
            nodes.add(target)
            to_connect.update(edges[target])

    return nodes


################################################################################
if __name__ == '__main__':
    edges = parse_edges('12.txt')
    print(f"Part 1: {len(find_connected_to(node='0', edges=edges))}")
