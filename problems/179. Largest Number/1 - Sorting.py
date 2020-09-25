from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]):
        if not any(nums):
            return '0'

        def cmp(num1, num2):
            forward = num1 + num2
            backward = num2 + num1
            return (forward < backward) - (forward > backward)

        return ''.join(sorted(map(str, nums), key=cmp_to_key(cmp)))
