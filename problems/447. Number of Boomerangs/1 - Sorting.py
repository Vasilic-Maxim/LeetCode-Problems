from collections import defaultdict
from typing import List


class Solution:
    """
    Time/Aux. Space: O(n ** 2)
    """

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)

        def squared_distance(p: List[int], q: List[int]) -> int:
            l, h = p[0] - q[0], p[1] - q[1]
            return l * l + h * h

        for i in range(n):
            counter = defaultdict(int)

            for j in range(n):
                counter[squared_distance(points[i], points[j])] += 1

            for count in counter.values():
                if count >= 2:
                    result += count * (count - 1)

        return result
