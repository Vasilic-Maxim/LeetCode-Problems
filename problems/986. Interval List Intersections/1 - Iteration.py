from typing import List


class Solution:
    """
    Time: O(a + b)
    Space: O(max(a, b))
    """

    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result = []
        p1 = p2 = 0
        while p1 < len(a) and p2 < len(b):
            start = max(a[p1][0], b[p2][0])
            end = min(a[p1][1], b[p2][1])
            if start <= end:
                result.append([start, end])
            if a[p1][1] > b[p2][1]:
                p2 += 1
            else:
                p1 += 1
        return result
