from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        result = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= line1 or word_set <= line2 or word_set <= line3:
                result.append(word)
        return result
