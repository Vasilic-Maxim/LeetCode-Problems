'''
Steps to solve the problem:
-   find any sublist what matches the condition
-   while sum of sublist matches the condition identify new
    minimum sublist length and subtract left elements from it
-   repeat until the right pointer is out of list indices

Time: O(n) -    we have two pointers since that we can visit an element
                of the list just twice
Space: O(1)
'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        minsub = float('inf')
        left = right = subsum = 0
        while right < len(nums):
            subsum += nums[right]
            right += 1
            
            while subsum >= s:
                minsub = min(minsub, right - left)
                subsum -= nums[left]
                left += 1
                
        return minsub if minsub != float('inf') else 0