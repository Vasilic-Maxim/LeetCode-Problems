class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_ones = cur_ones = 0
        for val in nums:
            if val:
                cur_ones += 1
            else:
                max_ones = max(max_ones, cur_ones)
                cur_ones = 0
        return max(max_ones, cur_ones)
