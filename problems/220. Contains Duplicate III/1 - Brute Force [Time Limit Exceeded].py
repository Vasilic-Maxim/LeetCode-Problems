from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False

        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, min(i + k + 1, n)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
