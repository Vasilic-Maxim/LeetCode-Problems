import sys
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = total = 0
        total_max, total_min = ~sys.maxsize, sys.maxsize
        for i, num in enumerate(nums):
            cur_max = max(cur_max + num, num)
            total_max = max(total_max, cur_max)
            cur_min = min(cur_min + num, num)
            total_min = min(total_min, cur_min)
            total += num
        return max(total_max, total - total_min) if total_max > 0 else total_max
