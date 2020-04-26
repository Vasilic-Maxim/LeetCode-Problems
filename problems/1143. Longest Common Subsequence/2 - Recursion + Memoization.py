class Solution:
    """
    m - len(text1)
    n - len(text2)
    Time: O(m * n)
    Space: O(m * n)
    """

    def __init__(self):
        self.memo = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.compare(text1, text2, len(text1) - 1, len(text2) - 1)

    def compare(self, text1: str, text2: str, p1: int, p2: int) -> int:
        key = f'{p1}-{p2}'
        if key in self.memo:
            return self.memo[key]

        if p1 < 0 or p2 < 0:
            self.memo[key] = 0
        elif text1[p1] == text2[p2]:
            self.memo[key] = 1 + self.compare(text1, text2, p1 - 1, p2 - 1)
        else:
            self.memo[key] = max(self.compare(text1, text2, p1 - 1, p2), self.compare(text1, text2, p1, p2 - 1))

        return self.memo[key]
