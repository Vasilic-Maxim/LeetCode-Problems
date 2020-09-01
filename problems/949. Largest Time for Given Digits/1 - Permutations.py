from itertools import permutations
from typing import List


class Solution:
    """
    Time: O(24) => O(1)
    Space: O(24) => O(1)
    """

    def largestTimeFromDigits(self, nums: List[int]) -> str:
        combs_set = set(permutations(nums))
        combs_list = sorted(combs_set, reverse=True)
        for comb in combs_list:
            if comb[:2] <= (2, 3) and comb[2] < 6:
                return '%d%d:%d%d' % comb
        return ''
