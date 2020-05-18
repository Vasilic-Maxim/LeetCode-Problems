from functools import reduce


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def titleToNumber(self, s: str) -> int:
        offset = ord("A") - 1
        return reduce(lambda x, y: x * 26 + (ord(y) - offset), s, 0)
