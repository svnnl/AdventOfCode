with open("../data/advent_2.txt") as f:
    data = list(map(int, f.read().split(",")))

END_COMMAND = 99
ADDITION_COMMAND = 1
MULTIPLY_COMMAND = 2


def run_intcode(noun, verb):
    program = data.copy()
    position = 0
    program[1] = noun
    program[2] = verb

    while program[position] != END_COMMAND:
        current_command = program[position]
        if current_command == ADDITION_COMMAND:
            program[program[position + 3]] = (
                program[program[position + 1]] + program[program[position + 2]]
            )
        elif current_command == MULTIPLY_COMMAND:
            program[program[position + 3]] = (
                program[program[position + 1]] * program[program[position + 2]]
            )
        position += 4

    return program[0]


print(f"Answer to Part 1: {run_intcode(12, 2)}")

for noun in range(0, 100):
    for verb in range(0, 100):
        if run_intcode(noun, verb) == 19690720:
            print(f"Answer to Part 2: {100 * noun + verb}")
            break
