import operator
from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.data = list(accumulate(nums, operator.add))

    def sumRange(self, i: int, j: int) -> int:
        return self.data[j] - (self.data[i - 1] if i else 0)
