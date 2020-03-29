class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def arrayPairSum(self, nums: list) -> int:
        ans = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans
