from typing import List


class WeightedUF:
    def __init__(self, n: int):
        self.__ids = list(range(n))
        self.__size = [1] * n
        self.__count = n

    def find(self, p: int) -> int:
        ids = self.__ids
        while ids[p] != p:
            ids[p] = ids[ids[p]]
            p = ids[p]
        return p

    def union(self, p: int, q: int):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return

        if self.__size[parent_p] > self.__size[parent_q]:
            self.__ids[parent_q] = parent_p
            self.__size[parent_p] += self.__size[parent_q]
        else:
            self.__ids[parent_p] = parent_q
            self.__size[parent_q] += self.__size[parent_p]

        self.__count -= 1

    def count(self) -> int:
        return self.__count


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        """
        Time: O(n ** 2 // 2) => O(n ** 2)
        Space: O(n)
        """

        n = len(matrix)
        uf = WeightedUF(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if matrix[i][j]:
                    uf.union(i, j)
        return uf.count()
