from typing import List


class Solution:
    """
    Time: O(n * m)
    Space: O(k)
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        visited, result = set(), []
        for col in zip(*mat):
            for i, val in enumerate(col):
                if not val and i not in visited:
                    visited.add(i)
                    result.append(i)

                    if len(result) == k:
                        return result

        for j in range(len(mat)):
            if j not in visited:
                visited.add(j)
                result.append(j)

                if len(result) == k:
                    return result
