class Solution:
    """
    Time: O(len(s) + len(t))
    Space: O(1)
    """
    def isSubsequence(self, s, t):
        return all(c in iter(t) for c in s)
