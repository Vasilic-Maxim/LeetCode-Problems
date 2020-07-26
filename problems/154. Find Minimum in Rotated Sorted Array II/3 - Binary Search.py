from typing import List


class Solution:
    """
    Time: O(log(n))
    Space: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            middle = (lo + hi) // 2
            if nums[middle] > nums[hi]:
                lo = middle + 1
            elif nums[middle] < nums[hi]:
                hi = middle
            else:  # lo <= mid <= hi
                hi -= 1
        return nums[lo]
