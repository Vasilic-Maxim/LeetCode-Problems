from operator import getitem
from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        common_end = float("inf")
        counter = int(len(points) > 0)
        for start, end in points:
            if start > common_end:
                counter += 1
                common_end = end

        return counter
