from itertools import count


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        for num in count(start=1):
            n -= num
            if n < 0:
                return num - 1
