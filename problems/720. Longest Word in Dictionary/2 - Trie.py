from collections import defaultdict
from typing import List


class Trie:
    class __TrieNode:
        def __init__(self, word: str = None):
            self.children = defaultdict(self.__class__)
            self.word = word

    def __init__(self):
        self.root = self.__TrieNode("")

    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = word

    def longest_word(self):
        def helper(node):
            longest = node.word
            if longest is None:
                return ""

            for child in node.children.values():
                candidate = helper(child)
                n, m = len(candidate), len(longest)
                if n > m or n == m and candidate < longest:
                    longest = candidate

            return longest

        return helper(self.root)


class Solution:
    """
    n - sum(len(word) for word in words)
    Time: O(n)
    Space: O(n)
    """

    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        return trie.longest_word()
