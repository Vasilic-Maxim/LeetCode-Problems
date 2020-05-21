from typing import List


class Solution:
    """
    Edge cases:
    First row and first column are the edge cases because there a re
    not previous row for the first row, and there are not previous
    column for the first column

    Time: O(n * m)
    Space: O(1)
    """

    def countSquares(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and i and j:
                    grid[i][j] = min(grid[i][j - 1], grid[i - 1][j], grid[i - 1][j - 1]) + 1
                counter += grid[i][j]
        return counter
