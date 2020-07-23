from collections import Counter
from typing import List


class Solution:
    """
    Notes:
        Your algorithm should run in linear runtime complexity.
        Could you implement it using only constant space complexity?

    Conclusion:
        Excellent improvement in terms of time, but still need some
        optimization for space.

    Time: O(n + n/2) => O(n)
    Space: O(n/2) => O(n)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        return [key for key, val in Counter(nums).items() if val == 1]
