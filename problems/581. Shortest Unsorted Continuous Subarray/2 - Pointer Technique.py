from typing import *


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = len(nums) - 1
        max_so_far = float('-inf')
        for idx, val in enumerate(nums):
            # update maximum value
            if nums[idx] >= max_so_far:
                max_so_far = nums[idx]
            # if the value is lower than the current maximum
            # then find the position at the left side to
            # switch with this element
            else:
                left = min(left, idx - 1)
                while left >= 0 and nums[left] > nums[idx]:
                    left -= 1
                ans = idx - left
        return ans
