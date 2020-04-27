from typing import List


class Solution:
    """
    This solution makes sense ONLY if you are allowed to modify the matrix
    m - len(matrix)
    n - len(matrix[0])
    Time: O(m * n)
    Space: O(1)
    """
    def maximalSquare(self, matrix: List[List]) -> int:
        max_square = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not i or not j or matrix[i][j] == "0":
                    matrix[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]):
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + int(matrix[i][j])
                max_square = max(max_square, matrix[i][j])
        return max_square ** 2
