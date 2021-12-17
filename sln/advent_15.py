# https://stackabuse.com/dijkstras-algorithm-in-python/
from queue import PriorityQueue
import numpy as np

with open('../data/advent_15.txt') as f:
    data = np.array(f.read().splitlines())

np.set_printoptions(linewidth=len(data[0]))

print(data)


def neighbours(node):
    pass


def find_shortest_path(graph, visited):
    shortest_path = []
    pass
