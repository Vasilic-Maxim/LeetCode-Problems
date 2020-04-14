class Solution:
    """
    n - len(pattern)
    m - len(string)

    Time: O(n + m)
    Space: O(n + m)
    """

    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()

        if len(pattern) != len(words):
            return False

        register, used_words = {}, set()
        for sign, word in zip(pattern, words):
            if sign not in register and word in used_words:
                return False
            used_words.add(word)
            register.setdefault(sign, word)
            if register[sign] != word:
                return False
        return True
