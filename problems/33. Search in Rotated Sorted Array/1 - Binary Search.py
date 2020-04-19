from typing import List


class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # search for start of the list
        # the start point is also the minimum element in the list
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        # reset pointers
        start = left
        left, right = 0, len(nums) - 1
        if target <= nums[-1]:
            left = start
        else:
            right = start

        # do basic binary search
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return -1
