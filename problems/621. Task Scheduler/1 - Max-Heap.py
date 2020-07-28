import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)

        # count task appearances
        counter = Counter(tasks)

        # create a heap
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        items_per_circle = n + 1
        cycles = 0
        while max_heap:
            items = [heapq.heappop(max_heap) for _ in range(n + 1) if max_heap]
            for item in items:
                if item < -1:
                    heapq.heappush(max_heap, item + 1)

            cycles += items_per_circle if max_heap else len(items)

        return cycles
