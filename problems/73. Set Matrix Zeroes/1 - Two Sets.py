'''
Time: O(n*m)
Space: O(n+m)
'''
class Solution:
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

s = Solution()
data = [[1,1,1],[1,0,1],[1,1,1]]
# [[1,0,1],[0,0,0],[1,0,1]]
s.setZeroes(data)
print(data)
