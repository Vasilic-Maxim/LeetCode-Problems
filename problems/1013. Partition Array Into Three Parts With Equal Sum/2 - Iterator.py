from typing import List


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(1)
    """

    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        # do not need to check if 'nums' is empty because
        # of  the condition [3 <= A.length <= 50000]
        step, reminder = divmod(sum(nums), 3)

        # if the total sum is not divisible by 3 then the
        # list cannot be divided
        if reminder:
            return False

        it = self.accumulate(nums)
        return all(step * i in it for i in range(1, 4))

    def accumulate(self, nums: List[int]):
        current_sum = 0
        for num in nums:
            current_sum += num
            yield current_sum
