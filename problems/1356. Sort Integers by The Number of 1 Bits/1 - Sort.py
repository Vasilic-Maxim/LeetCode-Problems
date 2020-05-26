from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(n)
    """

    def sortByBits(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda num: (bin(num).count('1'), num))
