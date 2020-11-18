from functools import lru_cache
from heapq import nsmallest


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def rank(num: int) -> int:
            if num == 1:
                return 0

            if num % 2:
                return rank(3 * num + 1) + 1

            return rank(num // 2) + 1

        pq = [(rank(i), i) for i in range(lo, hi + 1)]
        return nsmallest(k, pq)[-1][1]
