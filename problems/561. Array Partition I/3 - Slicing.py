class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def arrayPairSum(self, nums: list) -> int:
        return sum(sorted(nums)[::2])
