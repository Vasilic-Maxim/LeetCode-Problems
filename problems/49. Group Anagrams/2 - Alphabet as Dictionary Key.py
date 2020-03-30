from collections import defaultdict


class Solution:
    """
    n - length of the list
    k - maximum length of string in the list
    Time: O(n * k)
    Space: O(n * k) - n times will be created tuple with length k
    """
    def groupAnagrams(self, anagrams: list):
        mapped = defaultdict(list)
        for word in anagrams:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            # to use key-string we had to convert entire int-list to str-list
            # that action will take significant amount of time
            mapped[tuple(key)].append(word)
        return mapped.values()
