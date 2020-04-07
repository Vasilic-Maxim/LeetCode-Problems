class Solution:
    """
    https://leetcode.com/problems/to-lower-case/discuss/567443/Working-with-ASCII-(Python-O(n)-timespace)
    Time: O(n)
    Space: O(n)
    """
    def toLowerCase(self, s: str) -> str:
        data = []
        diff = ord('A') - ord('a')
        for char in s:
            if ord('A') <= ord(char) <= ord('Z'):
                data.append(chr(ord(char) - diff))
            else:
                data.append(char)

        return "".join(data)
