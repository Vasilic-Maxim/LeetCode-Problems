from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(m * n)
        Space: O(1)
        """
        if not matrix or matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        if not (matrix[0][0] <= target <= matrix[m - 1][n - 1]):
            return False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    return False
