from typing import List


class Solution:
    """
    https://leetcode.com/problems/sort-array-by-parity/discuss/614676/two-pointers-technique-python-on-time-o1-space
    Time: O(n)
    Space: O(1)
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = fast = 0
        while fast < len(nums):
            if not (nums[fast] % 2):
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if not (nums[slow] % 2):
                slow += 1

            fast += 1

        return nums
