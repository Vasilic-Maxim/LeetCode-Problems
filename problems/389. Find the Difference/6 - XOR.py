from itertools import chain


class Solution:
    """
    Same numbers are killed by XOR operation:
    10 ^ 10 ^ 11 = 11

    Time: O(n)
    Space: O(1)
    """

    def findTheDifference(self, string: str, ex_string: str) -> str:
        # One-line version of the code bellow:
        # return chr(reduce(lambda x, y: x ^ ord(y), chain(string, ex_string), 0))

        code = 0
        for ch in chain(string, ex_string):
            code ^= ord(ch)
        return chr(code)
