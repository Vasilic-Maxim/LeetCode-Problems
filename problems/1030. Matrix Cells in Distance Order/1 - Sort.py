from typing import List


class Solution:
    """
    n = rows * cols (all elements in the matrix)
    Time: O(n * log (n))
    Space: O(n) (space for result)
    """

    def allCellsDistOrder(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        coordinates = [[row, col]
                       for col in range(cols)
                       for row in range(rows)]
        coordinates.sort(key=lambda c: abs(r0 - c[0]) + abs(c0 - c[1]))
        return coordinates
