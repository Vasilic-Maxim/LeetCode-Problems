import bisect


class Solution(object):
    """
    Time: O(log (n))
    Space: O(1)
    """

    def findSpecialInteger(self, arr):
        size = len(arr) // 4
        loose = max(1, size)
        for i in range(0, len(arr), loose):
            left = bisect.bisect_left(arr, arr[i], max(0, i - loose), min(len(arr), i + loose))
            right = bisect.bisect_right(arr, arr[i], max(0, i - loose), min(len(arr), i + loose))
            if right - left > size:
                return arr[i]
