# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
import collections

with open("../data/advent_12.txt") as f:
    data = f.read().splitlines()

graph = collections.defaultdict(list)

for i in data:
    graph[i.split("-")[0]].append(i.split("-")[1])
    graph[i.split("-")[1]].append(i.split("-")[0])


def find_paths(path):
    tail = path[-1]

    if tail == "end":
        return [path]

    paths = []

    for cave in graph[tail]:
        if cave.islower() and cave in path:
            continue
        paths.extend(find_paths(path + [cave]))
    return paths


paths = find_paths(["start"])
print("Part 1: ", len(paths))


def paths_with_single_revisit(start_path, can_revisit_small=True):
    tail = start_path[-1]
    if tail == "end":
        return [start_path]
    paths = []
    for cave in graph[tail]:
        if cave == "start":
            continue
        if cave.islower() and cave in start_path:
            if can_revisit_small:
                paths.extend(paths_with_single_revisit(start_path + [cave], False))
        else:
            paths.extend(
                paths_with_single_revisit(start_path + [cave], can_revisit_small)
            )
    return paths


paths = paths_with_single_revisit(["start"])
print("Part 2: ", len(paths))
