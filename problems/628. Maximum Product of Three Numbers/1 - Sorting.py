from math import prod
from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(prod(nums[:2] + nums[-1:0]), prod(nums[-3:0]))
