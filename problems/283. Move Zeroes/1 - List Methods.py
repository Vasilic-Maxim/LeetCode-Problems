class Solution:
    """
    Time: O(n^2)
    Space: O(1)
    """

    def moveZeroes(self, nums: list) -> None:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
