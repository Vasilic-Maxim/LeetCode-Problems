from collections import Counter
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def majorityElement(self, nums: List[int]):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
