from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(1)
    """

    def heightChecker(self, nums: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(nums, sorted(nums)))
