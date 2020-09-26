from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findPoisonedDuration(self, time_series: List[int], duration: int) -> int:
        n = len(time_series)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(time_series[i + 1] - time_series[i], duration)

        return total + duration
