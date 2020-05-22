from collections import defaultdict


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        for char in t:
            if not counter[char]:
                return char
            counter[char] -= 1
