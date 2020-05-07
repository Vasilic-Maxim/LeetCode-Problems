from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(1)
    """

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        elements = rows * cols
        k %= elements
        if k:
            self.reverse(grid, 0, elements)
            self.reverse(grid, 0, k)
            self.reverse(grid, k, elements)

        return grid

    def reverse(self, grid: List[List[int]], start: int, end: int):
        rows, cols = len(grid), len(grid[0])
        for i in range((end - start) // 2):
            sr, sc = divmod(start + i, cols)
            er, ec = divmod(end + ~i, cols)
            grid[sr][sc], grid[er][ec] = grid[er][ec], grid[sr][sc]
