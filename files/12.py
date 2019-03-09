def parse_edges(filepath):
    with open(filepath) as file:
        lines = [ln.strip() for ln in file.readlines()]

    edges = {}
    for line in lines:
        nodes = line.split(' <-> ')
        edges[int(nodes[0])] = [int(n) for n in nodes[1].split(', ')]

    return edges


def find_connected_to(node, edges):
    nodes = set([node])

    if not edges:
        return nodes

    to_connect = set(edges[node])
    while to_connect:
        target = to_connect.pop()
        if not target in nodes:
            nodes.add(target)
            to_connect.update(edges[target])

    return nodes


def find_all_groups(edges):
    all_nodes = set(edges.keys())
    groups = []

    while all_nodes:
        group_lead = all_nodes.pop()
        group = find_connected_to(group_lead, edges)
        all_nodes.difference_update(group)
        groups.append(group)

    return groups


################################################################################
if __name__ == '__main__':
    edges = parse_edges('12.txt')
    print(f"Part 1: {len(find_connected_to(0, edges))}")
    print(f"Part 2: {len(find_all_groups(edges))}")