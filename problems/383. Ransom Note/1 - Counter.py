from collections import Counter


class Solution:
    """
    m - len(ransom_note)
    n - len(magazine)
    Time: O(m + n)
    Space: O(n)
    """
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for char in ransom_note:
            if char in counter and counter[char]:
                counter[char] -= 1
            else:
                return False

        return True
