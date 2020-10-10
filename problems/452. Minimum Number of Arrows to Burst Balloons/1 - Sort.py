from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        common_end = float("inf")
        counter = int(len(points) > 0)
        for start, end in points:
            if start <= common_end:
                common_end = min(common_end, end)
            else:
                counter += 1
                common_end = end

        return counter
