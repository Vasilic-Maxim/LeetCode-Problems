from typing import List


class Solution:
    """
    Time: O(n * max(bin(x) for x in range(num + 1), key=len))
    Space: O(n)
    """

    def countBits(self, num: int) -> List[int]:
        return list(map(lambda x: bin(x).count('1'), range(num + 1)))
