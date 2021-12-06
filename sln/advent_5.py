import numpy as np
import colorama


def color_sign(x):
    c = colorama.Fore.GREEN if x >= 2 else colorama.Fore.YELLOW if x == 1 else colorama.Fore.RED
    return f'{c}{x}'


def find_overlap(line_array, min_overlap: int) -> int:
    counter = 0
    for sub_array in line_array:
        for val in sub_array:
            if val >= min_overlap:
                counter += 1

    return counter


def sol5():
    with open('../data/advent_5.txt', 'r') as f:
        input = f.read().splitlines()

    line_array = np.zeros((10, 10), dtype=int)

    for line in input:
        print(line)
        x1, y1 = map(int, line.split(' -> ')[0].split(','))
        print('x1: ' + str(x1) + '-' + 'y1: ' + str(y1))
        x2, y2 = map(int, line.split(' -> ')[1].split(','))
        print('x2: ' + str(x2) + '-' + 'y2: ' + str(y2))
        if x1 == x2:
            print('-----Vertical Line----')
            for i in range(min(y1, y2), max(y1, y2) + 1):
                print(str(i) + ',' + str(x1))
                line_array[i][x1] += 1
        elif y1 == y2:
            print('-----Horizontal Line-----')
            for i in range(min(x1, x2), max(x1, x2) + 1):
                print(str(y1) + ',' + str(i))
                line_array[y1][i] += 1
        elif x1 == y1 and x2 == y2:
            print('------ Diagonal Line Scenario 1 -----')
            for i in range(min(x1, x2), max(x1, x2) + 1):
                print(str(i) + ',' + str(i))
                line_array[i][i] += 1
        elif x1 == y2 and x2 == y1:
            print('------ Diagonal Line Scenario 2 -----')
            minimal = min(x1, x2)
            maximal = max(x1, x2)
            for i in range(maximal - minimal + 1):
                print(str(minimal + i) + ',' + str(maximal - i))
                line_array[minimal + i][maximal - i] += 1
        else:
            if (x1 > x2 and y1 > y2) or (x2 > x1 and y2 > y1):
                print('------- Diagonal Line Scenario 3.1 -----')
                min_x = min(x1, x2)
                min_y = min(y1, y2)
                for i in range(abs(x2 - x1) + 1):
                    print(str(min_y + i) + ',' + str(min_x + i))
                    line_array[min_y + i][min_x + i] += 1
            elif x1 > x2 and y1 < y2:
                print('------- Diagonal Line Scenario 3.2 -----')
                for i in range(abs(x2 - x1) + 1):
                    print(str(y1 + i) + ',' + str(x1 - i))
                    line_array[y1 + i][x1 - i] += 1
            elif x1 < x2 and y1 > y2:
                print('------- Diagonal Line Scenario 3.3 -----')
                for i in range(abs(x2 - x1) + 1):
                    print(str(y2 + i) + ',' + str(x2 - i))
                    line_array[y2 + i][x2 - i] += 1

    np.set_printoptions(formatter={'int': color_sign})
    print(line_array)

    print('Amount of overlaps: ' + str(find_overlap(line_array, 2)))


sol5()
