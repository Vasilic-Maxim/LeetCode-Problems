'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum([min(nums[i], nums[i+1]) for i in range(0, len(nums), 2)])