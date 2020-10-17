from typing import List


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        """
        Time: O(n ** 2)
        Space: O(n)
        """

        def dfs(v: int):
            marked[v] = True
            for w in range(n):
                if not marked[w] and matrix[v][w]:
                    dfs(w)

        n = len(matrix)
        count = 0
        marked = [False] * n
        for i in range(n):
            if not marked[i]:
                dfs(i)
                count += 1
        return count
