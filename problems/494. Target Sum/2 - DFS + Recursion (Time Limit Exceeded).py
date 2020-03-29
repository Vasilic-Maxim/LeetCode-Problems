class Solution:
    """
    Basic implementation of DFS.

    N - length of list 'nums'
    Time: O(2^N)
    Space: O(N) - space allocated by stack calls
    """

    def findTargetSumWays(self, nums: list, target: int, curr_sum: int = 0, lvl: int = 0) -> int:
        if lvl >= len(nums):
            return int(curr_sum == target)

        left_sum = self.findTargetSumWays(nums, target, curr_sum - nums[lvl], lvl + 1)
        right_sum = self.findTargetSumWays(nums, target, curr_sum + nums[lvl], lvl + 1)

        return left_sum + right_sum
