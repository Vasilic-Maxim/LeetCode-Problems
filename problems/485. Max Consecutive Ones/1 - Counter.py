'''
Time: O(n)
Space: O(1)
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = curOnes = 0
        for val in nums:
            if val: curOnes += 1
            else:
                maxOnes = max(maxOnes, curOnes)
                curOnes = 0
        return max(maxOnes, curOnes)