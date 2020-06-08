import sys
from typing import List


class Solution:
    """
    Reed more:
    https://en.wikipedia.org/wiki/Change-making_problem

    m - len(coins)
    n - amount
    Time: O(m * n)
    Space: O(n)
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        exchange = [0] + [sys.maxsize] * amount
        for coin in coins:
            for i in range(len(exchange)):
                exchange[i] = min(exchange[i], exchange[i - coin] + 1)

        return exchange[-1] if exchange[-1] != sys.maxsize else -1
