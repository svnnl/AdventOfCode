with open("../data/advent_6.txt") as f:
    data = f.read().splitlines()

map = {}

for i in data:
    left, right = i.split(")")
    map[right] = left

print(map)

total = 0
for i in map:
    current = i
    while current != "COM":
        current = map[current]
        total += 1

print(total)

santa_dist = {}
you_dist = {}
x = "SAN"
dist = 0
while x != "COM":
    x = map[x]
    santa_dist[x] = dist
    dist += 1

x = "YOU"
dist = 0
while x not in santa_dist:
    x = map[x]
    you_dist[x] = dist
    dist += 1
print(santa_dist[x] + dist - 1)
