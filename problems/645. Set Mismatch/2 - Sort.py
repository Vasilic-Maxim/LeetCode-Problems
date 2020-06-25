from typing import List


class Solution:
    """
    Time: O(n log (n))
    Space: O(n)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup, missing = None, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                # searching for gap, such as [1, 3]
                missing = nums[i - 1] + 1

        # if the last element is not equal to  the length of the list
        # that means that the last element is missing
        return [dup, missing if nums[-1] == len(nums) else len(nums)]
