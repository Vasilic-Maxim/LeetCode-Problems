from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort()
        h_index = 1
        i = len(citations) - 1
        while i >= 0 and citations[i] >= h_index:
            i -= 1
            h_index += 1

        return h_index - 1
