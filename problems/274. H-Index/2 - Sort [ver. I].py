from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort(reverse=True)
        h_index = 0
        for count, citation in enumerate(citations, start=1):
            h_index = max(h_index, min(count, citation))

        return h_index
