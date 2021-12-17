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
    shortest_path = {}
    unvisited = {}

    for i in range(len(data)):
        for j in range(len(data[0])):
            unvisited.add((i, j))

    pq = PriorityQueue()

    neighbours = adj(start)

    for neighbours in neighbours:
        continue

    print(neighbours)

    print(unvisited)


find_shortest_path(data, (0, 0))
