class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if curr > n:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi
