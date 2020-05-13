import sys
from typing import List


class Solution:
    """
    m - len(houses)
    n - len(heaters)
    Time: O(m * n)
    Space: O(m)
    """

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        diff = [sys.maxsize] * len(houses)
        for heater in heaters:
            for i, house in enumerate(houses):
                diff[i] = min(diff[i], abs(heater - house))
        return max(diff)
