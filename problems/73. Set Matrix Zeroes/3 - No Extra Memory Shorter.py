'''
Time: O(n*m)
Space: O(1)
'''

class Solution:
    def setZeroes(self, matrix: list) -> None:
        isZeroCol = False
        
        # Mark all row and col which should be filled with zeros
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isZeroCol = True

            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        # FIRST iterate throw the cols
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                self.nullifyCol(matrix, i, 1)
        
        # Only after cols you can iterate throw the rows
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                self.nullifyRow(matrix, i, 1)
        
        # If there is '0' in (0, 0) cell then it came from this row
        # and entire row should be filled with zeros
        if matrix[0][0] == 0:
            self.nullifyRow(matrix, 0)
        
        # If initially there were any zeros in first column then we fill it completly with zeros
        if isZeroCol:
            self.nullifyCol(matrix, 0)

    def nullifyCol(self, matrix: list, colIdx: int, startFrom: int = 0) -> None:
        for i in range(startFrom, len(matrix)):
            matrix[i][colIdx] = 0
    
    def nullifyRow(self, matrix: list, rowIdx: int, startFrom: int = 0) -> None:
        for i in range(startFrom, len(matrix[rowIdx])):
            matrix[rowIdx][i] = 0

s = Solution()
data = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
s.setZeroes(data)
print(data)