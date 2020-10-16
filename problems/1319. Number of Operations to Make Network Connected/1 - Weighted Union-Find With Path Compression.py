from typing import List


class WeightedUF:
    def __init__(self, n):
        self.__ids = list(range(n))
        self.__count = [1] * n
        self.__n = n

    def union(self, p: int, q: int) -> bool:
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return False

        if self.__count[parent_p] < self.__count[parent_q]:
            self.__ids[parent_p] = parent_q
            self.__count[parent_q] += self.__count[parent_p]
        else:
            self.__ids[parent_q] = parent_p
            self.__count[parent_p] += self.__count[parent_q]

        self.__n -= 1
        return True

    def find(self, p: int) -> int:
        ids = self.__ids
        while p != ids[p]:
            ids[p] = ids[ids[p]]
            p = ids[p]
        return p

    def components(self) -> int:
        return self.__n


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Time: O(n * log (n))
        Space: O(2n) => O(n)
        """

        uf = WeightedUF(n)
        cables = 0
        for [p, q] in connections:
            if not uf.union(p, q):
                cables += 1

        return uf.components() - 1 if uf.components() - 1 <= cables else -1
