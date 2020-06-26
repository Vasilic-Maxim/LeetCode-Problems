from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(1) because there would be 52 or less keys
    (lower and upper case chars of English alphabet)
    """

    def longestPalindrome(self, string: str) -> int:
        div, mod = 0, 0
        for count in Counter(string).values():
            div = count // 2 * 2
            mod = count % 2
        return div + 1 if mod else div
