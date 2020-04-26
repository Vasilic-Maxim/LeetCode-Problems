class Solution:
    """
    m - len(text1)
    n - len(text2)
    Time: O(2 ** (m + n))
    Space: O(m + n)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.compare(text1, text2, len(text1) - 1, len(text2) - 1)

    def compare(self, text1: str, text2: str, p1: int, p2: int) -> int:
        if p1 < 0 or p2 < 0:
            return 0
        if text1[p1] == text2[p2]:
            return 1 + self.compare(text1, text2, p1 - 1, p2 - 1)
        else:
            return max(self.compare(text1, text2, p1 - 1, p2), self.compare(text1, text2, p1, p2 - 1))
