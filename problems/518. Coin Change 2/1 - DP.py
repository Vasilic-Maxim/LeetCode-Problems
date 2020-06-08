from typing import List


class Solution:
    """
    m - amount
    n - len(coins)
    Time: O(m * n)
    Space: O(m)
    """

    def change(self, amount: int, coins: List[int]) -> int:
        exchange = [1] + [0] * amount
        for coin in coins:
            for i in range(len(exchange)):
                if i >= coin:
                    exchange[i] += exchange[i - coin]
        return exchange[-1]
