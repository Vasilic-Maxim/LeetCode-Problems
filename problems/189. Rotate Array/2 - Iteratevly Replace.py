class Solution:
    """
    Time Limit Exceeded

    Time: O(k*n)
    Space: O(1)
    """

    def rotate(self, nums: list, k: int) -> None:
        if k == len(nums):
            return

        for i in range(k):
            for j in range(-1, -len(nums), -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
