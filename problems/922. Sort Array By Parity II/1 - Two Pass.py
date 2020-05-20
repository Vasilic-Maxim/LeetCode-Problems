from itertools import zip_longest
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = filter(lambda x: not x % 2, nums)
        odds = filter(lambda x: x % 2, nums)
        result = []
        for pair in zip_longest(evens, odds):
            result.extend(pair)
        return result
