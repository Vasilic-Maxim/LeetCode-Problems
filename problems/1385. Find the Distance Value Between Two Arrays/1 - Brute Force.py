from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(1)
    """

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d):
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)
