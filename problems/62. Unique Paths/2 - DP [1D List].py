class Solution:
    """
    Time: O(m * n)
    Space: O(m)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for _ in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1]
