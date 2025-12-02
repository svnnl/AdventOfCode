with open("../data/advent_4.txt") as f:
    start, end = map(int, f.read().split("-"))


def is_valid_password(password):
    valid = True
    for i in range(len(password) - 1):
        if not password[i + 1] >= password[i]:
            valid = False
    if not any(c1 == c2 for c1, c2 in zip(password, password[1:])):
        valid = False

    return valid


count = 0
for i in range(start, end):
    if is_valid_password(str(i)):
        count += 1

print(f"Answer to Part 1: {count}")


def check(n):
    return list(n) == sorted(n) and 2 in map(n.count, n)


print(f"Answer to Part 2: {sum(check(str(n)) for n in range(start, end))}")
