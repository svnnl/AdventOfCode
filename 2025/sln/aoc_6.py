import math
import re

TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2025/test/test_{day}.txt" if TEST else f"2025/data/{day}.txt"

data = [re.findall(r"\d+|[+*]", i) for i in open(path, "r").read().splitlines()]

cnt = 0
for i in range(len(data[0])):
    numbers = [int(data[j][i]) for j in range(len(data) - 1)]
    op = data[-1][i]
    cnt += sum(numbers) if op == "+" else math.prod(numbers)

print(f"Answer to Part 1: {cnt}")

lines = open(path, "r").read().splitlines()

cnt = 0
numbers = []
for i in range(len(lines[0]) - 1, -1, -1):
    number = "".join(line[i] for line in lines[:-1])
    if number.strip():
        numbers.append(int(number))
    op = lines[-1][i]
    if op in "+*":
        cnt += sum(numbers) if op == "+" else math.prod(numbers)
        numbers = []

print(f"Answer to Part 2: {cnt}")
