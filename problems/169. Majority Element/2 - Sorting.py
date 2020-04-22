from typing import List


class Solution:
    """
    Time: O(n * log n)
    Space: O(1)
    """
    def majorityElement(self, nums: List[int]):
        nums.sort()
        return nums[len(nums) // 2]
