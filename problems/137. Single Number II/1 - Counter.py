from collections import Counter
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]
