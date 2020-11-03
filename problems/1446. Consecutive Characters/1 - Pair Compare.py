class Solution:
    def maxPower(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(1)
        """

        res = counter = 1
        for i in range(1, len(s)):
            counter = counter + 1 if s[i] == s[i - 1] else 1
            res = max(res, counter)
        return res
