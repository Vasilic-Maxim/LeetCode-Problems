import heapq
from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(n)
    """

    def thirdMax(self, nums: List[int]) -> int:
        return heapq.nlargest(3, set(nums))[-1]
