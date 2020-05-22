from itertools import combinations
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        watch = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        times = []
        for lads in combinations(range(len(watch)), num):
            h = sum(watch[i] for i in lads if i < 4)
            m = sum(watch[i] for i in lads if i >= 4)
            if h <= 11 and m <= 59:
                times.append("{}:{:02d}".format(h, m))
        return times
