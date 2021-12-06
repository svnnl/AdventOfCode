import numpy as np


class BingoBoard:
    def __init__(self, board, numbers):
        if board[0] == '':
            self.board = board[1:]
        else:
            self.board = board

        self.bingo_count = 0
        self.bingo_found = False

        self.create_array()

        for number in numbers:
            self.bingo_count += 1
            self.check_number(number)
            if self.bingo_found:
                self.score = self.get_score(number)
                break

    def create_array(self):
        self.board_array = np.array([np.array(row.split(' ')) for row in self.board.split('\n')])
        for index, sub_array in enumerate(self.board_array):
            if '' in sub_array:
                temp_arr = list(sub_array)
                temp_arr.remove('')
                self.board_array[index] = np.array(temp_arr)

    def check_bingo(self):
        for sub_array in self.board_array:
            if list(sub_array) == ['X', 'X', 'X', 'X', 'X']:
                self.bingo_found = True
        for i in range(0, 5):
            if [sub_array[i] for sub_array in self.board_array] == ['X', 'X', 'X', 'X', 'X']:
                self.bingo_found = True

    def check_number(self, number):
        for index, sub_array in enumerate(self.board_array):
            if number in sub_array:
                sub_array = np.where(sub_array == number, 'X', sub_array)
                self.board_array[index] = sub_array
                self.check_bingo()

    def get_score(self, number):
        self.board_sum = 0
        for sub_array in self.board_array:
            for val in sub_array:
                if val != 'X':
                    print('Current Board Sum: ' + str(self.board_sum))
                    self.board_sum += int(val)
        return self.board_sum * int(number)


def sol4():
    with open('../data/advent_4.txt', 'r') as f:
        input = f.read().replace('  ', ' ')

    numbers = input.split('\n\n')[0].split(',')
    boards = input.split('\n\n')[1:]

    lowest_turns = 2000
    highest_turns = 0

    for board in boards:
        current_board = BingoBoard(board, numbers)
        if current_board.bingo_count <= lowest_turns:
            lowest_turns = current_board.bingo_count
            best_board = current_board
        if current_board.bingo_count >= highest_turns:
            highest_turns = current_board.bingo_count
            worst_board = current_board

    print('---------BEST BOARD---------')
    print('Amount of turns before bingo: ' + str(best_board.bingo_count))
    print(best_board.board_array)
    print(best_board.score)
    print('----------WORST BOARD--------')
    print('Amount of turns before bingo: ' + str(worst_board.bingo_count))
    print(worst_board.board_array)
    print(worst_board.score)


sol4()
