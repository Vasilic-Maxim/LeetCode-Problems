from functools import reduce
from operator import xor
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        # by using XOR we will drop all duplicates and the result will
        # be XOR between two numbers we are searching for
        s = reduce(xor, nums)

        # some kind of mask
        most_right_bit = s & (s - 1) ^ s
        first = reduce(xor, filter(lambda n: n & most_right_bit, nums))
        return [first, s ^ first]
