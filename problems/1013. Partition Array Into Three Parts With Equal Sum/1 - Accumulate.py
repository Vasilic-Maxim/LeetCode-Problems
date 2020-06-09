from itertools import accumulate
from typing import List


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(n)
    """

    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        # do not need to check if 'nums' is empty because
        # of  the condition [3 <= A.length <= 50000]
        nums_sums = list(accumulate(nums))
        step, reminder = divmod(nums_sums[-1], 3)

        # if the total sum is not divisible by 3 then the
        # list cannot be divided
        if reminder:
            return False

        it = iter(nums_sums)
        return all(step * i in it for i in range(1, 4))
