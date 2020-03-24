'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]