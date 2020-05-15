from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        i = 0
        while n and i < len(nums):
            if nums[i]:
                # Because flowers cannot be planted in adjacent
                # spots when we catch a spot with planted flower
                # it means that next spot is empty. We can ignore
                # it and check [i + 2] spot.
                i += 2
            elif i + 1 == len(nums) or nums[i + 1] == 0:
                # We can check only right side because we are certain
                # that left spot is an empty spot.
                nums[i] = 1
                n -= 1
                i += 2
            else:
                i += 1
        return not n
