'''
Basic implementation of DFS.

N - length of list 'nums'
Time: O(2^N)
Space: O(N) - space allocated by stack calls
'''

class Solution:
    def findTargetSumWays(self, nums: list, target: int, sum: int = 0, lvl: int = 0) -> int:
        if lvl >= len(nums):
            return int(sum == target)
        
        lsum = self.findTargetSumWays(nums, target, sum-nums[lvl], lvl+1)
        rsum = self.findTargetSumWays(nums, target, sum+nums[lvl], lvl+1)

        return lsum + rsum

s = Solution()
print(s.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47], 38))