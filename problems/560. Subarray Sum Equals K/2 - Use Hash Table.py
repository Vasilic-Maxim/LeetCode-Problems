from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        data = defaultdict(int)
        counter = summation = 0
        for num in nums:
            summation += num

            if summation == target:
                counter += 1

            diff = summation - target
            if diff in data:
                counter += data[diff]

            data[summation] += 1

        return counter
