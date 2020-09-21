from collections import defaultdict
from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(n)
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = defaultdict(int)
        for passengers, pick_up, drop in trips:
            counter[pick_up] += passengers
            counter[drop] -= passengers

        locations = sorted(counter.keys())
        on_board = 0
        for location in locations:
            on_board += counter[location]
            if on_board > capacity:
                return False

        return True
