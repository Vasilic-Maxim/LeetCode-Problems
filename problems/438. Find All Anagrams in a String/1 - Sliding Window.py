from typing import List


class Solution:
    """
    Time: O(s + p)
    Space: O(s)
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter, p_counter = {}, {}

        for char in p:
            p_counter[char] = p_counter.get(char, 0) + 1

        slow = 0
        result = []
        for fast, char in enumerate(s):
            if char in p_counter:
                s_counter[char] = s_counter.get(char, 0) + 1

                while s_counter[char] > p_counter[char]:
                    s_counter[s[slow]] -= 1
                    slow += 1

                if fast - slow + 1 == len(p):
                    result.append(slow)
                    s_counter[s[slow]] -= 1
                    slow += 1
            else:
                s_counter.clear()
                slow = fast + 1
        return result
