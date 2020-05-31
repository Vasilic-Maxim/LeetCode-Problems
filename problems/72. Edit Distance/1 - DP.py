class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0] * (len(word2) + 1) for _ in word1]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j:
                    break
                matrix[i][j] = j if not i else i

        for i, char1 in enumerate(word1, start=1):
            for j, char2 in enumerate(word2, start=1):
                if char1 == char2:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
        return matrix[-1][-1]
