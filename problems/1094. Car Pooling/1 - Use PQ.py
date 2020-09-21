from heapq import heapify, heappop
from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(n)
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []
        for passengers, pick_up, drop in trips:
            timestamps.append((pick_up, passengers))
            timestamps.append((drop, -passengers))

        heapify(timestamps)

        total_passengers = 0
        while timestamps:
            total_passengers += heappop(timestamps)[1]
            if total_passengers > capacity:
                return False

        return True
