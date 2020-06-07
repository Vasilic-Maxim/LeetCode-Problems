from collections import Counter
from typing import List


class Solution:
    """
    Number of divisors of NN is bounded by O(n * log * log (n))

    Time: O(n ** 2 * log * log (n))
    Space: O(n)
    """

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = len(deck)
        values = list(Counter(deck).values())
        for div in range(2, n + 1):
            if not n % div and self.is_common_divider(values, div):
                return True
        return False

    def is_common_divider(self, nums: List[int], div: int) -> bool:
        return all(not x % div for x in nums)
