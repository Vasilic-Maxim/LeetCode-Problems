from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums) - 1):
            curr_sum = 1 if nums[i] else -1
            for j in range(i + 1, len(nums)):
                curr_sum += 1 if nums[j] else -1
                if not curr_sum:
                    max_len = max(max_len, j - i + 1)
        return max_len
