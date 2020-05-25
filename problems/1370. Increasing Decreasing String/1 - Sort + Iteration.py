from collections import Counter
from itertools import chain


class Solution:
    def sortString(self, s: str) -> str:
        d = sorted([c, n] for c, n in Counter(s).items())
        result = []
        while len(result) < len(s):
            for char in chain(d, reversed(d)):
                if char[1]:
                    result.append(char[0])
                    char[1] -= 1
        return ''.join(result)
