'''
Approach #1: delete using 'del' operator
This approach is inefficient because each time then an item will be deleted
remaining elements will be shifted.

Time: O(n^2) - the worst case is then all the elements in the list are equal to 'val'
Space: O(1)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] == val: del nums[i]
            else: i += 1
        
        return len(nums)