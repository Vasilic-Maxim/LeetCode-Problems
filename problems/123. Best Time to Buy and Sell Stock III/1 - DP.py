import sys
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if not n:
            return 0

        dp = [0] * n
        for transaction in range(1, 3):
            max_dif = -sys.maxsize
            prev = dp[0]
            for day in range(1, n):
                tmp = dp[day]
                max_dif = max(max_dif, prev - prices[day - 1])
                dp[day] = max(dp[day - 1], prices[day] + max_dif)
                prev = tmp
        return dp[-1]
