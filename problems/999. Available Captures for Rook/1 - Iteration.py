from itertools import chain
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[int]]):
        for i, figure in enumerate(chain(*board)):
            if figure == 'R':
                x0, y0 = divmod(i, 8)

        result = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8 and board[x][y] != 'B':
                if board[x][y] == 'p':
                    result += 1
                    break
                x, y = x + i, y + j
        return result
