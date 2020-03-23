'''
Time: O(n^2)
Space: O(1)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] + nums[p2] == target:
                return [p1+1, p2+1]
            
            # Do not forget to escape duplicates
            if nums[p1] == nums[p2] or p2 + 1 == len(nums) or nums[p1]+nums[p2+1] > target:
                p1 += 1
                p2 = p1 + 1
            else:
                p2 += 1