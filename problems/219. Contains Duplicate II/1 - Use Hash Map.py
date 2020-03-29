class Solution:
    """
    Time: O(n)
    Space: O(n) - set + hash map
    """

    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False

        nums_map = {}

        for idx, val in enumerate(nums):
            if val in nums_map and idx - nums_map[val] <= k:
                return True

            nums_map[val] = idx

        return False
