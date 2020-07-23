from typing import List


class Solution:
    """
    Notes:
        Your algorithm should run in linear runtime complexity.
        Could you implement it using only constant space complexity?

    Conclusion:
        The algorithm is too slow!

    Time: O(n ** 2)
    Space: O(1)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        return [num for num in nums if nums.count(num) == 1]
