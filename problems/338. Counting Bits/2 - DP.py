from typing import List


class Solution:
    """
    Read: https://leetcode.com/problems/counting-bits/discuss/79557
    Time: O(n)
    Space: O(n)
    """

    def countBits(self, num: int) -> List[int]:
        result = []
        offset = 1
        for i in range(num + 1):
            if offset << 1 == i:
                offset <<= 1
            result.append(result[i - offset])
        return result
