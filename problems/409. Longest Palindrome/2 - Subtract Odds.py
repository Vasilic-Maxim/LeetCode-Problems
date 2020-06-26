from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(1) because there would be 52 or less keys
    (lower and upper case chars of English alphabet)
    """

    def longestPalindrome(self, s):
        # If rightmost bit is 1 then the number is odd.
        # Count them!
        odds = sum(val & 1 for val in Counter(s).values())
        # Subtract odds from total length and if there
        # wer any odd numbers it means that we can put
        # one of them in center of our palindrome
        return len(s) - odds + bool(odds)
