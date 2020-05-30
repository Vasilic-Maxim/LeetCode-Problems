from math import sqrt
from typing import List


class Solution:
    """
    Read about Euclidean distance:
    https://en.wikipedia.org/wiki/Euclidean_distance

    Time: O(n * log (n))
    Space: O(n)
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        points.sort(key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))
        return points[:k]
