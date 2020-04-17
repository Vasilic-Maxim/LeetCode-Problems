from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def peakIndexInMountainArray(self, heights: List[int]) -> int:
        for i, height in enumerate(heights):
            if height > heights[i + 1]:
                return i
