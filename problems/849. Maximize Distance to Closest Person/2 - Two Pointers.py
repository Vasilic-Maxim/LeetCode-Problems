from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        fast = 0
        while seats[fast] == 0:
            fast += 1

        slow = result = fast
        for fast in range(fast + 1, len(seats)):
            if seats[fast] == 1:
                result = max(result, (fast - slow) // 2)
                slow = fast

        return max(result, fast - slow)
