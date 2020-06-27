from itertools import chain
from typing import List


class Solution:
    """
    Elegant solution, but uses 3 times more time than
    it is needed.

    Time: O(3 * n ** 2) => O(n ** 2)
    Space: O(1)
    """

    def projectionArea(self, grid: List[List[int]]) -> int:
        result = sum(map(max, grid))
        result += sum(map(max, zip(*grid)))
        result += sum(v > 0 for v in chain(*grid))
        return result
