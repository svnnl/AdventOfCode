def sol1():
    file = open("data/advent_1.txt").read()
    numbers = list(map(int, file.splitlines()))

    answers = []

    # PART 1
    count = 0
    for i in range(0, len(numbers) - 1):
        current = numbers[i]
        next = numbers[i + 1]
        if next > current:
            count += 1

    answers.append(count)

    # PART 2
    count = 0
    for i in range(0, len(numbers) - 3):
        current = numbers[i]
        second = numbers[i + 1]
        third = numbers[i + 2]
        fourth = numbers[i + 3]
        if sum([second, third, fourth]) > sum([current, second, third]):
            count += 1

    answers.append(count)

    return answers
