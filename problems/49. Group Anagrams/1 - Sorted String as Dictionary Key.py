from collections import defaultdict


class Solution:
    """
    n - length of initial list
    k - maximum length of string
    Time: O(n * k * log_k) - iteration + sorting
    Space: O(n * k) - n times will be created string with length k
    """

    def groupAnagrams(self, anagrams: list):
        mapped = defaultdict(list)
        for val in anagrams:
            mapped[''.join(sorted(val))].append(val)

        return mapped.values()
