class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def dominantIndex(self, nums: list) -> int:
        if len(nums) == 1:
            return 0

        max_id = pre_max_id = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_id]:
                pre_max_id, max_id = max_id, i
            elif nums[i] > nums[pre_max_id]:
                pre_max_id = i

        return max_id if nums[max_id] >= nums[pre_max_id] * 2 else -1
