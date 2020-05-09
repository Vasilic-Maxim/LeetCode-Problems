from typing import List


class Solution:
    """
    Time: O(n * log n)
    Space: O(n)
    """

    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        ranks = {}
        for num in sorted(nums):
            ranks.setdefault(num, len(ranks) + 1)
        return list(map(ranks.get, nums))
