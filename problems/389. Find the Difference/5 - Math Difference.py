class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        return chr(diff + ord(t[-1]))
