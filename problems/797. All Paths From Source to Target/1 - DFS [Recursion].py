from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(graph, 0, [], paths)
        return paths

    def dfs(self, graph: List[List[int]], node: int, path: List[int], paths=List[List[int]]):
        path.append(node)

        if not graph[node]:
            paths.append(path[:])

        for child in graph[node]:
            self.dfs(graph, child, path, paths)

        path.pop()
