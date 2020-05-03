from heapq import heappush, heapify, heappop
from typing import List


class KthLargest(object):
    """
    Time: O(n * log n)
    Space: O(k)
    """

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int):
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
