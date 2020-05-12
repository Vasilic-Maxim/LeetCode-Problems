from collections import Counter
from typing import List


class Solution:
    """
    m - len(words)
    n - max(len(word) for word in words)
    s - len(chars)
    Time: O(s + m * n)
    Space: O(s + m * n)
    """

    def countCharacters(self, words: List[str], chars: str) -> int:
        alphabet = Counter(chars)
        return sum(len(word) for word in words if self.is_sub_dict(alphabet, Counter(word)))

    # This method is more faster than counters subtraction
    def is_sub_dict(self, initial: dict, sub_dict: dict) -> bool:
        return all((char in initial and initial[char] >= count) for char, count in sub_dict.items())
