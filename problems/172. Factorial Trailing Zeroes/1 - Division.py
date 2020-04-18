class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n:
            n //= 5
            zeros += n
        return zeros
