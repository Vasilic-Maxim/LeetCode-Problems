from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # in one day we can just buy the stocks, but no
        # profit will be earned
        if n <= 1:
            return 0

        # in just two days we can buy at first day and sell
        # at the second day
        if n == 2:
            return max(prices[1] - prices[0], 0)

        return self.helper(prices, None, 0)

    def helper(self, prices, stock, index):
        n = len(prices)
        if index >= n:
            return 0

        profit = 0
        if stock is None:
            # we can buy
            profit += self.helper(prices, prices[index], index + 1)
        else:
            # we can sell
            profit += prices[index] - stock
            profit += self.helper(prices, None, index + 2)

        # we keep the stock
        return max(profit, self.helper(prices, stock, index + 1))
