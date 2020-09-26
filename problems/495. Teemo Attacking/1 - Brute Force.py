from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    
    def findPoisonedDuration(self, time_series: List[int], duration: int) -> int:
        total = ends = 0
        for time in time_series:
            __ends = time + duration
            total += __ends - ends if time < ends else duration
            ends = __ends
        return total
