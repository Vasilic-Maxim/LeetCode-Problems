from typing import List


class Solution:
    """
    See:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/Share-my-thinking-process

    Time: O(n)
    Space: O(1)
    """
    def maxProfit(self, prices: List[int]):
        if len(prices) < 2:
            return 0

        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
