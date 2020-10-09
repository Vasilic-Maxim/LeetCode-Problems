from collections import defaultdict, Counter
from itertools import chain
from typing import List


class Solution:
    """
    Time/Space: O(n + m)
    """

    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        counter = Counter((a + " " + b).split())

        return [word
                for word, count in counter.items()
                if count == 1]
