with open("../data/advent_5.txt") as f:
    data, instructions = [i.split("\n") for i in f.read().split("\n\n")]

stacks = [""] * 10

for row in data[:-1]:
    for i, v in enumerate(row[1::4]):
        if v != " ":
            stacks[i + 1] += v

stacks_2 = stacks.copy()


def move(n, source, destination):
    popped_value = stacks[source][:n]
    new_value = stacks[source][n:]
    stacks[source] = new_value
    stacks[destination] = popped_value[::-1] + stacks[destination]


def move_2(n, source, destination):
    popped_value = stacks_2[source][:n]
    new_value = stacks_2[source][n:]
    stacks_2[source] = new_value
    stacks_2[destination] = popped_value + stacks_2[destination]


for i in instructions:
    _, n, _, source, _, destination = i.split(" ")
    move(int(n), int(source), int(destination))
    move_2(int(n), int(source), int(destination))

print(f'Answer to Part 1: {"".join([i[0] for i in stacks if i])}')
print(f'Answer to Part 2: {"".join(i[0] for i in stacks_2 if i)}')
