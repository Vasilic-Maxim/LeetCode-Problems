class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def rotate(self, nums: list, k: int) -> None:
        l = len(nums)
        k = k % l
        self.reverse(nums, 0, l - 1)  # rotate the whole list
        self.reverse(nums, 0, k - 1)  # rotate first k elements
        self.reverse(nums, k, l - 1)  # rotate remaining elements

    def reverse(self, nums: list, start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
