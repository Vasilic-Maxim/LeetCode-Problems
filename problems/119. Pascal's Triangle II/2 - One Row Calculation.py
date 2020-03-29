class Solution:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def getRow(self, row_index: int):
        # the length of the list should be (rowIndex + 1)
        row = [1] + [0] * row_index

        # start from first index and repeat (rowIndex-1) times
        for i in range(1, row_index + 1):
            # go backwards and fill cells with new values
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row
