from typing import List


class Solution:
    """
    If parity is even than the last zero is single
    bits:   [0010110]
    parity: [...101.]


    Time: O(n)
    Space: O(1)
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return not parity
