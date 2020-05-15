class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def sumZero(self, n):
        return range(1 - n, n, 2)
