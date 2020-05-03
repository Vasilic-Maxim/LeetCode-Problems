from collections import Counter


class Solution:
    """
    m - len(ransom_note)
    n - len(magazine)
    Time: O(m + n)
    Space: O(m + n)
    """
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        return not Counter(ransom_note) - Counter(magazine)
