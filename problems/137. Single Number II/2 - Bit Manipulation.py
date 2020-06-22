from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for num in nums:
            twos = twos | (ones & num)
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
