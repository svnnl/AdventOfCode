with open("../data/advent_1.txt") as f:
    data = list(map(int, f.read().splitlines()))

print(data)

for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(
                    "{0} + {1} + {2} = {3}".format(
                        data[i], data[j], data[k], data[i] + data[j] + data[k]
                    )
                )
                print(data[i] * data[j] * data[k])
