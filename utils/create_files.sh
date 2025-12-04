mkdir -p $1/data
mkdir -p $1/test

touch $1/data/aoc_$2.txt

touch $1/test/test_aoc_$2.txt

echo "TEST = 1
day = __file__.split(\"\\\\\")[-1][:-3]

path = f'$1/test/test_{day}.txt' if TEST else f'$1/data/{day}.txt'

data = open(path, 'r').read().splitlines()
print(data)" > $1/sln/aoc_$2.py
