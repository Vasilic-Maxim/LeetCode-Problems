from collections import defaultdict
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency, first_occurrence = defaultdict(int), {}
        max_frequency = degree = 0
        for i, num in enumerate(nums):
            first_occurrence.setdefault(num, i)
            frequency[num] += 1
            if frequency[num] > max_frequency:
                max_frequency = frequency[num]
                degree = i - first_occurrence[num] + 1
            elif frequency[num] == max_frequency:
                degree = min(degree, i - first_occurrence[num] + 1)

        return degree
