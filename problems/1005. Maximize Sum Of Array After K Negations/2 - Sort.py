from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        pointer = 0
        while pointer < len(nums) and nums[pointer] < 0 and pointer < k:
            nums[pointer] = -nums[pointer]
            pointer += 1

        return sum(nums) - (k - pointer) % 2 * min(nums) * 2
