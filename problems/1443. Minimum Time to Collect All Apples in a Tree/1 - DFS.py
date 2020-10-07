from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], has_apple: List[bool]) -> int:
        connections = defaultdict(set)
        for parent, child in edges:
            connections[parent].add(child)
            connections[child].add(parent)

        def dfs(node: int):
            if node in visited:
                return

            visited.add(node)
            counter = 0
            for child_node in connections[node]:
                counter += dfs(child_node)

            if node and (counter or has_apple[node]):
                counter += 2

            return counter

        visited = set()
        return dfs(0)
