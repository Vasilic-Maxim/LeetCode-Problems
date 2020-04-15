from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [1] * length, [1] * length

        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        for j in reversed(range(length - 1)):
            right[j] = right[j + 1] * nums[j + 1]

        for k in range(length):
            nums[k] = left[k] * right[k]

        return nums
