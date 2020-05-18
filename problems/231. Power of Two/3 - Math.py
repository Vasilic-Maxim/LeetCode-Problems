class Solution:
    """
    2 ** 30 // 2 ** x = 2 ** (30 - x)

    Time: O(1)
    Space: O(1)
    """

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2 ** 30 % n == 0
