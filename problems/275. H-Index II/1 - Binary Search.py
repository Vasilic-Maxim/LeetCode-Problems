from typing import List


class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        h = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            h = max(h, min(citations[mid], n - mid))
            if n - mid > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return h
