import numpy as np
from scipy import stats


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

    return answers
