from random import randrange
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        # Time/Space: O(n) / O(n)
        self.original = nums
        self.shuffled = nums[:]

    def reset(self) -> List[int]:
        # Time/Space: O(1) / O(1)
        return self.original

    def shuffle(self) -> List[int]:
        # Time/Space: O(n) / O(1)
        n = len(self.original)
        for i in range(n - 1):
            j = randrange(i, n)
            self.shuffled[i], self.shuffled[j] = self.shuffled[j], self.shuffled[i]
        return self.shuffled
