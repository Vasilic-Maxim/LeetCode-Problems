class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def repeatedSubstringPattern(self, word: str) -> bool:
        return word in (2 * word)[1:-1]
