from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def rob(self, nums: List[int]) -> int:
        rob = not_rob = 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)
