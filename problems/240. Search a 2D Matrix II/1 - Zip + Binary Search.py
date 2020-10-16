from typing import Tuple, List, Any


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        if not matrix or not matrix[0]:
            return False

        for col in zip(*matrix):
            if self.contains(col, target):
                return True

        return False

    def contains(self, nums: Tuple[Any], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return True
        return nums[lo] == target
