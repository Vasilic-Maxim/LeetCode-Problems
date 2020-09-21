from typing import List


class Solution:
    """
    Time: O(max(n, 1001))
    Space: O(1001) => O(1)
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = [0] * 1001
        for passengers, pick_up, drop in trips:
            counter[pick_up] += passengers
            counter[drop] -= passengers

        on_board = 0
        for count in counter:
            on_board += count
            if on_board > capacity:
                return False

        return True
