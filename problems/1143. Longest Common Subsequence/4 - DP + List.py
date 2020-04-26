class Solution:
    """
    m - len(text1)
    n - len(text2)
    Time: O(m * n)
    Space: O(n)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            prev = 0
            for j in range(1, len(text2) + 1):
                tmp = memo[j]
                if text1[i - 1] == text2[j - 1]:
                    memo[j] = 1 + prev
                else:
                    memo[j] = max(memo[j - 1], memo[j])
                prev = tmp
        return memo[-1]
