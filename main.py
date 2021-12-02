import os
import PySimpleGUI as sg
from sln.advent_1 import sol1
from sln.advent_2 import sol2


def run_solution(option):
    if option == '1':
        answer = sol1()
    elif option == '2':
        answer = sol2()

    for i in range(0, len(answer)):
        print("Solution of Day " + option + " - Part " + str(i + 1) + ": " + str(answer[i]))


def menu():
    print("Below are the available solutions to run:")
    for file in os.listdir('sln'):
        if file == '__pycache__':
            continue
        print(file)
    answer = input('Select the number of the Advent code you want to run:')

    run_solution(answer)


if __name__ == '__main__':
    sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
    menu()
