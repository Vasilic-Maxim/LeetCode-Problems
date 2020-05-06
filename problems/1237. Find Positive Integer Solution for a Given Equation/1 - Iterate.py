from typing import List


class Solution:
    """
    Time: O(col + row)
    Space: O(1)
    """
    def findSolution(self, fn: 'CustomFunction', target: int) -> List[List[int]]:
        result = []
        col = 1000
        for row in range(1, 1001):
            while col > 1 and fn.f(row, col) > target:
                col -= 1

            if fn.f(row, col) == target:
                result.append([row, col])

        return result
