class Solution:
    """
    Time: O(n*m)
    Space: O(1)
    """

    def setZeroes(self, matrix: list) -> None:
        is_zero_col = False

        # Mark all row and col which should be filled with zeros
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_zero_col = True

            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        # FIRST iterate throw the cols
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                self.nullify_col(matrix, i, 1)

        # Only after cols you can iterate throw the rows
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                self.nullify_row(matrix, i, 1)

        # If there is '0' in (0, 0) cell then it came from this row
        # and entire row should be filled with zeros
        if matrix[0][0] == 0:
            self.nullify_row(matrix, 0)

        # If initially there were any zeros in first column then we fill it completely with zeros
        if is_zero_col:
            self.nullify_col(matrix, 0)

    @staticmethod
    def nullify_col(matrix: list, col_idx: int, start_from: int = 0) -> None:
        for i in range(start_from, len(matrix)):
            matrix[i][col_idx] = 0

    @staticmethod
    def nullify_row(matrix: list, row_idx: int, start_from: int = 0) -> None:
        for i in range(start_from, len(matrix[row_idx])):
            matrix[row_idx][i] = 0
