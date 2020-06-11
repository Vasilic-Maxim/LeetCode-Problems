from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        if len(nums) >= 2:
            left, right = 0, len(nums) - 1
            i = left
            while i <= right:
                if nums[i] == 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                    i += 1
                elif nums[i] == 2:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                else:
                    i += 1
