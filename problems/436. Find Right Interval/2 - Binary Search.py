from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, _) in enumerate(intervals))
        return [self.binary_search(starts, end)
                for i, (start, end) in enumerate(intervals)]

    def binary_search(self, arr: List[tuple], target: int):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            start, _ = arr[mid]
            if start < target:
                lo = mid + 1
            else:
                hi = mid

        return arr[hi][1] if hi != len(arr) else -1
