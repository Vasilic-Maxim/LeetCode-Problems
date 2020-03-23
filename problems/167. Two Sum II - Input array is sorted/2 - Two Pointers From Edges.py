'''
Time: O(n)
Space: O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current = 0
        last = len(nums) - 1
        while True:
            if nums[current] + nums[last] > target:
                last -= 1
            elif nums[current] + nums[last] < target:
                current +=1
            else:
                return [current+1, last+1]