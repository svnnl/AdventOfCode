data = open("../data/advent_9.txt").read().splitlines()


def move_head(dir, head):
    match dir:
        case "R":
            head[0] += 1
        case "L":
            head[0] -= 1
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1

    return head


def move_tail(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    if diff_x**2 + diff_y**2 > 2:
        tail[0] += (diff_x > 0) - (diff_x < 0)
        tail[1] += (diff_y > 0) - (diff_y < 0)

    return tail


snake = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited_1, visited_2 = set(), set()

for cmd in data:
    direction, n = cmd.split()

    for _ in range(int(n)):
        snake[0] = move_head(direction, snake[0])

        for i in range(1, 10):
            snake[i] = move_tail(snake[i - 1], snake[i])

        visited_1.add(tuple(snake[1]))
        visited_2.add(tuple(snake[9]))

print(f"Answer to Part 1: {len(set(visited_1))}")
print(f"Answer to Part 2: {len(set(visited_2))}")
