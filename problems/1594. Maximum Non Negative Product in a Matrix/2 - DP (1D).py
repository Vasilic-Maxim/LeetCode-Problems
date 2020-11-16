from itertools import product
from typing import List, Any


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Time: O(m * n)
        Space: O(n)
        """

        m, n = len(grid), len(grid[0])
        dp: Any = [None] * n
        for r, c in product(range(m), range(n)):
            adj_min, adj_max = float('inf'), float('-inf')

            if r:
                adj_min = min(adj_min, dp[c][0])
                adj_max = max(adj_max, dp[c][1])
            if c:
                adj_min = min(adj_min, dp[c - 1][0])
                adj_max = max(adj_max, dp[c - 1][1])

            v1 = (1 if adj_min == float('inf') else adj_min) * grid[r][c]
            v2 = (1 if adj_max == float('inf') else adj_max) * grid[r][c]
            dp[c] = (min(v1, v2), max(v1, v2))

        if dp[-1][1] >= 0:
            return dp[-1][1] % (10 ** 9 + 7)

        return -1
