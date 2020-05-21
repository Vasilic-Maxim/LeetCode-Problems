from typing import List


class Solution:
    """
    Greedy, find i with nums[i-1]>nums[i] and
    modify nums[i-1] or nums[i], e.g, [3,4,2,3].

    Time: O(n)
    Space: O(1)
    """

    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                counter += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]  # modify nums[i-1]
                else:
                    nums[i] = nums[i - 1]  # modify nums[i]
        return counter <= 1
