from typing import List


class Solution:
    """
    w - length of a word
    Time: O(n * w ** 2)
    Space: O(w ** 2)
    """

    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        result = ""
        for word in words:
            m, n = len(word), len(result)
            if m > n or m == n and word < result:
                if all(word[:i] in words_set for i in range(1, m)):
                    result = word
        return result
