from itertools import chain
from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0

        for i in range(n):
            max_row = max_col = 0
            for j in range(n):
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
                if grid[i][j]:
                    result += 1
            result += max_row + max_col

        return result
