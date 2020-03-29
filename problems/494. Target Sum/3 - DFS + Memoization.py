class Solution:
    """
    Unlike first approach memoization can make the program significantly faster then.
    The idea is to store results of computing the path sum for each level in some data
    structure and if there is another path with the same sum for specific level than
    we already knew the number of paths which will match the target value. That
    phenomena appears only if one value is repeated several times in 'nums' list.
    """

    def findTargetSumWays(self, nums: list, target: int) -> int:
        return self.calculate(nums, target, 0, 0, {})

    def calculate(self, nums: list, target: int, val: int, lvl: int, memo: dict) -> int:
        if lvl >= len(nums):
            return int(val == target)

        key = f"{lvl}-{val}"
        if key in memo:
            return memo[key]

        left_sum = self.calculate(nums, target, val - nums[lvl], lvl + 1, memo)
        right_sum = self.calculate(nums, target, val + nums[lvl], lvl + 1, memo)

        memo[key] = left_sum + right_sum
        return memo[key]
