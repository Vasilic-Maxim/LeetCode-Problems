from collections import Counter
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [key for key, count in Counter(nums).items() if count == 2]
