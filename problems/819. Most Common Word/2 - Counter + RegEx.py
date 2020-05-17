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
        words = findall(r"\w+", string.lower())
        banned_set = set(banned)
        counter = Counter(word for word in words if word not in banned_set)
        return counter.most_common(1)[0][0]
