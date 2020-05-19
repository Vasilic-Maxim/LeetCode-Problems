import operator
from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(map(operator.eq, secret, guess))
        both = Counter(secret) & Counter(guess)
        return f"{bulls}A{sum(both.values()) - bulls}B"
