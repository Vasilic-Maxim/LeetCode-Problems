from heapq import nsmallest
from typing import List


class Solution:
    """
    Time: O( n*log(m) + n*log(k) )
    Space: O(k)
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for count, i in nsmallest(k, ((self.count_ones(row), i) for i, row in enumerate(mat)))]

    def count_ones(self, a):
        x, lo, hi = 0, 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] > x:
                lo = mid + 1
            else:
                hi = mid
        return lo
