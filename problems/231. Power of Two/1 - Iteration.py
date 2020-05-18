class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while not n % 2:
            n //= 2
        return n == 1
