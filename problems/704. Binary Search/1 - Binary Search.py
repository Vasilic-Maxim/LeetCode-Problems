from typing import List


class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1
