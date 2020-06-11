from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies) // 2, len(set(candies)))
