from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), weights=self.w)[0]
