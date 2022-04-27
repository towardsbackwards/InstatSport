import random
from random import choice as rnd


class TicTacToe:
    """
    Tic-Tac-Toe sample game with automatic step-by-step board fill
    """

    def __init__(self, field_size):
        self.field_size = field_size
        self.board = []
        self.move_count = 0

    def create_board(self):
        for i in range(self.field_size):
            row = []
            for j in range(self.field_size):
                row.append(None)
            self.board.append(row)

    def check_state(self):
        #  checking if any row is filled by 'X's or 'O's
        for row in self.board:
            chk = set(row)
            if len(chk) == 1 and None not in row:
                return print(f"{row[0]} won")

        #  checking if any column is filled by 'X's or 'O's
        rotated = zip(*self.board[::-1])
        for col in rotated:
            chk = set(col)
            if len(chk) == 1 and None not in col:
                return print(f"{col[0]} won")

        #  building left-top to right-bottom diagonal as top_diag
        top_diag = [self.board[i][i] for i in range(self.field_size)]
        #  checking if top_diag is filled by 'X's or 'O's
        if len(top_diag) == 1 and None not in top_diag:
            return print(f"{top_diag[0]} won")

        #  building left-bottom to right-top diagonal as bottom_diag
        bottom_diag = [self.board[self.field_size - n - 1][n] for n in range(self.field_size)]
        #  checking if bottom_diag is filled by 'X's or 'O's
        if len(bottom_diag) == 1 and None not in top_diag:
            return print(f"{bottom_diag[0]} won")

        #  if all cells are filled and still no winner
        if all([all(i) for i in self.board]):
            return print("It's a tie")

    def next_move(self):
        #  autofill empty cell as a next move with next symbol
        free_indexes = []
        self.move_count += 1
        for in_1, i in enumerate(self.board):
            for in_2, n in enumerate(i):
                if self.board[in_1][in_2] is None:
                    free_indexes.append([in_1, in_2])
        rand_index = rnd(free_indexes)
        symbol = ["X", "O"]
        self.board[rand_index[0]][rand_index[1]] = symbol[self.move_count % 2]
        self.check_state()


#  example usage
game = TicTacToe(3)
game.create_board()
[print(i) for i in game.board]
game.next_move()

