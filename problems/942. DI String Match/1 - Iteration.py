from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def diStringMatch(self, statistics: str) -> List[int]:
        lo, hi = 0, len(statistics)
        result = []
        for direction in statistics:
            if direction == 'I':
                result.append(lo)
                lo += 1
            else:
                result.append(hi)
                hi -= 1
        return result + [lo]
