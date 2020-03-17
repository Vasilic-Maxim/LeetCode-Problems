'''
n - length row/col
Time: O(n^2)
Space: O(1)
'''

class Solution:
    def rotate(self, matrix: list) -> None:
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = tmp

s = Solution()
s.rotate([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
])