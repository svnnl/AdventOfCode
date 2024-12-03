import re

with open('../data/advent_7.txt') as f:
    data = f.read().splitlines()


def get_root_nodes(graph):
    return [key for key, value in graph.items() if all(key not in v for k, v in graph.items())]


def get_weight(node):
    stacks = []

    for child in graph[node]:
        if child in graph.keys():
            values = get_weight(child)
            value = sum(values) + weights[child]
        else:
            value = weights[child]
        stacks.append(value)
    if len(set(stacks)) != 1:
        print(f'Issue  on {node}, due to children {graph[node]}, weighing {stacks}')
    return stacks


graph = {}
for i in data:
    if '->' in i:
        graph[i.split(' -> ')[0].split(' ')[0]] = i.split(' -> ')[1].split(', ')

weights = {}
for i in data:
    weights[i.split(' ')[0]] = int(re.sub(r"[()]", '', i.split(' ')[1]))

root = get_root_nodes(graph)[0]
print(f'Answer to Part 1: {root}')
print(f'Answer to Part 2: {get_weight(root)}')
