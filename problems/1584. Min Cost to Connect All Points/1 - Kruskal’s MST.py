import heapq
from typing import List


class WeightedUF:
    def __init__(self, n: int):
        self.__ids = list(range(n))
        self.__size = [1] * n
        self.__count = n

    def union(self, p: int, q: int) -> bool:
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return False

        ids, size = self.__ids, self.__size
        if size[parent_p] > size[parent_q]:
            ids[parent_q] = parent_p
            size[parent_p] += size[parent_q]
        else:
            ids[parent_p] = parent_q
            size[parent_q] += size[parent_p]

        self.__count -= 1
        return True

    def find(self, p: int) -> int:
        ids = self.__ids
        while p != ids[p]:
            ids[p] = ids[ids[p]]
            p = ids[p]

        return p

    def count(self):
        return self.__count


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = WeightedUF(n)
        pq = [(self.distance(points[i], points[j]), i, j)
              for i in range(n - 1)
              for j in range(i + 1, n)]

        heapq.heapify(pq)
        cost = 0
        while pq and uf.count() > 1:
            dist, either, other = heapq.heappop(pq)
            if uf.union(either, other):
                cost += dist

        return cost

    def distance(self, point_a: List[int], point_b: List[int]) -> int:
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
