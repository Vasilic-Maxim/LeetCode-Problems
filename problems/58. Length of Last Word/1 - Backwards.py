class Solution:
    """
    https://leetcode.com/problems/length-of-last-word/discuss/566499/Right-to-left-iteration-(Python-O(n)-time-O(1)-space)
    Time: O(n)
    Space: O(1)
    """
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                result += 1
            elif result:
                return result

        return result
