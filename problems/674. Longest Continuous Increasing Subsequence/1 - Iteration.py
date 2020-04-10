from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_sequence = pointer = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i - 1]:
                pointer = i

            max_sequence = max(max_sequence, i - pointer + 1)
        return max_sequence
