from typing import List


class Solution:
    class __WeightedUnionFind:
        def __init__(self, n):
            self.__ids = list(range(n + 1))
            self.__weights = [1] * (n + 1)

        def union(self, p: int, q: int) -> bool:
            parent_p = self.find(p)
            parent_q = self.find(q)
            if parent_p == parent_q:
                return False

            if self.__weights[parent_p] < self.__weights[parent_q]:
                self.__ids[parent_q] = parent_p
                self.__weights[parent_p] += self.__weights[parent_q]
            else:
                self.__ids[parent_p] = parent_q
                self.__weights[parent_q] += self.__weights[parent_p]

            return True

        def find(self, p: int) -> int:
            while self.__ids[p] != p:
                self.__ids[p] = self.__ids[self.__ids[p]]
                p = self.__ids[p]

            return p

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = self.__WeightedUnionFind(n)
        result = None
        for edge in edges:
            if not uf.union(*edge):
                result = edge

        return result
