from typing import List


class Solution:
    """
    Time: O(n * m)
    Space: O(1)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, col in enumerate(grid[i]):
                top = grid[i - 1][j] if i else 0
                left = grid[i][j - 1] if j else 0
                if i and j:
                    grid[i][j] = min(top, left) + col
                else:
                    grid[i][j] = max(top, left) + col

        return grid[-1][-1]
