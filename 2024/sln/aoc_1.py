TEST = 1
day = __file__.split("\\")[-1][:-3]

path = f"2024/test/test_{day}.txt" if TEST else f"2024/data/{day}.txt"

data = [i.replace("\n", "") for i in open(path, "r").readlines()]

list_1 = []
list_2 = []

for line in data:
    a, b = line.split("   ")
    list_1.append(int(a))
    list_2.append(int(b))


print(
    f"""Answer to Part 1: {sum([abs(int(sorted(list_1)[i]) - int(sorted(list_2)[i]))
                                for i in range(len(list_1))])}"""
)

print(f"""Answer to Part 2: {sum([value * list_2.count(value) for value in list_1])}""")
