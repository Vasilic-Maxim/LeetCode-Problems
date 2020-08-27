import heapq
from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        if n == 0:
            return []
        if n == 1:
            return [-1]

        starts = [(start, i) for i, (start, _) in enumerate(intervals)]
        ends = [(end, i) for i, (_, end) in enumerate(intervals)]
        heapq.heapify(starts)
        heapq.heapify(ends)

        result = [0] * n
        while ends:
            end, i = heapq.heappop(ends)

            while starts and starts[0][0] < end:
                heapq.heappop(starts)

            result[i] = starts[0][1] if starts else -1

        return result
