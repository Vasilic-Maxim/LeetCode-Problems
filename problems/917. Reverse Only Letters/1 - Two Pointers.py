class Solution:
    """
    https://leetcode.com/problems/reverse-only-letters/discuss/567272/Two-pointers-technique-(Python-O(n)-timespace)
    Time: O(n)
    Space: O(n)
    """

    def reverseOnlyLetters(self, s: str) -> str:
        data = list(s)
        p1, p2 = 0, len(data) - 1
        while p1 < p2:
            # if not self.isAlpha(data[p1]):
            if not data[p1].isalpha():
                p1 += 1
            # elif not self.isAlpha(data[p2]):
            elif not data[p2].isalpha():
                p2 -= 1
            else:
                data[p1], data[p2] = data[p2], data[p1]
                p1 += 1
                p2 -= 1

        return "".join(data)

    def isAlpha(self, character: str):
        return ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z')
