from collections import defaultdict

with open('../data/advent_7.txt') as f:
    data = f.read().splitlines()

graph = defaultdict(list)
for line in data:
    graph[line.split()[1]] += line.split()[7]

print(graph)


def get_root_nodes(graph):
    return [key for key, value in graph.items() if all(key not in v for k, v in graph.items())]


def check_predecessor(graph, node, path):
    predecessors = []
    for k, v in graph.items():
        if node in v:
            predecessors.append(k)

    return True if all(i in path for i in predecessors) else False


def get_next_node(graph, available, path):
    for i in sorted(available):
        if check_predecessor(graph, i, path):
            return i


def traverse(graph, available):
    path = ''

    while len(available) != 0:
        print(f'Current path: {path}')
        print(f'Current available nodes: {available}')
        next = get_next_node(graph, available, path)
        path += next
        available += [i for i in graph[next] if i not in available and i not in path]
        available.remove(next)

    return path


path = traverse(graph, get_root_nodes(graph))
print(f'Answer to Part 1: {path}')


def process(path, workers, start_time):
    total = 0
    for i in path:
        total += ord(i) - 64

    return total


print(process(path, 1, 0))
