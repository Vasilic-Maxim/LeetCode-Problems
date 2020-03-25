'''
Time: O(numRows^2)
Space: O(numRows^2)
'''
class Solution:
    def generate(self, numRows: list):
        triangle = []

        for rowIdx in range(numRows):
            row = [None]*(rowIdx+1)
            row[0] = row[-1] = 1

            for j in range(1, len(row)-1):
                row[j] = triangle[rowIdx-1][j-1] + triangle[rowIdx-1][j]

            triangle.append(row)

        return triangle