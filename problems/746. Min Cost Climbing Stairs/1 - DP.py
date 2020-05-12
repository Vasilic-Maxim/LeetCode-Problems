from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = second = 0
        for step_cost in cost:
            first, second = second, min(first, second) + step_cost
        return min(first, second)
