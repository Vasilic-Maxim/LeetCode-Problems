from collections import Counter
from re import findall
from typing import List


class Solution:
    """
    m - len(string)
    n - len(banned)

    Time: O(2m + n) => O(m + n)
    Space: O(m + n)
    """

    def mostCommonWord(self, string: str, banned: List[str]) -> str:
        counter = Counter(self.get_words(string.lower(), set(banned)))
        return max(counter.keys(), key=counter.get)

    def get_words(self, string: str, banned: set) -> str:
        for word in findall(r"\w+", string):
            if word not in banned:
                yield word
