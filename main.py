import os
from sln.advent_1 import sol1
from sln.advent_2 import sol2

def run_solution(option):
    if option == '1':
        answer = sol1()
    elif option == '2':
        answer = sol2()

    for i in range(0, len(answer)):
        print("Solution of Day " + option + " - Part " + str(i+1) + ": " + str(answer[i]))

def menu():
    print('Select the number of the Advent code you want to run:')
    for file in os.listdir('sln'):
        print(file)
    answer = input()

    run_solution(answer)


if __name__ == '__main__':
    menu()
