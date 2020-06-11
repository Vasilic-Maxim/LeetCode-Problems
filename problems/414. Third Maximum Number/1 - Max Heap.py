import heapq
from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(1)
    """

    def thirdMax(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if num in result:
                continue
            if len(result) < 3:
                heapq.heappush(result, num)
            else:
                heapq.heappushpop(result, num)

        return max(result) if len(result) < 3 else min(result)
