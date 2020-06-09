from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
