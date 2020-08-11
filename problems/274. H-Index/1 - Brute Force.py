from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n = len(citations)
        h_index = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if citations[i] <= citations[j]:
                    count += 1
            h_index = max(h_index, min(citations[i], count))
        return h_index
