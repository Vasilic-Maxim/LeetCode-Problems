from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = evens = 0
        for chip in chips:
            if chip % 2:
                odds += 1
            else:
                evens += 1
        return min(odds, evens)
