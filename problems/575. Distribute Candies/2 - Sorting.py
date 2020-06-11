from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(1)
    """

    def distributeCandies(self, candies: List[int]) -> int:
        candies.sort()
        kinds = 1
        for i in range(1, len(candies)):
            if candies[i] != candies[i - 1]:
                kinds += 1
        return min(len(candies) // 2, kinds)
