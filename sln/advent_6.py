def fish_count(input, days):
    fish_array = [input.count(i) for i in range(9)]
    for day in range(days):
        nn = fish_array[0]
        fish_array[0:8] = fish_array[1:9]
        fish_array[6] += nn
        fish_array[8] = nn
    return sum(fish_array)


def sol6():
    with open('data/advent_6.txt', 'r') as f:
        input = list(map(int, f.read().split(',')))

    return [fish_count(input, 80), fish_count(input, 256)]
