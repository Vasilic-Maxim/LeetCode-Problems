from typing import List


class Solution:
    """
    Time: O(3 ^ N)
    Space: O(N)
    """

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = col = None
        opened = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    row, col = i, j
                elif grid[i][j] == 0:
                    opened += 1

        return self.traverse(grid, row, col, opened + 1)

    def traverse(self, grid: List[List[int]], row: int, col: int, to_open: int) -> int:
        if grid[row][col] == 2:
            return int(to_open == 0)

        tmp = grid[row][col]
        grid[row][col] = -1
        to_open -= 1

        unique_paths = 0

        for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = row + ro, col + co

            if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
                continue
            if grid[next_row][next_col] == -1:
                continue

            unique_paths += self.traverse(grid, next_row, next_col, to_open)

        grid[row][col] = tmp

        return unique_paths
