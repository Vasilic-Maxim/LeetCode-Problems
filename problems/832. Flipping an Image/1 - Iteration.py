from typing import List


class Solution:
    def flipAndInvertImage(self, matrix: List[List[int]]) -> List[List[int]]:
        for row in matrix:
            for j in range((len(matrix[0]) + 1) // 2):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1

        return matrix
