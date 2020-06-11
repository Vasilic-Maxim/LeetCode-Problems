from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        for i in range(len(arr) - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]
