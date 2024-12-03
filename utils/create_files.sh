touch $1/data/aoc_$2.txt

touch $1/test/test_aoc_$2.txt

echo "TEST = 1
day = __file__.split(\"\\\\\")[-1][:-3]

path = f'2024/test/test_{day}.txt' if TEST else f'2024/data/{day}.txt'

data = open(path, 'r').read().splitlines()
print(data)" > $1/sln/aoc_$2.py