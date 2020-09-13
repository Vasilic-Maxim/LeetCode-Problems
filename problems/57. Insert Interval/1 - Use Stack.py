from bisect import bisect
from typing import List


class Solution:
    """
    Time/Space: O(n)
    """

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        insert_index = bisect(intervals, new_interval)
        intervals.insert(insert_index, new_interval)

        n = len(intervals)
        stack = [intervals[0]]
        for i in range(1, n):
            interval = intervals[i]
            if self.overlap(stack[-1], interval):
                interval = self.unite(stack.pop(), interval)

            stack.append(interval)

        return stack

    def overlap(self, left: List[int], right: List[int]) -> bool:
        lx1, lx2 = left
        rx1, rx2 = right
        return lx1 <= rx1 <= lx2

    def unite(self, left: List[int], right: List[int]) -> List[int]:
        lx1, lx2 = left
        _, rx2 = right
        return [lx1, max(lx2, rx2)]
