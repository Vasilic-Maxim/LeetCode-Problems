class Solution:
    """
    n - length of the string
    Time: O(n)
    Space: O(1)
    """

    def romanToInt(self, s: str) -> int:
        vocab = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        slow = fast = len(s) - 1
        result = 0

        while fast >= 0:
            s_val = vocab[s[slow]]
            f_val = vocab[s[fast]]

            result += -f_val if s_val > f_val else f_val
            slow = slow if s_val > f_val else fast
            fast -= 1

        return result
