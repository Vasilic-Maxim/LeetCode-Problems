from typing import List


class Solution:
    """
    Time: O(m * n)
    Space: O(1)
    """

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        for _ in range(n):
            prev = cells[0]
            for i in range(len(cells)):
                tmp = cells[i]
                if 1 < i + 1 < len(cells):
                    cells[i] = int(prev == cells[i + 1])
                else:
                    cells[i] = 0
                prev = tmp
        return cells
