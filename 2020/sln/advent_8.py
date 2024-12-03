with open('../data/advent_8.txt') as f:
    data = f.read().splitlines()

possibilities = [i for i, v in enumerate(data) if v.split(' ')[0] in ['nop', 'jmp']]


def create_program(index):
    program = data.copy()

    if 'nop' in data[index]:
        if program[index] == 'nop +0':
            return program
        else:
            program[index].replace('nop', 'jmp')
    else:
        program[index] = program[index].replace('jmp', 'nop')

    return program


def run(program, accumulator, next_command):
    operation, argument = program[next_command].split(' ')
    if operation == 'nop':
        next_command += 1
    elif operation == 'jmp':
        next_command += int(argument)
    elif operation == 'acc':
        accumulator += int(argument)
        next_command += 1
    else:
        pass

    return accumulator, next_command


# Part 1

visited = set()
accumulator = 0
next_command = 0
last_change = 0

while not next_command in visited:
    visited.add(next_command)
    accumulator, next_command = run(data, accumulator, next_command)

print('Answer to Part 1: {0}'.format(accumulator))

# Part 2

for i in range(len(possibilities)):
    visited = set()
    accumulator = 0
    next_command = 0

    program = create_program(possibilities[i])

    while next_command not in visited:
        try:
            visited.add(next_command)
            accumulator, next_command = run(program, accumulator, next_command)
        except IndexError:
            print('Answer to Part 2: {0}'.format(accumulator))
            break
