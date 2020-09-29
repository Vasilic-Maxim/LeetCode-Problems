from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        def node():
            return defaultdict(node)

        trie = node()
        for word in word_dict:
            pointer = trie
            for letter in word:
                pointer = pointer[letter]
            pointer.setdefault("_end")

        def verify(i: int, children: defaultdict):
            if i == len(s):
                return "_end" in children[s[i]]

            if s[i] not in children:
                return False

            result = False
            if "_end" in children[s[i]]:
                result = verify(i + 1, trie)

            return result or verify(i + 1, children[s[i]])

        return verify(0, trie)
