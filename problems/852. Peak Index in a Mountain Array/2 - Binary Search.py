from typing import List


class Solution:
    def peakIndexInMountainArray(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        while start < end:
            middle = (start + end) // 2
            if heights[middle] < heights[middle + 1]:
                start = middle + 1
            else:
                end = middle
        return end
