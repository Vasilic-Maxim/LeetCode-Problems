from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        return next((Counter(t) - Counter(s)).elements())
