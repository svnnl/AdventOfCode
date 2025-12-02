# import pandas as pd
# import re
from collections import defaultdict
from datetime import datetime

with open("../data/advent_4.txt") as f:
    data = sorted(
        f.read().splitlines(),
        key=lambda x: datetime.strptime(f"{x[1:17]}", "%Y-%m-%d %H:%M"),
    )

# rows = []
# for index, i in enumerate(data):
#     date = i[1:17]
#     event = i[19:]
#
#     print(event)
#
#     if event[0] == 'G':
#         rows.append([date[5:11], re.findall(r'\d+', event)[0], ''])
#     elif event[0] == 'f':
#         rows.append([date[5:11], rows[-1][1], [*range(int(data[index][15:17]), int(data[index + 1][15:17]))]])
#     else:
#         pass
#
# roster = pd.DataFrame(rows, columns=['Date', 'ID', 'Minutes'])
# print(roster.groupby(by=['Date', 'ID']).agg({'Minutes': lambda x: list(x)}))

C = defaultdict(int)
CM = defaultdict(int)
guard = None
start = None

for line in data:
    if line:
        time = int(line[15:17])
        if "begins shift" in line:
            guard = int(line.split()[3][1:])
            start = None
        elif "falls asleep" in line:
            start = time
        elif "wakes up" in line:
            for t in range(start, time):
                CM[(guard, t)] += 1
                C[guard] += 1

print(CM)
print(C)


def argmax(dic):
    best = None
    for k, v in dic.items():
        if best is None or v > dic[best]:
            best = k
    return best


best_guard = argmax(C)
best_min = argmax(CM[best_guard])
print(best_guard, best_min)
print(f"Answer to Part 1: {best_min * best_guard}")

best_guard2, best_min2 = argmax(CM)
print(best_guard2, best_min2)
print(f"Answer to Part 2: {best_guard2 * best_min2}")
