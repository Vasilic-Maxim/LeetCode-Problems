class Solution:
    """
    Time: O(n*m)
    Space: O(1)
    """

    def setZeroes(self, matrix: list) -> None:
        zero_first_col = False
        for row in matrix:
            if row[0] == 0:
                zero_first_col = True
                break

        zero_first_row = False
        for col in matrix[0]:
            if col == 0:
                zero_first_row = True
                break

        # Mark all row and col which should be filled with zeros
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        # Go throwout all the rows
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        # Go throwout all the cols
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        # If initially there were any zeros in first column then we fill it completely with zeros
        if zero_first_col:
            for row in matrix:
                row[0] = 0

        # If initially there were any zeros in first row then we fill it completely with zeros
        if zero_first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
