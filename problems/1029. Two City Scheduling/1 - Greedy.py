from typing import List


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        max_count = len(costs) // 2
        count_a = count_b = result = 0
        for cost in costs:
            if count_a < max_count > count_b:
                if cost[0] < cost[1]:
                    count_a += 1
                    result += cost[0]
                else:
                    count_b += 1
                    result += cost[1]
            elif count_a < max_count:
                count_a += 1
                result += cost[0]
            else:
                count_b += 1
                result += cost[1]
        return result
