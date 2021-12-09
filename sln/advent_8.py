def sol8():
    with open('../data/advent_8.txt') as f:
        data = f.read().splitlines()

    # PART 1
    count = 0
    for line in data:
        count += sum([1 for i in line.split(' | ')[1].split(' ') if len(i) in [2, 3, 4, 7]])

    print(count)

    # PART 2

    def create_options(s1, s2):
        options = []
        for i in s2:
            options.append(s1.replace(i, ''))
        return options

    def find_number(values, options):
        return [i for i in options if i in values]

    result = 0
    for line in data:
        input_values = [''.join(sorted(i)) for i in line.split(' | ')[0].split(' ')]
        output_values = [''.join(sorted(i)) for i in line.split(' | ')[1].split(' ')]
        print('{0} | {1} '.format(input_values, output_values))

        digits_with_5 = [i for i in input_values if len(i) == 5]
        digits_with_6 = [i for i in input_values if len(i) == 6]

        one = [i for i in input_values if len(i) == 2][0]
        four = [i for i in input_values if len(i) == 4][0]
        seven = [i for i in input_values if (len(i) == 3)][0]
        eight = [i for i in input_values if len(i) == 7][0]
        six = find_number(digits_with_6, create_options(eight, one))[0]
        five = find_number(digits_with_5, create_options(six, eight))[0]
        nine = eight.replace(set(six).symmetric_difference(set(five)).pop(), '')
        zero = [i for i in digits_with_6 if i not in [nine, six]][0]
        three = find_number(digits_with_5, create_options(nine, six))[0]
        two = [i for i in digits_with_5 if i not in [five, three]][0]

        numbers = {
            '1': one,
            '2': two,
            '3': three,
            '4': four,
            '5': five,
            '6': six,
            '7': seven,
            '8': eight,
            '9': nine,
            '0': zero
        }

        print(
            "1: {0}, 2: {1}, 3: {2}, 4: {3}, 5: {4}, 6: {5}, 7: {6}, 8: {7}, 9: {8}, 0: {9}".format(one, two, three,
                                                                                                    four, five,
                                                                                                    six,
                                                                                                    seven, eight, nine,
                                                                                                    zero))

        output = ''
        for i in output_values:
            output += list(numbers.keys())[list(numbers.values()).index(i)]

        print('Output: {0}'.format(output))
        result += int(output)

    print('Sum of all numbers: {0}'.format(result))


sol8()
