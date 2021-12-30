import numpy as np

with open('../data/advent_15.txt') as f:
    data = f.read().splitlines()

data = np.array([[int(i) for i in x] for x in data])

print(data)


def adj(node):
    i, j = node

    n = len(data[0])
    m = len(data)

    adjacent_indices = set()

    # North
    if i > 0:
        adjacent_indices.add((i - 1, j))

    # South
    if i + 1 < m:
        adjacent_indices.add((i + 1, j))

    # West
    if j > 0:
        adjacent_indices.add((i, j - 1))

    # East
    if j + 1 < n:
        adjacent_indices.add((i, j + 1))

    return adjacent_indices


def find_shortest_path(data, start, dest_node):
    print(data.shape)
    visited = np.zeros(data.shape, dtype=bool)
    distance_matrix = np.full(data.shape, np.inf, dtype=float)
    distance_matrix[start] = 0
    current_node = start

    while not visited[dest_node]:
        if not visited[current_node]:
            print(current_node)
            neighbours = adj(current_node)
            for neighbour in neighbours:
                if distance_matrix[current_node] + data[neighbour] < distance_matrix[neighbour]:
                    distance_matrix[neighbour] = distance_matrix[current_node] + data[neighbour]
            visited[current_node] = True
        nodes_min_d = np.where(np.logical_and(distance_matrix == np.amin(distance_matrix[np.invert(visited)]),
                                              np.invert(visited))
                               )
        current_node = (nodes_min_d[0][0], nodes_min_d[1][0])
        if current_node == dest_node:
            return distance_matrix[dest_node]
    return distance_matrix[dest_node]


# Part 1
print("Answer to Part 1 is {0}".format(find_shortest_path(data, (0, 0), (data.shape[0] - 1, data.shape[1] - 1))))


# Part 2
def create_large_cave(cave):
    old = np.copy(cave)
    result = np.copy(cave)
    for i in range(4):
        new_cols = old + np.ones(cave.shape, dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.c_[result, new_cols]
        old = result[:, -cave.shape[0]:]
    old = result
    for i in range(4):
        new_cols = old + np.ones((cave.shape[0], cave.shape[1] * 5), dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.r_[result, new_cols]
        old = result[-cave.shape[0]:, :]
    return result


large_cave = create_large_cave(data)
print("Answer to Part 2 is: {0}".format(
    find_shortest_path(large_cave, (0, 0), (large_cave.shape[0] - 1, large_cave.shape[1] - 1))))
