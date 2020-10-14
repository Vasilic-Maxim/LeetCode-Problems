from typing import List


class Solution:
    """
    .robber_calc() - is the solution of the first part
    of the problem

    Time: O(n)
    Space: O(1)
    """

    def rob(self, nums: List[int]) -> int:
        def robber_calc(start: int, end: int) -> int:
            rob = not_rob = 0
            for i in range(start, end):
                rob, not_rob = not_rob + nums[i], max(rob, not_rob)
            return max(rob, not_rob)

        n = len(nums)
        if n == 1:
            return nums[0]

        return max(robber_calc(0, n - 1), robber_calc(1, n))
