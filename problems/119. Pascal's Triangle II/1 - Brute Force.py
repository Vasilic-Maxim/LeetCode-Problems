'''
This solution comes from problem 118 where we create entire triangle.

Time: O(n^2)
Space: O(n^2)
'''
class Solution:
    def getRow(self, rowIndex: int):
        triangle = []

        for rowIdx in range(rowIndex + 1):
            row = [None] * (rowIdx + 1)
            row[0] = row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[rowIdx - 1][j - 1] + triangle[rowIdx - 1][j]

            triangle.append(row)

        return triangle[-1]