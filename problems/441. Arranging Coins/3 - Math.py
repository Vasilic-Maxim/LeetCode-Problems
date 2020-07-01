class Solution:
    """
    Read:
    https://en.wikipedia.org/wiki/Completing_the_square

    Time: O(1)
    Space: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)
