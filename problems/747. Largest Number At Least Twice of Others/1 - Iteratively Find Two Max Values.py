'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def dominantIndex(self, nums: list) -> int:
        if len(nums) == 1:
            return 0
        
        maxId = preMaxId = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maxId]:
                preMaxId, maxId = maxId, i
            elif nums[i] > nums[preMaxId]:
                preMaxId = i
        
        return maxId if nums[maxId] >= nums[preMaxId] * 2 else -1

s = Solution()
print(s.dominantIndex([0,0,1,2]))