from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(log(n))
        Space: O(1)
        """

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        if not (matrix[0][0] <= target <= matrix[m - 1][n - 1]):
            return False

        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row, col = divmod(mid, n)

            if matrix[row][col] < target:
                lo = mid + 1
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                return True
        return False
