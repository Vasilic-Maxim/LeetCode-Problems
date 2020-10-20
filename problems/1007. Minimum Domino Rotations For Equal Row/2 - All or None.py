from typing import List


class Solution:
    """
    n = len(row1)
    Time: O(4n) => O(n)
    Space: O(1)
    """

    def minDominoRotations(self, row1: List[int], row2: List[int]) -> int:
        for num in row1[0], row2[0]:
            if all(num in domino for domino in zip(row1, row2)):
                return len(row1) - max(row1.count(num), row2.count(num))

        return -1
