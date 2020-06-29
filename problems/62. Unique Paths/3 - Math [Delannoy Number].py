from math import factorial


class Solution:
    """
    WATCH:
    https://youtu.be/M8BYckxI8_U
    READ:
    https://www.geeksforgeeks.org/delannoy-number/

    Time: O(1)
    Space: O(1)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1))
