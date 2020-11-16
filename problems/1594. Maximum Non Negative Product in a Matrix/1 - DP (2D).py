from itertools import product
from typing import List, Any


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """ Time/Space: O(m * n) """

        m, n = len(grid), len(grid[0])
        dp: Any = [[None] * n for _ in range(m)]
        dp[0][0] = (grid[0][0], grid[0][0])
        for i in range(1, m):
            min_so_far, max_so_far = dp[i - 1][0]
            dp[i][0] = (min_so_far * grid[i][0], max_so_far * grid[i][0])

        for j in range(1, n):
            min_so_far, max_so_far = dp[0][j - 1]
            dp[0][j] = (min_so_far * grid[0][j], max_so_far * grid[0][j])

        for r, c in product(range(1, m), range(1, n)):
            min_top, max_top = dp[r - 1][c]
            min_left, max_left = dp[r][c - 1]
            min_cur = min(min_top, min_left) * grid[r][c]
            max_cur = max(max_top, max_left) * grid[r][c]
            dp[r][c] = (min(min_cur, max_cur), max(min_cur, max_cur))

        if dp[-1][-1][1] >= 0:
            return dp[-1][-1][1] % (10 ** 9 + 7)

        return -1
