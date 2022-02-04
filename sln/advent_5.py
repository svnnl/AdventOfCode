with open('../data/advent_5.txt') as f:
    data = list(map(int, f.read().split(',')))

print(data)

END_COMMAND = 99
ADDITION_COMMAND = 1
MULTIPLY_COMMAND = 2
STORE_COMMAND = 3
OUTPUT_COMMAND = 4


def run_intcode(noun, verb):
    program = data.copy()
    position = 0
    program[1] = noun
    program[2] = verb

    while program[position] != END_COMMAND:
        current_command = program[position]
        if current_command == ADDITION_COMMAND:
            program[program[position + 3]] = program[program[position + 1]] + program[program[position + 2]]
        elif current_command == MULTIPLY_COMMAND:
            program[program[position + 3]] = program[program[position + 1]] * program[program[position + 2]]
        elif current_command == STORE_COMMAND:
            pass
        elif current_command == OUTPUT_COMMAND:
            pass

        position += 4

    return program[0]
