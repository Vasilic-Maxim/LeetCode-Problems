from typing import List


class Solution:
    """
    NOTE:
        You must use only constant, O(1) extra space.

    Time: O(n)
    Space: O(n)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        counter = [0] * len(nums)
        for num in nums:
            if counter[num]:
                return num

            counter[num] += 1
