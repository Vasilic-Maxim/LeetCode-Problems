from typing import List


class Solution:
    """
    Note: we do not consider space for 'alphabet' because
    'order' has static length of 26 (length of English alphabet)

    n - the total length of words
    Time: O(n)
    Space: O(1)
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {char: val for val, char in enumerate(order)}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for c1, c2 in zip(word1, word2):
                if alphabet[c1] > alphabet[c2]:
                    return False
                if alphabet[c1] < alphabet[c2]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
