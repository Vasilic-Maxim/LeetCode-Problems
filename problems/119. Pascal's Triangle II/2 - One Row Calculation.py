'''
Time: O(n^2)
Space: O(n)
'''
class Solution:
    def getRow(self, rowIndex: int):
        # the length of the list should be (rowIndex + 1)
        row = [1] + [0]*(rowIndex)
        
        # start from first index and repeat (rowIndex-1) times
        for i in range(1, rowIndex + 1):
            # go backwards and fill cells with new values
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row