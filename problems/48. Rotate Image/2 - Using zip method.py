class Solution:
    """
    Fancy Python solution...

    n - length row/col
    Time: O(n^2)
    Space: O(1)
    """

    def rotate(self, matrix: list) -> None:
        for i, row in enumerate(zip(*matrix)):
            matrix[i] = list(reversed(row))
