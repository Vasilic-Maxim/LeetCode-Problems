class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def climbStairs(self, n: int) -> int:
        first, second = 0, 1
        for i in range(2, n + 1):
            first, second = second, first + second
        return second
