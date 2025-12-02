with open("../data/advent_2.txt") as f:
    data = f.read().splitlines()

count = 0
new_count = 0

for i in data:
    policy, password = i.split(": ")
    value, letter = policy.split(" ")
    _min, _max = map(int, value.split("-"))

    if _min <= password.count(letter) <= _max:
        count += 1

    if (password[_min - 1] == letter) != (password[_max - 1] == letter):
        new_count += 1

print("Answer to Part 1 is: {0} ".format(count))
print("Answer to Part 2 is: {0} ".format(new_count))
