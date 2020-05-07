from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    def shiftGrid(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        k %= len(matrix) * len(matrix[0])
        if k:
            elements = [x for row in matrix for x in row]
            k = len(elements) - k
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if k == len(elements):
                        k = 0

                    matrix[i][j] = elements[k]
                    k += 1

        return matrix
