from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def duplicateZeros(self, nums: List[int]) -> None:
        new_nums = [0] * len(nums)
        p1 = p2 = 0
        while p2 < len(new_nums):
            if not nums[p1]:
                p2 += 2
            else:
                new_nums[p2] = nums[p1]
                p2 += 1
            p1 += 1

        nums[:] = new_nums[:]
