'''
Time: O(n)
Space: O(1)
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([val for i, val in enumerate(sorted(nums)) if i % 2 == 0])