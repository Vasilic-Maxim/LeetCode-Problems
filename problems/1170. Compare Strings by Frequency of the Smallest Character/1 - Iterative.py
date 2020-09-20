from typing import List


class Solution:
    """
    n = len(queries)
    m = len(words)
    Time: O(m + n)
    Space: O(n)
    """

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        scores = [0] * 12
        for word in words:
            score = self.get_score(word)
            scores[score] += 1

        for i in range(10, 0, -1):
            scores[i] += scores[i + 1]

        result = [0] * len(queries)
        for j in range(len(queries)):
            score = self.get_score(queries[j])
            result[j] = scores[score + 1]

        return result

    # Max performance
    def get_score(self, word: str) -> int:
        min_char = 'z'
        count = 0
        for char in word:
            if char < min_char:
                min_char = char
                count = 1
            elif char == min_char:
                count += 1

        return count

    # Readability, minimalist and also performant
    # because word length is in range(1, 11)
    def get_score_alt(self, word):
        return word.count(min(word))
