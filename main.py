import os
from sln.advent_1 import sol1

def run_solution(option):
    print(option)


def menu():
    print('Select the number of the Advent code you want to run:')
    for file in os.listdir('sln'):
        print(file)
    option = input()
    os.system('cls')

    run_solution(option)


if __name__ == '__main__':
    sol1()
