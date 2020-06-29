from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(n)
    """

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + (dp[j - 1] if j else 0)
        return dp[-1]
