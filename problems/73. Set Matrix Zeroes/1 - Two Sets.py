class Solution:
    """
    Time: O(n*m)
    Space: O(n+m)
    """

    def setZeroes(self, matrix: list) -> None:
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
