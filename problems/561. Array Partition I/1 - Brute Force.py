class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def arrayPairSum(self, nums: list) -> int:
        nums = sorted(nums)
        return sum([min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])
