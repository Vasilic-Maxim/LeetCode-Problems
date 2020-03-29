class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
