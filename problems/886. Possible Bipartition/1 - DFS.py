from collections import defaultdict
from typing import List


class Solution:
    """
    m - nums
    n - len(relations)
    Time: O(m + n)
    Space: O(m + n)
    """

    def __init__(self):
        self.graph = defaultdict(list)
        self.colored = {}

    def possibleBipartition(self, nums: int, relations: List[List[int]]) -> bool:
        self.design_graph(relations)

        return all(self.dfs(node) for node in range(1, nums + 1) if node not in self.colored)

    def design_graph(self, relations: List[List[int]]):
        for left, right in relations:
            self.graph[left].append(right)
            self.graph[right].append(left)

    def dfs(self, node: int, color: int = 0):
        if node in self.colored:
            return self.colored[node] == color

        self.colored[node] = color

        return all(self.dfs(child, color ^ 1) for child in self.graph[node])
