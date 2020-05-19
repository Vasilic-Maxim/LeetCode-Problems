class Solution:
    """
    Time: O(1)
    Space: O(1)
    """

    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)
