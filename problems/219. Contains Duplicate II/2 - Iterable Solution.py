class Solution(object):
    """
    Time: O(n)
    Space: O(n) - for set only
    """

    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True

        return False
