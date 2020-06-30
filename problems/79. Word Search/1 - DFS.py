from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.rows = None
        self.cols = None
        self.chars = None
        self.gradients = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        # check if all data was given
        if not board or not word:
            return False

        # before we explore the board let's check if there
        # are necessary number of specific characters to
        # made the target word
        board_counter = Counter(chain(*board))
        word_counter = Counter(word)
        if word_counter - board_counter:
            return False

        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        self.chars = len(word)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.explore(row, col):
                    return True

    def explore(self, i: int, j: int, idx: int = 0) -> bool:
        if self.on_board(i, j) or self.board[i][j] != self.word[idx]:
            return False

        if idx == self.chars - 1:
            return True

        cell_value, self.board[i][j] = self.board[i][j], '#'

        for (di, dj) in self.gradients:
            if self.explore(i + di, j + dj, idx + 1):
                return True

        self.board[i][j] = cell_value

        return False

    def on_board(self, i: int, j):
        return not (0 <= i < self.rows and 0 <= j < self.cols)
