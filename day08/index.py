import itertools
import math


def parse(file):
    dirn, nodedata = file.read().split('\n\n')
    dirn = (list(dirn))
    nodes = {}
    for node in nodedata.split('\n'):
        if not node:
            continue
        name, edges = node.split(' = ')
        edges = edges.strip("()").split(', ')
        nodes[name] = tuple(edges)
    return dirn, nodes


def part_one(file):
    dirn, nodes = parse(file)
    dirn = itertools.cycle(dirn)
    curr_node = "AAA"
    num_steps = 0
    for d in dirn:
        i = 0 if d == 'L' else 1
        curr_node = nodes[curr_node][i]
        num_steps += 1
        if curr_node == "ZZZ":
            break

    return num_steps


def part_two_slow(file):
    dirn, nodes = parse(file)
    dirn = itertools.cycle(dirn)
    curr_nodes = filter(lambda k: k.endswith("A"), nodes.keys())
    num_steps = 0
    for d in dirn:
        i = 0 if d == "L" else 1
        curr_nodes = [nodes[n][i] for n in curr_nodes]
        num_steps += 1
        if all([n.endswith("Z") for n in curr_nodes]):
            break

    return num_steps


# HALT = True


def part_two(file):
    dirn, nodes = parse(file)
    curr_nodes = list(filter(lambda k: k.endswith("A"), nodes.keys()))
    num_steps = [0 for _ in curr_nodes]
    for i, node in enumerate(curr_nodes):
        curr = node
        _dir = itertools.cycle(dirn)
        for d in _dir:
            j = 0 if d == "L" else 1
            curr = nodes[curr][j]
            num_steps[i] += 1
            if curr.endswith("Z"):
                break
    return math.lcm(*num_steps)
