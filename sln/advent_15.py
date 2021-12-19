# https://stackabuse.com/dijkstras-algorithm-in-python/
from queue import PriorityQueue
import numpy as np

with open('../data/advent_15.txt') as f:
    data = np.array(f.read().splitlines())

np.set_printoptions(linewidth=len(data[0]))

print(data)


def adj(node):
    i = node[0]
    j = node[1]

    n = len(data[0])
    m = len(data)

    adjacent_indices = []

    # North
    # if i > 0:
    #    adjacent_indices.append((i - 1, j))

    # South
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))

    # West
    # if j > 0:
    #    adjacent_indices.append((i, j - 1))

    # East
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))

    return adjacent_indices


def find_shortest_path(graph, start):
    positions = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            positions.append((i, j))

    D = {v: float('inf') for v in positions}

    D[start] = 0

    print(D)

    pq = PriorityQueue()
    pq.put((0, start))
    visited = []

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

    neighbours = adj(start)

    for neighbour in neighbours:
        x = neighbour[0]
        y = neighbour[1]
        distance = int(graph[x][y])
        if neighbour not in visited:
            old_cost = D[neighbour]
            new_cost = D[current_vertex] + distance

            if new_cost < old_cost:
                pq.put((new_cost, neighbour))
                D[neighbour] = new_cost

    print(D)

    return D


find_shortest_path(data, (0, 0))
