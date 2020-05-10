from typing import List


class Solution:
    """
    m - len(grid)
    n - len(grid[0])
    Time: O(m * n)
    Space: O(m * n)
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.bfs(grid, i, j)

    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 1

        if grid[i][j] == -1:
            return 0

        grid[i][j] = -1

        return (self.bfs(grid, i - 1, j) +
                self.bfs(grid, i + 1, j) +
                self.bfs(grid, i, j - 1) +
                self.bfs(grid, i, j + 1))
