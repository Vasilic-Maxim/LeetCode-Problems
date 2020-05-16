from typing import List


class Solution:
    """
    m - len(arr1)
    n - len(arr2)
    Time: O(n + m * log (m))
    Space: O(n + m)
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: order.get(x, 1000 + x))
