from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def shortestToChar(self, string: str, target: str) -> List[int]:
        length, pointer = len(string), -float('inf')
        res = [length] * length
        for i in [*range(length), *range(length)[::-1]]:
            pass
            if string[i] == target:
                pointer = i
            res[i] = min(res[i], abs(i - pointer))
        return res
