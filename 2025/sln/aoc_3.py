TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2025/test/test_{day}.txt" if TEST else f"2025/data/{day}.txt"

data = [list(map(int, bank)) for bank in open(path).read().splitlines()]


def solve(line, total_digits):
    value = ""
    starting_index = 0

    for i in range(total_digits):
        end = len(line) - (total_digits - i - 1)
        next_largest = max(line[starting_index:end])
        index = line.index(next_largest, starting_index, end)
        value += str(next_largest)
        starting_index = index + 1

    return int(value)


print(f"Answer to Part 1: {sum(solve(bank, 2) for bank in data)}")
print(f"Answer to Part 2: {sum(solve(bank, 12) for bank in data)}")
