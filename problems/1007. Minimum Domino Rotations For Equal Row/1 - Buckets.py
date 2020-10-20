from typing import List


class Solution:
    def minDominoRotations(self, row1: List[int], row2: List[int]) -> int:
        """
        n = len(row1)
        Time/Space: O(n)
        """

        n = len(row1)
        buckets = [set() for _ in range(7)]
        counter = [0] * 7
        same = 0
        for i, (item1, item2) in enumerate(zip(row1, row2)):
            buckets[item1].add(i)
            buckets[item2].add(i)
            if item1 == item2:
                same += 1
            else:
                counter[item1] += 1
                counter[item2] -= 1

        for j in range(1, 7):
            if len(buckets[j]) == n:
                return (n - abs(counter[j]) - same) // 2

        return -1
