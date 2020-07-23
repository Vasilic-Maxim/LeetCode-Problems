from typing import List


class Solution:
    """
    Notes:
        Your algorithm should run in linear runtime complexity.
        Could you implement it using only constant space complexity?

    Conclusion:
        Better than first solution in terms of time, but worse in
        terms of space.

    Time: O(n * log (n))
    Space: O(n)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        i = 1
        while i < len(nums):
            if nums[i - 1] != nums[i]:
                result.append(nums[i - 1])
                i += 1
            else:
                i += 2

        if len(result) != 2:
            result.append(nums[-1])

        return result
