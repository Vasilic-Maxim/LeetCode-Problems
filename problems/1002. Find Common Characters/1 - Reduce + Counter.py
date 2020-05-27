import operator
from collections import Counter
from functools import reduce
from typing import List

class Solution:
    """
    m - len(words)
    n - max(words, key=len)
    Time: O(m * n)
    Space: O(m * n)
    """

    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(operator.and_, [Counter(word) for word in words]).elements())
