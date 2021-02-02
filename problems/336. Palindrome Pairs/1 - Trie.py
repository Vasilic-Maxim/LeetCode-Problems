from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str, word_id: int):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word_id = word_id
    
    def find_palindrome_pairs(self, word: str, word_id: int, is_prefix: bool):
        node = self.root
        pairs = []
        for i, char in enumerate(word):
            # if we find a word on our way then there isd a reason to check if the
            # unchecked part of the word is a palindrome
            if node.word_id is not None and self.is_palindrome(word, i):
                pairs.append(self.form_pair(node.word_id, word_id, is_prefix))
            
            # if there is no path than quit
            if char not in node.children:
                break
            
            # step forward
            node = node.children[char]
        else:
            # if two words are of the same length and it is the end in the trie
            # then one is the mirror of the other
            if node.word_id is not None:
                pairs.append(self.form_pair(node.word_id, word_id, is_prefix))
        
        return pairs
    
    def is_palindrome(self, word: str, start: int) -> bool:
        n = (len(word) - start) // 2
        for i in range(n):
            if word[start + i] != word[~i]:
                return False
        return True

    def form_pair(self, id1: int, id2: int, is_prefix: bool) -> List[int]:
        if is_prefix:
            return [id1, id2]
        return [id2, id1]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ids = {word: i for i, word in enumerate(words)}
        
        # sort the array in ascending order to make the
        # search a linear operation
        words.sort(key=len)
        
        # create a list with all words from the initial
        # list being reversed
        reversed_words = [word[::-1] for word in words]
        
        # a list that will hold the pairs
        result = []
        
        # create and populate the prefix and postfix trees
        prefix_tree = Trie()
        postfix_tree = Trie()
        for i in range(n):
            word, reversed_word = words[i], reversed_words[i]
            
            # try to find all prefixes to make a palindrome
            result.extend(prefix_tree.find_palindrome_pairs(reversed_word, ids[word], True))
            # add current word into prefixes
            prefix_tree.add_word(word, ids[word])
            
            # try to find all postfixes to make a palindrome
            result.extend(postfix_tree.find_palindrome_pairs(word, ids[word], False))
            # add current word into postfixes
            postfix_tree.add_word(reversed_word, ids[word])
        
        return result
