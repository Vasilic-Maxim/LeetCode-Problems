'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def pivotIndex(self, nums: list) -> int:
        totalSum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            # totalSum -= nums[i]
            # if totalSum == leftSum:
            #     return i
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            
            leftSum += nums[i]
        
        return -1