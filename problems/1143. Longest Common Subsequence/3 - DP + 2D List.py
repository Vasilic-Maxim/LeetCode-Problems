class Solution:
    """
    m - len(text1)
    n - len(text2)
    Time: O(m * n)
    Space: O(m * n)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text1[i - 1] == text2[j - 1]:
                    matrix[i][j] = 1 + matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        return matrix[-1][-1]
