from typing import List


class StockSpanner:
    """
    Time: O(n) or O(1) amortized
    Space: O(n)
    """

    def __init__(self):
        self.stack: List[tuple] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
