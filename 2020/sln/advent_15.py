with open("../data/advent_15.txt") as f:
    data = list(map(int, f.read().split(",")))


def play(numbers, turns):
    # Keep track of last time a number was spoken: key = (last_spoken, count)
    last_position = {}

    for i, v in enumerate(numbers[:-1]):
        last_position[v] = i + 1

    next_number = data[-1]

    for i in range(len(numbers) + 1, turns + 1):
        last_turn = i - 1
        if next_number in last_position:
            next_spoken = last_turn - last_position[next_number]
        else:
            next_spoken = 0
        last_position[next_number] = last_turn

        next_number = next_spoken

    return next_number


print(f"Answer to Part 1: {play(data, 2020)}")
print(f"Answer to Part 2: {play(data, 30000000)}")
