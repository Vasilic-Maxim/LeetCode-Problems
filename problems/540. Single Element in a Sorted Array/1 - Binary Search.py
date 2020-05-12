from typing import List


class Solution:
    """
    https://www.youtube.com/watch?v=4Gi8uAz666s
    Time: O(log (n))
    Space: O(1)
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2

            is_even = (right - middle) % 2 == 0
            if nums[middle] == nums[middle - 1]:
                if is_even:
                    right = middle - 2
                else:
                    left = middle + 1
            elif nums[middle] == nums[middle + 1]:
                if is_even:
                    left = middle + 2
                else:
                    right = middle - 1
            else:
                return nums[middle]
        return nums[left]
