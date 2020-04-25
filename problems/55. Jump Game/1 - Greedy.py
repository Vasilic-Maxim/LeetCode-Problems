from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        slow = 0
        for fast, steps in enumerate(reversed(nums)):
            if steps >= fast - slow:
                slow = fast

        return slow == len(nums) - 1
