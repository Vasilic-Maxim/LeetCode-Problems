from bisect import bisect
from typing import List


class Solution:
    """
    Time: O((m + n) * log (n))
    Space: O(n)
    """

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance = 0
        for num in arr1:
            i = bisect(arr2, num)
            if (i == 0 or arr2[i - 1] < num - d) and (i == len(arr2) or arr2[i] > num + d):
                distance += 1
        return distance
