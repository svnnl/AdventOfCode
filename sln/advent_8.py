with open('../data/advent_8.txt') as f:
    data = list(map(int, f.read().split()))


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def get_sum(self):
        child_sum = sum([c.get_sum() for c in self.children])
        return child_sum + sum(self.metadata)

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        value = 0
        for m in self.metadata:
            if 0 < m <= len(self.children):
                value += self.children[m - 1].get_value()
        return value

    def solve(self, data):
        num_children, num_metadata = data[0:2]
        del data[0:2]

        for i in range(num_children):
            child = Node()
            data = child.solve(data)
            self.children.append(child)

        for i in range(num_metadata):
            self.metadata.append(data[i])
        del data[:num_metadata]

        return data


root = Node()
root.solve(data)

print(f'Answer to Part 1: {root.get_sum()}')
print(f'Answer to Part 2: {root.get_value()}')
