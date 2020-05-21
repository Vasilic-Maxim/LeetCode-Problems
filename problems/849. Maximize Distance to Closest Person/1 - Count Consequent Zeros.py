from typing import List


class Solution:
    """
    Edge cases:
    Empty seats located in the beginning and the end of the row
    are complete distances and should not be modified

    Time: O(n)
    Space: O(1)
    """

    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = empty_count = 0
        for i, seat in enumerate(seats):
            if not seat:
                empty_count += 1
            elif empty_count:
                if i == empty_count:
                    max_distance = empty_count
                else:
                    max_distance = max(max_distance, (empty_count + 1) // 2)
                empty_count = 0
        return max(max_distance, empty_count) if empty_count else max_distance
