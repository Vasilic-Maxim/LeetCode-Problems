from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(m * n)
    """

    def __init__(self):
        self.memo = {}

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0)

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        if self.out_of_grid(grid, row, col) or grid[row][col]:
            return 0

        if self.finish(grid, row, col):
            return 1

        pair = (row, col)
        if pair not in self.memo:
            self.memo[pair] = (self.dfs(grid, row + 1, col) +
                               self.dfs(grid, row, col + 1))

        return self.memo[pair]

    def out_of_grid(self, grid: List[List[int]], row: int, col: int) -> bool:
        return not(0 <= row < len(grid) and 0 <= col < len(grid[0]))

    def finish(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row == len(grid) - 1 and col == len(grid[row]) - 1
