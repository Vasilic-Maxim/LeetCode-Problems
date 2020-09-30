from typing import List


class Solution:
    def numSpecialEquivGroups(self, a: List[str]) -> int:
        """
        n = len(a)
        w = len(word)
        Time: O(n * w)
        Space: O(n * 52) => O(n)
        """

        def count(s: str) -> tuple:
            result = [0] * 52
            for i, char in enumerate(s):
                result[26 * (i % 2) + ord(char) - ord("a")] += 1
            return tuple(result)

        return len({count(word) for word in a})
