class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def maximum69Number(self, num: int) -> int:
        s, p = str(num), 0
        while p < len(s) and s[p] == '9':
            p += 1
        return num if p == len(s) else int(s[:p] + '9' + s[p + 1:])
