from collections import Counter
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findPairs(self, nums: List[int], target: int) -> int:
        res = 0
        counter = Counter(nums)
        for i in counter:
            if target > 0 and i + target in counter or target == 0 and counter[i] > 1:
                res += 1
        return res
