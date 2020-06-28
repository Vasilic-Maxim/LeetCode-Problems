from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 1
        while fast < len(nums):
            if nums[fast] > nums[slow]:
                nums[slow] = nums[fast]

            if nums[slow] > nums[slow - 1]:
                slow += 1

            fast += 1
        return slow
