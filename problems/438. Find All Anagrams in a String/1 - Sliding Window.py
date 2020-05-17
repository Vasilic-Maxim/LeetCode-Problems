from collections import Counter
from typing import List


class Solution:
    """
    Time: O(s + p)
    Space: O(s + p)
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # count letters to balance their numbers in anagrams
        s_counter = Counter()
        p_counter = Counter(p)
        # count letters which are present in "p"
        s_value = slow = 0
        result = []
        # while fast < len(s):
        for fast, char in enumerate(s):
            if char in p_counter:
                s_counter[char] += 1
                s_value += 1

                while s_counter[char] > p_counter[char]:
                    s_counter[s[slow]] -= 1
                    s_value -= 1
                    slow += 1
            else:
                s_counter.clear()
                s_value = 0
                slow = fast + 1

            if s_value == len(p):
                result.append(slow)
                s_counter[s[slow]] -= 1
                s_value -= 1
                slow += 1
        return result
