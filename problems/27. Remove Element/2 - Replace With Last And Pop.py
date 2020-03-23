'''
Time: O(n)
Space: O(1)
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == val:
                nums[-1], nums[pointer] = nums[pointer], nums[-1]
                nums.pop()
            else:
                pointer += 1
        return len(nums)