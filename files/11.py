from copy import deepcopy

def find_child_distance(filepath):
    with open(filepath) as file:
        path = file.read().split(',')

    nodes = {'nw': 0, 'n': 0, 'ne': 0, 'sw': 0, 's': 0, 'se': 0}
    opps = {'nw': 'se', 'n': 's', 'ne': 'sw', 'sw': 'ne', 's': 'n', 'se': 'nw'}

    max_away = 0

    for node in path:
        if nodes[opps[node]] > 0:
            nodes[opps[node]] += -1
        else:
            nodes[node] += 1

        max_away = max(max_away, sum(shorten_path(deepcopy(nodes)).values()))

    return sum(shorten_path(nodes).values()), max_away


def shorten_path(nodes):

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

    if nodes['ne'] and nodes['nw']:
        while nodes['ne'] > 0 and nodes['nw'] > 0:
            nodes['n'] += 1
            nodes['nw'] += -1
            nodes['ne'] += -1

    if nodes['se'] and nodes['sw']:
        while nodes['se'] > 0 and nodes['sw'] > 0:
            nodes['s'] += 1
            nodes['sw'] += -1
            nodes['se'] += -1

    return nodes


################################################################################
if __name__ == '__main__':
    print(f"Parts 1, 2: {find_child_distance('11.txt')}")
