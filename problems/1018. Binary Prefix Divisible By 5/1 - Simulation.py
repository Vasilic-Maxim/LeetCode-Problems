from typing import List


class Solution:
    def prefixesDivBy5(self, a: List[int]) -> List[bool]:
        result = []
        num = 0
        for bit in a:
            num = (num * 2 + bit) % 5
            result.append(num == 0)
        return result
