from typing import List


class Solution:
    """
    Time: O(n) - usually sort takes O(n * log n) time< but here we sort just two values
    Space: O(n)
    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
