class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def missingNumber(self, nums: list) -> int:
        diff = set(range(len(nums))) - set(nums)
        return diff.pop() if diff else len(nums)
