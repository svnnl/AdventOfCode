import re
import math

TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f'2024/test/test_{day}.txt' if TEST else f'2024/data/{day}.txt'

data = open(path, 'r').read()

print("Answer to Part 1: {0}".format(sum(math.prod(i) for i in list(map(int, i)
      for i in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)))))

enabled = True
r = 0
for cmd in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", data):
    if "do()" in cmd:
        enabled = True
    if "don't()" in cmd:
        enabled = False
    if enabled and (cmd[0] or cmd[1]):
        r += int(cmd[0]) * int(cmd[1])

print(f"Answer to Part 2: {r}")
