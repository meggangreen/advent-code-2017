def part_one(filepath):
    with open(filepath) as file:
        path = file.read().split(',')

    nodes = {'nw': 0, 'n': 0, 'ne': 0, 'sw': 0, 's': 0, 'se': 0}
    opps = {'nw': 'se', 'n': 's', 'ne': 'sw', 'sw': 'ne', 's': 'n', 'se': 'nw'}

    for node in path:
        if nodes[opps[node]] > 0:
            nodes[opps[node]] += -1
        else:
            nodes[node] += 1

    if nodes['nw'] and nodes['s']:
        while nodes['nw'] > 0 and nodes['s'] > 0:
            nodes['sw'] += 1
            nodes['s'] += -1
            nodes['nw'] += -1
    if nodes['ne'] and nodes['s']:
        while nodes['ne'] > 0 and nodes['s'] > 0:
            nodes['se'] += 1
            nodes['s'] += -1
            nodes['ne'] += -1
    if nodes['sw'] and nodes['n']:
        while nodes['sw'] > 0 and nodes['n'] > 0:
            nodes['nw'] += 1
            nodes['n'] += -1
            nodes['sw'] += -1
    if nodes['se'] and nodes['n']:
        while nodes['se'] > 0 and nodes['n'] > 0:
            nodes['ne'] += 1
            nodes['n'] += -1
            nodes['se'] += -1

    return sum(nodes.values())


################################################################################
if __name__ == '__main__':
    print(f"Part 1: {part_one('11.txt')}")
