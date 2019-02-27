""" Day 7 P1 and P2 """

import re, copy

class Node:
    def __init__(self, title, weight=0, children=None):
        self.title = title
        self.weight = weight
        self.children = children if children else []

    def __repr__(self):
        return f'<Node {self.title} {self.weight}>'


def make_nodes_edges(filepath):

    title_patt = re.compile(r'^\w+(?= )')
    weight_patt = re.compile(r'(?<=\()[\d]+(?=\))')
    childs_patt = re.compile(r'(?<=-> )[\w ,]+$')

    with open(filepath) as file:
        lines = file.readlines()

    # get nodes
    nodes = {}
    for ln in lines:
        title = re.match(title_patt, ln)[0]
        weight = int(re.search(weight_patt, ln)[0])
        nodes[title] = Node(title, weight)

    edges = []
    for ln in lines:
        title = re.match(title_patt, ln)[0]
        children = re.search(childs_patt, ln)
        children = children[0].split(', ') if children else []
        for child in children:
            edges.append((title, child))
            nodes[title].children.append(nodes[child])

    return nodes, edges


def get_roots(edges):

    parents, children = zip(*edges)
    return set(parents).difference(children)


def part_two_solution(filepath):
    """ I wanted to do it without networkx, but then I got distracted and bored """

    def populate(node):
        sub_tree = {child_node: populate(child_node) for child_node in children[node]}
        child_full_weights = [full_weights[child_node] for child_node in children[node]]
        full_weights[node] = weights[node] + sum(child_full_weights)
        if len(set(child_full_weights)) > 1:
            target_weight = max(set(child_full_weights), key=child_full_weights.count)
            actual_weight = min(set(child_full_weights), key=child_full_weights.count)
            unbalanced[actual_weight] = weights[children[node][child_full_weights.index(actual_weight)]] + (target_weight - actual_weight)
        return sub_tree

    tree, children, weights, unbalanced = {}, {}, {}, {}

    for line in open(filepath):
        parts = re.split(r"\s\(|\)\s->\s|\)$", line.splitlines()[0])
        weights[parts[0]] = int(parts[1])
        children[parts[0]] = [word for word in (parts[2].split(", ") if parts[2] else [])]

    full_weights = copy.deepcopy(weights)

    for name in list(children.keys()):
        if name not in [word for children in children.values() for word in children]:
            tree[name] = populate(name)

    return unbalanced[min(unbalanced.keys())]


################################################################################
if __name__ == '__main__':
    filepath = '07.txt'
    nodes, edges = make_nodes_edges(filepath)
    pt1 = get_roots(edges).pop()



    print(f"Part 1: {pt1}")
    print(f"Part 2: {part_two_solution(filepath)}")
