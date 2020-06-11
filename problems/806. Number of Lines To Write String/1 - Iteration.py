from typing import List


class Solution:
    """
    n - len(s)
    Time: O(n)
    Space: O(1)
    """

    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        rows, letters = 1, 0
        for char in s:
            width = widths[ord(char) - ord('a')]
            letters += width
            if letters > 100:
                rows += 1
                letters = width
        return [rows, letters]
