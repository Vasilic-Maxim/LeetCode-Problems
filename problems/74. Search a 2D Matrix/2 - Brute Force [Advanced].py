from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(m + n)
        Space: O(1)
        """
        if not matrix or matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target < matrix[i][0]:
                return False

            if target > matrix[i][n - 1]:
                continue

            for j in range(n):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    return False
