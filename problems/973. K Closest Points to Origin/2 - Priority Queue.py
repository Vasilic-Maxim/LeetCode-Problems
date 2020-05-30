import heapq
from typing import List


class Solution:
    """
    Read about Euclidean distance:
    https://en.wikipedia.org/wiki/Euclidean_distance

    Time: O(n * log (k))
    Space: O(k)
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)
