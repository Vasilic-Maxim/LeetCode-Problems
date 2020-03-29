class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def arrayPairSum(self, nums: list) -> int:
        return sum([val for i, val in enumerate(sorted(nums)) if i % 2 == 0])
