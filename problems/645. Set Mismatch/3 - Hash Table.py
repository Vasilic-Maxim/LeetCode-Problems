from collections import Counter
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = missing = None
        counter = Counter(nums)
        for key in range(1, len(nums) + 1):
            if key not in counter:
                missing = key
            elif counter[key] == 2:
                dup = key
        return [dup, missing]
