from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(1)
    """

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0]:
            return 0

        grid[0][0] = 1

        for i in range(1, m):
            grid[i][0] = 0 if grid[i][0] else grid[i - 1][0]

        for i in range(1, n):
            grid[0][i] = 0 if grid[0][i] else grid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]
