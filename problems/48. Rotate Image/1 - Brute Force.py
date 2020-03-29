class Solution:
    """
    n - length row/col
    Time: O(n^2)
    Space: O(1)
    """

    def rotate(self, matrix: list) -> None:
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix) - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-j - 1][i]
                matrix[-j - 1][i] = matrix[-i - 1][-j - 1]
                matrix[-i - 1][-j - 1] = matrix[j][-i - 1]
                matrix[j][-i - 1] = tmp
