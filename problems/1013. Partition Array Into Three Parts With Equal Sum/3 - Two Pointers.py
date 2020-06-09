from typing import List


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(1)
    """

    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        step, reminder = divmod(sum(nums), 3)

        # if the total sum is not divisible by 3 then the
        # list cannot be divided
        if reminder:
            return False

        count = accumulator = 0
        for i, num in enumerate(nums):
            accumulator += num
            if accumulator == step:
                count += 1
                accumulator = 0
            if count == 2:
                return i < len(nums) - 1
