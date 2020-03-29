class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def containsDuplicate(self, nums: list) -> bool:
        return len(set(nums)) != len(nums)
