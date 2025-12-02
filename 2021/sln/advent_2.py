def sol2():
    # PART 1
    file = open("data/advent_2.txt").read()
    instructions = file.splitlines()

    horizontal = 0
    depth = 0
    depth2 = 0
    aim = 0

    for i in instructions:
        direction, number = i.split(" ")
        if direction == "forward":
            horizontal += int(number)
            depth2 += aim * int(number)
        elif direction == "up":
            depth -= int(number)
            aim -= int(number)
        elif direction == "down":
            depth += int(number)
            aim += int(number)

    return [horizontal * depth, horizontal * depth2]
