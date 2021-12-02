def sol1():
    file = open('data/advent_1.txt').read()
    numbers = file.splitlines()

    count = 0
    for i in range(0, len(numbers) - 1):
        current = int(numbers[i])
        next = int(numbers[i+1])
        if next > current:
            count += 1

    print("Solution of Day 1 - Part 1: " + count)
