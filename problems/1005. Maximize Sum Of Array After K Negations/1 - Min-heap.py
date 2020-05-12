from heapq import heapify, heapreplace
from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/628859
    n - len(nums)
    Time: O(n + k * log (n))
    Space: O(1)
    """

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k and nums[0] < 0:
            heapreplace(nums, -nums[0])
            k -= 1
        if k % 2:
            heapreplace(nums, -nums[0])
        return sum(nums)
