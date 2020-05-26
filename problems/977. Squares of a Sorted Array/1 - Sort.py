from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x * x for x in nums)
