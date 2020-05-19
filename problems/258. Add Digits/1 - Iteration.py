from functools import reduce


class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = reduce(lambda x, y: x + int(y), str(num), 0)
        return num
