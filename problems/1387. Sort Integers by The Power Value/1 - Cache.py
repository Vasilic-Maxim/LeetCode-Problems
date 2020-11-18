from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def rank(num: int) -> int:
            if num == 1:
                return 0

            if num % 2:
                return rank(3 * num + 1) + 1

            return rank(num // 2) + 1

        ranks = []
        for i in range(lo, hi + 1):
            ranks.append((rank(i), i))

        ranks.sort()
        return ranks[k - 1][1]