with open('../data/advent_5.txt') as f:
    input = list(f.read().splitlines())

scores = []


def find_missing_seat_id(seat_ids):
    shifted_seat_ids = seat_ids[1:] + [seat_ids[-1] + 1]
    diffs = list(map(lambda tup: tup[0] - tup[1], zip(shifted_seat_ids, seat_ids)))
    seat_before_missing = seat_ids[diffs.index(2)]
    return seat_before_missing + 1


def get_seat(pass_):
    row_spec, col_spec = pass_[:7], pass_[7:]
    row = bin_search(row_spec, 127)
    col = bin_search(col_spec, 7)
    return row, col


def bin_search(spec, high_bound):
    low_bound = 0
    for char in spec:
        if char in 'FL':
            high_bound = high_bound - int((high_bound - low_bound + 1) / 2)
        else:
            low_bound = low_bound + int((high_bound - low_bound + 1) / 2)

    return low_bound  # this should = high_bound


for row in input:
    row, col = get_seat(row)
    seat_id = row * 8 + col
    scores.append(seat_id)

print('Answer to Part 1: {0}'.format(max(scores)))

scores.sort()
my_seat_id = find_missing_seat_id(scores)
print('Answer to Part 2: {0}'.format(find_missing_seat_id(scores)))
