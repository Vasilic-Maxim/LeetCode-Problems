from string import ascii_uppercase


class Solution:
    """
    Time: O(log (n))
    Space: O(log (n))
    """

    def convertToTitle(self, num: int) -> str:
        result = []
        while num:
            num, mod = divmod(num - 1, 26)
            result.append(ascii_uppercase[mod])
        return ''.join(reversed(result))
