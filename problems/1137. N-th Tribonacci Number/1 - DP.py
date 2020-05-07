class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n

        a, b, c = 0, 1, 1

        for i in range(2, n):
            a, b, c = b, c, a + b + c

        return c
