from typing import List


class Solution:
    """
    This solution makes sense ONLY if you are allowed to modify the matrix
    m - len(matrix)
    n - len(matrix[0])
    Time: O(m * n)
    Space: O(n)
    """
    def maximalSquare(self, matrix: List[List]) -> int:
        memo = [0] * len(matrix[0]) if matrix else 0
        max_square = 0
        for i in range(len(matrix)):
            prev = 0
            for j in range(len(matrix[0])):
                tmp = memo[j]
                if matrix[i][j] == '1':
                    memo[j] = min(memo[j - 1], memo[j], prev) + 1
                    max_square = max(max_square, memo[j])
                else:
                    memo[j] = 0
                prev = tmp
        return max_square * max_square
