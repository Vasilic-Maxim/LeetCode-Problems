from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)

        for char in t:
            if char not in counter or not counter[char]:
                return char
            counter[char] -= 1
