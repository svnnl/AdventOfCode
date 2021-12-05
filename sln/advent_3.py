import numpy as np
from scipy import stats


def find_rating(is_oxygen: bool, binary_array: list) -> str:
    i = 0
    while len(binary_array) != 1:
        mode, count = stats.mode([item[i] for item in binary_array])
        if is_oxygen:
            mode = '1' if count == len(binary_array) / 2 else mode
        else:
            if mode == '1' or count == len(binary_array) / 2:
                mode = '0'
            elif mode == '0':
                mode = '1'

        binary_array = [j for j in binary_array if j[i] == mode]
        i += 1

    return ''.join(map(str, binary_array[0]))


def sol3():
    answers = []

    # PART 1
    file = np.loadtxt("data/advent_3.txt", dtype=str)
    binary_array = np.array([list(i) for i in file])

    modes = []

    for i in range(0, 12):
        mode = stats.mode([item[i] for item in binary_array])[0]
        modes.append(int(mode))

    gamma = ''.join(map(str, modes))
    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

    answers.append(int(gamma, 2) * int(epsilon, 2))

    # PART 2
    ogr = find_rating(True, binary_array)
    csr = find_rating(False, binary_array)

    answers.append(int(ogr, 2) * int(csr, 2))

    return answers
