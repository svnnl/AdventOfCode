with open('../data/advent_5.txt') as f:
    data = list(map(int, f.read().split(',')))

print(data)

END_COMMAND = 99
ADDITION_COMMAND = 1
MULTIPLY_COMMAND = 2
STORE_COMMAND = 3
OUTPUT_COMMAND = 4
JUMP_TRUE_COMMAND = 5
JUMP_FALSE_COMMAND = 6
LESS_THAN_COMMAND = 7
EQUAL_COMMAND = 8


def get_value(program, value, mode):
    return value if mode else program[value]


def run_intcode(input):
    output = None
    program = data.copy()
    position = 0

    while program[position] != END_COMMAND:
        current_command = program[position]
        position += 1

        mode3, current_command = divmod(current_command, 10000)
        mode2, current_command = divmod(current_command, 1000)
        mode1, current_command = divmod(current_command, 100)

        # Opcode 1: Addition(x1,x2) -> x3
        if current_command == ADDITION_COMMAND:
            x1, x2, pos = program[position:position + 3]
            program[pos] = get_value(program, x1, mode1) + get_value(program, x2, mode2)
            position += 3

        # Opcode 2: Multiply(x1,x2) -> x3
        elif current_command == MULTIPLY_COMMAND:
            x1, x2, pos = program[position: position + 3]
            program[pos] = get_value(program, x1, mode1) * get_value(program, x2, mode2)
            position += 3

        # Opcode 3: Store(input) -> x1
        elif current_command == STORE_COMMAND:
            pos = program[position]
            program[pos] = input
            position += 1

        # Opcode 4: Output(x1) -> output
        elif current_command == OUTPUT_COMMAND:
            pos = program[position]
            output = get_value(program, pos, mode1)
            position += 1

        # Opcode 5: if(x1) -> jump(x2)
        elif current_command == JUMP_TRUE_COMMAND:
            x1, x2 = program[position:position + 2]
            position += 2

            if get_value(program, x1, mode1) != 0:
                position = get_value(program, x2, mode2)

        # Opcode 6: if(!x1) -> jump(x2)
        elif current_command == JUMP_FALSE_COMMAND:
            x1, x2 = program[position: position + 2]
            position += 2

            if get_value(program, x1, mode1) == 0:
                position = get_value(program, x2, mode2)

        # Opcode 7: if_less(x1,x2) -> x3
        elif current_command == LESS_THAN_COMMAND:
            x1, x2, pos = program[position:position + 3]
            program[pos] = 1 if get_value(program, x1, mode1) < get_value(program, x2, mode2) else 0
            position += 3

        # Opcode 8: if_equal(x1,x2) -> x3
        elif current_command == EQUAL_COMMAND:
            x1, x2, pos = program[position:position + 3]
            program[pos] = 1 if get_value(program, x1, mode1) == get_value(program, x2, mode2) else 0
            position += 3

        else:
            pass

    return output


print(f'Answer to Part 1: {run_intcode(1)}')
print(f'Answer to Part 2: {run_intcode(5)}')
